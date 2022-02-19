import requests
from bs4 import BeautifulSoup

def set_url_target(url):
    return requests.get(url)

def DisplayList(list) -> None:
    for item in list:
        print(item)
    print()

def GetHtmlPageElementById(elementId, page):
    soup = BeautifulSoup(page.content, "html.parser")
    return soup.find(id=f"{elementId}")