from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static

from data import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^add_workflow/', include('upload.urls')),
    url(r'^', include('find.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL,\
                      document_root=settings.STATIC_ROOT)