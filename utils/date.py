import datetime
from dataclasses import dataclass


@dataclass
class DateTime:
    year: int
    month: int
    day: int
    hour: int
    minute: int
    second: int


class DateTimeUtils:
    @staticmethod
    def get_current_datetime() -> DateTime:
        """
        Function to get the current date and time.

        :return: current date and time
        """
        current_datetime = datetime.datetime.now()
        return DateTime(
            year=current_datetime.year,
            month=current_datetime.month,
            day=current_datetime.day,
            hour=current_datetime.hour,
            minute=current_datetime.minute,
            second=current_datetime.second,
        )

    @staticmethod
    def get_specific_datetime(
        year: int, month: int, day: int, hour: int = 0, minute: int = 0, second: int = 0
    ) -> DateTime:
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
        return DateTime(
            year=year, month=month, day=day, hour=hour, minute=minute, second=second
        )

    @staticmethod
    def format_datetime(datetime_obj: DateTime, format_str: str) -> str:
        """
        Function to work with different date and time formats.

        :param datetime_obj: date and time object
        :param format_str: format string
        :return: formatted date and time string
        """
        formatted_datetime = datetime.datetime(
            datetime_obj.year,
            datetime_obj.month,
            datetime_obj.day,
            datetime_obj.hour,
            datetime_obj.minute,
            datetime_obj.second,
        )
        formatted_datetime_str = formatted_datetime.strftime(format_str)
        return formatted_datetime_str

    @staticmethod
    def calculate_time_difference(
        datetime_obj1: DateTime, datetime_obj2: DateTime
    ) -> datetime.timedelta:
        """
        Function to calculate the difference between dates.

        :param datetime_obj1: first date and time object
        :param datetime_obj2: second date and time object
        :return: time difference
        """
        datetime1 = datetime.datetime(
            datetime_obj1.year,
            datetime_obj1.month,
            datetime_obj1.day,
            datetime_obj1.hour,
            datetime_obj1.minute,
            datetime_obj1.second,
        )
        datetime2 = datetime.datetime(
            datetime_obj2.year,
            datetime_obj2.month,
            datetime_obj2.day,
            datetime_obj2.hour,
            datetime_obj2.minute,
            datetime_obj2.second,
        )
        time_difference = datetime1 - datetime2
        return time_difference

    @staticmethod
    def add_time_to_datetime(
        datetime_obj: DateTime, time_delta: datetime.timedelta
    ) -> DateTime:
        """
        Function to add time to a date.

        :param datetime_obj: date and time object
        :param time_delta: time interval to add
        :return: new date and time object
        """
        datetime1 = datetime.datetime(
            datetime_obj.year,
            datetime_obj.month,
            datetime_obj.day,
            datetime_obj.hour,
            datetime_obj.minute,
            datetime_obj.second,
        )
        new_datetime = datetime1 + time_delta
        return DateTime(
            year=new_datetime.year,
            month=new_datetime.month,
            day=new_datetime.day,
            hour=new_datetime.hour,
            minute=new_datetime.minute,
            second=new_datetime.second,
        )

    @staticmethod
    def subtract_time_from_datetime(
        datetime_obj: DateTime, time_delta: datetime.timedelta
    ) -> DateTime:
        """
        Function to subtract time from a date.

        :param datetime_obj: date and time object
        :param time_delta: time interval to subtract
        :return: new date and time object
        """
        datetime1 = datetime.datetime(
            datetime_obj.year,
            datetime_obj.month,
            datetime_obj.day,
            datetime_obj.hour,
            datetime_obj.minute,
            datetime_obj.second,
        )
        new_datetime = datetime1 - time_delta
        return DateTime(
            year=new_datetime.year,
            month=new_datetime.month,
            day=new_datetime.day,
            hour=new_datetime.hour,
            minute=new_datetime.minute,
            second=new_datetime.second,
        )

    @staticmethod
    def get_year(datetime_obj: DateTime) -> int:
        """
        Function to get the year from a date.

        :param datetime_obj: date and time object
        :return: year
        """
        return datetime_obj.year

    @staticmethod
    def get_month(datetime_obj: DateTime) -> int:
        """
        Function to get the month from a date.

        :param datetime_obj: date and time object
        :return: month
        """
        return datetime_obj.month

    @staticmethod
    def get_day(datetime_obj: DateTime) -> int:
        """
        Function to get the day from a date.

        :param datetime_obj: date and time object
        :return: day
        """
        return datetime_obj.day

    @staticmethod
    def get_hour(datetime_obj: DateTime) -> int:
        """
        Function to get the hour from a date.

        :param datetime_obj: date and time object
        :return: hour
        """
        return datetime_obj.hour

    @staticmethod
    def get_minute(datetime_obj: DateTime) -> int:
        """
        Function to get the minute from a date.

        :param datetime_obj: date and time object
        :return: minute
        """
        return datetime_obj.minute

    @staticmethod
    def get_second(datetime_obj: DateTime) -> int:
        """
        Function to get the second from a date.

        :param datetime_obj: date and time object
        :return: second
        """
        return datetime_obj.second

    @staticmethod
    def get_weekday(datetime_obj: DateTime) -> int:
        """
        Function to get the weekday from a date (Monday = 0, Sunday = 6).

        :param datetime_obj: date and time object
        :return: weekday
        """
        datetime1 = datetime.datetime(
            datetime_obj.year,
            datetime_obj.month,
            datetime_obj.day,
            datetime_obj.hour,
            datetime_obj.minute,
            datetime_obj.second,
        )
        return datetime1.weekday()

    @staticmethod
    def is_leap_year(year: int) -> bool:
        """
        Function to check if a year is a leap year.

        :param year: year
        :return: True if it is a leap year, False otherwise
        """
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
