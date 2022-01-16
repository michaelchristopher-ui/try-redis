from django.core.exceptions import ViewDoesNotExist
from django.urls import path
from .views import home, entry, MQHome
app_name = "redis_as_cache"
urlpatterns = [
    path('', home),
    path('<str:entry_name>/', entry),
    path('mqhome', MQHome.as_view())
]
