from typing import List
from bs4 import BeautifulSoup

from utilities.General_Utilities import GetMeTheSoup


# fake static job site for testing: https://realpython.github.io/fake-jobs/

# def GetElementByAttribute2(soup: BeautifulSoup,  Attrs: List):
#     data = []
#     for dict in Attrs:
#         specific_element = soup.find_all(attrs=dict)
#         labels = dict.values()
#         label = list(labels)[0]
#         for target in specific_element:
#             print(f"{label}: {target.get_text().strip()}")
#     #         data.append(f"{label}: {target.get_text().strip()}")
#     # return data

# def GetElementByAttribute(soup: BeautifulSoup,  Attrs: list):
#     for a in range(len(Attrs)):
#         specific_element = soup.find_all(attrs=Attrs[a])
#         label = Attrs[a].values()
#         for attr in specific_element:
#             print(f"{list(label)[0]}: {attr.get_text().strip()}")


# def GetElementByAttribute3(soup: BeautifulSoup,  Attrs: list):
#     for dict in Attrs:
#         specific_element = soup.find_all(attrs=dict)
#         labels = dict.values()
#         label = list(labels)[0]
#         ElementBuilder(specific_element, label)


def GetElementByAttribute4(soup: BeautifulSoup,  Attrs: list):
    all_specific_elements = []

    for dict in Attrs:

        specific_element = soup.find_all(attrs=dict)
        all_specific_elements.append(specific_element)

    return all_specific_elements


def ElementBuilder(elementLists, all_attributes):
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
    return


def AttributeHandler(Attrs: list):
    all_attributes = []
    for dict in Attrs:
        all_attributes.append("".join(dict.values()))
    return all_attributes


def main() -> None:

    soup = GetMeTheSoup("https://realpython.github.io/fake-jobs/")

    attributes = [{"class": "title is-5"}, {"class": "location"}]

    all_attributes = AttributeHandler(attributes)

    targetedAttributes = GetElementByAttribute4(soup, attributes)

    targetElements = ElementBuilder(targetedAttributes, all_attributes)
    print(targetElements)


if __name__ == "__main__":
    main()