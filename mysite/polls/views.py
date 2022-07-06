from django.db.models import Q
from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import FormView
from .forms import CommentForm, UserForm
from django.contrib.auth import authenticate, login
from .models import Unisex, NewArrivals, CommentFormModel,weekly_best_slide_image,main_slide_image
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    main_slide = weekly_best_slide_image.objects.all()
    weekly_best_slide = main_slide_image.objects.all()
    photo = NewArrivals.objects.all()
    paginator = Paginator(photo, 12)
    page_numder = request.GET.get('page')
    page_obj = paginator.get_page(page_numder)
    return render(request, 'polls/index.html', {'page_obj':page_obj, 'main_slide':main_slide, 'weekly_best_slide':weekly_best_slide})

def UNISEX(request,):
    photo = Unisex.objects.all()
    paginator = Paginator(photo, 12)
    page_numder = request.GET.get('page')
    page_obj = paginator.get_page(page_numder)
    return render(request, 'polls/UNISEX.html',{'page_obj':page_obj})

def post_detail(request, post_id):
    post = Unisex.objects.get(pk=post_id)
    return render(request, 'polls/post_detail.html', {'post':post})

def comment(request):
    comment_list = CommentFormModel.objects.all()
    paginator = Paginator(comment_list, 12)
    page_numder = request.GET.get('page')
    page_obj = paginator.get_page(page_numder)
    form = CommentForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('comment')
    else:
        form = CommentForm()
    return render(request, 'polls/comment.html', {'form':form, 'page_obj':page_obj})

def comment_detail(request, comment_id):
    comment_detail = CommentFormModel.objects.get(pk=comment_id)
    return render(request, 'polls/comment_detail.html', {'comment_detail':comment_detail})


def search(request):
    blogs = Unisex.objects.all()
    query = request.GET.get('q')
    if query:
        blogs = Unisex.objects.filter(
            Q(name__icontains=query)).distinct()
    paginator = Paginator(blogs, 12)  # 6 posts per page
    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = { 'posts':posts }

    return render(request, "polls/search.html", context)

def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)  # 사용자 인증
            login(request, user)  # 로그인
            return redirect('index')
    else:
        form = UserForm()
    return render(request, 'polls/signup.html', {'form': form})
