import django_rq

'''
Constants
'''
CHANNEL_DEFAULT = "default"


class QManager:

    def enqueue(self, *args, **kwargs):
        channel = kwargs.pop('channel', CHANNEL_DEFAULT)
        django_rq.get_queue(channel).enqueue(*args, **kwargs)


class QJobs:
    def send_message_to_firebase_push_notifications(self, message):
        pass
