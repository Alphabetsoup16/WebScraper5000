from fastapi import Response
import requests
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
    if(len(image) > 0):
        for image in images:
            imageAlt = image.get('alt')
            imageSrc = image.get('src')
            print(f"Alternative Text: {imageAlt} Source: {imageSrc}")
    else:
        print("No images found")


def ExtractAllLinks(soup: BeautifulSoup, linkText):
    links = soup.find_all('a', text=f"{linkText}")
    if(len(links) > 0):
        for link in links:
            print(link.get('href'))

# Made previous function modular and reusable for grabbing data from a list of card like html els that can be expected to have the same structure
def GetNestedPropsList(soup: BeautifulSoup, elType, className, childrenTargets):

    el_collection = soup.find_all(elType, class_=className)

    data_collection = []

    for element in el_collection:
        el = {}

        for childAttr in childrenTargets:
            el[childAttr[1]] = element.find(childAttr[0], childAttr[1]).text.strip()

        data_collection.append(el)

    return data_collection