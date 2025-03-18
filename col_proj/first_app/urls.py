from django.urls import path
from .views import *

urlpatterns = [
    path('func1/', func1),
    path('func2/', func2)
]