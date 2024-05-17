from django.contrib import admin
from .models import User

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'year', 'degree_program', 'subscribed']
    list_per_page = 10
    search_fields = ["email",'first_name__istartswith', 'last_name__istartswith']
    list_select_related = ['degree_program']
    list_editable = ['subscribed']