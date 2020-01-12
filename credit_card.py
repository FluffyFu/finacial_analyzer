"""
File_name: credit_card.py
Time: 01/03/2020
Author: Fluffy Fu
Description: Base Class for managing data from a credit card statement.
"""

from os import listdir
from os.path import isfile, join
import pandas as pd
import numpy as np

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
        file_names = self._get_file_names()

        if file_names:
            print('loading the following statements:')
            for f in file_names:
                print(f)
        else:
            raise Exception('No statement in directory: {}'.format(self._file_path))

        df = pd.concat([pd.read_csv(file_name) for file_name in file_names])
        return self._data_cleaning(df)

    def _get_time_range(self):
        """
        Private method to retrieve the time range of the statements.
        """
        min_date = self._statement[self.date_col].min()
        max_date = self._statement[self.date_col].max()
        return (min_date, max_date)

    def _get_spending_categories(self):
        """
        Private method to retrieve the spending categories in the statements.
        Return purchase categories in sorted order.
        """
        raw_cats = self._statement[self.category_col].unique().tolist()
        raw_cats.remove(np.nan)
        return sorted(raw_cats)

    def _get_file_names(self):
        """
        return a list of file names from the given file_path that matches the regex.
        """
        # TODO check the file type and handle possible file types (csv, xls)
        if self._file_name_regex:
            # TODO implement code to read files that match the given regex.
            # should get a list of matched file names.
            pass
        else:
            # When the regex is not given, read all the files in the directory.
            file_names = [join(self._file_path, f) for
                          f in listdir(self._file_path) if f.endswith(('.csv', '.CSV'))]
        return file_names

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
