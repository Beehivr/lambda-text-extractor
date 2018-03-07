import aws_events.event_parser
import ocr_extractor
import simple_logger
from aws_events import factory
from utils import get_ext

logger = simple_logger.logger()

def handler(event, context):
    aws_event = aws_events.event_parser.EventParser(event)
    logger.info(aws_event.event_types())
    event = True
    while event:
        event = aws_event.next_event('s3')
        logger.info(event)
        if(event is not None):
            event_klass = factory.instantiate('s3', event)
            new_file = event_klass.change_file_extension('txt')
            logger.info(new_file)
            # ext = get_ext(event_klass.key)
            # logger.info(ext)

            try:
                status, text = ocr_extractor.extract( {"document_uri": event_klass.document_uri(), "page": None }, context )
                if (status=='ok'):
                    event_klass.put_content(new_file, text)
                elif (status=='ocr'):
                    logger.info('>>> Sending to OCR lambda')

            except Exception as e:
                logger.exception('Extraction exception for <{}>'.format(event_klass.key))
            #end try
