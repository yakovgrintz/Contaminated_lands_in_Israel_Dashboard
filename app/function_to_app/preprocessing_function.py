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
            preprocessing_func.pre_processing_data(data)
            return data
        else:
            print(f"Failed to retrieve data. Status code: {response.status_code}")
            return None

    @staticmethod
    def pre_processing_data(data):
        columns_to_drop = ['_id', 'X', 'Y', 'ktuvet']
        data.drop(columns_to_drop, axis=1, inplace=True)
        data['Peelut mezahemet'] = data['Peelut mezahemet'].replace('-', 'אחר')
        data['Drisha lemigun mivnim'] = data['Drisha lemigun mivnim'].replace('------', 'אחר')
        data['Matzav Minhali'] = data['Matzav Minhali'].replace('-', 'אחר')

        # Preprocess 'Moed thilat tipul' to extract the year or leave as empty string
        data['Moed thilat tipul'] = data['Moed thilat tipul'].apply(lambda x: preprocessing_func.handle_year_conversion(x))
        data['Moed thilat tipul'] = pd.to_numeric(data['Moed thilat tipul'], errors='coerce').fillna(0).replace(41275,
                                                                                                                0)
    @staticmethod
    def handle_year_conversion(x):
        try:
            if '.' in x:
                float_x = float(x)
                if float_x.is_integer():
                    return str(int(float_x))
            year = pd.to_datetime(x, errors='coerce').year
            if pd.notnull(year):
                return str(int(year))
        except Exception:
            pass
        return ''


