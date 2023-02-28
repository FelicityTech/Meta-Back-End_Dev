def add(x: int, y: int) -> int:
    """Add Function"""
    return x + y


def subtract(x: int ,y: int) -> int:
    """Subtract Function"""
    return x - y

def multiply(x: int, y: int) -> int:
    """Multiply Function"""
    return x * y

def divide(x: int, y: int) -> int:
    """Divide Function"""
    if y == 0:
        raise ValueError("Can not divide by zero!")
    return x / y