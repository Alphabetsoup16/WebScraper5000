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


# class ideas:
# first we need to design data schema.
# then we can add methods for all of those data points
# lastly we have a method that combines all outputs into a singular Json element
