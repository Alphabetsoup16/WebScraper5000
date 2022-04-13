import re
from bs4 import BeautifulSoup
from utilities.general import GetMeTheSoup


def ElementsWithRegexByClass(soup: BeautifulSoup, class_string: str):
    return soup.find_all(class_=re.compile(class_string))


def ElementsWithRegexById(soup: BeautifulSoup, id_string: str):
    return soup.find_all(id=re.compile(id_string))


def ElementsWithRegexByString(soup: BeautifulSoup, string: str):
    return soup.find_all(string=re.compile(string))


def GetElementWithRegex(json_data: dict, regex_search: str, regex_type: str):
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
