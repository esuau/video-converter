import time
import logging
import json

from google.cloud import pubsub_v1


class ConversionMessaging(object):

    def __init__(self, _config_, database_service):
        project_id = _config_.get_gcloud_project_id()
        subscription_name = _config_.get_gcloud_subscription_name()

        subscriber = pubsub_v1.SubscriberClient()
        subscription_path = subscriber.subscription_path(project_id, subscription_name)

        def callback(message):
            logging.info('Received message: {}'.format(message.data))
            received_data = json.loads(message.data.decode('utf-8'))
            database_service.update_item_status(received_data['uuid'], 'converted')
            message.ack()

        subscriber.subscribe(subscription_path, callback=callback)

        logging.info('Listening for messages on {}'.format(subscription_path))
        while True:
            time.sleep(60)
