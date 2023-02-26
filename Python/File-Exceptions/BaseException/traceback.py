import traceback

try:
    x = 1 / 0
except ZeroDivisionError as e:
    tb = traceback.format_exc()
    raise ZeroDivisionError("Custom message").with_traceback(e.__traceback__) from None