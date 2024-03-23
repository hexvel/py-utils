import datetime

from commands import DateTimeUtils

if __name__ == "__main__":
    # Get current date and time
    current_datetime = DateTimeUtils.get_current_datetime()
    print("Current Date and Time:", current_datetime)

    # Create a specific date and time
    specific_datetime = DateTimeUtils.get_specific_datetime(2022, 10, 1, 12, 30)
    print("Specific Date and Time:", specific_datetime)

    # Format the date and time
    formatted_datetime = DateTimeUtils.format_datetime(
        specific_datetime, "%Y-%m-%d %H:%M:%S"
    )
    print("Formatted Date and Time:", formatted_datetime)

    # Calculate the difference between two dates
    datetime1 = DateTimeUtils.get_specific_datetime(2022, 1, 1)
    datetime2 = DateTimeUtils.get_specific_datetime(2022, 1, 15)
    time_difference = DateTimeUtils.calculate_time_difference(datetime2, datetime1)
    print("Time Difference:", time_difference)

    # Add time to a date
    new_datetime = DateTimeUtils.add_time_to_datetime(
        datetime1, datetime.timedelta(days=7)
    )
    print("New Date and Time (After adding 7 days):", new_datetime)

    # Subtract time from a date
    new_datetime = DateTimeUtils.subtract_time_from_datetime(
        datetime2, datetime.timedelta(weeks=2)
    )
    print("New Date and Time (After subtracting 2 weeks):", new_datetime)
