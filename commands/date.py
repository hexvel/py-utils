import datetime


class DateTimeUtils:
    @staticmethod
    def get_current_datetime():
        """
        Function to get the current date and time.

        :return: current date and time
        """
        current_datetime = datetime.datetime.now()
        return current_datetime

    @staticmethod
    def get_specific_datetime(year, month, day, hour=0, minute=0, second=0):
        """
        Function to work with specific dates and time intervals.

        :param year: year
        :param month: month
        :param day: day
        :param hour: hour (default 0)
        :param minute: minute (default 0)
        :param second: second (default 0)
        :return: specific date and time
        """
        specific_datetime = datetime.datetime(year, month, day, hour, minute, second)
        return specific_datetime

    @staticmethod
    def format_datetime(datetime_obj, format_str):
        """
        Function to work with different date and time formats.

        :param datetime_obj: date and time object
        :param format_str: format string
        :return: formatted date and time string
        """
        formatted_datetime = datetime_obj.strftime(format_str)
        return formatted_datetime

    @staticmethod
    def calculate_time_difference(datetime_obj1, datetime_obj2):
        """
        Function to calculate the difference between dates.

        :param datetime_obj1: first date and time object
        :param datetime_obj2: second date and time object
        :return: time difference
        """
        time_difference = datetime_obj1 - datetime_obj2
        return time_difference

    @staticmethod
    def add_time_to_datetime(datetime_obj, time_delta):
        """
        Function to add time to a date.

        :param datetime_obj: date and time object
        :param time_delta: time interval to add
        :return: new date and time object
        """
        new_datetime = datetime_obj + time_delta
        return new_datetime

    @staticmethod
    def subtract_time_from_datetime(datetime_obj, time_delta):
        """
        Function to subtract time from a date.

        :param datetime_obj: date and time object
        :param time_delta: time interval to subtract
        :return: new date and time object
        """
        new_datetime = datetime_obj - time_delta
        return new_datetime
