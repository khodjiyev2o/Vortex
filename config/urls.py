from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.conf.urls.static import static
from django.conf import settings
from phones.views import *
from profiles.views import *
from stores.views import *

router = routers.DefaultRouter()
router.register(r'phones', PhoneViewSet,basename="phone")
router.register(r'profiles',ProfileViewSet,basename='profile')
router.register(r'stores',StoreViewSet,basename='store')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
