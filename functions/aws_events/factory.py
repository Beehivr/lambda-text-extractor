from aws_events.s3_event import S3Event
import simple_logger
logger=simple_logger.logger()

event_types={
    's3': S3Event
}

__name__ = 'factory'

def instantiate(type, event):
    if (type in event_types):
        return event_types[type](event)
    return None
