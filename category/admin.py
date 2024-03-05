from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import *
from author.models import *




class  AdminVideos(admin.ModelAdmin):
      list_display = ['id', 'name']

      list_filter = ['id', 'name']

admin.site.register(Category)
admin.site.register(Videos, AdminVideos)
admin.site.register(Lessons)






# #
# # class LessonInline(admin.TabularInline):
# #     model = Lessons
# #
# #
# # @admin.register(Category)
# # class CategoryAdmin(admin.ModelAdmin):
# #     inlines = (LessonInline,)
# #
# #
# # @admin.register(Videos)
# # class CostingAdmin(admin.ModelAdmin):
# #     inlines = (LessonInline,)
#
#
# class LessonInline(admin.StackedInline):
#     model = Lessons
#
#
# class AuthorAdmin(admin.ModelAdmin):
#     list_display = ('id','category')
#     inlines = [LessonInline]
