from django.shortcuts import render

# Create your views here.
from rest_framework import generics

from basic_app import models, serializers


class ListProcids(generics.ListCreateAPIView):
    queryset = models.Procids.objects.all()
    serializer_class = serializers.ProcidsSerializer


class DetailProcids(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Procids.objects.all()
    serializer_class = serializers.ProcidsSerializer
