from bs4 import BeautifulSoup

from utilities import SetUrlTarget, DisplayList, GetHtmlPageElementById

# fake static job site for testing: https://realpython.github.io/fake-jobs/


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

    return job_list


def SpecificJobFinder(substring, html) -> None:

    python_jobs = html.find_all(
        "h2", string=lambda text: f"{substring}" in text.lower()
    )

    python_job_elements = [
        h2_element.parent.parent.parent for h2_element in python_jobs
    ]

    print(f"Found: {len(python_jobs)} of those jobs")

    for job_element in python_job_elements:
        link_url = job_element.find_all("a")[1]["href"]
        print(f"Apply here: {link_url}\n")


def main() -> None:

    page = SetUrlTarget("https://realpython.github.io/fake-jobs/")

    results = GetHtmlPageElementById("ResultsContainer", page)

    all_jobs = JobListFinder(results)

    DisplayList(all_jobs)

    SpecificJobFinder("python", results)


if __name__ == "__main__":
    main()
