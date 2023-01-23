from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.conf.urls.static import static
from django.conf import settings
from phones.views import *

router = routers.DefaultRouter()
router.register(r'phones', PhoneViewSet,basename="phone")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
