# File Name : anomaly_detector.py
# Student Name: Vishwaja Painjane, Zulqarnayan Hossain
# email:  painjavv@mail.uc.edu, hossaizn@mail.uc.edu
# Assignment Number: Assignment 11
# Due Date:   April 17, 2025
# Course #/Section:   IS 4010 Section 001
# Semester/Year:   Spring 2025
# Brief Description of the assignment:  We are creating a data processing pipeline from a CSV file that includes cleaning, anomaly detection, and ZIP code updating.

# Brief Description of what this module does. We are detecting anomalies in the fuel purchase data.
# Citations: openai.com/chatgpt

# Anything else that's relevant: N/A

import pandas as pd
import os

class AnomalyDetector:
    def __init__(self, df, anomalies_filename):
        self.df = df
        self.anomalies_filename = anomalies_filename

    def detect_anomalies(self):
        # Normalize and find rows where Fuel Type is exactly "Pepsi"
        anomalies = self.df[self.df['Fuel Type'].str.strip().str.lower() == 'pepsi']
        
        # Remove those rows from the original dataset
        cleaned_data = self.df[self.df['Fuel Type'].str.strip().str.lower() != 'pepsi']

        # Save anomalies to a separate CSV
        os.makedirs("Data", exist_ok=True)
        anomalies.to_csv(os.path.join("Data", self.anomalies_filename), index=False)

        print(f"Found {len(anomalies)} Pepsi rows")
        print(f"Returning {len(cleaned_data)} cleaned rows")

        return cleaned_data





