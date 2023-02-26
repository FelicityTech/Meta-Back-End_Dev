class CustomException(Exception):
    def __init__(self, message, cause=None):
        self.message = message
        self.cause = cause
        super().__init__(message)


try:
    raise CustomException("Something went wrong", ValueError("Invalid value"))
except CustomException as e:
    print(f"Error message: {e.message}\nCause: {e.cause}")