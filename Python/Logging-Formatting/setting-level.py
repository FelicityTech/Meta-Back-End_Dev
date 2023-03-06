import logging

class CustomFilter(logging.Filter):
    def filter(self, record):
        return 'error' in record.getMessage().lower()

# Create a custom logger with a console handler
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

console_handler = logging.FileHandler('mylog0.log')
console_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)

# Add a custom filter to the console handler
console_handler.addFilter(CustomFilter())

logger.addHandler(console_handler)

# Log some messages
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')
