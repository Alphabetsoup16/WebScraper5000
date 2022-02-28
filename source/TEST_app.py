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


def ElementBuilder(element_lists, all_attributes):
    """Creates initial objects for each attribute"""
    # Need to test this one to replace the older one
    target_elements = {}
    target_list = []
    if len(element_lists) > 1:
        for numOfList in range(len(element_lists)):
            for target in element_lists[numOfList]:
                target_elements = {
                    "Id": element_lists[numOfList].index(target),
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


def main() -> None:

    soup = GetMeTheSoup("https://realpython.github.io/fake-jobs/")

    attributes = [{"class": "title is-5"}, {"class": "location"}]

    all_attributes = AttributeHandler(attributes)

    targeted_attributes = GetElementByAttribute(soup, attributes)

    target_elements = ElementBuilder(targeted_attributes, all_attributes)

    grouped_elements = ResultElementGrouper(target_elements)

    results = ResultHandler(grouped_elements)

    print(*results, sep="\n")


if __name__ == "__main__":
    main()