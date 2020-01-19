"""
File_name: amex.py
Author: Fluffy Fu
Date: 01/12/2020
Description: Implement child class of CreditCard that handles credit statements
from American Express.
"""
import pandas as pd
from financial.credit_card import CreditCard

class Amex(CreditCard):
    """
    Class used to handle statements from Amex.
    """
    date_col = 'Date'
    category_col = 'Category'
    type_col = 'Type'
    desc_col = 'Description'
    amount_col = 'Amount'

    date_format_str = '%m/%d/%y'

    def __init__(self, file_path, file_suffix=None):
        super(Amex, self).__init__(file_path, file_suffix)

    def _data_cleaning(self, df):
        """
        Cleaning the data. Currently, it does the following:
            1. convert dates from string to datetime object.

            2. remove columns that does not appear in class columns.

        """
        df[self.date_col] = pd.to_datetime(
            df[self.date_col],
            format=self.date_format_str)

        cols_of_interest = {self.date_col, self.category_col, self.type_col,
                            self.desc_col, self.amount_col}
        cols_to_drop = [col for col in df.columns if col not in cols_of_interest]
        return df.drop(columns=cols_to_drop)
