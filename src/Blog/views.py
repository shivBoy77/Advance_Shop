from django.shortcuts import render
from .models import Blog
from .models import NewsLetterUser
from .forms import NewsLetterSignupForm
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count, Q


def index(request):
    return render(request, 'index.html', {})


def search(request):
    template = ""
    pss


def get_category_count():
    queryset = Blog \
        .objects \
        .values('categories__title') \
        .annotate(Count('categories__title'))
    return queryset


def blog(request):
    category_count = get_category_count()
    print(category_count)
    blog_list = Blog.objects.all()
    paginator = Paginator(blog_list, 1)
    page = request.GET.get('page')
    featured = Blog.objects.filter(featured=True)
    latest = Blog.objects.order_by('-timestamp')[0:3]
    form = NewsLetterSignupForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        if NewsLetterUser.objects.filter(email=instance.email).exists():
            messages.warning(request, "You have already Subscribed.",
                             "alert alert-warning alert-dismissible fade show")
        else:
            instance.save()
            messages.success(request, "subscription added successfully.",
                             "alert alert-success alert-dismissible fade show")

    context = {
        'object_list': featured,
        'latest': latest,
        'form': form,
        'blog_list': blog_list,
        'category_count': category_count
    }
    return render(request, 'blog.html', context)


def blog_details(request):
    return render(request, 'blog_details.html', {})


def newsletter_unsubscribe(request):
    form_u = NewsLetterSignupForm(request.POST or None)
    if form_u.is_valid():
        instance = form_u.save(commit=False)
        if NewsLetterUser.objects.filter(email=instance.email).exists():
            NewsLetterUser.objects.filter(email=instance.email).delete()
            messages.success(request, "subscription removed successfully",
                             "alert alert-success alert-dismissible fade show")
        else:
            messages.error(request, "Sorry, it seems like you never subscribed.",
                           "alert alert-danger alert-dismissible fade show")
    context = {
        'form_u': form_u,
    }
    template = "Un_news.html"
    return render(request, template, context)
