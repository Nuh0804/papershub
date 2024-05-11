from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', "name",)


@admin.register(PastPaper)
class PastPaperAdmin(admin.ModelAdmin):
    list_display = ("id", "course", "title", "file", "solution", "is_free")
    list_select_related = ["course"]
    list_per_page = 10
    search_fields = ["title"]


@admin.register(DegreeProgram)
class DegreeProgramAdmin(admin.ModelAdmin):
    list_display = ["id", "degree_name"]