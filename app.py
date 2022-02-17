from bs4 import BeautifulSoup
import requests

# fake static job site for testing: https://realpython.github.io/fake-jobs/

url = "https://realpython.github.io/fake-jobs/"

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


page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="ResultsContainer")

JobFinderAndPrinter(results)