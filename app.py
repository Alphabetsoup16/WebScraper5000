from bs4 import BeautifulSoup
import requests

# fake static job site for testing: https://realpython.github.io/fake-jobs/

url = "https://realpython.github.io/fake-jobs/"
page = requests.get(url)


def JobFinderAndPrinter(results) -> None:
    job_elements = results.find_all("div", class_="card-content")

    for element in job_elements:
        title_element = element.find("h2", class_="title")
        company_element = element.find("h3", class_="company")
        location_element = element.find("p", class_="location")
        print(title_element.text.strip())
        print(company_element.text.strip())
        print(location_element.text.strip())
        print()


def HtmlPageResults(elementId, page):

    soup = BeautifulSoup(page.content, "html.parser")
    return soup.find(id=f"{elementId}")


results = HtmlPageResults("ResultsContainer", page)

JobFinderAndPrinter(results)

# Gets all links for jobs that contain substring python
# TODO: Simplify this and maybe add it to jobFinderAndPrinter?
# or make it its own function or 2 functions, 1 for getting the jobs
# and one for getting the links

python_jobs = results.find_all(
    "h2", string=lambda text: "python" in text.lower()
)

python_job_elements = [
    h2_element.parent.parent.parent for h2_element in python_jobs
]

for job_element in python_job_elements:
    link_url = job_element.find_all("a")[1]["href"]
    print(f"Apply here: {link_url}\n")
