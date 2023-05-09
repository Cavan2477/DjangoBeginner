from django.contrib import admin
from .models import Member


# Register your models here.
# Membership details are displayed on admin management page
# Modified by CodeCaptain 2023-5-9
class MemberAdmin(admin.ModelAdmin):
    list_display = ("firstname", "lastname", "joined_date",)


admin.site.register(Member, MemberAdmin)
