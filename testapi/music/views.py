from django.shortcuts import render
from rest_framework import viewsets

from .serializers import SongSerializer
from .models import Songs
# Create your views here.


class SongViewSet(viewsets.ModelViewSet):
	#1 query database for all Song
    queryset = Songs.objects.all().order_by('artist')
    # Pass that database queryset into the serializer we just created, so that it gets converted into JSON and rendered
    serializer_class = SongSerializer