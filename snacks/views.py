from rest_framework import generics
from .serializers import SnackSerializer
from .models import Snack
from django.http import HttpResponse

class SnackList(generics.ListCreateAPIView):
    queryset = Snack.objects.all()
    serializer_class = SnackSerializer

class SnackDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snack.objects.all()
    serializer_class = SnackSerializer

def home(request):
    return HttpResponse("Welcome to the Snacks API! Access the API at /api/v1/snacks/")
