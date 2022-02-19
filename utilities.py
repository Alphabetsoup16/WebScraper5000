from fastapi import Response
import requests
from bs4 import BeautifulSoup


def GetHtmlPageElementById(soup: BeautifulSoup, elementId):
    return soup.find(id=f"{elementId}")


def GetMeTheSoup(url):
    page = requests.get(url)
    return BeautifulSoup(page.content, "html.parser")
