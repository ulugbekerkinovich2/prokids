from rest_framework import serializers

from basic_app import models


class ProcidsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.Procids
