"""The output handler takes its 3 arguments from
the data processor and writes the
data to a csv file."""

import csv

__author__ = "Owen Maxwell"
__version__ = "1.0.0"
__credits__ = "COMP-1327 Faculty"

class OutputHandler:
    """Takes 3 arguements and after verification,
    writes the data in a csv file"""

    def __init__(self, account_summaries: dict, 
                       suspicious_transactions: list, 
                       transaction_statistics: dict):
        """Initializes the class instance with 3 arguements.
        
        Args:
            account_summaries (dict): Summarized data for each account.
            suspicious_transactions (list): A list of all transactions
            flagged as suspicious.
            transaction_statistics (dict): Stores statistics relative to each transaction.
        """

        self.__account_summaries = account_summaries
        self.__suspicious_transactions = suspicious_transactions
        self.__transaction_statistics = transaction_statistics
    
    @property
    def account_summaries(self) -> dict:
        """Enables access to account_summaries for value retrieval."""

        return self.__account_summaries
    
    @property
    def suspicious_transactions(self) -> list:
        """Enables access to suspicious_transactions for value retrieval."""

        return self.__suspicious_transactions
    
    @property
    def transaction_statistics(self) -> dict:
        """Enables access to transaction_statistics for value retrieval."""

        return self.__transaction_statistics

    def write_account_summaries_to_csv(self, file_path: str) -> None:
        """REQUIRED: METHOD DOCSTRING"""

        with open(file_path, "w", newline="") as output_file:
            writer = csv.writer(output_file)
            writer.writerow(["Account number", 
                             "Balance", 
                             "Total Deposits", 
                             "Total Withdrawals"])

            for account_number, summary in self.__account_summaries.items():
                writer.writerow([account_number,
                                summary["balance"],
                                summary["total_deposits"],
                                summary["total_withdrawals"]])

    def write_suspicious_transactions_to_csv(self, file_path: str) -> None:
        """REQUIRED: METHOD DOCSTRING"""

        with open(file_path, "w", newline="") as output_file:
            writer = csv.writer(output_file)
            writer.writerow(["Transaction ID", 
                            "Account number", 
                            "Date", 
                            "Transaction type", 
                            "Amount", 
                            "Currency", 
                            "Description"])

            for transaction in self.__suspicious_transactions:
                writer.writerow([transaction["Transaction ID"],
                                transaction["Account number"],
                                transaction["Date"],
                                transaction["Transaction type"],
                                transaction["Amount"],
                                transaction["Currency"],
                                transaction["Description"]])

    def write_transaction_statistics_to_csv(self, file_path: str) -> None:
        """REQUIRED: METHOD DOCSTRING"""

        with open(file_path, "w", newline="") as output_file:
            writer = csv.writer(output_file)
            writer.writerow(["Transaction type", 
                             "Total amount", 
                             "Transaction count"])

            for transaction_type, statistic in self.__transaction_statistics.items():
                writer.writerow([transaction_type, 
                                 statistic["total_amount"], 
                                 statistic["transaction_count"]])
