from collections import defaultdict
from dataclasses import dataclass, field
import requests
from bs4 import BeautifulSoup
from BETA_app import AttributeConstructor_Specific, GetDataFromJson


@dataclass
class StaticParser():
    config: dict
    attributes: list[dict]
    #elements: list[str] = field(default_factory=list)
    #all_attributes: list[str] = field(default_factory=list)

    def GetMeTheSoup(self) -> BeautifulSoup:
        """Gets html content from url"""
        try:
            page = requests.get(self.config['url'])
            return BeautifulSoup(page.content, "html.parser")
        except Exception as e:
            print(f"Request for html was unsuccessful, error: {e}")

    def AttributeHandler(self):
        """Extracts target attribute names"""
        all_attributes = []
        if self.attributes is None or len(self.attributes) is 0:
            print("Attribute list is empty or None.")
            return

        for attr_dict in self.attributes:
            all_attributes.append("".join(attr_dict.values()))
        return all_attributes

    def GetElementByAttribute(self) -> list:
        """Gets all html elements from list of target attributes"""
        soup = self.GetMeTheSoup()
        if soup is not None:
            all_specific_elements = []
            for attr_dict in self.attributes:
                specific_element = soup.find_all(attrs=attr_dict)
                all_specific_elements.append(specific_element)
            return all_specific_elements

    def ElementBuilder(self):
        """Creates initial objects for each attribute"""
        element_lists = self.GetElementByAttribute()
        all_attributes = self.AttributeHandler()

        if element_lists is None or len(element_lists) < 1 or all_attributes is None:
            print("list of elements or attributes is empty or None")
            return

        target_List = []
        for list_count in range(len(element_lists)):
            for index, target in enumerate(element_lists[list_count]):
                target_List.append({
                    "Id": index,
                    all_attributes[list_count]: target.get_text().strip()
                })
        return target_List

    def ResultElementGrouper(self) -> list:
        """Creates groups of results by Id"""
        extracted_result = self.ElementBuilder()
        if len(self.attributes) <= 1:
            return extracted_result

        if extracted_result is not None:
            result_groups = defaultdict(list)
            for result in extracted_result:
                result_groups[result['Id']].append(result)
            return result_groups

    def ResultHandler(self) -> list:
        """Creates completed JSON object from target attributes"""
        grouped_results = self.ResultElementGrouper()
        if grouped_results is not None and len(grouped_results) > 0:
            results_combined = []
            for result_value in grouped_results.values():
                result_object = {}
                for value in result_value:
                    result_object |= value
                results_combined.append(result_object)
            return results_combined
        else:
            return ["Ultra Generic Error"]


def main() -> None:

    ###### This is for testing parser_class ######
    json_file_path = 'source/parser_request.json'

    json_data = GetDataFromJson(json_file_path)

    attributes = AttributeConstructor_Specific(json_data, 'class')

    static_site = StaticParser(config=json_data, attributes=attributes)

    results = static_site.ResultHandler()

    print(*results, sep="\n")

    # TODO: Need to slim down ElementBuilder method... and result handler...
    # TODO: finalize request output model, decide if parameters are optional

    # TODO: Include list of available parsers? "html.parser", "lxml", "xml", "html5lib"
    # TODO: Make functionaity to input an html file and parse it?

    # TODO: find_all with regex function? find_all(string=re.compile("example"))
    # TODO: If elementBuilder isn't required, have fall back method? or pass list to ResultHandler?

    # TODO: Handle duplicate element attributes, on_duplicate_attribute='replace' or 'ignore' or function
    # TODO: Make enum of types for request? Or make definite list like class, string, id, regex etc


if __name__ == "__main__":
    main()
