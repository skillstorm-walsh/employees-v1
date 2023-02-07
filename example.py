import json
import requests


def lambda_handler(event, context):
    print('Hello', event['name'])
    response = requests.get('https://my-json-server.typicode.com/skillstorm-walsh/employees-v1/employees')
    data = json.loads(response.text)

    result = {}
    for emp in data:
        if emp['name'] == event['name']:
            result = emp

    return result
