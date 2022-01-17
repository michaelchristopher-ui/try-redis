import django_rq
import requests
import json
from django.conf import settings

'''
Constants
'''
CHANNEL_DEFAULT = "default"


class QManager:

    def enqueue(self, *args, **kwargs):
        channel = kwargs.pop('channel', CHANNEL_DEFAULT)
        print(args)
        django_rq.get_queue(channel).enqueue(*args, **kwargs)


#django-rq seems to hate the param "self" that indicates that the method is executed by an instance
# Once a method in this class has been changed, please restart the workers
class QJobs:
        
    def send_notification(registration_ids, message_title, message_desc, img_link, icon_link):
        # fcm_api is filled in with the cloud messaging server key
        #TODO: Put the fcm api key in the env
        fcm_api = getattr(settings, "FCM_API", "")
        url = getattr(settings, "FIREBASE_URL", "")
        headers = {
            "Content-Type": "application/json",
            "Authorization": "key="+fcm_api
        }
        payload = {
            "registration_ids":registration_ids,
            "priority" : "high",
            "notification" : {
                "body" : message_desc,
                "title" : message_title,
            }
        }

        result = requests.post(url, data=json.dumps(payload), headers=headers)
        print(result.json())  

    def send_message_to_firebase_push_notifications(message_desc):
        # Use the /redis_as_cache/fetchtoken/ endpoint to generate the token which will be printed in the console
        # There is also the problem of getting this token automatically
        # If that is not possible, then we can opt to put it in env
        registration = [getattr(settings, "FIREBASE_REGISTRATION_ID", "")]
        message_title = "New Message from Try-Redis"
        QJobs.send_notification(registration, message_title, message_desc, "", "")
        print("sent")  