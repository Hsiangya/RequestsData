import requests

"""
https://www.ku6.com/video/feed?pageNo=0&pageSize=40&subjectId=76
数据：title、picPath、playUrl
"""
url = "https://www.ku6.com/video/feed?pageNo=0&pageSize=40&subjectId=76"
response = requests.get(url=url).json()
print(response)
data_list = response["data"]

for data in data_list:
    title = data["title"]
    picPath = data["picPath"]
    playUrl = data["playUrl"]
    print(title, picPath, playUrl, sep=" | ")
