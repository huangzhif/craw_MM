#coding:utf-8
import urllib.request
import requests
import re
from bs4 import BeautifulSoup
from Init_pkg import craw_downloader,craw_manager,craw_outputer,craw_parser

class SpiderMain:
    def __init__(self):
        self.urls = craw_manager.UrlManager()
        self.downloader = craw_downloader.HtmlDownloader()
        self.parser = craw_parser.HtmlParser()

    def craw(self,root_url):
        count = 1
        pic_pkg = 0
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2107.204 Safari/537.36'}

        #反盗链
        Picreferer = {
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
            'Referer': 'http://i.meizitu.net'
        }
        try:
            html_cont = self.downloader.download(root_url)
            # 获取套图urls
            root_urls = self.parser.parse(html_cont)
            #把urls放到 url管理器中统一管理
            self.urls.add_new_urls(root_urls)
            pic_pkg = len(self.urls.new_urls)
        except:
            print("fail")

        while self.urls.has_new_url():
            #获取套图主路径
            new_url = self.urls.get_new_url()
            html_cont_pic = self.downloader.download(new_url)
            #把每个套图的所有图片链接，放到parser里
            root_urls = self.parser.parse_pic(new_url,html_cont_pic)
            #print(root_urls)


            count += 1

            if count == pic_pkg: #pic_pkg
                break

        #循环所有图片
        for index,url in enumerate(self.parser.new_urls_pic):
            html_cont_con = self.downloader.download(url)
            #pic_cont = self.parser.parse(html_cont_con)
            mess = BeautifulSoup(html_cont_con,'html.parser')
            title = mess.find('h2', class_='main-title').text

            try:
                aa = str(title).index('（')
            except ValueError:
                print("ValueError")

            titles = title[:aa]
            pic_url = mess.find('img',alt = titles)
            try:
                file_name = pic_url['src'].split(r'/')[-1]
                html = requests.get(pic_url['src'], headers=Picreferer)
            except TypeError:
                print("TypeError")


            with open(file_name,"wb") as f:
                f.write(html.content)

            # if index == 1:
            #     break

            print(index)
        print("index")


if __name__ == "__main__":
    root_url="http://www.mzitu.com"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
