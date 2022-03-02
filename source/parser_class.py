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
        try:
            page = requests.get(self.url)
        except Exception as e:
            print(f"Request for html was unsuccessful, error: {e}")

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

    def ElementBuilder(self, element_lists, all_attributes) -> list:
        """Creates initial objects for each attribute"""
        target_elements = {}
        target_List = []
        if len(element_lists) > 1:
            for list_count in range(len(element_lists)):
                for key, target in enumerate(element_lists[list_count]):
                    target_elements = {
                        "Id": key,
                        all_attributes[list_count]: target.get_text().strip()
                    }
                    target_List.append(target_elements)
            return target_List
        else:
            return print("list of elements is either empty or only contains 1 element")

    def ResultElementGrouper(self, extracted_result: list) -> list:
        """Creates groups of results by Id"""
        result_groups = defaultdict(list)
        for result in extracted_result:
            result_groups[result['Id']].append(result)
        return result_groups

    def ResultHandler(self, grouped_results: list) -> list:
        """Creates completed JSON object from target attributes"""
        results_combined = []
        for result_value in grouped_results.values():
            result_object = {}
            for value in result_value:
                result_object |= value
            results_combined.append(result_object)
        return results_combined


def main() -> None:
    attributes = [{"class": "title is-5"}, {"class": "location"}]

    url = "https://realpython.github.io/fake-jobs/"

    static_site = StaticParser(url, "", False, [""], attributes)

    html = static_site.GetMeTheSoup()

    element_list = static_site.GetElementByAttribute(html)

    attribute_names = static_site.AttributeHandler()

    element_dicts = static_site.ElementBuilder(element_list, attribute_names)

    grouped_results = static_site.ResultElementGrouper(element_dicts)

    results = static_site.ResultHandler(grouped_results)

    print(*results, sep="\n")


# We can most definitely simplify these functions and or
# break them up into smaller pieces and create sub or separate classes

# TODO: Need to slim down ElementBuilder method...
if __name__ == "__main__":
    main()
