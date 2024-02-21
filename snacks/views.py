from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Snack
from .serializers import SnackSerializer
from .permissions import IsOwnerOrReadOnly

class SnackList(ListCreateAPIView):
    queryset = Snack.objects.all()
    serializer_class = SnackSerializer

class SnackDetail(RetrieveUpdateDestroyAPIView):
    queryset = Snack.objects.all()
    serializer_class = SnackSerializer
    permission_classes = (IsOwnerOrReadOnly,)
