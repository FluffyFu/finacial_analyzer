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
    holder_col = 'Holder'

    def __init__(self, chase_path=None, chase_file_suffix=None,
                 amex_path=None, amex_file_suffix=None, holder=None, reports=None
                 ):
        if reports == None:
            # construct the object from raw data
            self._chase = Chase(chase_path, chase_file_suffix)
            if amex_path != None:
                self._amex = Amex(amex_path, amex_file_suffix)
            else:
                self._amex = None
            self._holder = holder
            self._statement = None
        else:
            # combine a few Report objects to form a single one.
            self._statement = pd.concat([report.statement for report in reports])

    @property
    def statement(self):
        """
        Return combined statement from Chase and Amex.
        """
        if self._statement is not None:
            return self._statement

        if self._amex is not None:
            self._statement = pd.concat(
                [self._chase.statement, self._amex.statement],
                ignore_index=True,
                join='inner',
            )
        else:
            self._statement = self._chase.statement
        # add holder name column
        self._statement[self.holder_col] = self._holder
        return self._statement

    def summary(self, start, end):
        """
        Group spending by categories.
        Arg:
            start(int): start point of the time window. Format yyyymmdd.

            end(int): end point of the time window. Format yyyymmdd.
        """

        filtered = window_filter(self.statement, self.date_col, start, end)
        result = filtered.groupby([self.category_col, self.holder_col]).agg('sum').reset_index()
        return result

    def category_trans(self, category, start, end):
        """
        Filter by the given category and the time window.

        Args:
            category(str): the category of interest.

            start(int): start point of the time window. Format yyyymmdd.

            end(int): end point of the time window. Format yyyymmdd.
        """
        filtered = window_filter(self.statement, self.date_col, start, end)
        filtered = filtered[filtered[self.category_col]==category]

        return filtered
