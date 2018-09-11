from django.contrib import admin
from django.db import models

from .models import Student, Meeting, SignIn

# Register your models here.
class SignInInline(admin.TabularInline):
    model = SignIn
    extra = 1

class StudentAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'first_name', 'subteam', 'meetings_attended','percent_attended']
    search_fields = ['first_name', 'last_name']
    inlines = (SignInInline,)

    def get_queryset(self, request):
        qs = super(StudentAdmin, self).get_queryset(request)
        qs = qs.annotate(models.Count('signin'))
        qs = qs.annotate(models.Count('signin'))
        return qs

    def meetings_attended(self, obj):
        return obj.signin__count

    def percent_attended(self, obj):
        return obj.percent_attended()

    meetings_attended.admin_order_field = 'signin__count'
    percent_attended.admin_order_field = 'signin__count'

class MeetingAdmin(admin.ModelAdmin):
    inlines = (SignInInline,)

admin.site.register(Student, StudentAdmin)
admin.site.register(Meeting, MeetingAdmin)
admin.site.register(SignIn)
admin.site.site_header = 'AdMOEnistration'
