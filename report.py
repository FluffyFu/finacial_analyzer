"""
File_name: report.py
Author: Fluffy
Date: 01/18/2020
Description: This class is used to combine the statements from different banks.
    The main functions are listed as follows:
        1. map the spending categories in each bank to general categories so
        that the spending from different banks can be combined together.
"""
import pandas as pd
from datetime import datetime
from financial.chase import Chase
from financial.amex import Amex
from financial.utils import window_filter

class Report:
    """
    Combine the statements from Chase and Amex.

    """
    date_col = 'Transaction_Date'
    category_col = 'Category'
    type_col = 'Type'
    desc_col = 'Description'
    amount_col = 'Amount'

    def __init__(self, chase_path, chase_file_suffix,
                 amex_path, amex_file_suffix
                 ):
        self._chase = Chase(chase_path, chase_file_suffix)
        self._amex = Amex(amex_path, amex_file_suffix)
        self._statement = None

    @property
    def statement(self):
        """
        Return combined statement from Chase and Amex.
        """
        if self._statement:
            return self._statement
        self._statement = pd.concat(
            [self._chase.statement, self._amex.statement],
            ignore_index=True,
            join='inner',
        )
        return self._statement

    def summary(self, start, end):
        """
        Group spending by categories.
        Arg:
            start(int): start point of the time window. Format yyyymmdd.

            end(int): end point of the time window. Format yyyymmdd.
        """

        filtered = window_filter(self._statement, self.date_col, start, end)
        result = filtered.groupby(self.category_col).agg('sum').reset_index()
        return result

    def category_trans(self, category, start, end):
        """
        Filter by the given category and the time window.

        Args:
            category(str): the category of interest.

            start(int): start point of the time window. Format yyyymmdd.

            end(int): end point of the time window. Format yyyymmdd.
        """
        filtered = window_filter(self._statement, self.date_col, start, end)
        filtered = filtered[filtered[self.category_col]==category]

        return filtered
