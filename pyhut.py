import pandas as pd
import requests

token = '<insert token here>'
def show():
    """
    Lists all available datasets in a panda dataframe
    """
    response = requests.post(url="http://localhost:8080/user/getUploadedDatasets",data={'token': token})
    if response.status_code == 200:
        data = response.json()
        return pd.DataFrame(data=[x['data'] for x in data],index=[x['id'] for x in data])
    else:
        return 'Error getting list of datasets'

def load(dataset_id):
    """
    Loads a dataset into a panda dataframe
    """
    parameters = {'token': token, 'dataSetId': dataset_id}
    response = requests.post(url="http://localhost:8080/user/downloadFile",data=parameters)
    if response.status_code == 200:
        data = response.json()
        return pd.DataFrame(data=data['data'],columns=[x['name'] for x in data['header']])
    else:
        return 'Error loading dataset'
