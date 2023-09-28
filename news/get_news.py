from .news_api import NewsAPI


class GetNews(NewsAPI):
    def __init__(self):
        super().__init__()
        self.path = "/"
        self.request_timeout = 30 # 30 sec timeout

    def execute(self, keyword):
        response_data, completed = self.get_response(
            "get", self.get_url(self.path), headers=self.get_headers(),
            timeout=self.request_timeout,
            params={'q': keyword}
        )
        return response_data, completed