import logging
from logging.handlers import TimedRotatingFileHandler

# Create a custom logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


# Create a timed rotating file handler that rotates every day
file_handler = TimedRotatingFileHandler('example4.log', when='midnight')
file_handler.setLevel(logging.DEBUG)
logger = logging
# Add the file handler to the logger
logger.Handler(file_handler)

# Log some messages
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')