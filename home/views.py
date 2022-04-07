from django.shortcuts import render
from news.models import Post


def home_index(request):
    featured_post_list = Post.objects.order_by("-post_is_featured").all()[:2]
    context = {
        "featured_post_list": featured_post_list,
    }
    return render(request, "home/index.html", context=context)

    # project_list = Project.objects.order_by("-post_publication_date").all()
    # project_count = len(project_list)  # Количество проектов
    # paginator = Paginator(project_list, 10)  # max: 10
    # page = request.GET.get("page")
    # try:
    #     project_list = paginator.page(page)
    # except PageNotAnInteger:
    #     project_list = paginator.page(1)
    # except EmptyPage:
    #     project_list = paginator.page(paginator.num_pages)
    # context = {
    #     "project_list": project_list,
    #     "project_count": project_count,  # Количество проектов
    # }
