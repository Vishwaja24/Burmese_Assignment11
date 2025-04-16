# File Name : main.py
# Student Name: Vishwaja Painjane, Zulqarnayan Hossain
# email:  painjavv@mail.uc.edu, hossaizn@mail.uc.edu
# Assignment Number: Assignment 11
# Due Date:   April 17, 2025
# Course #/Section:   IS 4010 Section 001
# Semester/Year:   Spring 2025
# Brief Description of the assignment:  We are creating a data processing pipeline from a CSV file that includes cleaning, anomaly detection, and ZIP code updating.

# Brief Description of what this module does. We are orchestrating the entire data processing pipeline.
# Citations: openai.com/chatgpt

# Anything else that's relevant: N/A

from dataProcessorPackage.file_handler import FileHandler
from dataProcessorPackage.cleaner import DataCleaner
from dataEnhancerPackage.anomaly_detector import AnomalyDetector
from dataEnhancerPackage.zip_updater import ZipCodeUpdater

def main():
    # STEP 1: Load the original fuel purchase data from the Data folder
    fh = FileHandler()
    df = fh.load_csv("fuelPurchaseData.csv")

    # STEP 2: Clean the data
    cleaner = DataCleaner(df)
    cleaner.round_gross_price()
    cleaner.remove_duplicates()
    cleaned_df = cleaner.get_cleaned_data()

    # STEP 3: Detect anomalies (non-fuel rows like Pepsi)
    anomaly_detector = AnomalyDetector(cleaned_df, "dataAnomalies.csv")
    fuel_only_df = anomaly_detector.detect_anomalies()

    # STEP 4: Fill in missing ZIP codes using API
    zip_updater = ZipCodeUpdater(fuel_only_df, "f8bf6bbbbe78f07bfbfebfa8f0f66be10fb07bf")
    updated_df = zip_updater.update_missing_zip_codes()


    # STEP 5: Save final cleaned + enriched data
    fh.save_csv(updated_df, "cleanedData.csv")

    print("Data processing pipeline completed! Output saved to 'Data/cleanedData.csv'")


# Run the script
if __name__ == "__main__":
    main()


