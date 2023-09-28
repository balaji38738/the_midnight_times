from .constants import NEWS_API_ENDPOINT
import os
import requests
import logging
import json

class NewsAPI(object):

    def __init__(self):
        self.host_url = NEWS_API_ENDPOINT
        self.api_key = os.environ.get('news_api_key')
        self.request_timeout = 30 # 30 sec timeout

    def get_response(self, method: str, *args, **kwargs):
        """
            Get response from News Endpoint
        """
        completed = False
        try:
            if "timeout" not in kwargs:
                kwargs["timeout"] = self.request_timeout
            response = getattr(requests, method)(*args, **kwargs)
            response_json = response.json()  # Get json response
            completed = True
        except requests.exceptions.RequestException as exc:
            logging.error("Request failed with %s", str(exc))
            response_json = {"error": str(exc)}
        except json.decoder.JSONDecodeError as err:
            logging.error("Request failed with %s", str(err))
            response_json = {"error": str(err), "text": response.text()}

        return response_json, completed

    def get_url(self, path: str):
        """
            Build url using path
        """

        return f'{self.host_url}/{path.lstrip("/")}'

    def get_headers(self):
        """
            Get headers
        """

        headers = {"x-api-key": self.api_key}
        return headers