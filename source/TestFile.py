
from bs4 import BeautifulSoup
from source.utilities.API_Utilities import GetNestedPropsList

from utilities import GetMeTheSoup

# Just a place for testing ideas*
soup = GetMeTheSoup("https://realpython.github.io/fake-jobs/")


def SpecificElementFinder(soup: BeautifulSoup, element, substring) -> None:

    all_specific_elements = soup.find_all(
        f"{element}", string=lambda text: f"{substring}" in text.lower()
    )

    # # Still specific to this particular site...
    # specific_elements = [
    #     el.parent.parent.parent for el in all_specific_elements
    # ]

    # print(f"Found: {len(all_specific_elements)} of those jobs")

    # # Also specific to this site
    # for job_element in specific_elements:
    #     link_url = job_element.find_all("a")[1]["href"]
    #     print(f"Apply here: {link_url}\n")

# Testing child retrieval


def GetNestedPropsList2(soup: BeautifulSoup):

    parent_element = soup.find_all(["h2", "h3", "p"])

    for child in parent_element:
        print(child.get_text().strip())


# Testing find/findall for any element


def GetElementByAttribute(soup: BeautifulSoup, AttrType, Attrs):
    specific_element = soup.find_all(AttrType, Attrs)
    for attr in specific_element:
        print(attr.get_text().strip())


# testing this function, the idea is that
# We can find/find_all by "attributes" ex: {"id" : "blah"}
# Makes it more customizable than using class_ = or id =
print(GetElementByAttribute(soup, "h2", {"class": "title"}))


def ExtractedHtmlAsJson(soup):
    extractedSoup = {
        "page": soup.title.get_text(),
        "jobs": GetNestedPropsList(soup, "card-content", ["title", "company", "location"]),
        "images": ExtractAllImages(soup),
        "links": ExtractAllLinks(soup, "Apply")
    }

    return json.dumps(extractedSoup)


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
