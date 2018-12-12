import logging

from configuration.configuration import Configuration
from messaging.conversion_messaging import ConversionMessaging
from database.conversion_database import ConversionDatabase
from conversion.conversion_service import ConversionService

if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', level=logging.DEBUG)
    configuration = Configuration()

    database = ConversionDatabase(configuration)
    conversion = ConversionService(configuration)
    video_messaging = ConversionMessaging(configuration, database, conversion)
