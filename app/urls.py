from django.urls import path
from .views import views

urlpatterns = [
    path('todo/', views.create_or_update_todo, name='create_or_update_todo'),
]
