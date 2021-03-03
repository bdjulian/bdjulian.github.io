# -*- coding: utf-8 -*-
"""search-query

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1AmRszDvQdZyp3l-Sb54PNKwv3fpwXNTT
"""

import requests
import json

#this runs the query that returns job id's  and threat scoress, threat scores are nice, verdicts too. jobid's are then used in the next one
import requests
import json
url = "https://www.hybrid-analysis.com/api/v2/search/terms?_timestamp=1614630850155"
headers = {'Content-Type': 'application/x-www-form-urlencoded', 'api-key': 'zcxpuuhp272a1e1bvcq18bg46bd2d94609x2l9xv1eef8812c5pu6hmi9a438676', 'user-agent': 'Falcon Sandbox', 'accept': 'application/json'}
payload = {
    'filetype': 'url',
    'env_id': 100,
    'verdict': 5,
    'date_from': '2020-09-28 00:00',
    'date_to': '2020-10-29 00:00',
}
r = requests.post(url, data=payload, headers=headers)
r.json
data = r.json()
data_result = data['result']

for i in data_result:
  print(i['job_id'])

data

#this is neceessary for some reason, json.loads(r.text) throws an error
#r = r.text
data = json.loads(r.text)

#data.keys(), here I am testing to see at what level Ican access job id's, it is in the results key, and then each one is simply the job id
#using this I can hopefully begin a pipelined process in which I store job id's and insert them into the next query to begin 
data_result = data['result']
data_result

for i in data_result:
  print(i['job_id'])

for i in data_result:
  print('hi'+i['job_id'])

# print from dropboox I dowloaded job id = 5f9a05839fb71b523c1a2b59
# url = 'https://www.dropbox.com/s/ohd4dw3u8wb0skm/290605d4e1a27ba1bf5539f0390d4b7437fe0eac0260984cf4c5fa259fc97b11_report.misp.json?dl=1'
# r = requests.get(url)
# json_object = r.json()
# json_object

#proper getrequest from HA, looks like simple URL hacking is possible?
url = "https://www.hybrid-analysis.com/api/v2/report/5f9a05839fb71b523c1a2b59/report/misp-json?_timestamp=1614629473094"
headers = {'api-key': 'zcxpuuhp272a1e1bvcq18bg46bd2d94609x2l9xv1eef8812c5pu6hmi9a438676', 'user-agent': 'Falcon Sandbox', 'accept': 'application/json', 'accept-encoding': 'gzip'}

r = requests.get(url, headers=headers)

job1 = json.loads(r.text)
job1