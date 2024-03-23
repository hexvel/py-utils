import multiprocessing as mp

from .data_analyzer import DataAnalyzer


class ParallelDataProcessor:
    """
    A class that processes data in parallel using multiprocessing.

    Attributes:
        analyzer (DataAnalyzer): An instance of the DataAnalyzer class.
    """

    def __init__(self):
        """
        Initializes the ParallelDataProcessor with a new DataAnalyzer instance.
        """
        self.analyzer = DataAnalyzer()

    def process_data(self, data) -> list:
        """
        Processes data in parallel using multiprocessing.

        Args:
            data (list): A list of data to be processed.

        Returns:
            list: A list of results after processing the data.
        """
        num_processes = mp.cpu_count()
        chunk_size = len(data) // num_processes

        with mp.Pool(processes=num_processes) as pool:
            results = [
                pool.apply_async(self.analyzer.analyze, args=(chunk,))
                for chunk in (
                    data[i : i + chunk_size] for i in range(0, len(data), chunk_size)
                )
            ]

        pool.close()
        pool.join()

        combined_results = [result.get() for result in results]
        return combined_results
