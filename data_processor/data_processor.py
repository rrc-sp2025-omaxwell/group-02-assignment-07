"""REQUIRED MODULE DOCUMENTATION"""

__author__ = ""
__version__ = ""
__credits__ = "COMP-1327 Faculty"

class DataProcessor:
    """This class process financial transactions."""

    LARGE_TRANSACTION_THRESHOLD = 10000
    """Transactions above 10000 is considered large. """

    UNCOMMON_CURRENCIES = ["XRP", "LTC"]
    """This list stores currencies that are not common."""

    def __init__(self, transactions: list):
        """
        Args:
            transactions (list): List of all transactions including transaction ID, account number, currency, amount, transaction type etc.
        Attributes:
            __transactions : Saves the input data of transactions.
            __account_summaries (dict): It stores total for each account.
            __suspicious_transactions (list): Stores all suspicious transactions.
            __transaction_statistics (dict): Stores statistics related to total transactions and amount. 
        """
 
        self.__transactions = transactions
        self.__account_summaries = {}
        self.__suspicious_transactions = []
        self.__transaction_statistics = {}

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

        return {"account_summaries": self.__account_summaries,
                "suspicious_transactions": self.__suspicious_transactions,
                "transaction_statistics": self.__transaction_statistics}

    def update_account_summary(self, transaction: dict) -> None:
        """
        It updates the account summaries on specified transactions.
        
        Args:
            transactions (dict): It is a dictionary that contains data of transactions like Account Number, Transaction type, Amount.
        
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

    def check_suspicious_transactions(self, transaction: dict) -> None:
        """
        It checks whether a transaction that has been made is suspicious by checking amount and currency. The transaction will be suspicious if transaction amount is greater than 10000 or currency is uncommon.
        
        Args: 
            transaction (dict): It is a dictionary that contains data of transactions like 'Amount' and 'Currency'.
        
        Returns:
            None
        """

        amount = float(transaction["Amount"])
        currency = transaction["Currency"]

        if amount > self.LARGE_TRANSACTION_THRESHOLD \
            or currency in self.UNCOMMON_CURRENCIES:
            self.__suspicious_transactions.append(transaction)

    def update_transaction_statistics(self, transaction: dict) -> None:
        """
        It updates the transaction statistics as per transaction type and amount.
        
        Args: 
            transaction (dict): A dictionary containing transaction details about Transaction type and Amount.
        
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
