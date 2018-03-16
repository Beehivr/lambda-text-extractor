import json
import re
from urllib.parse import unquote_plus

__name__ = 'pdf_to_search_text_formatter'

class PdfToSearchTextFormatter:

    def __init__(self, key_filter=None):
        self.key_filter = key_filter

    def format(self, event, source, text=''):
        filtered_key = self.filter_key(source['object']['key'])
        return json.dumps({
            'update_date': event['eventTime'],
            'length': len(text),
            'path': filtered_key,
            'raw_text': text
        })

    def filter_key(self, key):
        if(self.key_filter is not None):
            r = re.compile('.*'+self.key_filter)
            key = r.sub('', key)
            key = unquote_plus(key)
        return key
