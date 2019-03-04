from rest_framework.viewsets import ModelViewSet

from .models import Meme
from .serializers import MemeSerializer


class MemeViewSet(ModelViewSet):
    model = Meme
    queryset = Meme.objects.all()
    serializer_class = MemeSerializer
