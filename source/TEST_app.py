from collections import defaultdict
import re
from bs4 import BeautifulSoup
from utilities.General_Utilities import GetMeTheSoup

# fake static job site for testing: https://realpython.github.io/fake-jobs/


def AttributeHandler(Attrs: list) -> list:
    """Extracts target attribute names"""
    all_attributes = []
    if len(Attrs) == 0:
        return "Attribute list is empty."

    for dict in Attrs:
        all_attributes.append("".join(dict.values()))
    return all_attributes


def GetElementByAttribute(soup: BeautifulSoup,  Attrs: list) -> list:
    """Gets all html elements from list of target attributes"""
    all_specific_elements = []
    for dict in Attrs:
        specific_element = soup.find_all(attrs=dict)
        all_specific_elements.append(specific_element)
    return all_specific_elements


def ElementBuilder_OLD(elementLists, all_attributes):
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

# element_lists[numOfList].index(target)


def ElementBuilder(element_lists, all_attributes):
    """Creates initial objects for each attribute"""
    # Need to test this one to replace the older one
    target_elements = {}
    target_list = []
    if len(element_lists) > 1:
        for numOfList in range(len(element_lists)):
            for key, target in enumerate(element_lists[numOfList]):
                target_elements = {
                    "Id": key,
                    all_attributes[numOfList]: target.get_text().strip()
                }
                target_list.append(target_elements)
        return target_list
    else:
        return print("list of elements is either empty or only contains 1 element")


def ResultHandler_OLD(extractedResult: list):
    jsonObj = {}
    jsonList = []
    for result in extractedResult:
        for key, val in result.items():
            # See this works if its hardcoded to a number...
            if key == "Id" and val == 1:
                jsonObj.update(result)
    jsonList.append(jsonObj)
    return jsonList


def ResultElementGrouper(extracted_result: list) -> list:
    """Creates groups of results by ID"""
    result_groups = defaultdict(list)
    for result in extracted_result:
        result_groups[result['Id']].append(result)
    return result_groups


def ResultHandler(grouped_result: list) -> list:
    """Creates completed JSON object from target attributes"""

    results_combined = []
    for result_value in grouped_result.values():
        jsonObj = {}
        for value in result_value:
            jsonObj |= value
        results_combined.append(jsonObj)

    return results_combined
 ##############################Already tested above this line###################################


def FindParentElementsChild(soup: BeautifulSoup):
    content = soup.find(class_="media-content")
    print(content)
    siblings = content.find_next_siblings("h2")
    print(siblings)
    # for element in content:
    #     parent = content.find_parent()
    #     print(element.get_text().strip())


def ElementsWithRegexByClass(soup: BeautifulSoup, class_string: str):
    content = soup.find_all(class_=re.compile(class_string))
    for element in content:
        print(element.get_text(), sep="\n")


def ElementsWithRegexById(soup: BeautifulSoup, id_string: str):
    content = soup.find_all(id=re.compile(id_string))
    for element in content:
        print(element.get_text(), sep="\n")


def main() -> None:

    soup = GetMeTheSoup("https://realpython.github.io/fake-jobs/")

    attributes = [{"class": "title is-5"}, {"class": "location"}]

    # FindParentElementsChild(soup)

    # can change to list and find multiple class elements, can also use different attributes like id
    ElementsWithRegexByClass(soup, "title")


if __name__ == "__main__":
    main()
