from django.contrib import admin
from .models import product, description, TeaType, TeaTypeFavor, MainType, Country, Manufacturer

#--------Categories---------
class MainTypeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'typeslug': ['Type']}
    list_display = ('Type', 'typeslug')

class TeaTypeAdmin(admin.ModelAdmin):
    list_display = ('Type', 'slug')
    prepopulated_fields = {'slug': ['Type']}

class TeaTypeFavorAdmin(admin.ModelAdmin):
    list_display = ('Type', 'slug')
    prepopulated_fields = {'slug': ['Type']}

class CountryAdmin(admin.ModelAdmin):
    list_display = ('country', 'slug')
    prepopulated_fields = {'slug': ['country']}


admin.site.register(TeaType, TeaTypeAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(MainType, MainTypeAdmin)
admin.site.register(TeaTypeFavor, TeaTypeFavorAdmin)
admin.site.register(Manufacturer)






#-------Product-------
class DescriptionTabular(admin.TabularInline):
    model = description
    fields = ('is_big', 'descriptionKey', 'descriptionValue', 'image')

class ProductAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Основное', {"fields": ('name', 'price', 'available')}),
        ('информация', {"fields": ('TeaType', 'TeaTypeFavor', 'country', 'manufacturer')}),
        ('Дополнительное', {"fields": ('ProductAvt', 'ProductMain', 'added', 'slug')}),
    )
    list_filter = ['country', 'TeaType', 'available',]
    list_display = ('name', 'price' ,'TeaType', 'country', 'available')

    inlines = [DescriptionTabular]
    prepopulated_fields = {'slug': ['name',]}

admin.site.register(product, ProductAdmin)
    

