"""
File_name: chase.py
Author: Fluffy Fu
Date: 01/08/2020
Description: Implement child class of CreditCard that handles credit statements from Chase bank.
"""
from os import listdir
from os.path import isfile, join
from datetime import datetime
import pandas as pd
from financial.credit_card import CreditCard


class Chase(CreditCard):
    """
    Class to read statements from Chase and pull out stats from them.
    """
    date_col = 'Transaction Date'
    category_col = 'Category'
    type_col = 'Type'
    desc_col = 'Description'
    amount_col = 'Amount'

    date_format_str = '%m/%d/%Y'

    def __init__(self, file_path, file_suffix=None):
        # TODO currently, file_path is assumed to be an absolute one.
        # this is will be generalized in the future.
        super(Chase, self).__init__(file_path, file_suffix)

    def _data_cleaning(self, df):
        """
        Cleaning the data. Currently, it does the following:
            1. convert dates from string to datetime object.

            2. make spending positive and payment negative.

        Args:
            df(pd.DataFrame): dataframe needs to be cleaned.


        Returns:
            pd.DataFrame, cleaned dataframe.
        """
        df[self.date_col] = pd.to_datetime(
            df[self.date_col],
            format=self.date_format_str)

        df[self.amount_col] = -df[self.amount_col]
        return  df
