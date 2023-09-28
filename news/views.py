from django.shortcuts import render
from .get_news import GetNews
from .serializers import ArticleSerializer
from .models import Article
from itertools import groupby
from datetime import datetime, timedelta
from .constants import HISTORY_DAYS
from django.contrib.auth.decorators import login_required


def home(request):
    """
      Home view
    """
    return render(request, "news/base.html")


@login_required
def news(request):
    """
        Method to handle user search request
        Renders html page based upon request method.
            Parameters:
                   request
            Returns:
                html page for news
    """

    if request.method == "POST":
        keyword = request.POST.get("search_query", "")
        get_news = GetNews()
        response, completed = get_news.execute(keyword=keyword)
        if completed:
            articles = response["articles"]
            articles = sorted(articles, key=lambda k: k["publishedAt"], reverse=True)
            data = {"user_id": request.user, "keyword": keyword}
            articles = [{**article, **data} for article in articles]
            articles = [{**article, **article["source"]} for article in articles]
            context = {"articles": articles}
            serialized_data = ArticleSerializer(articles, many=True).data
            serialized_data = [
                {**data_dict, **{"user_id": request.user}}
                for data_dict in serialized_data
            ]
            obj_list = [Article(**data_dict) for data_dict in serialized_data]
            Article.objects.bulk_create(obj_list)
            return render(request, "news/home.html", context=context)
    elif request.method == "GET":
        return render(request, "news/base.html")


def trends(request):
    """
        Method to get the trending articles
        Renders trends html page.
            Parameters:
                   request
            Returns:
                html page for trends
    """

    results = Article.objects.all().values()
    results = list(
        filter(
            lambda article: article["date_published"].date()
            >= (datetime.now() - timedelta(days=HISTORY_DAYS)).date(),
            results,
        )
    )
    key_func = lambda article: article["keyword"]
    grouped_results = {}
    for keyword, articles in groupby(results, key_func):
        grouped_results[keyword] = list(articles)[1:5]
    context = {"grouped_results": grouped_results}
    return render(request, "news/trends.html", context=context)

@login_required
def history(request):
    """
        Method to get the user history
        Renders trends html page.
            Parameters:
                   request
            Returns:
                html page for user history
    """

    results = Article.objects.filter(user_id=request.user).values()
    key_func = lambda article: article["keyword"]
    results = sorted(results, key=lambda k: k["date_published"])
    grouped_results = {}
    for keyword, articles in groupby(results, key_func):
        grouped_results[keyword] = list(articles)[1:5]
    context = {"grouped_results": grouped_results}
    return render(request, "news/history.html", context=context)
