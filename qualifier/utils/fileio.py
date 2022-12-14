# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv
from pathlib import Path

def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data


def save_csv(data, outputPath):
    """save_csv saves data to a csv file
    Args:
        data (list of lists): list of loans

    Returns:
        csvPath (string): path to CSV file
    """
    #headers for the csv file
    headers = ["Lender", "Max Loan Amount", "Max LTV", "Max DTI", "Max Credit Score", "Interest Rate"]



    #open the csv gathered from prompt, write in the headers and data
    with open(outputPath, "w", newline='') as csvFile:

        csvWriter = csv.writer(csvFile, delimiter = ",")
        csvWriter.writerow(headers)
        for row in data:
            csvWriter.writerow(row)

    return outputPath
