from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('movies.urls')), #подключаем все urls в корневой файл urls
]

#при включенном DEBUG-режиме django будет раздавать наши файлы с MEDIA при включенном DEBUG-режиме
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)