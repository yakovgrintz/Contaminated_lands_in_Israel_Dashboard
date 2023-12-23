import requests, pandas as pd


class preprocessing_func:
    @staticmethod
    def get_data():
        url = r"https://data.gov.il/api/3/action/datastore_search?resource_id=cbb2ed28-310d-4389-a1ec-64bb538fc090"

        response = requests.get(url)
        if response.status_code == 200:
            data_json = response.json()
            # get only records
            records = data_json['result']['records']
            data = pd.json_normalize(records)
            # convert_data_to_geo
            return data
        else:
            print(f"Failed to retrieve data. Status code: {response.status_code}")
            return None
