from collections import defaultdict
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


def GetElementByAttribute(soup: BeautifulSoup,  Attrs: list):
    """Gets all html elements from list of target attributes"""
    all_specific_elements = []
    for dict in Attrs:
        specific_element = soup.find_all(attrs=dict)
        all_specific_elements.append(specific_element)
    return all_specific_elements


def ElementBuilder(elementLists, all_attributes):
    """Creates initial objects for each attribute"""
    # Need to fix all_attributes iterating... remove n += 1 / n
    # Can add if stattment for if n < len(all_attributes)
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


def ElementBuilder2(elementLists, all_attributes):
    targetElements = {}
    numOfElementLists = len(elementLists)
    if numOfElementLists > 1:
        for numOfList in range(len(elementLists)):
            for target in elementLists[numOfList]:
                targetElements = {
                    "Id": elementLists[numOfList].index(target),
                    all_attributes[numOfList]: target.get_text().strip()
                }
                print(targetElements)


def ResultHandler(extractedResult: list):
    """Creates completed JSON object from target attributes"""
    jsonObj = {}
    jsonList = []
    for result in extractedResult:
        for key, val in result.items():
            # See this works if its hardcoded to a number...
            if key == "Id" and val == 1:
                jsonObj.update(result)
    jsonList.append(jsonObj)
    return jsonList


def ResultHandler2(extractedResult: list):
    result_groups = defaultdict(list)
    for result in extractedResult:
        result_groups[result['Id']].append(result)

    results_combined = []
    for result_key, result_value in result_groups.items():
        jsonObj = {}
        for value in result_value:
            jsonObj |= value
        results_combined.append(jsonObj)

    return results_combined


def main() -> None:

    soup = GetMeTheSoup("https://realpython.github.io/fake-jobs/")

    attributes = [{"class": "title is-5"}, {"class": "location"}]

    all_attributes = AttributeHandler(attributes)

    targetedAttributes = GetElementByAttribute(soup, attributes)

    targetElements = ElementBuilder(targetedAttributes, all_attributes)

    print(ResultHandler2(targetElements))


if __name__ == "__main__":
    main()
