from django.contrib import admin

from .models import Student, Meeting, SignIn

# Register your models here.
class SignInInline(admin.TabularInline):
    model = SignIn
    extra = 1

class StudentAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'first_name', 'subteam', 'meetings_attended','percent_attended']
    inlines = (SignInInline,)

class MeetingAdmin(admin.ModelAdmin):
    inlines = (SignInInline,)

admin.site.register(Student, StudentAdmin)
admin.site.register(Meeting, MeetingAdmin)
admin.site.register(SignIn)
