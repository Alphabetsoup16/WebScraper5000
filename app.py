from bs4 import BeautifulSoup
import requests

# fake static job site for testing: https://realpython.github.io/fake-jobs/

url = "https://realpython.github.io/fake-jobs/"
page = requests.get(url)

# changed to method that returns a list of dictionaries for each job_element
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

def DisplayList(list) -> None:
    for item in list:
        print(item)
    print()


def HtmlPageResults(elementId, page):

    soup = BeautifulSoup(page.content, "html.parser")
    return soup.find(id=f"{elementId}")


def main() -> None:
    results = HtmlPageResults("ResultsContainer", page)

    all_jobs = JobListFinder(results)

    # Example of how the JobListFinder refactor can be used
    DisplayList(all_jobs)

    # TODO: Simplify the code below... maybe add it to jobFinderAndPrinter?
    # or make it its own function or 2 functions, 1 for getting the jobs
    # and one for getting the links, also abiity to add whatever substring we want to look for

    # lambda functions in python are mad ugly...
    # but it finds all h2 elements in the text(html) with the substring python
    python_jobs = results.find_all(
        "h2", string=lambda text: "python" in text.lower()
    )

    # kinda silly but it gets the h2's great grandparent element which contains the html for each job...
    # I am using list comprehension here to make it one line
    python_job_elements = [
        h2_element.parent.parent.parent for h2_element in python_jobs
    ]

    print(f"Found: {len(python_jobs)} of those jobs")

    # gets each jobs hyper link by getting all the "a" elements from each job and gets the href
    for job_element in python_job_elements:
        link_url = job_element.find_all("a")[1]["href"]
        print(f"Apply here: {link_url}\n")


if __name__ == "__main__":
    main()
