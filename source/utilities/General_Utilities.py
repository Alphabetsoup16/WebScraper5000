import json
import requests
from bs4 import BeautifulSoup


def GetMeTheSoup(url):
    page = requests.get(url)
    return BeautifulSoup(page.content, "html.parser")


def SaveAsJson(response, title: str):
    with open(f'scraped_{title}.json', mode='w', encoding='latin-1') as f:
        json.dump(response, f, indent=8, ensure_ascii=False)
    print("Created Json File")


def GetHeaderInfo(soup: BeautifulSoup):
    tag_list = []
    for tag in soup.head.contents:
        tag_list.append(tag)
    print(f"The header contains: {len(tag_list)} elements")
    return tag_list
