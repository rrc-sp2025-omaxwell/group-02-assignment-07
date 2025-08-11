"""
Contains a class named DataProcessor, it stores transaction list, updates the account summary, checks suspicious transactions, 
and keeps track of total amount in different transaction types.  
"""

__author__ = "Khushpreet Kaur"
__version__ = "2.49.0.windows.1"
__credits__ = "COMP-1327 Faculty"

import logging

class DataProcessor:
    """
    This class process financial transactions.
    logging is used to track major actions performed by class.
    """

    LARGE_TRANSACTION_THRESHOLD = 10000
    """Transactions above 10000 is considered large. """

    UNCOMMON_CURRENCIES = ["XRP", "LTC"]
    """This list stores currencies that are not common."""

    def __init__(
            self,
            transactions: list,
            logging_level: str = "WARNING",
            logging_format: str = "%(asctime)s - %(levelname)s - %(message)s",
            log_file: str = ""
        ):
        """
        Initialize the DataProcessor with transaction data and optional logging configuration.
        
        Args:
            transactions (list): List of all transactions including transaction ID, account number, currency, amount, transaction type etc.
            logging_level (str, optional):
                The minimum severity level of message to log.
                Acceptable values: "DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL".
                Defaults to "WARNING".

            logging_format (str, optional):
                The style of the log messages.
                Default: "%(asctime)s - %(levelname)s - %(message)s"
                
            log_file (str, optional):
                The file path to write log messages. If left blank (""), messages will only show on the screen.
        Attributes:
            __transactions : Saves the input data of transactions.
            __account_summaries (dict): It stores total for each account.
            __suspicious_transactions (list): Stores all suspicious transactions.
            __transaction_statistics (dict): Stores statistics related to total transactions and amount. 
        Citations:
            Real Python. (2018, September 12). Logging in Python. Realpython.com; Real Python. https://realpython.com/python-logging/

            Python Logging Basics - The Ultimate Guide To Logging. (2025, June 27). Log Analysis | Log Monitoring by Loggly. https://www.loggly.com/ultimate-guide/python-logging-basics/
        """
 
        self.__transactions = transactions
        self.__account_summaries = {}
        self.__suspicious_transactions = []
        self.__transaction_statistics = {}

        # convert string level to logging module level
        level = getattr(logging, logging_level.upper(), logging.WARNING)

        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(level)

        if not self.logger.hasHandlers():
            if log_file:
                handler = logging.FileHandler(log_file)
            else:
                handler = logging.StreamHandler()

            formatter = logging.Formatter(logging_format)
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)
        
        self.logger.info("DataProcessor initialized.")

    @property
    def input_data(self) -> list:
        """It will return transactions in the form of list."""

        return self.__transactions
    
    @property
    def account_summaries(self) -> dict:
        """Returns a dictionary containing summary of all transactions of all accounts."""

        return self.__account_summaries
    
    @property
    def suspicious_transactions(self) -> list:
        """Returns a list containing suspicious transactions."""

        return self.__suspicious_transactions
    
    @property
    def transaction_statistics(self) -> dict:
        """Returns statistics of transaction data. It may include currency, amount that has been transferred, and currency. """

        return self.__transaction_statistics

    def process_data(self) -> dict:
        """
        It process transaction data and return account summaries, suspicious transactions, and transaction statistics.
        
        Returns:
            dict: Returns a dictionary containing summaries of accounts,
                  transactions that are suspicious,
                  statistics of transactions made.
        """

        for transaction in self.__transactions:
            self.update_account_summary(transaction)
            self.check_suspicious_transactions(transaction)
            self.update_transaction_statistics(transaction)

        # ensures the log entry appears only after processing is done.
        self.logger.info("Data Processing Complete")

        return {"account_summaries": self.__account_summaries,
                "suspicious_transactions": self.__suspicious_transactions,
                "transaction_statistics": self.__transaction_statistics}

    def update_account_summary(self, transaction: dict) -> None:
        """
        It updates the account summaries on specified transactions.
        
        Args:
            transactions (dict): It is a dictionary that contains data of transactions like Account Number, Transaction type, Amount.
        Logs:
            INFO - after account summary is updated.
        Returns:
            None
        """

        account_number = transaction["Account number"]
        transaction_type = transaction["Transaction type"]
        amount = float(transaction["Amount"])

        if account_number not in self.__account_summaries:
            self.__account_summaries[account_number] = {
                "account_number": account_number,
                "balance": 0,
                "total_deposits": 0,
                "total_withdrawals": 0
            }

        if transaction_type == "deposit":
            self.__account_summaries[account_number]["balance"] += amount
            self.__account_summaries[account_number]["total_deposits"] += amount
        elif transaction_type == "withdrawal":
            self.__account_summaries[account_number]["balance"] -= amount
            self.__account_summaries[account_number]["total_withdrawals"] += amount

        # log account update
        self.logger.info(f"Account summary updated: {account_number}")

    def check_suspicious_transactions(self, transaction: dict) -> None:
        """
        It checks whether a transaction that has been made is suspicious by checking amount and currency. The transaction will be suspicious if transaction amount is greater than 10000 or currency is uncommon.
        
        Args: 
            transaction (dict): It is a dictionary that contains data of transactions like 'Amount' and 'Currency'.
        Logs:
            WARNING - used when a suspicious transaction is detected.
        Returns:
            None
        """

        amount = float(transaction["Amount"])
        currency = transaction["Currency"]

        if amount > self.LARGE_TRANSACTION_THRESHOLD \
            or currency in self.UNCOMMON_CURRENCIES:
            self.__suspicious_transactions.append(transaction)

            self.logger.warning(f"Suspicious transaction: {transaction}")

    def update_transaction_statistics(self, transaction: dict) -> None:
        """
        It updates the transaction statistics as per transaction type and amount.
        
        Args: 
            transaction (dict): A dictionary containing transaction details about Transaction type and Amount.
        Logs:
            INFO - when statistics are updated for transaction type
        Returns:
            None
        """

        transaction_type = transaction["Transaction type"]
        amount = float(transaction["Amount"])

        if transaction_type not in self.__transaction_statistics:
            self.__transaction_statistics[transaction_type] = {
                "total_amount": 0,
                "transaction_count": 0
            }

        self.__transaction_statistics[transaction_type]["total_amount"] += amount
        self.__transaction_statistics[transaction_type]["transaction_count"] += 1

        # log update
        self.logger.info(f"Updated transaction statistics for: {transaction_type}")

    def get_average_transaction_amount(self, transaction_type: str) -> float:
        """
        It analyze the transaction amount for specific transaction. It calculates total amount and number of transactions for different transaction types and returns average amount.
        It returns 0 if there are no transactions of any transaction type.

        Args:
            transaction_type (str): Calculates the average amount for specific transaction type.
        
        Returns:
            float: Returns average transaction amount of specific transaction type, if there is no transaction for any type it returns 0.
        """
        
        total_amount = self.__transaction_statistics[transaction_type]["total_amount"]
        transaction_count = self.__transaction_statistics[transaction_type]["transaction_count"]
    
        return 0 if transaction_count == 0 else total_amount / transaction_count
