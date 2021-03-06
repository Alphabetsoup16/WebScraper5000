import re
from bs4 import BeautifulSoup
from BETA_app import AttributeConstructor_All, AttributeConstructor_Specific, ExtractHyperLinksWithBaseAddress, GetDataFromJson
from utilities.general_utilities import GetMeTheSoup, GetHeaderInfo, SaveAsJson

# fake static job site for testing
URL = "https://realpython.github.io/fake-jobs/"


def GetTextFromSoupContent(content: list):
    text_content = []
    for result_set in content:
        for index, element in enumerate(result_set):
            text_content.append({index: element.get_text().strip()})
    return text_content


def ElementsWithRegexByClass(soup: BeautifulSoup, class_string: str):
    return soup.find_all(class_=re.compile(class_string))


def ElementsWithRegexById(soup: BeautifulSoup, id_string: str):
    return soup.find_all(id=re.compile(id_string))


def ElementsWithRegexByString(soup: BeautifulSoup, string: str):
    return soup.find_all(string=re.compile(string))


def GetTypesFromParserConfig(json_data: dict) -> bool:
    type_list = []
    for i in range(len(json_data['parser_config'])):
        type_list.append(json_data['parser_config'][i]['type'])
    return CheckDuplicateConfigTypes(type_list)


def CheckDuplicateConfigTypes(type_list: list) -> bool:
    if len(type_list) == len(set(type_list)):
        return False
    else:
        return True


def AttributeConstructor_Duplicate(json_data: dict, attribute_type: str) -> list:
    specific_attributes = []
    for config in json_data["parser_config"]:
        if config["type"] == attribute_type:
            specific_attributes.append(
                {config["type"]: config["attributes"]})
    return specific_attributes


def ConstructAttributesBasedOnConfig(json_data: dict, element_type: str = "default") -> list:
    is_duplicate = GetTypesFromParserConfig(json_data)
    if is_duplicate and element_type != "default":
        return AttributeConstructor_Duplicate(json_data, element_type)
    elif is_duplicate and element_type == "default":
        return AttributeConstructor_All(json_data)
    else:
        return AttributeConstructor_Specific(json_data, element_type)


def AggregateDuplicateAttributes(config_attr: list):
    # Ugh this is so inefficient.....
    final_list = []
    for list_attr in config_attr:
        attr_value_list = []
        for key, val in list_attr.items():
            for attr_val in val:
                attr_value_list.append({key: attr_val})
        final_list.append(attr_value_list)
    return final_list

    #############################---Functions above need to be tested---#############################


def main() -> None:

    soup = GetMeTheSoup(url=URL)

    # test4 = GetHeaderInfo(soup)
    # print(test4)
    # for header in test4:
    #     print(header.name, header.get_text())
    # SaveAsJson(test3, "page_links")

    test_attr2 = {"jobs": {"class": ["title is-5", "location", "company"]},
                  "page-details": {"class": ["subtitle is-3", "title is-1"]}}

    json_file_path = 'source/parser_request.json'

    json_data = GetDataFromJson(json_file_path)

    base_address = "https://realpython.github.io/"

    test6 = GetTypesFromParserConfig(json_data)
    # print(test6)

    test7 = ConstructAttributesBasedOnConfig(json_data, "class")
    AggregateDuplicateAttributes(test7)

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
    test9 = GetTextFromSoupContent([string_elements, class_elements])
    print(*test9, sep='\n')

    a_string = soup.find(string="Apply")
    # print(*soup.select("body a"), sep='\n')


if __name__ == "__main__":
    main()
