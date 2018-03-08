import boto3
import botocore
import simple_logger
import re
import urllib

logger=simple_logger.logger()

__name__='s3_event'


class S3Event:
    def __init__(self, event):
        logger.info('INIT S3Event')
        logger.info(event)
        self.s3 = boto3.client('s3')
        self.event = event
        self.source = event['s3']
        self.bucket = self.source['bucket']['name']
        self.key = self.__decode_key(self.source['object']['key'])
        self.etag = self.source['object']['eTag']
        self.size = self.source['object']['size']
        self.arn = self.source['bucket']['arn'] + self.source['bucket']['name']
        self.uri = None
        self.formatter = None

    def document_uri(self):
        if(self.uri == None):
            self.uri = self.s3.generate_presigned_url(
                ClientMethod='get_object',
                Params={
                    'Bucket': self.bucket,
                    'Key': self.key
                }
            )
        return self.uri

    def change_file_extension(self, ext):
        if(ext[0] != '.'):
            ext = '.'+ext
        return '.'.join(self.key.split('.')[0:-1])+ext

    def get_content(self):
        response = self.s3.get_object(
            Bucket = self.bucket,
            Key = self.key
        )
        return response['Body']


    def put_content(self, new_key, body):
        logger.info('----------------------------------------------------------------')
        logger.info('Writing > ' + self.bucket+'/'+new_key)
        logger.info('Writing > ' + body)
        logger.info('----------------------------------------------------------------')
        self.s3.put_object(
            Bucket = self.bucket,
            Body = self.formatter.format(event = self.event, source=self.source, text=body),
            Key = new_key
        )

    def __decode_key(self, key):
        return urllib.parse.unquote_plus(key)
