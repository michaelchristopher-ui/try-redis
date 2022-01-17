from typing import ContextManager
from django.shortcuts import render
from django.core.cache import cache
import django_rq

from .models import Country
# Create your views here.
from .serializers import CountrySerializer

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from redis_as_mq.queue_funcs import QManager, QJobs


def home(request):
    countries = Country.objects.all()
    print("COUNTRIES: ")

    context = {'countries': countries}
    return render(request, 'htmls/home.html', context)


def entry(request, entry_name):
    source = "Cache"
    entry = cache.get(entry_name)
    print(entry, source)
    if not entry:
        entry = Country.objects.get(name=entry_name)
        cache.set(entry_name, entry)
        source = "Database"
    else:
        cache.delete(entry_name)

    entry = Country.objects.get(name=entry_name)
    context = {'entry': entry, 'source': source}
    return render(request, 'htmls/entry.html', context)

def fetchToken(request):
    return render(request , 'htmls/fetchToken.html')

class MQHome(APIView):

    def get(self, request, format=None):

        context = {}
        return Response()

    def post(self, request, format=None):

        serializer = CountrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # With the below code, jobs can still be lost since Redis is a fire and forget system.
            #This is equal to executing QJobs.send_message_to_firebase_push_notifications("IT ALSO WORKSSSS") but within another worker
            django_rq.get_queue("default").enqueue(
                QJobs.send_message_to_firebase_push_notifications, "IT ALSO WORKSSSS")

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # Track here
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


