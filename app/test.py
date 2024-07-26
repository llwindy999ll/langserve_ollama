import requests
import json
url = "http://3.37.62.120:11434/api/generate"
data = {
    "model": "llama3",
    "prompt": "대한민국의 역대 왕조를 100자내외로 소개해줄래?"
}

headers = {'Content-Type': 'application/json'}

response = requests.post(url, json=data, headers=headers)


# 개별 JSON 객체로 분할
json_objects = response.content.decode().strip().split("\n")

# 각 JSON 객체를 Python 사전으로 변환
data = [json.loads(obj) for obj in json_objects]
res_text = ''
# 변환된 데이터 출력
for item in data:
    print(item)
    res_text += item['response']
    
print(res_text)