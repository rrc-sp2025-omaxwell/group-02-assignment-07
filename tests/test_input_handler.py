"""Unittesting for input_handler to verify the functionality
of the class methods.
"""

import unittest
from unittest import TestCase
from unittest.mock import patch, mock_open
from input_handler.input_handler import InputHandler
import csv
import json
from io import StringIO

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
    @patch("builtins.open", new_callable = mock_open(read_data = ""))
    def test_read_csv_data_return_list(self, mock_file):
        
        # Arrange
        # Utilize StringIO to treat the file as if it were a file.
        mock_file.return_value = StringIO(self.FILE_CONTENTS)

        # Act
        with patch("os.path.isfile", return_value = True):
            filepath = InputHandler("file.csv")
            transaction_list = filepath.read_csv_data()

        # Assert
        # tests a single transaction
        expected = {"Transaction ID": "1", "Account number": "1001",
                     "Date": "2023-03-01", "Transaction type": "deposit",
                       "Amount": "1000", "Currency": "CAD", "Description": "Salary"}

        self.assertEqual(expected, transaction_list[0])


    # read_input_data, Returns a list containing the transaction data from an existing csv file.
    @patch("builtins.open", new_callable = mock_open(read_data = ""))
    def test_read_input_data_csv(self, mock_file):
        
        # Arrange
        mock_file.return_value = StringIO(self.FILE_CONTENTS)

        # Act
        with patch("os.path.isfile", return_value = True):
            filepath = InputHandler("file.csv")
            transaction_list = filepath.read_input_data()

        # Assert
        # tests a single transaction
        expected = {"Transaction ID": "1", "Account number": "1001",
                     "Date": "2023-03-01", "Transaction type": "deposit",
                       "Amount": "1000", "Currency": "CAD", "Description": "Salary"}

        self.assertEqual(expected, transaction_list[0])


    # read_input_data, Returns a list containing the transaction data from an existing json file.
    @patch("builtins.open", new_callable = mock_open(read_data = ""))
    def test_read_input_data_json(self, mock_file):
        
        # Arrange

        json_format = json.dumps([
                                    {
                                        "Transaction ID": "1",
                                        "Account number": "1001",
                                        "Date": "2023-03-01",
                                        "Transaction type": "deposit",
                                        "Amount": "1200",
                                        "Currency": "CAD",
                                        "Description": "Salary"
                                    }
                                ])
        mock_file.return_value = StringIO(json_format)

        # Act
        with patch("os.path.isfile", return_value = True):
            filepath = InputHandler("file.json")
            transaction_list = filepath.read_input_data()

        # Assert
        # tests a single transaction
        expected = {"Transaction ID": "1", "Account number": "1001",
                     "Date": "2023-03-01", "Transaction type": "deposit",
                       "Amount": "1200", "Currency": "CAD", "Description": "Salary"}

        self.assertEqual(expected, transaction_list[0])

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
