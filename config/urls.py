
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('melon/', include('melon.urls')), # melon app url 등록
    path('apple/', include('apple.urls')), # apple app url 등록
]
