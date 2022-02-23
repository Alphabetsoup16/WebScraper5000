import json
from multiprocessing.sharedctypes import Value
from bs4 import BeautifulSoup
from pydantic import Json
from utilities.General_Utilities import GetMeTheSoup


# fake static job site for testing: https://realpython.github.io/fake-jobs/

def GetElementByAttribute(soup: BeautifulSoup,  Attrs: list):
    """Gets all html elements from list of target attributes"""
    all_specific_elements = []
    for dict in Attrs:
        specific_element = soup.find_all(attrs=dict)
        all_specific_elements.append(specific_element)
    return all_specific_elements


def ElementBuilder(elementLists, all_attributes):
    """Creates initial objects for each attribute"""
    targetElements = []
    targets = {}
    n = 0
    for elements in elementLists:
        for target in elements:
            targets = {
                "Id": elements.index(target),
                all_attributes[n]: target.get_text().strip()
            }
            targetElements.append(targets)
        n += 1
    return targetElements


def ResultHandler(extractedResult: list):
    """Creates completed JSON object from target attributes"""
    JsonObj = {}
    for result in extractedResult:
        for key, val in result.items():
            if(key == "Id" and val == 1):
                JsonObj.update(result)
    print(JsonObj)


def AttributeHandler(Attrs: list):
    """Extracts target attribute names"""
    all_attributes = []
    for dict in Attrs:
        all_attributes.append("".join(dict.values()))
    return all_attributes


def main() -> None:

    soup = GetMeTheSoup("https://realpython.github.io/fake-jobs/")

    attributes = [{"class": "title is-5"}, {"class": "location"}]

    all_attributes = AttributeHandler(attributes)

    targetedAttributes = GetElementByAttribute(soup, attributes)

    targetElements = ElementBuilder(targetedAttributes, all_attributes)
    # print(targetElements)

    JsonObj = ResultHandler(targetElements)
    # print(JsonObj)


if __name__ == "__main__":
    main()
