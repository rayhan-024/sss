from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post,Comment,Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}



# Register your models here.
class PostAdmin(SummernoteModelAdmin):

    list_display = [
        'title',
        'short_desc',
        'thumbnail',

    ]
    # summernote_fields = ('description',)
    summernote_fields = ('description',)

admin.site.register(Post, PostAdmin)

class CommentAdmin(admin.ModelAdmin):

    list_display = [
        'name',
        'body',

    ]

admin.site.register(Comment, CommentAdmin)
