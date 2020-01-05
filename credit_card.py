"""
File_name: credit_card.py
Time: 01/03/2020
Auther: Xinlin Song
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

    def _load_statements(self):
        """
        Load statemet(s) with given file_name_regex in the given file path.
        """
        pass

    @property
    def statement(self):
        return self._statement

    @property
    def time_range(self):
        """
        Returns the start and end time of the available statements.

        tuple of datetime.date.
        """
        pass

    @property
    def spending_categories(self):
        """
        Returns a list of spending_categories given by a specific bank.

        a list of string.
        """
        pass
