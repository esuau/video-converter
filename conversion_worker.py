import logging

from configuration.configuration import Configuration
from messaging.conversion_messaging import VideoConversionMessaging

if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', level=logging.DEBUG)
    configuration = Configuration()

    video_messaging = VideoConversionMessaging(configuration)
