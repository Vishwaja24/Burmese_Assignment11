#Vish

import pandas as pd
import os

class AnomalyDetector:
    def __init__(self, input_file, anomalies_file, clean_data_file):
        self.input_file = input_file
        self.anomalies_file = anomalies_file
        self.clean_data_file = clean_data_file

    def detect_anomalies(self):
        df = pd.read_csv(self.input_file) #This will read the input CSV file.

        anomalies = df[df['Product'] != 'Fuel']
        cleaned_data = df[df['Product'] == 'Fuel'] #Filter out the anomalies

        os.makedirs('Data', exist_ok=True) #Create a directory named 'Data' if it doesn't exist
        anomalies.to_csv(os.path.join('Data', self.anomalies_file), index=False) #Save the anomalies to a CSV file

        cleaned_data.to_csv(os.path.join('Data', self.clean_data_file), index=False) #Save the cleaned data to a CSV file

        print("Anomalies and cleaned data processed successfully.")





