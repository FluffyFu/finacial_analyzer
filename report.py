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
from financial.chase import Chase
from financial.amex import Amex

class Report:
    """
    Combine the statements from Chase and Amex.

    """
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
