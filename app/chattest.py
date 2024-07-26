import requests
import json

url = "http://3.37.62.120:11434/api/chat"

headers = {'Content-Type': 'application/json'}
data = {
    "model": "llama3",
    "messages": [
        {
            "role": "user",
            "content": "why is the sky blue?"
        }
    ]
}

response = requests.post(url, headers=headers, json=data)

# if response.status_code == 200:
# #     result = response.json()
#     print("Success")  # Assuming the API returns the answer in JSON
# else:
#     print(f"Request failed with status code: {response.status_code}")


# 개별 JSON 객체로 분할
json_objects = response.content.decode().strip().split("\n")

# 각 JSON 객체를 Python 사전으로 변환
data = [json.loads(obj) for obj in json_objects]
res_text = ''

# 변환된 데이터 출력
for item in data:
    print(item)
    res_text += item['message']['content']
    
print(res_text)