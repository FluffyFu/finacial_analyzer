"""
File_name: report.py
Author: Fluffy
Date: 01/18/2020
Description: This class is used to combine the statements from different banks.
    The main functions are listed as follows:
        1. map the spending categories in each bank to general categories so
        that the spending from different banks can be combined together.
"""
from finacial.chase import Chase
from finacial.amex import Amex

class Report:
    """

    """
    def __init__(self, chase_path, chase_file_suffix, amex_path, amex_file_suffix):
        self._chase = Chase(chase_path, chase_file_suffix)
        self._amex = Amex(amex_path, amex_file_suffix)
