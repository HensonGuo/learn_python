from django.contrib import admin
from .models import Article, Person, Test1

class ArticleAdmin(admin.ModelAdmin):
    #需要显示一些其它的fields
    list_display = ('title', 'pub_date','update_time',)

class PersonAdmin(admin.ModelAdmin):
    list_display = ('full_name',)

admin.site.register(Article, ArticleAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Test1)