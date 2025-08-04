"""Unittesting for input_handler to verify the functionality
of the class methods.
"""

import unittest
from unittest import TestCase
from unittest.mock import patch, mock_open
import os
from input_handler.input_handler import InputHandler

__author__ = "Owen Maxwell"
__version__ = "1.0.0"
__credits__ = "COMP-1327 Faculty"

class InputHandlerTests(TestCase):
    """Defines the unit tests for the InputHandler class."""

    def setUp(self):
        """This function is invoked before executing a unit test
        function.

        The following class attribute has been provided to reduce the 
        amount of code needed when testing the InputHandler class in 
        the tests that follow.
        
        Example:
            >>> data_processor = DataProcessor(self.FILE_CONTENTS)
        """
        
        self.FILE_CONTENTS = \
            ("Transaction ID,Account number,Date,Transaction type,"
            + "Amount,Currency,Description\n"
            + "1,1001,2023-03-01,deposit,1000,CAD,Salary\n"
            + "2,1002,2023-03-01,deposit,1500,CAD,Salary\n"
            + "3,1001,2023-03-02,withdrawal,200,CAD,Groceries")

    # Define unit test functions below

    # get_file_format, Returns the file extension of the file path.
    def test_get_file_format(self):
        # Arrange
        expected = "csv"  
        filename = InputHandler("file.csv")

        # Act
        actual = InputHandler.get_file_format(filename)

        # Assert
        self.assertEqual(expected, actual)

    # read_csv_data, Raises a FileNotFoundError when the file
    # path does not exist to a file. 
    def test_read_csv_data_not_found(self):

        # Arrange
        file = InputHandler("file.csv")
        expected = "File: file.csv does not exist."

        # Act and Assert
        with self.assertRaises(FileNotFoundError) as context:
            InputHandler.read_csv_data(file)
        
        self.assertEqual(expected, str(context.exception))

    # read_csv_data, Returns a list containing the transaction data from an existing csv file.
    def test_read_csv_data_list_return(self):

        # Arrange
        filename = InputHandler(self.FILE_CONTENTS)
        expected = self.FILE_CONTENTS

        with patch('builtins.open', mock_open(read_data = self.FILE_CONTENTS)):


            actual = InputHandler.read_csv_data(self.FILE_CONTENTS)
            self.assertEqual(expected, actual)

    # read_input_data, Returns a list containing the transaction data from an existing csv file.

    # read_input_data, Returns a list containing the transaction data from an existing json file.
    def test_input_data_json_list(self):
        # Arrange
        expected = self.FILE_CONTENTS
        filename = "file.json"


        # Act
        with patch('builtins.open', mock_open(read_data=expected)) as mocked_file:

            actual = InputHandler.read_input_data(InputHandler(filename))

        # Assert
        self.assertEqual(expected, actual)

    # read_input_data, Returns an empty list if the file is not a csv or json file.
    def test_read_input_data_no_file(self):
        # Arrange
        expected = []
        file_name = InputHandler("file.txt")

        # Act
        actual = InputHandler.read_input_data(file_name)

        # Assert
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()
