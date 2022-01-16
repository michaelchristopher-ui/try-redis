from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .queue_funcs import QManager, QJobs

# Create your views here.


class MQHome(APIView):

    def get(self, request, format=None):

        context = {}
        return Response()

    def post(self, request, format=None):
        serializer = None
        # serializer = CountrySerializerFetcher.get_country_serializer(request.data)
        if serializer.is_valid():
            serializer.save()
            # With the below code, jobs can still be lost since Redis is a fire and forget system.
            QManager.enqueue(
                QJobs.send_message_to_firebase_push_notifications, "message")

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # Track here
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
