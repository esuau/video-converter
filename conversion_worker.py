import logging

from configuration.configuration import Configuration
from messaging.conversion_messaging import ConversionMessaging
from database.conversion_database import ConversionDatabase

if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', level=logging.DEBUG)
    configuration = Configuration()

    database = ConversionDatabase(configuration)
    video_messaging = ConversionMessaging(configuration, database)
