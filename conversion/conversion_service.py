import logging
import boto3
import ffmpy
import os
import shutil
import tempfile

from botocore.exceptions import ClientError


class ConversionService(object):

    def __init__(self, _config_):
        self.s3 = boto3.resource('s3')
        self.client = boto3.client('s3')
        self.configuration = _config_

    def convert_video(self, _origin_, _target_):
        extension = self.get_last_split(_origin_, '.')
        tempdir = tempfile.mkdtemp()
        input_file = os.path.join(tempdir, 'input.' + extension)
        output_file = os.path.join(tempdir, 'output.avi')
        try:
            self.s3.Bucket(self.configuration.get_bucket_name()).download_file(_origin_, input_file)
        except ClientError as e:
            if e.response['Error']['Code'] == "404":
                logging.error('The object does not exist.')
            else:
                raise
        ff = ffmpy.FFmpeg(
            inputs={input_file: None},
            outputs={output_file: '-y -vcodec mpeg4 -b 4000k -acodec mp2 -ab 320k'}
        )
        ff.run()
        self.client.upload_file(output_file, self.configuration.get_bucket_name(), _target_)
        shutil.rmtree(tempdir)

    @staticmethod
    def get_last_split(_string_, _delimiter_):
        split = _string_.split(_delimiter_)
        return split[len(split) - 1]
