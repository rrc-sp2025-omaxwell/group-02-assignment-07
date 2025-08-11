
"""
Main file is entry point for data processing.
This is main file to run the data processing. 
It reads input data, processes data with logging, write output data to files.
""" 

from os import path
from input_handler.input_handler import InputHandler
from data_processor.data_processor import DataProcessor
from output_handler.output_handler import OutputHandler

__author__ = "Khushpreet Kaur"
__version__ = "2.49.0.windows.1"
__credits__ = "COMP-1327 Faculty"

def main() -> None:
    """Main function to read input data, process it, and write the 
    results to output files.

    - Reads input data from a CSV file using InputHandler.
    - Processes the data using DataProcessor.
    - Writes the processed data to CSV and JSON files using 
    OutputHandler.
    """

    # Retrieves the directory name of the current script or module file.
    current_directory = path.dirname(path.abspath(__file__))

    # Joins the current directory, the relative path to the input folder 
    # and the filename to create a complete path to the file.
    input_file_path = path.join(current_directory, "input/input_data.csv")

    input_handler = InputHandler(input_file_path)
    transactions = input_handler.read_input_data()

    # Logging integration start
    group_number = 2
    log_filename = f"fdp_team_{group_number}.log"

    data_processor = DataProcessor(transactions, logging_level="INFO", log_file=log_filename)
    processed_data = data_processor.process_data()
    # Logging integration ends

    account_summaries = processed_data["account_summaries"]
    suspicious_transactions = processed_data["suspicious_transactions"]
    transaction_statistics = processed_data["transaction_statistics"]
    
    output_handler = OutputHandler(account_summaries, 
                                   suspicious_transactions, 
                                   transaction_statistics)

    # Joins the current directory, the relative path to the output 
    # folder and the filename to create a complete path to each of the 
    # output files.
    file_prefix = "output_data"
    filenames = ["account_summaries", 
                 "suspicious_transactions", 
                 "transaction_statistics"]

    file_path = {}

    for filename in filenames:
        file_path[filename] = path.join(current_directory,
                                        f"output/{file_prefix}_{filename}.csv")

    output_handler.write_account_summaries_to_csv(file_path["account_summaries"])
    output_handler.write_suspicious_transactions_to_csv(file_path["suspicious_transactions"])
    output_handler.write_transaction_statistics_to_csv(file_path["transaction_statistics"])

    # Filtering 
    filtered_filename = path.join(
        current_directory,
        "output",
        "fdp_filter_team_2.csv"   
    )

    filtered_summaries = output_handler.filter_account_summaries(
        "balance", 5000, False
    )

    output_handler.write_filtered_summaries_to_csv(filtered_summaries, filtered_filename)

    print(f"Filtered account summaries written to: {filtered_filename}")


if __name__ == "__main__":
    main()
