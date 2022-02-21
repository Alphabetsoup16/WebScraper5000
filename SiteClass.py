# Just a place for testing ideas*

from abc import ABC, abstractmethod
from bs4 import BeautifulSoup
import requests


def SpecificElementFinder(soup: BeautifulSoup, element, substring) -> None:

    all_specific_elements = soup.find_all(
        f"{element}", string=lambda text: f"{substring}" in text.lower()
    )

    # # Still specific to this particular site...
    # specific_elements = [
    #     el.parent.parent.parent for el in all_specific_elements
    # ]

    # print(f"Found: {len(all_specific_elements)} of those jobs")

    # # Also specific to this site
    # for job_element in specific_elements:
    #     link_url = job_element.find_all("a")[1]["href"]
    #     print(f"Apply here: {link_url}\n")

# Testing child retrieval


def GetNestedPropsList2(soup: BeautifulSoup):

    parent_element = soup.find_all(["h2", "h3", "p"])

    for child in parent_element:
        print(child.get_text().strip())

# Testing find/findall for any element


def GetElementByAttribute(soup: BeautifulSoup, AttrType, Attrs):
    specific_element = soup.find_all(AttrType, Attrs)
    for attr in specific_element:
        print(attr.get_text().strip())


# Testing classes
# trying to think of more general abstract methods vs just putting methods in the sub classes


class Parser(ABC):
    @abstractmethod
    def GetWebPageHtmlData(self):
        '''Gets the html from webpage'''


class StaticParser(Parser):
    def __init__(self, url):
        self.url = url

    def GetWebPageHtmlData(self, url):
        html = requests.get(url)
        return BeautifulSoup(html.content, "html.parser")
