from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Unisex, NewArrivals,CommentFormModel, weekly_best_slide_image, main_slide_image

admin.site.register(NewArrivals)
admin.site.register(CommentFormModel)
admin.site.register(weekly_best_slide_image)
admin.site.register(main_slide_image)

class PostDetailAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)

admin.site.register(Unisex, PostDetailAdmin)

