"""	-- 网址： https://www.bige7.com/book/1031/"""
import os
import re

import parsel
import requests

url = "https://www.bqg70.com/book/1031/"
response = requests.get(url)
html = response.text
# 将html文本转化为html对象
selector = parsel.Selector(html)

ChapterURLList = selector.css(".listmain>dl>dd>a::attr(href)").getall()

# 只获取前10章
for url in ChapterURLList[:5]:
    ContextURL = "https://www.bqg70.com" + url
    ResponseContent = requests.get(ContextURL)
    ContextHtml = ResponseContent.text

    """获取章节标题"""
    selector = parsel.Selector(ContextHtml)
    ChapterTitle = selector.css(".content>.wap_none::text").getall()[0]
    # print(ChapterTitle)

    """获取小说内容"""
    ReSelect = re.findall(
        'chaptercontent.*?Readarea ReadAjax_content">(.*?)<p class="readinline"',
        ContextHtml,
        re.S,
    )

    """处理小说内容"""
    Context = ReSelect[0].replace(r"\u3000", "").replace("<br />", "\n")
    # print(Context)

    """保存到txt"""
    if not os.path.exists("剑来"):
        os.mkdir("剑来")
    with open("剑来/" + ChapterTitle + ".txt", "w", encoding="utf-8") as file:
        file.write(Context)
        print(f"保存：{ChapterTitle}成功")
