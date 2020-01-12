"""
File_name: credit_card.py
Time: 01/03/2020
Author: Fluffy Fu
Description: Base Class for managing data from a credit card statement.
"""

class CreditCard:
    """
    Base class for handling credit card statement from different banks.
    """
    def __init__(self, file_path, file_name_regex):
        self._file_path = file_path
        self._file_name_regex = file_name_regex
        self._statement = self._load_statements()
        self._time_range = self._get_time_range()
        self._spending_categories = self._get_spending_categories()

    def _load_statements(self):
        """
        Load statemet(s) with given file_name_regex in the given file path.
        """
        raise NotImplementedError

    def _get_time_range(self):
        """
        Private method to retrieve the time range of the statements.
        """
        raise NotImplementedError

    def _get_spending_categories(self):
        """
        Private method to retrieve the spending categories in the statements.
        """
        raise NotImplementedError

    @property
    def statement(self):
        """
        Returns the read statements a pandas dataframe.
        """
        return self._statement

    @property
    def time_range(self):
        """
        Returns the start and end time of the available statements.

        tuple of datetime.date.
        """
        return self._time_range

    @property
    def spending_categories(self):
        """
        Returns a list of spending_categories given by a specific bank.

        a list of string.
        """
        return self._spending_categories

    def date_filter(self, start=None, end=None):
        """
        Filter the statement based on the given time.

        Args:
            start (datetime.datetime): transaction date >= start will be kept.
            If None, no filter will be applied. Default = None.

            end (datetime.datetime): transaction date <= end will be kept.
            If None, no filter will be applied. Default = None.
        """
        result = self._statement
        if start:
            result = result[self._statement[self.date_col] >= start]
        if end:
            result = result[self._statement[self.date_col] <= end]

        return result
