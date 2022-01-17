from django.core.exceptions import ViewDoesNotExist
from django.urls import path
from .views import home, entry, MQHome, fetchToken
app_name = "redis_as_cache"
urlpatterns = [
    path('', home),
    path('countries/<str:entry_name>/', entry),
    path('mqhome/', MQHome.as_view()),
    path('fetchtoken/', fetchToken),
]
