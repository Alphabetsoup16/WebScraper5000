from collections import defaultdict
from dataclasses import dataclass, field
import requests
from bs4 import BeautifulSoup
from TEST_app import AttributeConstructor_Specific, GetDataFromJson


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
        if len(self.attributes) == 0:
            return "Attribute list is empty."

        for dict in self.attributes:
            all_attributes.append("".join(dict.values()))
        return all_attributes

    def GetElementByAttribute(self) -> list:
        """Gets all html elements from list of target attributes"""
        soup = self.GetMeTheSoup()
        if soup is not None:
            all_specific_elements = []
            for dict in self.attributes:
                specific_element = soup.find_all(attrs=dict)
                all_specific_elements.append(specific_element)
            return all_specific_elements

    def ElementBuilder(self):
        """Creates initial objects for each attribute"""
        element_lists = self.GetElementByAttribute()
        if element_lists == None or len(element_lists) < 1:
            return print("list of elements is either empty or only contains no elements")

        else:
            all_attributes = self.AttributeHandler()
            target_elements = {}
            target_List = []

            for list_count in range(len(element_lists)):
                for index, target in enumerate(element_lists[list_count]):
                    target_elements = {
                        "Id": index,
                        all_attributes[list_count]: target.get_text().strip()
                    }
                    target_List.append(target_elements)
            return target_List

    def ResultElementGrouper(self) -> list:
        extracted_result = self.ElementBuilder()
        """Creates groups of results by Id"""
        if len(self.attributes) <= 1:
            return extracted_result

        if extracted_result is None:
            return
        else:
            result_groups = defaultdict(list)
            for result in extracted_result:
                result_groups[result['Id']].append(result)
            return result_groups

    def ResultHandler(self) -> list:
        """Creates completed JSON object from target attributes"""
        grouped_results = self.ResultElementGrouper()
        if grouped_results is not None:
            results_combined = []
            for result_value in grouped_results.values():
                result_object = {}
                for value in result_value:
                    result_object |= value
                results_combined.append(result_object)
            return results_combined

    # @classmethod
    # def JsonToObject(cls, json_request):
    #     '''Converts json to object dictionary'''
    #     json_dict = json.loads(json_request)
    #     return cls(**json_dict)


def main() -> None:

    ###### These are for testing parser_class ######
    json_file_path = 'source/parser_request.json'

    json_data = GetDataFromJson(json_file_path)

    attributes = AttributeConstructor_Specific(json_data, 'class')

    static_site = StaticParser(config=json_data, attributes=attributes)

    results = static_site.ResultHandler()

    print(*results, sep="\n")

    #parser_json = StaticParser.JsonToObject()

    # We can most definitely simplify these functions and or
    # break them up into smaller pieces and create sub or separate classes

    # TODO: Need to slim down ElementBuilder method... and result handler...
    # TODO: finalize request output model, decide if parameters are optional

    # TODO: Include list of available parsers? "html.parser", "lxml", "xml", "html5lib"
    # TODO: Make functionaity to input an html file and parse it?

    # TODO: find_all with regex function? find_all(string=re.compile("example"))
    # TODO: If elementBuilder isn't required, have fall back method? or pass list to ResultHandler?

    # TODO: Need to test GetMeTheSoup with a bad url and make sure other methods can handle error
    # TODO: Handle duplicate element attributes, on_duplicate_attribute='replace' or 'ignore' or function


if __name__ == "__main__":
    main()
