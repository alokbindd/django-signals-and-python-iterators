from django.urls import path
from .views import rectangle_demo

urlpatterns = [
    path("", view=rectangle_demo, name='rectangle-demo'),
]