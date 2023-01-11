"""	-- 网址： https://www.bige7.com/book/1031/"""
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
    # print(ContextURL)
    ResponseContent = requests.get(ContextURL)
    ContextHtml = ResponseContent.text
    # print(ContextHtml)
    # print(ResponseContent.status_code)
    ReSelect = re.findall(
        'chaptercontent.*?Readarea ReadAjax_content">(.*?)<p class="readinline"',
        ContextHtml,
        re.S,
    )
    # print(ReSelect)
    Context: list = ReSelect[0].replace(r"\u3000", "").replace("<br />", "\n")
    print(Context)
# if __name__ == '__main__':
#     print(ChapterList)
