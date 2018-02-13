import urllib.request

class HtmlDownloader:
    def download(self,new_roof):
        if new_roof is None:
            return

        response = urllib.request.urlopen(new_roof)

        if response.getcode() != 200:
            return None

        return response.read()

