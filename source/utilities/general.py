import json
import requests
from bs4 import BeautifulSoup


def GetMeTheSoup(url):
    """Gets html content from url"""
    try:
        page = requests.get(url)
        return BeautifulSoup(page.content, "html.parser")
    except Exception as e:
        print(f"Request for html was unsuccessful, error: {e}")
        return


def GetDataFromJson(file_path: str):
    """Decodes JSON from file"""
    with open(file=file_path, mode='r') as config:
        data = json.load(config)
    return data


def SaveAsJson(response, title: str):
    """Saves parser response into a JSON"""
    with open(f'scraped_{title}.json', mode='w', encoding='latin-1') as f:
        json.dump(response, f, indent=8, ensure_ascii=False)
    print("Created Json File")


def GetHeaderInfo(soup: BeautifulSoup):
    """"Gets all information from site header"""
    tag_list = []
    for tag in soup.head.contents:
        if tag != '\n':
            tag_list.append(tag)
    print(f"The header contains: {len(tag_list)} elements")
    return tag_list
