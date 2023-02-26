import traceback

class CustomException(Exception):
    def __init__(self, message):
        self.message = message
        self.traceback = traceback.format_exc()



try:
    raise CustomException("Something went wrong")
except CustomException as e:
    print(f"Error message: {e.message}\nTraceback: {e.traceback}")