from collections import defaultdict
from dataclasses import dataclass, field
import requests
from bs4 import BeautifulSoup


@dataclass
class StaticParser():
    # This is for testing purposes
    url: str
    attributes: list[dict]
    method: str = ""
    nested: bool = False
    elements: list[str] = field(default_factory=list)

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

    def GetElementByAttribute(self) -> list:
        """Gets all html elements from list of target attributes"""
        soup: BeautifulSoup = self.GetMeTheSoup()
        all_specific_elements = []
        for dict in self.attributes:
            specific_element = soup.find_all(attrs=dict)
            all_specific_elements.append(specific_element)
        return all_specific_elements

    def ElementBuilder(self, element_lists) -> list:
        """Creates initial objects for each attribute"""
        all_attributes = self.AttributeHandler()
        target_elements = {}
        target_List = []
        if len(element_lists) > 1:
            for list_count in range(len(element_lists)):
                for index, target in enumerate(element_lists[list_count]):
                    target_elements = {
                        "Id": index,
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

    static_site = StaticParser(url, attributes)

    element_list = static_site.GetElementByAttribute()

    element_dicts = static_site.ElementBuilder(element_list)

    grouped_results = static_site.ResultElementGrouper(element_dicts)

    results = static_site.ResultHandler(grouped_results)

    print(*results, sep="\n")


# We can most definitely simplify these functions and or
# break them up into smaller pieces and create sub or separate classes

# TODO: Need to slim down ElementBuilder method... and result handler...
# TODO: finalize request output model, decide if parameters are optional

# TODO: Include list of available parsers? "html.parser", "lxml", "xml", "html5lib"
# TODO: Make functionaity to input an html file and parse it?
# TODO: find_all with regex function? find_all(string=re.compile("example"))
if __name__ == "__main__":
    main()
