from itertools import count
import stat
from django.contrib import admin
from .models import User

# Register your models here.



class UserAdmin(admin.ModelAdmin):

    # def count_followers(self, obj):
    #     return obj.followers.count()

    # def count_followings(self, obj):
    #     return obj.followings.count()
    
    list_display = ['username', 'email']
    # count_followers.short_description = 'Count followers'
    # count_followers.admin_order_field = 'user.count_followers'

admin.site.register(User, UserAdmin)