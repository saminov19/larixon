from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Advert
from .serializers import AdvertSerializer

class AdvertListView(generics.ListAPIView):
    queryset = Advert.objects.all().select_related('city', 'category')
    serializer_class = AdvertSerializer

class AdvertDetailView(APIView):
    def get(self, request, pk):
        advert = Advert.objects.select_related('city', 'category').get(pk=pk)
        advert.views += 1
        advert.save()
        serializer = AdvertSerializer(advert)
        return Response(serializer.data)
