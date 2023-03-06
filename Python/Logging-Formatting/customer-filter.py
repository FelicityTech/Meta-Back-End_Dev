import re, logging


class PIIFilter(logging.Filter):
    def __init__(self, fields):
        super().__init__()
        self.fields = fields



    def filter(self, record):
        for field in self.fields:
            if hasattr(record, 'args') and isinstance(record.args, tuple):
                for i, arg in enumerate(record.args):
                    if field in str(arg):
                        record.args = tuple(
                    x if i != j else re.sub(r'([^\s]{2,})', lambda m: '*' * (len(m.group())-2) + m.group()[-2:], x)
                    for j, x in enumerate(record.args)
                        )
                        break
        return True
    
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

handler = logging.FileHandler('example5.log')
handler.setLevel(logging.DEBUG)

# set up the formatter
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
handler.setFormatter(formatter)

# add the filter to the handler
handler.addFilter(PIIFilter(['email', 'phone', 'ssn', 'credit_card']))

# add the handler to the logger
logger.addHandler(handler)

# test the logger
logger.debug('Here is some PII: email=jane.smith@example.com, phone=555-1234, ssn=123-45-6789, credit_card=1111-2222-3333-4444')
