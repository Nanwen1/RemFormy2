from rest_framework import serializers
from .models import Rem


class RemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rem
        fields = ('asset_function', 'region', 'grade', 'jobFamily', 'midpoint', 'STI', 'superannuation')
