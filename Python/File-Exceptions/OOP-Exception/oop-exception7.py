class CustomException(Exception):
    def __init__(self, message, error_code):
        self.message = message
        self.error_code = error_code
        super().__init__(message)


try:
    raise CustomException("Something went wrong", 500)
except CustomException as e:
    print(f"Error code: {e.error_code} - Message: {e.message}")