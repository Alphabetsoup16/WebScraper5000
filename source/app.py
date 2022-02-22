from ast import Num
from typing import Dict, List
from attr import attrs
from bs4 import BeautifulSoup

from utilities.General_Utilities import GetMeTheSoup


# fake static job site for testing: https://realpython.github.io/fake-jobs/


def GetElementByAttribute(soup: BeautifulSoup,  Attrs: List):
    for a in range(len(Attrs)):
        specific_element = soup.find_all(attrs=Attrs[a])
        label = Attrs[a].values()
        for attr in specific_element:
            print(f"{list(label)[0]}: {attr.get_text().strip()}")


def GetElementByAttribute2(soup: BeautifulSoup,  Attrs: List):
    data = []
    targets = {}
    for dict in Attrs:
        specific_element = soup.find_all(attrs=dict)
        labels = dict.values()
        label = list(labels)[0]
        for target in specific_element:
            targets = {
                "Id": 1,
                label: target.get_text().strip()
            }
            data.append(targets)
        #print(f"{label}: {target.get_text().strip()}")
    return data


def main() -> None:

    soup = GetMeTheSoup("https://realpython.github.io/fake-jobs/")

    # test_attr = [{"class": "title"}, {"class": "location"}]
    # test = soup.find_all(attrs={"class": "title"})
    # print(test)

    # print(GetElementByAttribute(soup, [
    #       {"class": "title"}, {"class": "location"}]))

    print(GetElementByAttribute2(soup, [
          {"class": "title"}, {"class": "location"}]))


if __name__ == "__main__":
    main()
