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
                "account_number": "1002", 
                "balance": 200, 
                "total_deposits": 200, 
                "total_withdrawals": 0
            },
             "1004": {
                "account_number": "1004", 
                "balance": 11500, 
                "total_deposits": 11500, 
                "total_withdrawals": 0
            },
            "1005": {
                "account_number": "1005", 
                "balance": -2200, 
                "total_deposits": 222, 
                "total_withdrawals": 2422
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

        # Initialize handler for tests that use self.handler
        self.handler = OutputHandler(self.account_summaries, self.suspicious_transactions, self.transaction_statistics)

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
        self.assertEqual(mock_file.write.call_count, 5)


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

    # filtered_account_summaries
    def test_filtered_account_summaries_returns_list_using_mode_true(self):
        """
        Test that filtered_account_summaries returns only summaries when filter_mode is True.
        """
        result = self.handler.filter_account_summaries(
            filter_field="balance",
            filter_value=5000,
            filter_mode=True
        )

        expected = [
            {"account_number": "1004", "balance": 11500, "total_deposits": 11500, "total_withdrawals": 0}
        ]

        self.assertEqual(result, expected)

    def test_filtered_account_summaries_returns_list_using_mode_false(self):
        """
        Test to check if accounts with balance less than or equal to 5000 are returned when filter_mode is False.
        """
        filtered = self.handler.filter_account_summaries(
            filter_field="balance",
            filter_value=5000,
            filter_mode=False
        )

        expected = [
            {"account_number": "1001", "balance": 50, "total_deposits": 100, "total_withdrawals": 50},
            {"account_number": "1002", "balance": 200, "total_deposits": 200, "total_withdrawals": 0},
            {"account_number": "1005", "balance": -2200, "total_deposits": 222, "total_withdrawals": 2422}
        ]

        self.assertEqual(filtered, expected)
    
    def test_write_filtered_summaries_to_csv(self):
        # Arrange
        output = OutputHandler(self.account_summaries,
                                self.suspicious_transactions,
                                self.transaction_statistics)
        filepath = "filtered_account_summaries.csv"
    
        filtered_data = output.filter_account_summaries("balance", 5000, False)
        # Act
        with patch("builtins.open", mock_open()) as mocked_open:
       
            output.write_filtered_summaries_to_csv(filtered_data, filepath)
            mock_file = mocked_open()
    
        # Assert
        expected_rows = 1 + len(filtered_data)
    
        self.assertEqual(mock_file.write.call_count, expected_rows)

if __name__ == "__main__":
    main()
