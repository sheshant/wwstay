import os

from django.contrib import admin

# Register your models here.
from django.utils.html import format_html
from expenses.models import Expense


class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'user', 'price', 'image_tag',)

    def image_tag(self, obj):
        return format_html(obj.get_image_path_with_html())

    image_tag.short_description = 'Image'
    image_tag.allow_tags = True


admin.site.register(Expense, ExpenseAdmin)

