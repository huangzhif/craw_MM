from bs4 import BeautifulSoup
import urllib.parse
import re

class HtmlParser:
    def __init__(self):
        #self.page = set()
        self.new_urls = set()
        self.new_urls_pic = set()


    def _get_new_urls(self,soup):

        links = soup.find_all('a',href=re.compile(r"http://www.mzitu.com/\d+"))
        # #每个套图的最大页数
        #pic_max = soup.find_all('span')[10].text

        for link in links:
            new_url = link['href']
            self.new_urls.add(new_url)
        return self.new_urls

    #获取套图的每个图片
    def _get_new_urls_pic(self,soup):
        links = soup.find_all('a',href=re.compile(r"http://www.mzitu.com/\d+\d+"))
        for link in links:
            new_Url = link['href']
            self.new_urls_pic.add(new_Url)
        return self.new_urls_pic

    def parse(self,html_cont):
        if html_cont is None:
            return
        soup = BeautifulSoup(html_cont,'html.parser',from_encoding='utf-8')
        # #每个套图的最大页数
        #pic_max = soup.find_all('span')[11]
        new_urls = self._get_new_urls(soup)
        #url_page = self.page.add(pic_max)
        return new_urls

    def parse_pic(self,new_url,html_cont_pic):
        if html_cont_pic is None:
            return
        try:
            soup_pic = BeautifulSoup(html_cont_pic,'html.parser',from_encoding='utf-8')
            #每个套图的最大页数
            pic_max = soup_pic.find_all('span')[10].text

            #is_dig = int(pic_max).isdigit()
            #if is_dig:
            for i in range(1,int(pic_max) + 1):
                #new_full_url = urllib.parse.urljoin(new_url,i)
                new_full_url = new_url +'/'+ str(i)
                self.new_urls_pic.add(new_full_url)
        except:
            pass

        return self.new_urls_pic


















