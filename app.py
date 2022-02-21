from bs4 import BeautifulSoup
import json
from SiteClass import GetElementByAttribute, GetNestedPropsList2
from utilities import GetMeTheSoup, GetNestedPropsList, ExtractAllImages, ExtractAllLinks, GetHeaderInfo


def main() -> None:

    # fake static job site for testing: https://realpython.github.io/fake-jobs/

    soup = GetMeTheSoup("https://realpython.github.io/fake-jobs/")

    # print(GetHtmlPageElementById(soup, "ResultsContainer").prettify())

    extractedSoup = {
        "page": soup.title.get_text(),
        "jobs": GetNestedPropsList(soup, "card-content", ["title", "company", "location"]),
        "images": ExtractAllImages(soup),
        "links": ExtractAllLinks(soup, "Apply")
    }

    # turns dict into Json...
    extractedJSON = json.dumps(extractedSoup)
    print(extractedJSON)

    # testing this function, the idea is that
    # We can find/find_all by "attributes" ex: {"id" : "blah"}
    # Makes it more customizable than using class_ = or id =
    print(GetElementByAttribute(soup, "h2", {"class": "title"}))
    # GetHeaderInfo(soup)

    # TODO: Need to make generic
    # SpecificElementFinder(soup, "h2", "python")


if __name__ == "__main__":
    main()
