from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from news.models import Post


def news_index(request):
    post_list = Post.objects.order_by("-post_publication_date").all()
    paginator = Paginator(post_list, 10)
    page = request.GET.get("page")
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.page(paginator.num_pages)
    context = {
        "post_list": post_list,
    }
    return render(request, "news/index.html", context=context)