"""Testing for output_handler.py to verify functionality."""

from unittest import TestCase, main
from output_handler.output_handler import OutputHandler
from unittest.mock import patch, mock_open

__author__ = "Owen Maxwell"
__version__ = "1.0.0"
__credits__ = "COMP-1327 Faculty"

class TestOutputHandler(TestCase):
    """Defines the unit tests for the OutputHandler class."""

    def setUp(self):
        """This function is invoked before executing a unit test
        function.

        The following class attributes have been provided to reduce the 
        amount of code needed when creating OutputHandler class objects 
        in the tests that follow.  
        
        Example:
            >>> OutputHandler(self.account_summaries, 
                              self.suspicious_transactions, 
                              self.transaction_statistics)
        """
        
        self.account_summaries = { 
            "1001": {
                "account_number": "1001", 
                "balance": 50, 
                "total_deposits": 100, 
                "total_withdrawals": 50
            },
            "1002": {
                "account_number": "2", 
                "balance": 200, 
                "total_deposits": 200, 
                "total_withdrawals": 0
            }
        }

        self.suspicious_transactions = [
            {
                "Transaction ID": "1",
                "Account number": "1001",
                "Date": "2023-03-14",
                "Transaction type": "deposit",
                "Amount": 250,
                "Currency": "XRP",
                "Description": "crypto investment"
            }
        ]

        self.transaction_statistics = {
            "deposit": {
                "total_amount": 300, 
                "transaction_count": 2
            }, 
            "withdrawal": {
                "total_amount": 50, 
                "transaction_count": 1
            }
        }

    # Define unit test functions below

    # test by initializing an OutputHandler object.

    def test_init(self):
        # Arrange
        output = OutputHandler(self.account_summaries,
         self.suspicious_transactions, self.transaction_statistics,)
        
        # Act
        expected_summary = self.account_summaries
        expected_suspicious_list = self.suspicious_transactions
        expected_statistics = self.transaction_statistics

        # Assert
        self.assertEqual(expected_summary, output._OutputHandler__account_summaries)
        self.assertEqual(expected_suspicious_list, output._OutputHandler__suspicious_transactions)
        self.assertEqual(expected_statistics, output._OutputHandler__transaction_statistics)


    # Return current state of account_summaries
    def test_account_summaries_state(self):
        # Arrange and Act
        state = OutputHandler(self.account_summaries,
         self.suspicious_transactions, self.transaction_statistics,)
        
        # Assert
        self.assertEqual(self.account_summaries, state.account_summaries)


    # Return current state of suspicious_transactions
    def test_suspicious_transactions_state(self):
        # Arrange and Act
        state = OutputHandler(self.account_summaries,
         self.suspicious_transactions, self.transaction_statistics,)
        
        # Assert
        self.assertEqual(self.suspicious_transactions, state.suspicious_transactions)


    # Return current state of suspicious_transactions
    def test_transaction_statistics_state(self):
        # Arrange and Act
        state = OutputHandler(self.account_summaries,
         self.suspicious_transactions, self.transaction_statistics,)
        
        # Assert
        self.assertEqual(self.transaction_statistics, state.transaction_statistics)


    # write_account_summaries_to_csv
    def test_write_account_summaries(self):
        # Arrange
        output = OutputHandler(self.account_summaries,
         self.suspicious_transactions, self.transaction_statistics,)
        filepath = "account_summaries.csv"

        # Act
        with patch("builtins.open", mock_open()) as mocked_open:
            output.write_account_summaries_to_csv(filepath)

        #mocked_open.assert_called_once_with(filename, 'w')

        # Assert
        mock_file = mocked_open()

        # utilize .call_args_list every time write is called
        # to print the line to verify.
        print ("account_summaries")
        for line in mock_file.write.call_args_list:
            print(line)

        # verify there are 3 lines total
        self.assertEqual(mock_file.write.call_count, 3)


    # write_suspicious_transactions_to_csv
        # write_account_summaries_to_csv
    def test_write_suspicious_transactions(self):
        # Arrange
        output = OutputHandler(self.account_summaries,
         self.suspicious_transactions, self.transaction_statistics,)
        filepath = "suspicious_transactions.csv"

        # Act
        with patch("builtins.open", mock_open()) as mocked_open:
            output.write_suspicious_transactions_to_csv(filepath)

        #mocked_open.assert_called_once_with(filename, 'w')

        # Assert
        mock_file = mocked_open()

        # utilize .call_args_list every time write is called
        # to print the line to verify.
        print("suspicious_transactions")
        for line in mock_file.write.call_args_list:
            print(line)

        # verify there are 2 lines total
        self.assertEqual(mock_file.write.call_count, 2)


    # write_transaction_statistics_to_csv
    def test_write_transaction_statistics(self):
        # Arrange
        output = OutputHandler(self.account_summaries,
         self.suspicious_transactions, self.transaction_statistics,)
        filepath = "transaction_statistics.csv"

        # Act
        with patch("builtins.open", mock_open()) as mocked_open:
            output.write_transaction_statistics_to_csv(filepath)

        #mocked_open.assert_called_once_with(filename, 'w')

        # Assert
        mock_file = mocked_open()

        # utilize .call_args_list every time write is called
        # to print the line to verify.
        print("transaction_statistics")
        for line in mock_file.write.call_args_list:
            print(line)

        # verify there are 3 lines total
        self.assertEqual(mock_file.write.call_count, 3)


if __name__ == "__main__":
    main()
