from typing import List
from bs4 import BeautifulSoup

from utilities import SetUrlTarget, DisplayList, GetHtmlPageElementById

# fake static job site for testing: https://realpython.github.io/fake-jobs/

# tricky to make this generic


def JobListFinder(results):
    job_elements = results.find_all("div", class_="card-content")

    job_list = []

    for element in job_elements:
        job = {
            "title": None,
            "company": None,
            "location": None
        }

        job["title"] = element.find("h2", class_="title").text.strip()
        job["company"] = element.find("h3", class_="company").text.strip()
        job["location"] = element.find("p", class_="location").text.strip()

        job_list.append(job)

    DisplayList(job_list)


def SpecificElementFinder(element, substring, html) -> None:

    all_specific_elements = html.find_all(
        f"{element}", string=lambda text: f"{substring}" in text.lower()
    )

    # Still specific to this particular site...
    specific_elements = [
        el.parent.parent.parent for el in all_specific_elements
    ]

    print(f"Found: {len(all_specific_elements)} of those jobs")

    # Also specific to this site
    for job_element in specific_elements:
        link_url = job_element.find_all("a")[1]["href"]
        print(f"Apply here: {link_url}\n")


def main() -> None:

    page = SetUrlTarget("https://realpython.github.io/fake-jobs/")

    results = GetHtmlPageElementById("ResultsContainer", page)

    JobListFinder(results)

    SpecificElementFinder("python", results)


if __name__ == "__main__":
    main()
