from django.urls import path

from basic_app import views

urlpatterns = [
    path('connect/', views.ListProcids.as_view()),
    path('connect/<int:pk>', views.ListProcids.as_view()),
]
