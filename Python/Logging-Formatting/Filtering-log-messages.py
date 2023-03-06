import logging

class InfoFilter(logging.Filter):
    def filter(self, record):
        return record.levelno == logging.INFO
    


# Creating a custom logger with an info filter
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


# Add a file handler with a custom formatter and the info filter
file_handler = logging.FileHandler('example5.log')
file_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
file_handler.addFilter(InfoFilter())

# add the handlers to the logger
logger.addHandler(file_handler)


# Log some messages
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')