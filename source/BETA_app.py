import json
from bs4 import BeautifulSoup
from utilities.general_utilities import GetMeTheSoup

# File for functions outside of testing but still not finalized...


def GetDataFromJson(file_path: str):
    """Decodes JSON from file"""
    with open(file=file_path, mode='r') as config:
        data = json.load(config)
    return data


def AttributeConstructor_All(json_data: dict) -> list:
    """Constructs all attributes for parser"""
    attributes = []
    config_data = json_data['parser_config']
    for i in range(len(config_data)):
        for target in config_data[i]['attributes']:
            target_type = config_data[i]['type']
            attributes.append({target_type: target})
    return attributes


def AttributeConstructor_Specific(json_data: dict, attribute_type: str) -> list:
    """Constructs attributes for parser for specific element type"""
    specific_attributes = []
    config_data = json_data['parser_config']
    for i in range(len(config_data)):
        for target in config_data[i]['attributes']:
            target_type = config_data[i]['type']
            if target_type == attribute_type:
                specific_attributes.append({target_type: target})
    return specific_attributes


def HyperLinkListConstructor(links_list: list):
    indexed_list_of_links = []
    for index, link in enumerate(links_list):
        indexed_list_of_links.append({index: link['href']})
    return indexed_list_of_links


def ExtractHyperLinksWithBaseAddress(json_dict: dict, base_address: str = None) -> list:
    """Extracts hyper links from html"""
    soup: BeautifulSoup = GetMeTheSoup(json_dict["url"])
    if base_address is not None:
        links_list = soup.select(f'a[href^="{base_address}"]')
        return HyperLinkListConstructor(links_list)
    else:
        links_list = soup.select('a[href]')
        return HyperLinkListConstructor(links_list)


def GetConfigByElementNameValue(json_dict: dict, element_name: str):
    for config in json_dict["parser_config"]:
        if element_name in config.values():
            return config
