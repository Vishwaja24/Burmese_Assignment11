#Vish

import requests
import pandas as pd
import os

class ZipUpdater:
    def __init__(self, input_file, output_file, api_key):
        self.input_file = input_file
        self.output_file = output_file
        self.api_key = api_key
        self.api_url = "https://app.zipcodebase.com/api/v1/search"

    def update_zip_codes(self):
        # Read the input file
        df = pd.read_csv(self.input_file)

        # Identify rows with missing zip codes
        missing_zips = df[df['ZipCode'].isnull()]

        for index, row in missing_zips.iterrows():
            city = row['City']
            state = row['State']

            # Make API request
            params = {'apikey': self.api_key, 'city': city, 'state': state}
            try:
                response = requests.get(self.api_url, params=params)
                response_data = response.json()

                if 'results' in response_data and response_data['results']:
                    # Use the first zip code from results
                    df.at[index, 'ZipCode'] = response_data['results'][0]['zipcode']

            except Exception as e:
                print(f"Error updating zip code for {city}, {state}: {e}")

        # Write the updated data to a new file
        os.makedirs('Data', exist_ok=True)
        df.to_csv(os.path.join('Data', self.output_file), index=False)
        print("Zip codes updated successfully.")
