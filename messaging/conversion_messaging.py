import time
import logging
import json

from google.cloud import pubsub_v1


class ConversionMessaging(object):

    def __init__(self, _config_, database_service, conversion_service):
        project_id = _config_.get_gcloud_project_id()
        subscription_name = _config_.get_gcloud_subscription_name()

        subscriber = pubsub_v1.SubscriberClient()
        subscription_path = subscriber.subscription_path(project_id, subscription_name)

        def callback(message):
            logging.info('Received message: {}'.format(message.data))
            received_data = json.loads(message.data.decode('utf-8'))
            t0 = time.time()
            conversion_service.convert_video(received_data['originPath'])
            t1 = time.time()
            database_service.update_item_status(received_data['uuid'], 'converted')
            database_service.set_conversion_time(received_data['uuid'], str(t1 - t0))
            message.ack()

        subscriber.subscribe(subscription_path, callback=callback)

        logging.info('Listening for messages on {}'.format(subscription_path))
        while True:
            time.sleep(60)
