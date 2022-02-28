from collections import defaultdict
from dataclasses import dataclass
import requests
from bs4 import BeautifulSoup


@dataclass
class RequestConfig():
    url: str
    method: str
    nested: bool
    elements: list[str]
    attributes: list[dict]


class StaticParser(RequestConfig):

    def GetMeTheSoup(self):
        """Gets html content from url"""
        page = requests.get(self.url)
        return BeautifulSoup(page.content, "html.parser")

    def AttributeHandler(self) -> list:
        """Extracts target attribute names"""
        all_attributes = []
        if len(self.attributes) == 0:
            return "Attribute list is empty."

        for dict in self.attributes:
            all_attributes.append("".join(dict.values()))
        return all_attributes

    def GetElementByAttribute(self, soup: BeautifulSoup) -> list:
        """Gets all html elements from list of target attributes"""
        all_specific_elements = []
        for dict in self.attributes:
            specific_element = soup.find_all(attrs=dict)
            all_specific_elements.append(specific_element)
        return all_specific_elements

    def ElementBuilder(self, elementLists, all_attributes):
        """Creates initial objects for each attribute"""
        targetElements = {}
        targetElementsList = []
        if len(elementLists) > 1:
            for numOfList in range(len(elementLists)):
                for target in elementLists[numOfList]:
                    targetElements = {
                        "Id": elementLists[numOfList].index(target),
                        all_attributes[numOfList]: target.get_text().strip()
                    }
                    targetElementsList.append(targetElements)
            return targetElementsList
        else:
            return print("list of elements is either empty or only contains 1 element")

    def ResultHandler(self, extractedResult: list) -> list:
        """Creates completed JSON object from target attributes"""
        result_groups = defaultdict(list)
        for result in extractedResult:
            result_groups[result['Id']].append(result)

        results_combined = []
        for result_value in result_groups.values():
            jsonObj = {}
            for value in result_value:
                jsonObj |= value
            results_combined.append(jsonObj)

        return results_combined


def main() -> None:
    attributes = [{"class": "title is-5"}, {"class": "location"}]

    static_site = StaticParser(
        "https://realpython.github.io/fake-jobs/", "", False, [""], attributes)

    html = static_site.GetMeTheSoup()
    element_list = static_site.GetElementByAttribute(html)
    attribute_names = static_site.AttributeHandler()
    element_dicts = static_site.ElementBuilder(element_list, attribute_names)
    results = static_site.ResultHandler(element_dicts)
    print(*results, sep="\n")


if __name__ == "__main__":
    main()
