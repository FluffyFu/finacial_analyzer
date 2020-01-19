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
from financial.file_suffix import FileSuffix

class CreditCard:
    """
    Base class for handling credit card statement from different banks.
    """
    date_col = 'Transaction_Date'
    category_col = 'Category'
    type_col = 'Type'
    desc_col = 'Description'
    amount_col = 'Amount'

    def __init__(self, file_path, file_suffix):
        """
        file_path(str): path to the data.
        file_suffix(FileSuffix): type of file suffix of interest.
        """
        self._file_path = file_path
        self._file_suffix = file_suffix
        self._statement = self._load_statements()
        self._time_range = self._get_time_range()
        self._spending_categories = self._get_spending_categories()

    def _load_statements(self):
        """
        Load statement(s) with given file_suffix in the given file path.
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

        file_names = [join(self._file_path, f) for f in listdir(self._file_path)]
        if self._file_suffix == FileSuffix.CSV:
            suffix = (FileSuffix.CSV.value, FileSuffix.CSV.value.upper())
        elif self._file_suffix == FileSuffix.XLSX:
            suffix = (FileSuffix.XLSX.value, FileSuffix.CSV.value.upper())
        else:
            raise Exception("Invalid file_suffix: {}".format(self._file_suffix))
        filter_file_names = [f for f in file_names if f.endswith(suffix)]
        return filter_file_names

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
