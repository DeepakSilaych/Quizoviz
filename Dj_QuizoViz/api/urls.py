from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_questions),
    path('add/',views.add_questions)
]
