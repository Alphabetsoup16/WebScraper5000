from extractor_functions import GetTypesFromParserConfig


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
