from rest_framework import serializers
from .models import UpgradeDB


class UpgradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UpgradeDB
        fields = '__all__'
