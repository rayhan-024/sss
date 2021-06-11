
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('myapp/', include('myapp2.urls', namespace = 'myapp2')),
    path('', include('blog.urls', namespace = 'blog')),
    path('album/', include('album.urls', namespace = 'album')),
    path('summernote/', include('django_summernote.urls'))
]

if settings.DEBUG : 
    urlpatterns += static(settings.MEDIA_URL,
    document_root = settings.MEDIA_ROOT)