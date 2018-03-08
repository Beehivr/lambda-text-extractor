import simple_logger
from utils import get_ext
from urllib.parse import urlparse


logger=simple_logger.logger()

__name__='s3_event'


class ApiEvent:
    def __init__(self, event):
        logger.info('INIT ApiEvent')
        logger.info(event)
        self.event = event
        self.key = event['document_uri']
        self.formatter = DefautFormatter()


    def document_uri(self):
        return uri

    def change_file_extension(self, ext):
        if(ext[0]!='.'):
            ext = '.'+ext
        return '.'.join(self.key.split('.')[0:-1])+ext

    def get_content(self):
        return uri_read(self.document_uri(), mode='rb')


    def put_content(self, new_key, body):
        uri_dump(new_key, formatter.format(self, body), mode='w', textio_args={'errors': 'ignore'}, storage_args=dict(ContentType='text/plain', Metadata=dict(Exception=str(e))))
