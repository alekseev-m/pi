from django.urls import path, include
from db.models import Parcel, ParcelLocker
from rest_framework import routers, serializers, viewsets


# from rest_framework.validators import
class ParcelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Parcel
        fields = ['sender', 'receiver', 'status', 'size']


class ParcelLockerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ParcelLocker
        fields = ['address', 'status', 'size', 'parcel']


class ParcelViewSet(viewsets.ModelViewSet):
    queryset = Parcel.objects.all()
    serializer_class = ParcelSerializer


class ParcelLockerViewSet(viewsets.ModelViewSet):
    queryset = ParcelLocker.objects.all()
    serializer_class = ParcelLockerSerializer


router = routers.DefaultRouter()
router.register(r'parcel', ParcelViewSet)
router.register(r'parcellocker', ParcelLockerViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
