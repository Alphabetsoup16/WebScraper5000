from bs4 import BeautifulSoup


def GetHtmlPageElementById(soup: BeautifulSoup, elementId):
    return soup.find(id=f"{elementId}").text.strip()
