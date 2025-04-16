# File Name : file_handler.py
# Student Name: Vishwaja Painjane, Zulqarnayan Hossain
# email:  painjavv@mail.uc.edu, hossaizn@mail.uc.edu
# Assignment Number: Assignment 11
# Due Date:   April 17, 2025
# Course #/Section:   IS 4010 Section 001
# Semester/Year:   Spring 2025
# Brief Description of the assignment:  We are creating a data processing pipeline from a CSV file that includes cleaning, anomaly detection, and ZIP code updating.

# Brief Description of what this module does. We are handling file operations for reading and writing CSV files.
# Citations: openai.com/chatgpt

# Anything else that's relevant: N/A

import os
import pandas as pd

class FileHandler:
    """
    Handles reading from and writing to CSV files
    within the Data folder of the project.
    """

    def __init__(self):
        # Dynamically construct the absolute path to the Data folder
        self.data_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'Data')

    def load_csv(self, filename):
        """
        Loads a CSV file from the Data directory and returns a DataFrame.
        
        Parameters:
            filename (str): Name of the file to read (e.g., 'fuelPurchaseData.csv')
        
        Returns:
            pd.DataFrame: The loaded CSV data
        """
        path = os.path.join(self.data_dir, filename)
        if not os.path.exists(path):
            raise FileNotFoundError(f"File not found: {path}")
        return pd.read_csv(path)

    def save_csv(self, df, filename):
        """
        Saves a DataFrame to a CSV file in the Data directory.
        
        Parameters:
            df (pd.DataFrame): The data to save
            filename (str): The name of the output file (e.g., 'cleanedData.csv')
        """
        path = os.path.join(self.data_dir, filename)
        df.to_csv(path, index=False)

    def ensure_data_folder(self):
        """
        Creates the Data folder if it doesn't already exist.
        """
        if not os.path.exists(self.data_dir):
            os.makedirs(self.data_dir)

