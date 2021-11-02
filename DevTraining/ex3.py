import requests
from requests.exceptions import HTTPError
import json
import pandas as pd

apikey = '97ca7bc1a4a8a2cb7d0a3c14189778a6'
password = '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'
hostname = 'justblue0312.myshopify.com'
version = '2021-10'
resource = 'customers'

apiURL = f'https://{apikey}:{password}@{hostname}/admin/api/{version}/{resource}.json'

try:
    response_API = requests.get(apiURL)

    data = response_API.text
    parse_json = json.loads(data)

    customer_data = parse_json['customers']
    df = pd.DataFrame(data=customer_data)

    for item in customer_data:
        item['addresses'] = ''

    df.to_csv('output.csv', index=False)

except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')
except Exception as err:
    print(f'Other error occurred: {err}')  #
else:
    print('Success!')

df = pd.read_csv('output.csv')
print(df.to_string())
