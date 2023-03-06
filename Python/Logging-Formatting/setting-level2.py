import logging

# Create a custom logger with a file handler

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


file_handler = logging.FileHandler('mylog.log')
file_handler.setLevel(logging.DEBUG)



formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)


logger.addHandler(file_handler)


#log some messages
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message ')
logger.error('This is an error message')
logger.critical('This is a critical message')