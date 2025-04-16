#main.py

from dataEnhancerPackage.anomaly_detector import AnomalyDetector
from dataEnhancerPackage.zip_updater import ZipUpdater

if __name__ == "__main__":
    # Anomaly Detection
    anomaly_detector = AnomalyDetector("fuel_data.csv", "dataAnomalies.csv", "cleanedData.csv")
    anomaly_detector.detect_anomalies()

    # Zip Code Update
    zip_updater = ZipUpdater("cleanedData.csv", "updatedData.csv", "YOUR_API_KEY")
    zip_updater.update_zip_codes()
