# Just a place for testing ideas*

from bs4 import BeautifulSoup

# Testing child retrieval


def GetNestedPropsList2(soup: BeautifulSoup, parentTarget, childrenTargets):

    parent_element = soup.find_all(class_=parentTarget)

    # data_collection = []

    # for element in el_collection:
    #     el = {}

    #     for childAttr in childrenTargets:
    #         el[childAttr] = element.find(class_=childAttr).text.strip()

    #     data_collection.append(el)

    # return data_collection
