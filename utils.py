"""
File_name: utilts.py
Author: Fluffy
Date: 01/20/2020
Description: Utility functions.
"""
from datetime import datetime

def window_filter(df, date_col, start, end):
    """
    Filter the given dataframe based the given time window.

    Args:
        df(pandas.DataFrame): the dataframe of interest.

        date_col(str): column name that contains the dates.

        start(int): window start point(inclusive) in the format of YYYYMMDD.

        end(int): window end point(inclusive) in the format of YYYYMMDD.

    """
    date_format = '%Y%m%d'
    start_date = datetime.strptime(str(start), date_format)
    end_date = datetime.strptime(str(end), date_format)
    return df[(df[date_col] >= start_date) & (df[date_col] <= end_date)]
