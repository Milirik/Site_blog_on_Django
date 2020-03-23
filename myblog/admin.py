from django.contrib import admin
from .models import *
from django_summernote.admin import SummernoteModelAdmin

class NewAdmin(SummernoteModelAdmin):
	summernote_fields = ['body']

# Register your models here.
admin.site.register(Post, NewAdmin)
admin.site.register(Article, NewAdmin)
admin.site.register(Feedback)
admin.site.register(Project, NewAdmin)
