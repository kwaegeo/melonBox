import json
import logging
from json import JSONDecodeError
from urllib.request import urlopen
from bs4 import BeautifulSoup
from django.core.exceptions import ValidationError
from django.http import HttpResponse, JsonResponse
from ytmusicapi import YTMusic

from common.api_response import ApiResponse as API
from melon.utils import request_data_vaild


def index(request):
    return HttpResponse('멜론 박스의 멜론 앱.')


def get_melon_play_list(request):
    """
    멜론 플레이 리스트 조회
    :param request:
    :return POST : JsonResponse
    """

    try:
        # 1. 데이터 파싱
        data = json.loads(request.body)

        # 2. 필수값 확인
        melon_share_url = data.get('melon_share_url', '').strip()
        auth_json_data = data.get('auth_json_data', '').strip()

        # 임시로 위의 과정 패스 (하드코딩 사용)

        # 3. 멜론 공유 URL 크롤링 후 데이터 수집
        melon_share_url = urlopen("https://kko.to/wh3o03SbXW")  # 임시 하드 코딩 값 사용
        soup = BeautifulSoup(melon_share_url, "html.parser")  # BeautifulSoup 객체 생성

        # 3.1. 플레이 리스트 제목 수집
        title_tag_with_class = soup.find('h1', class_='tit-gnb tit-transparent')  # 플레이리스트 제목을 가져오기 위한 태그 탐색

        if title_tag_with_class:
            play_list_title = title_tag_with_class.get_text(strip=True)
            print("플레이 리스트 제목:", play_list_title)
        else:
            print("플레이 리스트 제목을 찾을 수 없습니다.")

        # 3.2. 곡명, 가수명 수집
        song_tags = soup.select('.txt-title.ellipsis')  # 곡명 태그 선택
        songs = [tag.get_text(strip=True) for tag in song_tags]  # 데이터 추출

        artist_tags = soup.select('.txt-description.ellipsis')  # 가수명 태그 선택
        artists = [tag.get_text(strip=True) for tag in artist_tags]  # 데이터 추출

        # 3.3. 곡명과 가수명을 각각의 인덱스에 맞게 추가
        play_list_result = []
        for song, artist in zip(songs, artists):
            play_list_result.append({'song': song, 'artist': artist})

        # 결과 출력
        for idx, item in enumerate(play_list_result, start=1):
            print(f"{idx}. 곡명: {item['song']}, 가수: {item['artist']}")

        return JsonResponse({"code": API.SUCCESS.code, "msg": API.SUCCESS.msg, "play_list_result": play_list_result})

    except ValidationError as e:
        print("### 멜론 플레이 리스트 조회 ### 필수값 에러 => [{}]".format(str(e)))
        return JsonResponse({'code': API.NO_DATA_REQUIRED.code, 'msg': API.NO_DATA_REQUIRED.msg})
    except JSONDecodeError as e:
        print("### 멜론 플레이 리스트 조회 ### JSON 누락 에러 => [{}]".format(str(e)))
        return JsonResponse({'code': API.JSON_DECODE_ERROR.code, 'msg': API.JSON_DECODE_ERROR.msg})


def youtube_music_connection():
    """
    유튜브 뮤직 연결 (연결 객체)
    :param :
    :return POST : JsonResponse
    """

    # ytmusicapi.setup(filepath="browser.json",  headers_raw="<headers copied above>")
    # data = json.loads(request.body)
    # urls = data.get()
    ytmusic = YTMusic("oauth.json")
    playlistId = ytmusic.create_playlist("test_play_list", "test description")
    search_results = ytmusic.search("아이유 비밀의 화원")
    # print([search_results[0]['videoId']])
    ytmusic.add_playlist_items(playlistId, ["eGXJs7zOHC4"])

    return HttpResponse(search_results)
