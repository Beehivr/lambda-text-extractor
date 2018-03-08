import os
import sys
import logging

__name__='simple_logger'

LOG_LEVELS = {
    'debug': logging.DEBUG,
    'info': logging.INFO,
    'warn': logging.WARN,
    'error': logging.ERROR,
    'critical': logging.CRITICAL
}
LOG_LEVEL=LOG_LEVELS[os.environ.get('LOG_LEVEL', 'error')]

def logger():
    logger = logging.getLogger()
    logger.setLevel(LOG_LEVEL)
    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(LOG_LEVEL)
    # formatter = logging.Formatter('%(filename)s - %(lineno)d - %(asctime)s - %(name)s - %(levelname)s - %(message)s')
    formatter = logging.Formatter('%(name)s - %(lineno)d - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    # logger.addHandler(ch)
    return logger
