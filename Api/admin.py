from django.contrib import admin
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin


UserAdmin.list_display = ['username','email', 'is_active', 'last_login']

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register([Teacher,Student,Courses,Quiz,Result,Assignment,Classes,Notifications,Contact])
# Register your models here.
admin.site.site_header  =  "E_School admin"  
admin.site.site_title  =  "E_School admin site"
admin.site.index_title  =  "E_School Admin"

