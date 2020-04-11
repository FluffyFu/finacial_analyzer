"""
File_name: amex.py
Author: Fluffy Fu
Date: 01/12/2020
Description: Implement child class of CreditCard that handles credit statements
from American Express.
"""
import pandas as pd
import numpy as np
from financial.credit_card import CreditCard

class Amex(CreditCard):
    """
    Class used to handle statements from Amex.
    """
    original_date_col = 'Date'
    date_format_str = '%m/%d/%y'

    cat_map = {
        'Merchandise & Supplies-Groceries': 'Groceries',
        'Merchandise & Supplies-Clothing Stores': 'Shopping',
        'Transportation-Fuel': 'Travel',
        'Restaurant-Bar & Café': 'Food',
        'Merchandise & Supplies-Internet Purchase': 'Others',
        'Entertainment-General Attractions': 'Food',
        'Restaurant-Restauran': 'Food',
        'Merchandise & Supplies-Arts & Jewelry': 'Others',
        'Merchandise & Supplies-Department Store': 'Others',
    }

    def __init__(self, file_path, file_suffix=None):
        super(Amex, self).__init__(file_path, file_suffix)

    def _data_cleaning(self, df):
        """
        Cleaning the data. Currently, it does the following:
            1. convert dates from string to datetime object.

            2. remove columns that does not appear in class columns.

            3. convert 'DEBIT' to 'Sale' and 'CREDIT' to 'Payment' in Type column
            to align with that in Chase statements.

            4. rename 'Date' column to 'Transaction_Date' to align with that in
            Chase statements.
        """
        df = self._date_cleaning(df)
        df = self._spending_type_cleaning(df)
        df = self._drop_irrelavent_cols(df)
        df = self._map_to_general_categories(df)
        df['Bank'] = 'Amex'

        return df

    def _date_cleaning(self, df):
        """
        convert dates from string to datetime object. And rename the date column
        name to general date column name.
        """
        df[self.original_date_col] = pd.to_datetime(
            df[self.original_date_col],
            format=self.date_format_str)

        df = df.rename(columns={self.original_date_col: self.date_col})
        return df

    def _drop_irrelavent_cols(self, df):
        """
        remove columns that does not appear in class columns.

        """
        cols_of_interest = {self.date_col, self.category_col, self.type_col,
                            self.desc_col, self.amount_col}
        cols_to_drop = [col for col in df.columns if col not in cols_of_interest]

        return df.drop(columns=cols_to_drop)

    def _spending_type_cleaning(self, df):
        """
        First add Type column, then fill the column with 'Sale' and 'Payment'.
        """
        df[self.type_col] = np.where(df[self.amount_col] > 0, 'Sale', 'Payment')

        return df

    def _map_to_general_categories(self, df):
        """
        Map Amex specific spending categories to general categories.
        Payment has NaN category. Map them to 'Payment'.
        """
        df[self.category_col] = df[self.category_col].map(self.cat_map)
        df[self.category_col] = df[self.category_col].fillna('Payment')

        return df
