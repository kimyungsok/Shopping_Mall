from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.db.models import Q

class PostDetail(models.Model):
    post_name = models.CharField(max_length=30, null=True)
    main_photo = models.ImageField(upload_to='PostDetailPhoto/')
    content = models.TextField()

    def __str__(self):
        return self.post_name

class NewArrivals(models.Model):
    main_photo = models.ImageField(upload_to='NewArrivals/')
    name = models.CharField(max_length=30)
    price = models.IntegerField()

    def __str__(self):
        return self.name

class Unisex(models.Model):
    main_photo = models.ImageField(upload_to='upload/')
    name = models.CharField(max_length=30)
    price = models.IntegerField()
    content = models.TextField(null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/polls/detail/{self.pk}/'

class main_slide_image(models.Model):
    first_slide = models.ImageField(upload_to='first_slide/')
    second_slide = models.ImageField(upload_to='second_slide/')
    third_slide = models.ImageField(upload_to='third_slide/')

class weekly_best_slide_image(models.Model):
    first_slide = models.ImageField(upload_to='first_slide/')
    second_slide = models.ImageField(upload_to='second_slide/')
    third_slide = models.ImageField(upload_to='third_slide/')


class CommentFormModel(models.Model):
    comment_title = models.CharField(max_length=30, help_text='최대 30글자')
    comment = models.CharField(max_length=300, help_text='최대 300글자')
    recomment_title = models.CharField(max_length=30, blank=True, help_text='댓글 작성중입니다...')
    recomment_content = models.CharField(max_length=30, blank=True, help_text='댓글 작성중입니다...')

    def __str__(self):
        return self.comment_title

    def get_absolute_url(self):
        return f'/polls/{self.pk}/'

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Unisex, on_delete=models.CASCADE)
    active = models.BooleanField(default=False)
    # 수량은 -1 과 같은 수량이 없기 때문에 아래의 필드로 선언하여 최소값을 1 로 설정
    quantity = models.PositiveSmallIntegerField(null=True, default=1, validators=[MinValueValidator(1), MaxValueValidator(100)])
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = '장바구니'
        verbose_name_plural = f'{verbose_name} 목록'
        ordering = ['-pk']

    def sub_total(self):
        return self.product.price * self.quantity

    def __str__(self):
        return self.product.name





