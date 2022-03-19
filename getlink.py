import urllib.request
from html.parser import HTMLParser

DURL = "http://localhost:8080/"

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag: str, attrs: list) -> None:
        if tag == "a":
            print(attrs)
        return super().handle_starttag(tag, attrs)

    def handle_endtag(self, tag: str) -> None:
        pass
        return super().handle_endtag(tag)
    
    def handle_data(self, data: str) -> None:
        pass
        return super().handle_data(data)

url = input("input URL : ")
if url == "":
    url = DURL

chcode = input("Character code : ")
if url == "":
    chcode = "UTF-8"

urlinfo = urllib.request.urlopen(url)

html = urlinfo.read()

parser = MyHTMLParser()
parser.feed(html.decode(chcode))