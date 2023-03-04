import logging
import employee

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')

file_handler = logging.FileHandler('sample1.log')
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

# DEBUG Detailed information, typically of interest
#  only when diagnosing problems.

#INFO: Configuration that things are working as expected

#WARNING: An indication that soemthing unexpected
#  happened, or indicative of some problem in 
# the near future(e.g 'disk space low'
# the software is still working as expected
#ERROR: Due to a more serious problem, the software 
# has been able to perform some function.

# CRITICAL: A serious error, indicating that the program 
# itself may be unable to continue running.

# logging.basicConfig(filename='test.log', level=logging.DEBUG, format='%(asctime)s:%(name)s:%(levelname)s:%(message)s')

def add(x, y):
    """Add Function"""
    return x + y


def subtract(x, y):
    """Subtract Function"""
    return x - y

def multiply(x, y):
    """Multiply Function"""
    return x * y

def divide(x, y):
    """Divide Function"""
    # if y == 0:
    #     raise ValueError("Can not divide by zero!")
    return x / y


num_1 = 20
num_2 = 10

add_result = add(num_1, num_2)
logger.debug(f'Add: {num_1} + {num_2} = {add_result}')

sub_result = subtract(num_1, num_2)
logger.debug(f'Add: {num_1} - {num_2} = {sub_result}')

mul_result = multiply(num_1, num_2)
logger.debug(f'Add: {num_1} * {num_2} = {mul_result}')

div_result = divide(num_1, num_2)
logger.debug(f'Add: {num_1} / {num_2} = {div_result}')
