from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import Http404
from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import FormView
from .forms import CommentForm, UserForm
from django.contrib.auth import authenticate, login
from .models import Unisex, NewArrivals, CommentFormModel,weekly_best_slide_image,main_slide_image, CartItem
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.exceptions import ObjectDoesNotExist

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


@login_required
def add_cart(request, product_pk):
    product = Unisex.objects.get(pk=product_pk)

    try:
        cart = CartItem.objects.get(product__id=product.pk, user__id=request.user.pk)
        if cart:
            if cart.product.name == product.name:
                cart.quantity += 1
                cart.save()
    except CartItem.DoesNotExist:
        user = User.objects.get(pk=request.user.pk)
        cart = CartItem(
            user=user,
            product=product,
            quantity=1,
        )
        cart.save()
    return redirect('my_cart')

@login_required
def my_cart(request):
    cart_item = CartItem.objects.filter(user__id=request.user.pk)
    total_price = 0
    for each_total in cart_item:
        total_price += each_total.product.price * each_total.quantity
    if cart_item is not None:
        return render(request, 'polls/cart_list.html', {'cart_item': cart_item, 'total_price': total_price})
    return redirect('my_cart')

def minus_cart_item(request, product_pk):
    cart_item = CartItem.objects.filter(product__id=product_pk)
    product = Unisex.objects.get(pk=product_pk)
    try:
        for item in cart_item:
            if item.product.name == product.name:
                if item.quantity > 1:
                    item.quantity -= 1
                    item.save()
                if item.quantity == 1:
                    item.delete()
                return redirect('my_cart')
            else:
                return redirect('my_cart')
    except CartItem.DoesNotExist:
        raise Http404