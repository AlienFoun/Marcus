from .models import UpgradeDB
from rest_framework import viewsets, permissions
from .serializer import UpgradeSerializer


class UpgradeViewSet(viewsets.ModelViewSet):
    queryset = UpgradeDB.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = UpgradeSerializer
