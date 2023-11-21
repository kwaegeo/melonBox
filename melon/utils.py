from django.core.exceptions import ValidationError


def request_data_vaild(request_data):
    """
    요청 데이터 유효성 검사 (필수값)
    :param request_data:
    :return:
    """

    if request_data is None:
        raise ValidationError(API.NO_DATA_REQUIRED.code)  # 필수 값이 업습니다.
    elif not request_data:
        raise ValidationError(API.NO_DATA_REQUIRED.code)  # 필수 값이 없습니다.
    else:
        return request_data