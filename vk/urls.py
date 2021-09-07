from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views
from .views import VkToTg

urlpatterns = [
    path('cb/', csrf_exempt(VkToTg.as_view()))
]