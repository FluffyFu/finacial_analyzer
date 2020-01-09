"""
File_name: chase.py
Author: Fluffy Fu
Date: 01/08/2020
Description: Impliment child class of CreditCard that handles credit statements from Chase bank.
"""
from os import listdir
from os.path import isfile, join
import pandas as pd
from credit_card import CreditCard

class Chase(CreditCard):
    """
    Class to read statements from Chase and pull out stats from them.
    """
    def __init__(self, file_path, file_name_regex):
        # TODO currently, file_path is assumed to be an absolute one.
        # this is will be generalized in the future.
        super(Chase, self).__init__(file_path, file_name_regex)


    def _load_statements(self):
        """
        load statements from csv files.
        """
        file_names = self._get_file_names()
        self._statement = pd.concat([pd.read_csv(file_name) for file_name in file_names])

    def _get_file_names(self):
        """
        return a list of file names from the given file_path that matches the regex.
        """
        # TODO check the file type and handle possible file types (csv, xls)
        if self._file_name_regex:
            # TODO implement code to read files that match the given regex.
            # should get a list of matched file names.
            pass
        else:
            # When the regex is not given, read all the files in the directory.
            file_names = [f for f in listdir(self._file_path) if isfile(join(self._file_path, f))]

        return file_names
