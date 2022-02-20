# Just a place for testing ideas*

from abc import ABC, abstractmethod
from bs4 import BeautifulSoup

# Testing child retrieval


def GetNestedPropsList2(soup: BeautifulSoup):

    parent_element = soup.find_all(["h2", "h3", "p"])

    for child in parent_element:
        print(child.get_text().strip())


# Testing classes

class Parser(ABC):
    def __init__(self, url):
        self.url = url

    @abstractmethod
    def GetWebPageHtmlData(self):
        '''Gets the html from webpage'''
