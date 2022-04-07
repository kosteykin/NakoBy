from django.shortcuts import render
from django.http import HttpResponse


def news_index(request):
    context = {}
    return render(request, "news/index.html", context=context)
# Create your views here.
