import logging

#Create a custom logger

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


# Create a file handler and set the log level
file_handler = logging.FileHandler('example2.log')
file_handler.setLevel(logging.DEBUG)


# Create a console handler and set the log level
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.ERROR)


# Create a log message format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Add the formatter to the handlers
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)


#Add the handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# Log some messages
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')

