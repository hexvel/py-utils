class StringUtils:
    """A class containing utility methods for working with strings and text."""

    @staticmethod
    def split_string(s: str, separator: str) -> list:
        """Splits a string into a list of substrings using a separator.

        Args:
            s (str): The string to split.
            separator (str): The separator to use for splitting.

        Returns:
            list: A list of substrings.
        """
        return s.split(separator)

    @staticmethod
    def join_strings(string_list: list, separator: str) -> str:
        """Joins a list of strings into a single string using a separator.

        Args:
            string_list (list): The list of strings to join.
            separator (str): The separator to use for joining.

        Returns:
            str: The joined string.
        """
        return separator.join(string_list)

    @staticmethod
    def find_substring(s: str, substring: str) -> int:
        """Finds the index of the first occurrence of a substring in a string.

        Args:
            s (str): The string to search.
            substring (str): The substring to find.

        Returns:
            int: The index of the first occurrence of the substring, or -1 if not found.
        """
        return s.find(substring)

    @staticmethod
    def replace_substring(s: str, old_substring: str, new_substring: str) -> str:
        """Replaces all occurrences of an old substring with a new substring in a string.

        Args:
            s (str): The string to modify.
            old_substring (str): The substring to replace.
            new_substring (str): The new substring to use.

        Returns:
            str: The modified string.
        """
        return s.replace(old_substring, new_substring)

    @staticmethod
    def is_number(s: str) -> bool:
        """Checks if a string can be converted to a number.

        Args:
            s (str): The string to check.

        Returns:
            bool: True if the string can be converted to a number, False otherwise.
        """
        try:
            float(s)
            return True
        except ValueError:
            return False

    @staticmethod
    def to_upper(s: str) -> str:
        """Converts a string to uppercase.

        Args:
            s (str): The string to convert.

        Returns:
            str: The converted string.
        """
        return s.upper()

    @staticmethod
    def to_lower(s: str) -> str:
        """Converts a string to lowercase.

        Args:
            s (str): The string to convert.

        Returns:
            str: The converted string.
        """
        return s.lower()

    @staticmethod
    def format_string(s: str, args: tuple) -> str:
        """Formats a string using a tuple of arguments.

        Args:
            s (str): The string to format.
            args (tuple): The tuple of arguments to use for formatting.

        Returns:
            str: The formatted string.
        """
        return s.format(*args)

    @staticmethod
    def parse_integer(s: str) -> int:
        """Parses a string as an integer.

        Args:
            s (str): The string to parse.

        Returns:
            int: The parsed integer.
        """
        return int(s)

    @staticmethod
    def parse_float(s: str) -> float:
        """Parses a string as a float.

        Args:
            s (str): The string to parse.

        Returns:
            float: The parsed float.
        """
        return float(s)
