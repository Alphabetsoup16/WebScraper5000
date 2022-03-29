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

#############################---Functions above need to be tested---#############################


def main() -> None:

    soup = GetMeTheSoup(url=URL)

    test4 = GetHeaderInfo(soup)
    # print(test4)
    # for header in test4:
    #     print(header.name, header.get_text())
    #SaveAsJson(test3, "page_links")

    attributes = [{"class": "title is-5"},
                  {"class": "location"},
                  {"class": "company"}]

    test_attrs = {"jobs": {"class": "title is-5", "class": "location", "class": "company"},
                  "page-details": {"class": "subtitle is-3", "class": "title is-1"}}

    json_file_path = 'source/parser_request.json'

    json_data = GetDataFromJson(json_file_path)

    base_address = "https://realpython.github.io/"

    test3 = ExtractHyperLinksWithBaseAddress(json_data, base_address)
    #print(*test3, sep="\n")

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
    #print(*soup.select("body a"), sep='\n')

    # TODO: Testing nested dictionaries to better understand them
    # This will be used for parser_request for different element_names but same type
    # The idea is that the attributeConstructor needs to separate them by element_names into nested dicts
    # So that the rest of the functions can run the 2 (in this case) separately
    people = {1: {'Name': 'Joann', 'Age': '27', 'Sex': 'Female'},
              2: {'Name': 'Jordan', 'Age': '69', 'Sex': 'Male'}}

    for p_id, p_info in people.items():
        print("\nPerson ID:", p_id)

        for key, val in p_info.items():
            print(key + ':', val)


if __name__ == "__main__":
    main()
