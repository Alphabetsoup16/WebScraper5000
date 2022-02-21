from fastapi import Response
import requests
import json
from bs4 import BeautifulSoup


def GetHtmlPageElementById(soup: BeautifulSoup, elementId):
    return soup.find(id=f"{elementId}")


def GetMeTheSoup(url):
    page = requests.get(url)
    return BeautifulSoup(page.content, "html.parser")


def GetHeaderInfo(soup: BeautifulSoup):
    print(f"The header contains: {len(soup.head.contents)} elements")
    for tag in soup.head.contents:
        print(tag)


def ExtractAllImages(soup: BeautifulSoup):
    images = soup.find_all('img')

    if(len(images)) == 0:
        return None

    image_collection = []

    for image in images:
        img = {
            "alt": image.get('alt'),
            "src": image.get('src')
        }
        image_collection.append(img)
    return image_collection


def ExtractAllLinks(soup: BeautifulSoup, linkText):
    links = soup.find_all('a', text=f"{linkText}")

    if(len(links) == 0):
        return None

    link_collection = []

    for link in links:
        link_collection.append(link.get('href'))
    return link_collection


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


def ExtractedHtmlAsJson(soup):
    extractedSoup = {
        "page": soup.title.get_text(),
        "jobs": GetNestedPropsList(soup, "card-content", ["title", "company", "location"]),
        "images": ExtractAllImages(soup),
        "links": ExtractAllLinks(soup, "Apply")
    }

    return json.dumps(extractedSoup)

# more FP example of data handling
def UseConfig(config, response):
    soup = GetMeTheSoup(config["url"])
    # loop through each config "object" and set new keys/values on response dict based on config contents
    for target in config["configs"]:
        if target["method"] == "nested-props":
            response[target["name"]] = GetNestedPropsList(soup, *target["arguments"])
        if target["method"] == "extract-links":
            response[target["name"]] = ExtractAllLinks(soup, *target["arguments"])