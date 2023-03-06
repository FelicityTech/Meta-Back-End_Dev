import logging
import re

class PIIFilter(logging.Filter):
    def __init__(self, fields):
        self.fields = fields
        self.pattern = re.compile(r'(?i)(' + '|'.join(fields) + ')')


    def filter(self, record):
        if record.args:
            args = list(record.args)
            for i, arg in enumerate(args):
                if isinstance(arg, str) and self.pattern.search(arg):
                    args[i] = re.sub(r'\b\w{4,}\b', '***')