# File Name : cleaner.py
# Student Name: Vishwaja Painjane, Zulqarnayan Hossain
# email:  painjavv@mail.uc.edu, hossaizn@mail.uc.edu
# Assignment Number: Assignment 11
# Due Date:   April 17, 2025
# Course #/Section:   IS 4010 Section 001
# Semester/Year:   Spring 2025
# Brief Description of the assignment:  We are creating a data processing pipeline from a CSV file that includes cleaning, anomaly detection, and ZIP code updating.

# Brief Description of what this module does. We are cleaning the fuel purchase data by rounding prices and removing duplicates.
# Citations: openai.com/chatgpt

# Anything else that's relevant: N/A

import pandas as pd

class DataCleaner:
    """
    Cleans the fuel purchase data by:
    - Rounding 'Gross Price' to 2 decimal places
    - Removing duplicate rows
    """

    def __init__(self, dataframe):
        """
        Initializes with a pandas DataFrame.
        
        Parameters:
            dataframe (pd.DataFrame): Raw data to clean
        """
        self.df = dataframe

    def round_gross_price(self):
        """
        Rounds the 'Gross Price' column to exactly 2 decimal places.
        If the column doesn't exist, nothing happens.
        """
        if 'Gross Price' in self.df.columns:
            self.df['Gross Price'] = self.df['Gross Price'].round(2)

    def remove_duplicates(self):
        """
        Removes exact duplicate rows from the DataFrame.
        """
        before = len(self.df)
        self.df = self.df.drop_duplicates()
        after = len(self.df)
        print(f"Removed {before - after} duplicate rows.")

    def get_cleaned_data(self):
        """
        Returns the cleaned DataFrame.
        
        Returns:
            pd.DataFrame: Cleaned data
        """
        return self.df

