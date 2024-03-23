from .data_analyzer import DataAnalyzer


class DataProcessor:
    def __init__(self):
        """
        Initializes the DataProcessor with a new DataAnalyzer instance.
        """
        self.analyzer = DataAnalyzer()

    def analyze_data(self, data):
        """
        Analyzes the given data using the DataAnalyzer.

        Args:
            data: The data to be analyzed.

        Returns:
            The result of the data analysis.
        """
        return self.analyzer.analyze(data)
