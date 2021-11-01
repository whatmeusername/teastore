from django.contrib import admin
from .models import User
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'FirstName', 'LastName', 'PhoneNumber', 'Address')
    fieldsets = (('Основная информация', {'fields' : ('email', 'password')}),
                ('Личная информация', {'fields': ('FirstName', 'LastName', 'PhoneNumber', 'Address')})
                )


admin.site.register(User, UserAdmin)
