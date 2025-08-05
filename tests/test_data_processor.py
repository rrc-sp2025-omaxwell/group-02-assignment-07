"""REQUIRED MODULE DOCUMENTATION"""

import unittest
from unittest import TestCase
from data_processor.data_processor import DataProcessor

__author__ = ""
__version__ = ""
__credits__ = "COMP-1327 Faculty"

class TestDataProcessor(TestCase):
    """Defines the unit tests for the DataProcessor class."""

    def setUp(self):
        """This function is invoked before executing a unit test
        function.

        The following class attribute has been provided to reduce the 
        amount of code needed when creating DataProcessor class objects 
        in the tests that follow.  
        
        Example:
            >>> data_processor = DataProcessor(self.transactions)
        """
        
        self.transactions = [
            {
                "Transaction ID": "1",
                "Account number": "1001",
                "Date": "2023-03-01",
                "Transaction type": "deposit",
                "Amount": 1000,
                "Currency": "CAD",
                "Description": "Salary"
            }, 
            {
                "Transaction ID": "2",
                "Account number": "1002",
                "Date": "2023-03-01",
                "Transaction type": "deposit",
                "Amount": 1500,
                "Currency": "CAD",
                "Description": "Salary"
            },
            {
                "Transaction ID": "3",
                "Account number": "1001",
                "Date": "2023-03-02",
                "Transaction type": "withdrawal",
                "Amount": "300",
                "Currency": "CAD",
                "Description": "Groceries"
            },
            {
                "Transaction ID": "11",
                "Account number": "1001",
                "Date": "2023-03-13",
                "Transaction type": "deposit",
                "Amount": "13000",
                "Currency": "CAD",
                "Description": "Car Sale"
            },
            {
                "Transaction ID": "13",
                "Account number": "1001",
                "Date": "2023-03-14",
                "Transaction type": "deposit",
                "Amount": "300",
                "Currency": "XRP",
                "Description": "Crypto Investment"
            }

        ]

    # Define unit test functions below

    # update_account_summary
    def test_update_account_summary_for_deposit(self):
        """
        Test to check if update_account_summary creates dictionary for account number for deposit transaction type.
        """
        # Arrange
        data_processor = DataProcessor([])
        transaction = self.transactions[0]

        # Act
        data_processor.update_account_summary(transaction)

        # Assert
        summary = data_processor.account_summaries["1001"]
        self.assertEqual(summary["account_number"], "1001")
        self.assertEqual(summary["balance"], 1000)
        self.assertEqual(summary["total_deposits"], 1000)
        self.assertEqual(summary["total_withdrawals"], 0)
    
    def test_update_account_summary_for_withdrawal(self):
        """
        Test to check if update_account_summary creates dictionary for account number for 'withdrawal' transaction type. 
        """
        # Arrange
        data_processor = DataProcessor([])
        transaction = self.transactions[2]

        # Act
        data_processor.update_account_summary(transaction)

        # Assert
        summary = data_processor.account_summaries["1001"]
        self.assertEqual(summary["account_number"], "1001")
        self.assertEqual(summary["balance"], -300)
        self.assertEqual(summary["total_deposits"], 0)
        self.assertEqual(summary["total_withdrawals"], 300)

    # check_suspicious_transactions

    def test_check_suspicious_transactions_for_large_amount(self):
        """
        Checks if the transaction for amount greater than large transaction threshold is added to suspicious transactions.
        """
        # Arrange
        data_processor = DataProcessor([])
        transaction = self.transactions[3]

        # Act
        data_processor.check_suspicious_transactions(transaction)

        # Assert
        self.assertEqual(data_processor.suspicious_transactions, [transaction])
    
    def test_check_suspicious_transactions_for_uncommon_currencies(self):
        """
        Checks if transaction for uncommon currency is added to suspicious_transactions.
        """
        # Arrange
        data_processor = DataProcessor([])
        transaction = self.transactions[4]

        # Act
        data_processor.check_suspicious_transactions(transaction)

        # Assert
        self.assertEqual(data_processor.suspicious_transactions, [transaction])

    def test_check_suspicious_transactions_if_transaction_not_suspicious_is_not_added(self):
        """
        Checks if a transaction is not suspicious and is not added to suspicious_transactions.
        """
        # Arrange
        data_processor = DataProcessor([])
        transaction = self.transactions[1]

        # Act
        data_processor.check_suspicious_transactions(transaction)

        # Assert
        self.assertEqual(data_processor.suspicious_transactions, [])

    # update_transaction_statistics

    def test_update_transaction_statistics_for_specified_transaction_type(self):
        """
        Checks if dictionary is defined as part of transaction statistics dictionary for the specified transaction type.
        """
        # Arrange
        data_processor = DataProcessor([])
        transaction = self.transactions[0]

        # Act
        data_processor.update_transaction_statistics(transaction)

        # Assert
        self.assertIn("deposit", data_processor.transaction_statistics)
        self.assertEqual(data_processor.transaction_statistics["deposit"]["total_amount"], 1000)
        self.assertEqual(data_processor.transaction_statistics["deposit"]["transaction_count"], 1)

if __name__ == "__main__":
    unittest.main()
