import logging


from logging.handlers import RotatingFileHandler
# Create a rotating file handler with a max size of 10MB and 5 backups
file_handler = RotatingFileHandler('example3.log', maxBytes=10_000_000, backupCount=5)
file_handler.setLevel(logging.DEBUG)

logger = logging.getLogger(__name__)
# Add the file handler to the logger
logger.addHandler(file_handler)



# log some messages
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')
