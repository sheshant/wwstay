from django.contrib import admin

from accounts.models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'birth_date', )


admin.site.register(Profile, ProfileAdmin)
