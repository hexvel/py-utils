import statistics


class DataAnalyzer:
    def analyze(self, data):
        """
        Analyzes the given data by calculating the mean, median, and standard deviation.

        Args:
            data: A list of numbers to analyze.

        Returns:
            A tuple of (mean, median, standard deviation) values.
        """
        mean = statistics.mean(data)
        median = statistics.median(data)
        std_dev = statistics.stdev(data)

        return mean, median, std_dev
