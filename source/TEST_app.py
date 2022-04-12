import re
from bs4 import BeautifulSoup
from BETA_app import AttributeConstructor_All, AttributeConstructor_Specific, ExtractHyperLinksWithBaseAddress, GetDataFromJson, AggregateDuplicateAttributes, ConstructAttributesBasedOnConfig, GetTypesFromParserConfig
from utilities.general_utilities import GetMeTheSoup, GetHeaderInfo, SaveAsJson

# fake static job site for testing
URL = "https://realpython.github.io/fake-jobs/"


def ElementsWithRegexByClass(soup: BeautifulSoup, class_string: str):
    return soup.find_all(class_=re.compile(class_string))


def ElementsWithRegexById(soup: BeautifulSoup, id_string: str):
    return soup.find_all(id=re.compile(id_string))


def ElementsWithRegexByString(soup: BeautifulSoup, string: str):
    return soup.find_all(string=re.compile(string))


def GetElementWithRegex(json_data: dict, regex_search: str, regex_type: str):
    # Need to test this
    soup: BeautifulSoup = GetMeTheSoup(json_data["url"])
    if regex_type == "class":
        return ElementsWithRegexByClass(soup, regex_search)
    elif regex_type == "string":
        return ElementsWithRegexByString(soup, regex_search)
    elif regex_type == "id":
        return ElementsWithRegexById(soup, regex_search)
    else:
        print("you can only assign regex_type to class, string, or id")
        return

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
    print(test7)
    # print(AggregateDuplicateAttributes(test7))

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

    a_string = soup.find(string="Apply")
    # print(*soup.select("body a"), sep='\n')


if __name__ == "__main__":
    main()
