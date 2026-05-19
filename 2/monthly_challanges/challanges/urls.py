from django.urls import path
from . import views

# URL config
urlpatterns = [
    path('', views.index),
    path('<int:month>', views.monthly_challange_by_num),
    path('<str:month>', views.monthly_challange, name='monthly-challange'),
]
