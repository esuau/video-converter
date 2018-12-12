import yaml
import logging
import os

logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', level=logging.DEBUG)


class Configuration(object):

    def __init__(self):
        self.configuration_file = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'application.yml')
        self.configuration_data = None

        f = open(self.configuration_file, 'r')
        self.configuration_data = yaml.load(f.read())
        f.close()

    def get_gcloud_project_id(self):
        return self.configuration_data['gcloud']['project-id']

    def get_gcloud_subscription_name(self):
        return self.configuration_data['gcloud']['subscription-name']

    def get_database_name(self):
        return self.configuration_data['aws']['dynamodb']['name']

    def get_database_table(self):
        return self.configuration_data['aws']['dynamodb']['table']
