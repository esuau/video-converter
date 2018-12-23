import time
import logging
import json

from google.cloud import pubsub_v1


class ConversionMessaging(object):

    def __init__(self, _config_, database_service, conversion_service):
        self.database_service = database_service
        self.conversion_service = conversion_service

        project_id = _config_.get_gcloud_project_id()
        subscription_name = _config_.get_gcloud_subscription_name()

        subscriber = pubsub_v1.SubscriberClient()
        subscription_path = subscriber.subscription_path(project_id, subscription_name)
        subscriber.subscribe(subscription_path, callback=self.receive_message)

        logging.info('Listening for messages on {}'.format(subscription_path))
        while True:
            time.sleep(60)

    def receive_message(self, message):
        logging.info('Received message: {}'.format(message.data))
        self.process_message(json.loads(message.data.decode('utf-8')))
        message.ack()

    def process_message(self, _data_):
        origin_path = _data_['originPath']
        target_path = _data_['targetPath']
        self.database_service.update_item_status(_data_['uuid'], 'in progress')
        t0 = time.time()
        try:
            self.conversion_service.convert_video(origin_path, target_path)
        except:
            self.database_service.update_item_status(_data_['uuid'], 'aborted')
            return
        t1 = time.time()
        self.database_service.update_item_status(_data_['uuid'], 'converted')
        self.database_service.set_conversion_time(_data_['uuid'], str(t1 - t0))
