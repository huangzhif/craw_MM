
#url管理器
class UrlManager:
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    #增加url
    def add_new_url(self,root_url):
        if root_url is None:
            return
        #如果不在新url集合 并且 不在旧url集合，则新增
        if root_url not in self.new_urls and root_url not in self.old_urls:
            self.new_urls.add(root_url)

    def add_new_urls(self,root_urls):
        if root_urls is None or len(root_urls) ==0:
            return

        for root_url in root_urls:
            self.add_new_url(root_url)

    def has_new_url(self):
        return len(self.new_urls) != 0

    def get_new_url(self):
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url