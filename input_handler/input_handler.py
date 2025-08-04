"""REQUIRED MODULE DOCUMENTATION"""

import csv
import json
from os import path

__author__ = "Owen Maxwell"
__version__ = "1.0.0"
__credits__ = "COMP-1327 Faculty"

class InputHandler:
    """Takes an input file path and proceeds to 
    verify the file type before logging the data within
    inside of a list titled transactions.    
    """

    def __init__(self, file_path: str):
        """defines a file path based on an input string.

        Args:
            file_path (str): string outlining which
        """

        self.__file_path = file_path

    @property
    def file_path(self) -> str:
        """Accessor for file_path allowing access to
        the file_path attribute, retrieving its value.
        
        Returns:
            str: file path for file.
        """

        return self.__file_path

    def get_file_format(self) -> str:
        """Takes the input file path string and splits it
        based on the period between the name and file type,
        it then returns the file type.
        
        Returns:
            str: File type represented as a string.
        """
        return self.__file_path.split(".")[-1]

    def read_input_data(self) -> list:
        """Checks the file type provided by get_file_format
        before selecting the appropriate method to execute,
        those results will then be logged into transactions.
        
        Returns:
            list: updated transactions list with latest transaction added.
        """

        transactions = []
        file_format = self.get_file_format()
        
        # checks if the file format is csv or json
        # then logs transaction.
        if file_format == "csv":
            transactions =  self.read_csv_data()
        elif file_format == "json":
            transactions = self.read_json_data()

        return transactions

    def read_csv_data(self) -> list:
        """First verifies if the file type is csv,
        if valid, it opens and reads the contents of the file.
        The contents of the opened file are then logged
        into the transactions list.
          
        Raises:
            FileNotFoundError: Raised when file cannot
             be found with file_path.

        Returns:
            list: transactions list containing the data from a csv file.
        """
        # detects whether or not file path leads to a file.
        if not path.isfile(self.__file_path):
            raise FileNotFoundError(f"File: {self.__file_path} does not exist.")

        transactions = []

        with open(self.__file_path, "r") as input_file:
            reader = csv.DictReader(input_file)
            for row in reader:
                transactions.append(row)
            
        return transactions
            
    def read_json_data(self) -> list:
        """First verifies if the file type is json,
         if valid, it opens and reads the contents of the file.
         The contents of the opened file are then logged
         into the transactions list.
          
        Raises:
            FileNotFoundError: Raised when file cannot
             be found with file_path.

        Returns:
            list: transactions list containing the data from a json file.
        """

        # Research the json.load function so that you 
        # understand the format of the data once it is
        # placed into input_data

        # detects whether or not file path leads to a file.
        if not path.isfile(self.__file_path):
            raise FileNotFoundError(f"File: {self.__file_path} does not exist.")

        # json.load will gather the data into a dictionary
        with open(self.__file_path, "r") as input_file:
            transactions = json.load(input_file)

        return transactions

