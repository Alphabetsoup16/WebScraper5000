from abc import ABC, abstractmethod
import requests
from bs4 import BeautifulSoup


class Parser(ABC):
    @abstractmethod
    def GetWebPageHtmlData(self):
        '''Gets the html from webpage'''


class StaticParser(Parser):
    def __init__(self, url):
        self.url = url

    def GetWebPageHtmlData(self):
        html = requests.get(self.url)
        return BeautifulSoup(html.content, "html.parser")
