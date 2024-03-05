from django.contrib import admin
from .models import *



class AdminAuthor(admin.ModelAdmin):
      list_display = ['id', 'full_name', 'bio','job']

      list_filter = ['full_name']


admin.site.register(Author, AdminAuthor)
