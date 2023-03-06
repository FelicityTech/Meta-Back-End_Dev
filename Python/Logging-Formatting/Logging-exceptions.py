import logging
logger = logging.getLogger(__name__)
try:
    #Some code that might raise an exception
    raise ValueError('oops')
except ValueError:
    # Log the exception traceback
    logger.exception('An error occurred')