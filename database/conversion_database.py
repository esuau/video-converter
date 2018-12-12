import logging
import boto3


class ConversionDatabase(object):

    def __init__(self, _config_):
        dynamodb = boto3.resource(_config_.get_database_name(), region_name='eu-west-3')
        self.table = dynamodb.Table(_config_.get_database_table())
        logging.info(self.table.creation_date_time)

    def update_item_status(self, _id_, _status_):
        self.table.update_item(
            Key={'uuid': _id_},
            UpdateExpression='SET video_status = :status',
            ExpressionAttributeValues={':status': _status_}
        )
        response = self.table.get_item(Key={{'uuid': _id_}})
        item = response['Item']
        logging.info(item)
