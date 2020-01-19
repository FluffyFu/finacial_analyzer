"""
File_name: chase.py
Author: Fluffy Fu
Date: 01/08/2020
Description: Implement child class of CreditCard that handles credit statements from Chase bank.
"""
import pandas as pd
from financial.credit_card import CreditCard


class Chase(CreditCard):
    """
    Class to read statements from Chase and pull out stats from them.
    """
    original_date_col = 'Transaction Date'
    date_format_str = '%m/%d/%Y'

    cat_map = {
        'Food & Drink': 'Food',
        'Bills & Utilities': 'Bill',
        'Personal': 'Others',
        'Travel': 'Travel',
        'Shopping': 'Shopping',
        'Groceries': 'Groceries',
    }

    def __init__(self, file_path, file_suffix=None):
        # TODO currently, file_path is assumed to be an absolute one.
        # this is will be generalized in the future.
        super(Chase, self).__init__(file_path, file_suffix)

    def _data_cleaning(self, df):
        """
        Cleaning the data. Currently, it does the following:
            1. Convert dates from string to datetime object.

            2. Make spending positive and payment negative.

            3. Replace the space in column name to '_'

            4. Keep columns of interest.

        Args:
            df(pd.DataFrame): dataframe needs to be cleaned.


        Returns:
            pd.DataFrame, cleaned dataframe.
        """
        df = self._date_cleaning(df)
        df = self._amount_cleaning(df)
        df = self._col_name_cleaning(df)
        df = self._drop_irrelavent_cols(df)
        df = self._map_to_general_categories(df)

        return  df

    def _date_cleaning(self, df):
        """
        Convert dates from string to datetime object.

        df (pandas.DataFrame): dataframe need to be cleaned.
        """
        df[self.original_date_col] = pd.to_datetime(
            df[self.original_date_col],
            format=self.date_format_str)

        return df

    def _amount_cleaning(self, df):
        """
        Make spending positive and payment negative.

        df (pandas.DataFrame): dataframe need to be cleaned.
        """
        df[self.amount_col] = -df[self.amount_col]

        return df

    def _col_name_cleaning(self, df):
        """
        Replace the space in column name to '_'.

        df (pandas.DataFrame): dataframe need to be cleaned.
        """
        old_cols = df.columns
        new_cols = [col.replace(' ', '_') for col in old_cols]

        col_map = {old: new for old, new in zip(old_cols, new_cols)}
        df_new = df.rename(columns=col_map)

        return df_new

    def _drop_irrelavent_cols(self, df):
        """
        remove columns that does not appear in class columns.

        """
        cols_of_interest = {self.date_col, self.category_col, self.type_col,
                            self.desc_col, self.amount_col}
        cols_to_drop = [col for col in df.columns if col not in cols_of_interest]

        return df.drop(columns=cols_to_drop)

    def _map_to_general_categories(self, df):
        """
        Map Chase specific spending categories to general categories.
        Payment has NaN category. Map them to 'Payment'.
        """
        # payment has NaN category.
        df[self.category_col] = df[self.category_col].fillna('Payment')

        df[self.category_col] = df[self.category_col].map(self.cat_map)
        return df
