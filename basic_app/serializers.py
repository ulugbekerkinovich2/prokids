import requests
from rest_framework import serializers

from basic_app import models

API_TOKEN = '5087104877:AAEmqu0xk9s71Pr5dTmNB11jepYd9Ka96CY'


class ProcidsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.Procids

    def create(self, validated_data):
        ob = models.Procids.objects.create(**validated_data)
        print(ob)
        requests.get(
            url=f"https://api.telegram.org/bot5087104877:AAEmqu0xk9s71Pr5dTmNB11jepYd9Ka96CY/sendMessage?chat_id=935920479&parse_mode=HTML&text={ob}")
        return ob
