# -*- coding: utf-8 -*-

import requests
import json

token = ""
api_name = "http://comdo.hanlp.com/hanlp/v1/ner/place"
headers = {
    'token': ""
}

with open(r'./shPlace_data.json', 'r', encoding='utf8')as fp:
    json_data = json.load(fp)
# print("length of data:", len(json_data))

test_result = {}
sample_name = "test_"
sample_cnt = 0
for item in json_data:
    for index in range(10):
        text = json_data[item][index]["name"]
        data = {
            "text": text
        }
        res = requests.post(api_name, data=data, headers=headers)
        name = sample_name+str(sample_cnt)
        sample_cnt += 1
        res = json.loads(res.text)
        test_result[name] = dict(name=text, res=res["data"])

filepath = "apiTestResult.json"
with open(filepath, 'w', encoding='utf-8') as file_obj:
    json.dump(test_result, file_obj, indent=4, ensure_ascii=False)


