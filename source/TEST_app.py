from cgi import test
from distutils.command.config import config
import re
from bs4 import BeautifulSoup
from BETA_app import AttributeConstructor_All, AttributeConstructor_Specific, ExtractHyperLinksWithBaseAddress, GetDataFromJson
from utilities.general_utilities import GetMeTheSoup, GetHeaderInfo, SaveAsJson

# fake static job site for testing
URL = "https://realpython.github.io/fake-jobs/"


def GetTextFromSoupContent(content: list):
    for result_set in content:
        for element in result_set:
            print(element.get_text().strip(), sep="\n")


def ElementsWithRegexByClass(soup: BeautifulSoup, class_string: str):
    return soup.find_all(class_=re.compile(class_string))


def ElementsWithRegexById(soup: BeautifulSoup, id_string: str):
    return soup.find_all(id=re.compile(id_string))


def ElementsWithRegexByString(soup: BeautifulSoup, string: str):
    return soup.find_all(string=re.compile(string))


def GetTypesFromParserConfig(json_data: dict) -> bool:
    type_list = []
    config_data = json_data['parser_config']
    for i in range(len(config_data)):
        type_list.append(config_data[i]['type'])
    return CheckDuplicateConfigTypes(type_list)


def CheckDuplicateConfigTypes(type_list: list) -> bool:
    if len(type_list) == len(set(type_list)):
        return False
    else:
        return True


def AttributeConstructor_Duplicate(json_data: dict, attribute_type: str) -> dict:
    specific_attributes = []
    for config in json_data['parser_config']:
        target_type = config["type"]
        if target_type == attribute_type:
            specific_attributes.append({config["element_name"]: {
                target_type if i == 1 else f'{target_type}_{i}': attr
                for i, attr in enumerate(config["attributes"], start=1)}
            })
    return specific_attributes


def ConstructAttributesBasedOnConfig(json_data: dict, element_type: str = "default"):
    is_duplicate = GetTypesFromParserConfig(json_data)
    if is_duplicate and element_type != "default":
        return AttributeConstructor_Duplicate(json_data, element_type)
    elif is_duplicate and element_type == "default":
        return AttributeConstructor_All(json_data)
    else:
        return AttributeConstructor_Specific(json_data, element_type)

    #############################---Functions above need to be tested---#############################


def main() -> None:

    soup = GetMeTheSoup(url=URL)

    # test4 = GetHeaderInfo(soup)
    # print(test4)
    # for header in test4:
    #     print(header.name, header.get_text())
    # SaveAsJson(test3, "page_links")

    attributes = [{"class": "title is-5"},
                  {"class": "location"},
                  {"class": "company"}]

    test_attrs1 = {"jobs": {"class": "title is-5", "class": "location", "class": "company"},
                   "page-details": {"class": "subtitle is-3", "class": "title is-1"}}

    test_attr2 = {"jobs": {"class": ["title is-5", "location", "company"]},
                  "page-details": {"class": ["subtitle is-3", "title is-1"]}}

    json_file_path = 'source/parser_request.json'

    json_data = GetDataFromJson(json_file_path)

    base_address = "https://realpython.github.io/"

    test6 = GetTypesFromParserConfig(json_data)
    # print(test6)
    test7 = ConstructAttributesBasedOnConfig(json_data, "class")
    print(test7)

    test3 = ExtractHyperLinksWithBaseAddress(json_data, base_address)
    # print(*test3, sep="\n")

    test = AttributeConstructor_All(json_data)
    test2 = AttributeConstructor_Specific(json_data, 'string')
    # print(test2)

    # Need to test out RegexByString more. Simplfied process to make more efficient.
    class_string = "title"
    string_str = "er"

    class_elements = ElementsWithRegexByClass(soup, class_string)
    string_elements = ElementsWithRegexByString(soup, string_str)
    # for string in string_elements:
    #     print(string.strip(), sep='\n')
    # GetTextFromSoupContent([string_elements])

    a_string = soup.find(string="Apply")
    # print(*soup.select("body a"), sep='\n')


if __name__ == "__main__":
    main()
