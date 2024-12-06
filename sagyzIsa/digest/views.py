from django.shortcuts import render
from .newsintegration import external_api_view, available
from .amongus import getTheNews, getTheEgovUser
import json
import random

def call_egovus(request):
    return getTheEgovUser(request.GET.get('idn'))

def home_view(request):
    if request.method == "POST" and 'recommend' in request.POST:
        selected_tags = random.sample(available, 5)
        news_response = getTheNews()
        news_data = json.loads(news_response.content)
        articles = []
        for tag in selected_tags:
            if tag in news_data:
                for article in news_data[tag]:
                    articles.append({
                        'title': article.get('title'),
                        'date': article.get('date'),
                        'scope': article.get('scope'),
                        'link': article.get('link')
                    })
        context = {'articles': articles, 'show_all': True}
    else:
        news_response = getTheNews()
        news_data = json.loads(news_response.content)
        articles = []
        for tag in available:
            if tag in news_data:
                for article in news_data[tag]:
                    articles.append({
                        'title': article.get('title'),
                        'date': article.get('date'),
                        'scope': article.get('scope'),
                        'link': article.get('link')
                    })
        context = {'articles': articles, 'show_all': False}
    return render(request, 'digest/home.html', context)

def call_newsogus(request):
    return getTheNews()

def get_digest(request):
    return external_api_view(request.GET.get('search', 'it'))