import aws_events.event_parser
import simple_extractor
import simple_logger
import os
import re
import json
from aws_events import factory
from utils import get_ext
from content_formatters.pdf_to_search_text_formatter import PdfToSearchTextFormatter

S3_OBJ_PREFIX_FILTER = os.environ.get('PREFIX_FILTER', 'library/draft/')
S3_OBJ_TARGET_PREFIX = S3_OBJ_PREFIX_FILTER+'.metadata/'

logger = simple_logger.logger()

def handle(event, context):
    logger.info(json.dumps(event))
    aws_event = aws_events.event_parser.EventParser(event)
    logger.info(aws_event.event_types())
    event = True
    while event:
        event = aws_event.next_event('s3')
        logger.info(event)
        if(event is not None):
            event_klass = factory.instantiate('s3', event)
            event_klass.formatter = PdfToSearchTextFormatter(key_filter=S3_OBJ_PREFIX_FILTER)

            ext = get_ext(event_klass.key)
            logger.info(ext)

            try:
                status, text = simple_extractor.extract(event_handler=event_klass, ext=ext, disable_ocr=False )
                if (status=='ok'):
                    new_file = event_klass.change_file_extension('json')
                    new_file = get_target_key(new_file)
                    logger.info(new_file)
                    event_klass.put_content(new_file, text)
                elif (status=='ocr'):
                    logger.info('>>> Sending to OCR lambda')

            except Exception as e:
                logger.exception('Extraction exception for <{}>'.format(event_klass.key))
            #end try


def get_target_key(key):
    r = re.compile('('+S3_OBJ_PREFIX_FILTER+')')
    return r.sub(S3_OBJ_TARGET_PREFIX, key)


    # TODO: if the status is ocr, forward the task to the OCR to Txt Lambda
    #
    # payload = event.copy()
    # if not disable_ocr and fallback_to_ocr:
    #     response = lambda_client.invoke(
    #         FunctionName=TEXTRACTOR_OCR,
    #         InvocationType='Event',
    #         LogType='None',
    #         Payload=json.dumps(payload)
    #     )
    #     response['Payload'] = response['Payload'].read().decode('utf-8')
    #     textractor_results = dict(method='ocr', size=-1, success=False)
    #     logger.info('Invoked OCR lambda <{}> with payload {}.\nResponse is {}'.format(TEXTRACTOR_OCR, json.dumps(payload), response))
    #
    # else:
    #     payload['text_uri'] = text_uri
    #
    #     for cb in event.get('callbacks', []):
    #         if cb['step'] == 'textractor':
    #             try:
    #                 uri_dump(cb['uri'], json.dumps(payload), mode='w')
    #                 logger.info('Called callback {} with payload {}.'.format(json.dumps(cb), json.dumps(payload)))
    #
    #             except Exception as e: logger.exception('Callback exception for {} with payload {}.'.format(json.dumps(cb), json.dumps(payload)))
    #         #end if
    #     #end for
    # #end if
    #
    # payload.setdefault('results', {})
    # payload['results']['textractor'] = textractor_results
    # logger.info('Textraction complete.')
    #
    # return payload
