import json
import datetime

with open('ourjson.json') as f:
    json_file = json.load(f)

token = ourjson['token']
expires = ourjson['expires']

expires_date = datetime.datetime.strptime(expires, '%Y-%m-%d %H:%M:%S')
remaining_time = expires_date - datetime.datetime.now()

print(f'Token: {token}')
print(f'Time remaining: {remaining_time}')
