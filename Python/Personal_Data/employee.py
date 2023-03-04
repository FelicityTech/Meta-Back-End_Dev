import logging


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(levelname)s:%(name)s:%(message)s')

file_handler = logging.FileHandler('employee.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

# logging.basicConfig(filename='employee.log', level=logging.INFO,
                    # format='%(levelname)s:%(message)s')
class Employee:
    """A simple Employee class"""


    def __init__(self, first, last):
        self.first = first
        self.last = last

        logger.info(f'Created Employee: {self.fullname} - {self.email}')



    @property
    def email(self):
        return (f'{self.first}.{self.last}@email.com')
    
    @property
    def fullname(self):
        return (f'{self.first} {self.last}')
    
emp_1 = Employee('John', 'Smith')
emp_2 = Employee('Corey', 'Schafer')
emp_3 = Employee('Japheth', 'Adebare')