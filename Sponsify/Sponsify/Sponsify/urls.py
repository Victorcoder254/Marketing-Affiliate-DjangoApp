from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('ADsListing.urls')),
    path('Partner/', include('ADsPartner.urls')),
    path('authenticate/', include('authenticate.urls')),
    path('admin/', admin.site.urls),
]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
