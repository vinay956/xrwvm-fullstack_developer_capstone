# Uncomment the imports below before you add the function code
import requests  # Added the requests import
import os
from dotenv import load_dotenv
# Removed the import of get_request, analyze_review_sentiments, post_review

load_dotenv()

backend_url = os.getenv(
    'backend_url', default="http://localhost:3030")
sentiment_analyzer_url = os.getenv(
    'sentiment_analyzer_url',
    default="http://localhost:5050/")


# Add code for get requests to backend
def get_request(endpoint, **kwargs):
    params = ""
    if kwargs:
        for key, value in kwargs.items():  # Added whitespace after the comma
            params = params + key + "=" + value + "&"  # Added whitespace around operator

    request_url = backend_url + endpoint + "?" + params

    print("GET from {} ".format(request_url))
    try:
        # Call get method of requests library with URL and parameters
        response = requests.get(request_url)
        return response.json()
    except requests.exceptions.RequestException as e:  # Specify exception type
        # If any error occurs
        print(f"Network exception occurred: {e}")


# Add code for retrieving sentiments
def analyze_review_sentiments(text):

    request_url = sentiment_analyzer_url + "analyze/" + text
    try:
        # Call get method of requests library with URL and parameters
        response = requests.get(request_url)
        return response.json()
    except requests.exceptions.RequestException as err:  # Specify exception type
        print(f"Unexpected {err=}, {type(err)=}")
        print("Network exception occurred")


# Add code for posting review
def post_review(data_dict):

    request_url = backend_url + "/insert_review"
    try:
        response = requests.post(request_url, json=data_dict)  # Added whitespace after the comma
        print(response.json())
        return response.json()
    except requests.exceptions.RequestException as e:  # Specify exception type
        print(f"Network exception occurred: {e}")
