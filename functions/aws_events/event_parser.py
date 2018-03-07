import json
import simple_logger

__name__ = 'event_parser'
logger = simple_logger.logger()


class EventParser:
    def __init__(self, event):
        self.source_event = event
        self.event_iterators={}
        self.classified_events={}
        self.classify_events()
    # end __init__

    def classify_events(self):
        for record in self.source_event['Records']:
            event_source = record.get('eventSource', record.get('EventSource'))
            if(event_source is None): continue
            source = event_source.split(':')[-1]
            if(source == 'sns'):
                self.parse_sns_event(record['Sns'])
                continue
            elif( source not in self.classified_events):
                self.classified_events[source] = []
                self.event_iterators[source] = 0
            self.classified_events[source].append(record)

    # end classify_events

    def event_types(self):
        logger.info('event_type')
        types=[]
        for record in self.source_event['Records']:
            logger.info(record)
            event_source = record.get('eventSource', record.get('EventSource'))
            if(event_source is None): continue
            source = event_source.split(':')[-1]
            if(source == 'sns'): continue
            types.append(source)

        logger.info(types)
        return list(set(types))
    # end event_types

    def next_event(self, type):
        if(type not in self.event_iterators):
            self.reset_iterator(type)
        if(self.event_iterators[type] >= len(self.classified_events[type])):
            return None
        event = self.classified_events[type][self.event_iterators[type]]
        self.event_iterators[type]+=1
        return event
    # end next_event

    def reset_iterator(self, type):
        self.event_iterators[type]=0
    # end reset_iterator

    def parse_sns_event(self, sns_event):
        new_records = json.loads(sns_event['Message'])
        for record in new_records['Records']:
            self.source_event['Records'].append(record)
