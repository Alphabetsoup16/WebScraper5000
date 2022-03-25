# Project: Web Crawler Of Doom
## Idea: Make generic web scraper for *educational purposes ONLY!* 
### Description: Written in Python 3.9 and using [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) Library for HTML data extraction 
### **How to use:** 
- Currently this project is still in the testing phase and needs to be refined on the front and backend. You can run the `parser_class.py` file to see most of the functionality in action. 
- The `TEST_app.py` is where all the new functions are getting tested and created. The API and API model are not complete yet and only have partial functionality. 
- You can run the `api.py` file and navigate to the FastAPI docs at localhost/docs ex:`127.0.0.1:8000/docs` in order to view current API documentation. 
- The `parser_request.json` is the latest iteration of the general type of request the API will most likely handle. The hope is that the parser_class will be generic enough to handle any combination of request parameters and extract information from any type of website. 