from django.shortcuts import render

# Create your views here.

news_articles = [
    {
        "id": 1,
        "title": "Tech giant is a piece of garbage",
        "description": (
            "This is the description part of article 1"
        ),
        "date": "2025-02-11"
    },
    {
        "id": 2,
        "title": "Global market is about to collapse",
        "description": (
            "Some stuff about global economy."
        ),
        "date": "2025-03-12"
    },
    {
        "id": 3,
        "title": "Wonderful news about something pointless",
        "description": (
            "Hello there, how are you donig today?"
        ),
        "date": "2025-05-10"
    }
]


def index(request):
    context = {"news_articles": news_articles}
    return render(request, "home/index.html", context)


def get_article(request, pk: int):
    article = next((a for a in news_articles if a["id"] == pk), None) # ?
    return render(request, "home/fragments/article.html", {'description': article['description']})