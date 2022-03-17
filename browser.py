import webbrowser

DURL = "http://localhost:8080/"

url = input("input URL : ")
if url == "":
    url = DURL
    webbrowser.open(url)