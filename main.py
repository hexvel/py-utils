import datetime

from utils import DateTimeUtils

if __name__ == "__main__":
    current_datetime = DateTimeUtils.get_current_datetime()
    specific_datetime = DateTimeUtils.get_specific_datetime(2022, 10, 1, 12, 30)
    formatted_datetime = DateTimeUtils.format_datetime(
        specific_datetime, "%Y-%m-%d %H:%M:%S"
    )
    datetime1 = DateTimeUtils.get_specific_datetime(2022, 1, 1)
    datetime2 = DateTimeUtils.get_specific_datetime(2022, 1, 15)
    time_difference = DateTimeUtils.calculate_time_difference(datetime2, datetime1)
    new_datetime = DateTimeUtils.add_time_to_datetime(
        datetime1, datetime.timedelta(days=7)
    )
    new_datetime = DateTimeUtils.subtract_time_from_datetime(
        datetime2, datetime.timedelta(weeks=2)
    )
    year = DateTimeUtils.get_year(specific_datetime)
    month = DateTimeUtils.get_month(specific_datetime)
    day = DateTimeUtils.get_day(specific_datetime)
    hour = DateTimeUtils.get_hour(specific_datetime)
    minute = DateTimeUtils.get_minute(specific_datetime)
    second = DateTimeUtils.get_second(specific_datetime)
    weekday = DateTimeUtils.get_weekday(specific_datetime)
    is_leap = DateTimeUtils.is_leap_year(2022)

    print(year, month, day, hour, minute, second, weekday, is_leap)
