import requests

from basic_app.models import Procids
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import api_view
from basic_app import models

API_TOKEN = '5087104877:AAEmqu0xk9s71Pr5dTmNB11jepYd9Ka96CY'


class ProcidsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.Procids
        # obj1 = models.Procids.objects.all()
        # print(obj1)

    def create(self, validated_data):
        ob = models.Procids.objects.create(**validated_data)
        print(ob)
        requests.get(
            url=f"https://api.telegram.org/bot5087104877:AAEmqu0xk9s71Pr5dTmNB11jepYd9Ka96CY/sendMessage?chat_id=935920479&parse_mode=HTML&text={ob}")
        return ob


# https://api.telegram.org/bot5087104877:AAEmqu0xk9s71Pr5dTmNB11jepYd9Ka96CY/sendMessage?chat_id=9359320479&parse_mode=HTML&text=bu habar API dan

import logging

import wikipedia
from aiogram import Bot, Dispatcher, executor, types

# wikipedia.set_lang('uz')

# logging.basicConfig(level=logging.INFO)
#
# bot = Bot(token=API_TOKEN)
# dp = Dispatcher(bot)
#
#
# @dp.message_handler()
# async def send_welcome(message: types.Message):
#     await message.reply("Salom :) botimizga hush kelibsiz.")
#
#
# if __name__ == '__main__':
#     executor.start_polling(dp, skip_updates=True)
