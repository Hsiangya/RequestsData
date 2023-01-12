"""
https://m.maoyan.com/board/4 电影名字、主演、上映时间、评分等信息
"""
import parsel
import requests

url = "https://m.maoyan.com/board/4"
headers = {
    # "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    # "Accept-Encoding": "gzip, deflate, br",
    # "Accept-Language": "zh-CN,zh-HK;q=0.9,zh;q=0.8,en-US;q=0.7,en;q=0.6",
    # "Cache-Control": "no-cache",
    # "Connection": "keep-alive",
    # "Cookie": "uuid_n_v=v1; iuuid=3F998A40921C11ED8D40893BDF77854AAC5C2738B47D464CA98D1A14F05723F8; webp=true; ci=108%2C%E7%8F%A0%E6%B5%B7; ci=108%2C%E7%8F%A0%E6%B5%B7; ci=108%2C%E7%8F%A0%E6%B5%B7; featrues=[object Object]; _lxsdk_cuid=185a3b0e284c8-0d6e9e11f6a7c-26021051-190140-185a3b0e284c8; _lxsdk=3F998A40921C11ED8D40893BDF77854AAC5C2738B47D464CA98D1A14F05723F8; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1673488557; _lxsdk_s=185a3d480e2-64-e17-951%7C%7CNaN; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1673491098",
    # "Host": " m.maoyan.com",
    # "Pragma": "no-cache",
    # "sec-ch-ua": '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
    # "sec-ch-ua-mobile": "?0",
    # "sec-ch-ua-platform": "Windows",
    # "Sec-Fetch-Dest": "document",
    # "Sec-Fetch-Mode": "navigate",
    # "Sec-Fetch-Site": "none",
    # "Sec-Fetch-User": "?1",
    # "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
}
response = requests.get(url=url, headers=headers)
"""自动识别编码"""
response.encoding = response.apparent_encoding
ResponseHtml = response.text
# print(ResponseHtml)
selector = parsel.Selector(ResponseHtml)
MovieInfos = selector.css(".board-card").getall()
# print(len(MovieInfos))
for movie in MovieInfos:
    SelectorData = parsel.Selector(movie)
    Title = SelectorData.css(".title::text").getall()[0]
    Actors = SelectorData.css(".actors::text").getall()[0]
    Date = SelectorData.css(".date::text").getall()[0][:10]
    Number = SelectorData.css(".extra-right>div>.number::text").getall()[0] + "分"
    print(Title, Actors, Date, Number)
