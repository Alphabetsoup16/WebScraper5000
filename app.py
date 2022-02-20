from bs4 import BeautifulSoup
from utilities import GetMeTheSoup, GetHtmlPageElementById, GetNestedPropsList, ExtractAllImages, ExtractAllLinks, GetHeaderInfo


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


def main() -> None:

    # fake static job site for testing: https://realpython.github.io/fake-jobs/

    soup = GetMeTheSoup("https://realpython.github.io/fake-jobs/")

    # print(GetHtmlPageElementById(soup, "ResultsContainer").prettify())

    extractedSoup = {
        "page": soup.title.get_text(),
        "jobs": GetNestedPropsList(soup, ["div", "card-content"], [["h2", "title"], ["h3", "company"], ["p", "location"]]),
        "images": ExtractAllImages(soup),
        "links": ExtractAllLinks(soup, "Apply")
    }
    
    print(extractedSoup)

    # GetHeaderInfo(soup)

    # TODO: Need to make generic
    # SpecificElementFinder(soup, "h2", "python")


if __name__ == "__main__":
    main()
