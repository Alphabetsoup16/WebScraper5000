import json
from bs4 import BeautifulSoup
from source.parser_class import StaticParser

##############################Already tested, these are old junk###################################


def AttributeHandler_OLD(Attrs: list) -> list:
    """Extracts target attribute names"""
    all_attributes = []
    if len(Attrs) == 0:
        return "Attribute list is empty."

    for dict in Attrs:
        all_attributes.append("".join(dict.values()))
    return all_attributes


def GetElementByAttribute_OLD(soup: BeautifulSoup,  Attrs: list) -> list:
    """Gets all html elements from list of target attributes"""
    all_specific_elements = []
    for dict in Attrs:
        specific_element = soup.find_all(attrs=dict)
        all_specific_elements.append(specific_element)
    return all_specific_elements


def ElementBuilder_OLD(elementLists, all_attributes):
    targetElements = []
    targets = {}
    n = 0
    for elements in elementLists:
        for target in elements:
            targets = {
                "Id": elements.index(target),
                all_attributes[n]: target.get_text().strip()
            }
            targetElements.append(targets)
        n += 1
    return targetElements


def ElementBuilder_OLD(element_lists, all_attributes):
    """Creates initial objects for each attribute"""
    # Need to test this one to replace the older one
    target_elements = {}
    target_list = []
    if len(element_lists) > 1:
        for numOfList in range(len(element_lists)):
            for key, target in enumerate(element_lists[numOfList]):
                target_elements = {
                    "Id": key,
                    all_attributes[numOfList]: target.get_text().strip()
                }
                target_list.append(target_elements)
        return target_list
    else:
        return print("list of elements is either empty or only contains 1 element")


def ResultHandler_OLD(extractedResult: list):
    jsonObj = {}
    jsonList = []
    for result in extractedResult:
        for key, val in result.items():
            # See this works if its hardcoded to a number...
            if key == "Id" and val == 1:
                jsonObj.update(result)
    jsonList.append(jsonObj)
    return jsonList


def ResultElementGrouper_OLD(extracted_result: list) -> list:
    """Creates groups of results by ID"""
    result_groups = defaultdict(list)
    for result in extracted_result:
        result_groups[result['Id']].append(result)
    return result_groups


def ResultHandler_OLD(grouped_result: list) -> list:
    """Creates completed JSON object from target attributes"""

    results_combined = []
    for result_value in grouped_result.values():
        jsonObj = {}
        for value in result_value:
            jsonObj |= value
        results_combined.append(jsonObj)

    return results_combined


def MultipleJsonToObject_OLD(file_name: str) -> list:
    # Probably don't need this... depends on JSON set up
    json_list = []
    with open(file=file_name, mode='r') as json_file:
        json_data = json.loads(json_file.read())
        for data in json_data:
            json_list.append(StaticParser(**data))
    return json_list


@classmethod
def JsonToObject_OLD(cls, json_string):
    '''Converts json to object dictionary'''
    json_dict = json.loads(json_string)
    return cls(**json_dict)


def AttributeConstructor_Duplicate_OLD(json_data: dict, attribute_type: str) -> list:
    specific_attributes = []
    for config in json_data['parser_config']:
        target_type = config["type"]
        if target_type == attribute_type:
            specific_attributes.append({config["element_name"]: {
                target_type if i == 1 else f'{target_type}_{i}': attr
                for i, attr in enumerate(config["attributes"], start=1)}
            })
    return specific_attributes

# API methods:
# @app.post(f"{api_url}/scrape")
# async def get_config(request: Request):
#     config = await request.json()
#     soup = GetMeTheSoup(config["url"])
#     response = {}
#     UseConfig(soup, config, response)
#     return response

    attributes = [{"class": "title is-5"},
                  {"class": "location"},
                  {"class": "company"}]

    test_attrs1 = {"jobs": {"class": "title is-5", "class": "location", "class": "company"},
                   "page-details": {"class": "subtitle is-3", "class": "title is-1"}}
