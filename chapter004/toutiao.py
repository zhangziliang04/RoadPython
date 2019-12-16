# 搜索关键字，并下载文章标题
import requests
import json
from urllib.parse import quote
print(quote('广州地铁塌陷'))
'''
>>> from urllib.parse import quote
>>> quote('汉字')
'%E6%B1%89%E5%AD%97'
>>> import urllib
>>> urllib.parse.unquote('%E6%B1%89%E5%AD%97')
'汉字'
>>>
>>> url = 'http://localhost:8000/odooallpro/%E7%9B%B8%E5%86%8C/'
>>> urllib.parse.unquote(url)
'http://localhost:8000/odooallpro/相册/'
>>>
'''

def page(startPage, endPage):
    for i in range(startPage-1, endPage):
        print("当前第%s页" % (i+1))
        url="https://www.toutiao.com/api/search/content/?aid=24&app_name=web_search&offset={}&format=json&keyword=%E5%B9%BF%E5%B7%9E%E5%9C%B0%E9%93%81%E5%A1%8C%E9%99%B7&autoload=true&count=20&en_qc=1&cur_tab=1&from=search_tab&pd=synthesis&timestamp=1562467283218".format(i*20)
        print(url)
        isPage=loadPage(url)
        if isPage==False:
            return

def loadPage(url):
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
        "cookie":"tt_webid=6710713392061285902; WEATHER_CITY=%E5%8C%97%E4%BA%AC; tt_webid=6710713392061285902; UM_distinctid=16bc9db8a29f6-0417349b599406-516d3e71-13c680-16bc9db8a2d85; csrftoken=5eb2a0e00bcbb888f417ef261ee5269a; CNZZDATA1259612802=1761938442-1562456487-https%253A%252F%252Fwww.baidu.com%252F%7C1562461887; s_v_web_id=ddb620b1224506f21ba99de20d4169e3; __tasessionId=ned4t635k1562467258609"
    }
    try:
        data = requests.get(url, headers=headers).text
        news = json.loads(data)
        print(news)
        for new in news["data"]:
            if "title" in new.keys():
                print(new["title"])
    except Exception as e:
        print(e)
        return False
    return True

if __name__ == '__main__':
    startPage = int(input("请输入起始页码："))
    endPage = int(input("请输入终止页码："))
    page(startPage,endPage)

