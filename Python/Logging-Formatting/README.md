# Logging to Files, Setting Levels, and Formatting

1. [log-message for different level](log-message.py)

    The Python standard library includes the logging module, which provides a powerful and flexible way to log messages to a file or other output destination.

2. [log-with features of format](log-formating.py)

     the logging module provides a variety of other features, such as the ability to set custom log levels, format log messages, and configure loggers for different parts of an application. Here's an example of how to configure a custom log level and format log messages

3. [custom log for different part of app](custom-log.py)

      create a custom logger object and use it to log messages from different parts of our application. Here's an example of how to configure a custom logger
      a custom logger object using the getLogger() function, and set its log level to DEBUG. We also create a file handler and a console handler, and set their log levels

4. [Rotating log file](Rotating-log-file.py)

    Rotating log files: You can use the RotatingFileHandler class to automatically rotate log files based on size or time. This can be useful for managing disk space and keeping log files organized.

5. [Timed rotating log files](Time-Rotating-log.py)

    Timed rotating log files: You can use the TimedRotatingFileHandler class to automatically rotate log files based on a time interval, such as daily or hourly

6. [Logging exceptions](logging-exceptions.py)

    You can use the exception() method of a logger object to log an exception traceback

7. [Filtering log messages](Filtering-log-messages.py)

    You can use the Filter class to selectively filter log messages based on their level, message, or other attributes
    we define a custom filter class called InfoFilter that only allows log messages with a level of INFO or higher. We then create a custom logger and add a file handler with the InfoFilter filter
