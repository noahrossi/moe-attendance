from django.contrib import admin

from .models import Student, Meeting, SignIn

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'first_name', 'subteam']

admin.site.register(Student, StudentAdmin)
admin.site.register(Meeting)
admin.site.register(SignIn)
