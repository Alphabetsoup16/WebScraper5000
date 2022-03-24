import json
import re
from bs4 import BeautifulSoup
from source.utilities.general_utilities import GetMeTheSoup

# fake static job site for testing: https://realpython.github.io/fake-jobs/


def GetTextFromSoupContent(content: list):
    # Probably don't need to do this and can just use 1 for loop
    for result_set in content:
        for element in result_set:
            print(element.get_text().strip(), sep="\n")


def ElementsWithRegexByClass(soup: BeautifulSoup, class_string: str):
    return soup.find_all(class_=re.compile(class_string))


def ElementsWithRegexById(soup: BeautifulSoup, id_string: str):
    return soup.find_all(id=re.compile(id_string))


def ElementsWithRegexByString(soup: BeautifulSoup, string: str):
    return soup.find_all(string=re.compile(string))


def GetDataFromJson(file_path: str):
    # testing opening json file to read and then create object with it
    with open(file=file_path, mode='r') as config:
        data = json.load(config)
    return data


def AttributeConstructor_All(json_data: dict) -> list:
    # Need to make this more efficient....
    attributes = []
    config_data = json_data['parser-config']
    for i in range(len(config_data)):
        for target in config_data[i]['target-attributes']:
            target_type = config_data[i]['target-attribute-type']
            attributes.append({target_type: target})
    return attributes


def AttributeConstructor_Specific(json_data: dict, attribute: str) -> list:
    # Need to test more and refine....
    specific_attributes = []
    config_data = json_data['parser-config']
    for i in range(len(config_data)):
        if config_data[i]['target-attribute-type'] == attribute:
            print({attribute: config_data[i]['target-attributes']})
        else:
            print(f"The attribute: {attribute}, is not valid")


def ExtractHyperLinksWithBaseAddress(soup: BeautifulSoup, base_address: str) -> list:
    indexed_list_of_links = []
    list_of_links = soup.select(f'a[href^="{base_address}"]')
    for index, link in enumerate(list_of_links):
        indexed_list_of_links.append({index: link['href']})
    return indexed_list_of_links


#############################---Functions above need to be tested---#############################


def main() -> None:

    soup = GetMeTheSoup(url="https://realpython.github.io/fake-jobs/")

    base_address = "https://realpython.github.io/"

    test3 = ExtractHyperLinksWithBaseAddress(soup, base_address)
    #print(*test3, sep="\n")

    def SaveAsJson(response, title: str):
        with open(f'scraped_{title}.json', mode='w', encoding='latin-1') as f:
            json.dump(response, f, indent=8, ensure_ascii=False)
        print("Created Json File")

    SaveAsJson(test3, "page_links")

    attributes = [{"class": "title is-5"}, {"class": "location"}]

    json_file_path = 'source/parser_request.json'

    json_data = GetDataFromJson(json_file_path)

    test = AttributeConstructor_All(json_data)
    #test2 = AttributeConstructor_Specific(json_data, 'wrong')

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


if __name__ == "__main__":
    main()
