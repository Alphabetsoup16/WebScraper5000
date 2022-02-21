from bs4 import BeautifulSoup
from utilities import GetMeTheSoup

# fake static job site for testing: https://realpython.github.io/fake-jobs/


def main() -> None:

    soup = GetMeTheSoup("https://realpython.github.io/fake-jobs/")


if __name__ == "__main__":
    main()
