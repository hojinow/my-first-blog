from django.urls import path
from.views import Jisview

urlpatterns = [
    path('', Jisview.as_view(), name='main'),
]
