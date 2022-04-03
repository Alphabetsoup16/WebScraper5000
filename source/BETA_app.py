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


def HyperLinkListConstructor(links_list: list) -> list:
    indexed_list_of_links = []
    for index, link in enumerate(links_list):
        indexed_list_of_links.append({index: link['href']})
    return indexed_list_of_links


def ExtractHyperLinksWithBaseAddress(json_dict: dict, base_address: str = None) -> list:
    """Extracts hyper links from parsed html"""
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
