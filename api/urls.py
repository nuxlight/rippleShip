from django.urls import path
from . import views

urlpatterns = [
    path('newgame/<int:test>', views.generate_party),
]
