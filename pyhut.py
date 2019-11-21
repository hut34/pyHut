import pandas as pd
import requests

token = 'eyJhbGciOiJSUzI1NiIsImtpZCI6IjhhMzY5M2YxMzczZjgwYTI1M2NmYmUyMTVkMDJlZTMwNjhmZWJjMzYiLCJ0eXAiOiJKV1QifQ.eyJuYW1lIjoiSmFuIEhvY2hicnVlY2tuZXIiLCJwaWN0dXJlIjoiaHR0cHM6Ly9saDMuZ29vZ2xldXNlcmNvbnRlbnQuY29tLy1uQVd2cW9BWG5Zby9BQUFBQUFBQUFBSS9BQUFBQUFBQUFBQS9BQ0hpM3JmUGtySUxkc2I5dlJqSGJ2dlNiZmJLdng5N1NBL3Bob3RvLmpwZyIsIm93bmVyIjp0cnVlLCJhZG1pbiI6dHJ1ZSwiaXNzIjoiaHR0cHM6Ly9zZWN1cmV0b2tlbi5nb29nbGUuY29tL3N0YW5kYXJkZGF0YWh1YiIsImF1ZCI6InN0YW5kYXJkZGF0YWh1YiIsImF1dGhfdGltZSI6MTU3NDIyOTA4NiwidXNlcl9pZCI6Im9hdkttaDdFWmdoZ3I3R00yaHo3blFTWXduRjMiLCJzdWIiOiJvYXZLbWg3RVpnaGdyN0dNMmh6N25RU1l3bkYzIiwiaWF0IjoxNTc0MzA4NjQxLCJleHAiOjE1NzQzMTIyNDEsImVtYWlsIjoiamFuQGh1dDM0LmlvIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsImZpcmViYXNlIjp7ImlkZW50aXRpZXMiOnsiZ29vZ2xlLmNvbSI6WyIxMTQxNzUwMjI3NDMwMTIwNTkxNTUiXSwiZW1haWwiOlsiamFuQGh1dDM0LmlvIl19LCJzaWduX2luX3Byb3ZpZGVyIjoiZ29vZ2xlLmNvbSJ9fQ.pAMnMqlN2_16cAh6mOeca6XbyKXIY0-10K5U7Xe1znAxsZn3HIGPgvP0bqz4YueEmV6FAmj7YeX5zSnFxjGUBRr_AtltitwoqWZ00KuNdYjWy-xuVoj6LiRNQAiPUbF5L1OmrwOckqI77iL5p3mPOs-QbJ_q6agy4A5vzpJU0YBjNVdX8GzkVwlSFdmfqN7iJodRwjfC6K-qVBwKgfXb0pMsy2JibIXdrgUSazdOQmQ-TojAa2ocCsSHpdefi3u2Q8ss7G2NlqM7GaDHI3ofoctY_SnD7eH_8gFjPAxJ6lajArTTPQhgqaWFvSkuQVUgEFZCxJTUEa8_hEQhyKJ7cQ'
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