# Project: Web Scraper 5000
## Idea: Make generic web scraper for *educational purposes ONLY!* 
### Description: Written in Python 3.9 and using [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) Library for HTML data extraction 
### **How to use:** 
- Currently this project is still in the testing phase and needs to be refined on the front and backend. You can run the `parser_class.py` file to see most of the functionality in action. 
- The `TEST_app.py` contains all the new functions are getting tested and created. 
- The `api.py` and `api_model.py` are not complete yet but the 2 post methods work in `api.py` if you run the file and use PostMan to send a post request(in the shape of `parser_request.json`).
- The `BETA_app.py` contains all the functions that have passed initial testing but are still in development.  
- You can run the `api.py` file and navigate to the FastAPI docs at localhost/docs ex:`127.0.0.1:8000/docs` in order to view current API documentation. 
- The `parser_request.json` is the latest iteration of the general type of request the API will most likely handle. The hope is that the parser_class will be generic enough to handle any combination of request parameters and extract information from any type of website. 
- You will need to switch the api_url, port, and host in `api.py` to the values in the comments in order to run the uvicorn server locally. We are currently storing them as environment variables for testing. 