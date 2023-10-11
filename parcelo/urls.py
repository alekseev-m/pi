from django.urls import path
from django.conf.urls import include
from api.viewsets import router

urlpatterns = [
    path(r'api/', include(router.urls)),
    # path(r'api/', include(('api.urls', 'api'))),
]
