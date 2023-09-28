from .news_api import NewsAPI
from .constants import REQUEST_TIMEOUT_SEC
""" This module deals with get news api """

class GetNews(NewsAPI):
    """
        This class deals with get news api
    """

    def __init__(self):
        super().__init__()
        self.path = "/"
        self.request_timeout = REQUEST_TIMEOUT_SEC

    def execute(self, keyword):
        """
            Method to execute get news request
            returns news api response & success_status for the searched keyword
            Parameters:
                   keyword
            Returns:
                json api response, success status
        """
        response_data, completed = self.get_response(
            "get", self.get_url(self.path), headers=self.get_headers(),
            timeout=self.request_timeout,
            params={'q': keyword}
        )
        return response_data, completed