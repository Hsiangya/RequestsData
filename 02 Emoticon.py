import os

import parsel
import requests

url = "https://www.biaoqingbao.net/gaoxiao/page_{}.html"
for page in range(1, 20):
    response = requests.get(url.format(page))
    # print(url.format(page))
    ResponseHtml = response.text
    # with open("html.html", "w", encoding="utf-8") as file:
    #     file.write(ResponseHtml)
    # print(ResponseHtml)
    # with open("html.txt", "w", encoding="utf-8") as FileHtml:
    #     FileHtml.write(ResponseHtml)
    selector = parsel.Selector(ResponseHtml)
    # EmotionUrls = selector.css(".post-img>a>img::attr(src)").getall()
    EmotionUrls = selector.css(".waitpic::attr(data-original)").getall()
    # print(len(EmotionUrls))
    for EmotionUrl in EmotionUrls:
        try:
            """获取图片文本数据"""
            ImgBin = requests.get(EmotionUrl).content
            """文件名"""
            FileName = EmotionUrl.split("/")[-1]
            """保存到文件"""
            if not os.path.exists("img"):
                os.mkdir("img")
            with open("img/" + FileName, "wb") as file:
                file.write(ImgBin)
                print("已保存表情：" + FileName)
        except Exception as e:
            with open("errors.txt", "w+", encoding="utf-8") as ErrorsFile:
                ErrorsFile.write("获取失败：" + EmotionUrl)
