from bs4 import BeautifulSoup
from numpy import linspace
from sqlalchemy import null
from utilities import GetMeTheSoup, GetHtmlPageElementById


# def JobListFinder(soup: BeautifulSoup):

#     # tricky to make this function generic
#     # Would need to pass it parent component, dict, class, specific html elements
#     job_elements = soup.find_all("div", class_="card-content")

#     job_list = []

#     for element in job_elements:
#         job = {
#             "title": None,
#             "company": None,
#             "location": None
#         }

#         job["title"] = element.find("h2", class_="title").text.strip()
#         job["company"] = element.find("h3", class_="company").text.strip()
#         job["location"] = element.find("p", class_="location").text.strip()

#         job_list.append(job)

#     print([job["title"] for job in job_list], sep="\n")


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


def ExtractAllLinks(soup: BeautifulSoup):
    links = soup.find_all('a')
    if(len(links) > 0):
        for link in links:
            print(link.get("href"))


def main() -> None:

    # fake static job site for testing: https://realpython.github.io/fake-jobs/

    soup = GetMeTheSoup("https://realpython.github.io/fake-jobs/")

    # GetHtmlPageElementById(soup, "ResultsContainer")

    # GetHeaderInfo(soup)

    # ExtractAllImages(soup)

    # JobListFinder(soup)

    # TODO: Need to make generic
    # SpecificElementFinder(soup, "h2", "python")

    ExtractAllLinks(soup)


if __name__ == "__main__":
    main()
