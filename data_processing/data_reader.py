import pandas as pd


class DataReader:
    def read_csv(self, file_path):
        """
        Reads a CSV file and returns a pandas DataFrame.

        Args:
            file_path (str): The path to the CSV file.

        Returns:
            pd.DataFrame: A pandas DataFrame containing the data from the CSV file.
        """
        data = pd.read_csv(file_path)
        return data


class XMLReport:
    def __init__(self, count, attributes, values):
        self.count = count
        self.attributes = attributes
        self.values = values
