from django.http import HttpResponse


def index(request):
    return HttpResponse('멜론 박스의 애플 뮤직 앱.')
