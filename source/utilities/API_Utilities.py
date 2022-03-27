from bs4 import BeautifulSoup

# Made previous function modular and reusable for grabbing data from a list of card like html els that can be expected to have the same structure


def GetNestedPropsList(soup: BeautifulSoup, parentTarget, childrenTargets):

    el_collection = soup.find_all(class_=parentTarget)

    data_collection = []

    for element in el_collection:
        el = {}

        for childAttr in childrenTargets:
            el[childAttr] = element.find(class_=childAttr).text.strip()

        data_collection.append(el)

    return data_collection


def UseConfig(soup, config, response):
    """sets key : value pairs based on config settings"""
    for target in config["configs"]:
        if target["method"] == "nested-props":
            response[target["name"]] = GetNestedPropsList(
                soup, *target["arguments"])
