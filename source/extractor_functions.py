from bs4 import BeautifulSoup
from constructors import HyperLinkListConstructor
from utilities.general import GetMeTheSoup


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


def AggregateDuplicateAttributes(config_attr: list):
    final_attr_list = []
    for list_attr in config_attr:
        attr_value_list = []
        for key, val in list_attr.items():
            for attr_val in val:
                attr_value_list.append({key: attr_val})
        final_attr_list.append(attr_value_list)
    return final_attr_list
