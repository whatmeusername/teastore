from django.db import models
import datetime


#-------Categories----------------
class Country(models.Model):
    country = models.CharField(max_length = 300, verbose_name = 'страна производитель', unique = True)
    slug = models.CharField(max_length = 400 , verbose_name = 'url')

    class Meta:
        verbose_name = 'категория (Страна)'
        verbose_name_plural = 'Категории (Страна)'

    def __str__(self):
        return self.country

    def get_short_name(self):
        return self.country

    def save(self, *args, **kwargs):
        self.country = self.country.lower()
        return super(Country, self).save(*args, **kwargs)


class Manufacturer(models.Model):
    manufacturer = models.CharField(max_length= 400, verbose_name = 'произовдитель', unique = True)
    
    class Meta:
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'

    def __str__(self):
        return self.manufacturer
    
    def get_short_name(self):
        return self.manufacturer

    def save(self, *args, **kwargs):
        self.manufacturer= self.manufacturer.lower()
        return super(Manufacturer, self).save(*args, **kwargs)




class MainType(models.Model):
    Type = models.CharField(max_length = 200, unique = True)
    typeslug = models.CharField(max_length = 200, verbose_name = 'url', null=True)

    class Meta:
        verbose_name = 'Главный вид'
        verbose_name_plural = 'Главный вид'

    def __str__(self):
        return self.Type

    def get_short_name(self):
        return self.Type

    def save(self, *args, **kwargs):
        self.Type = self.Type.lower()
        return super(MainType, self).save(*args, **kwargs)






class TeaType(models.Model):
    Type = models.CharField(max_length = 200, verbose_name = 'тип/вид чая', unique = True)
    slug = models.CharField(max_length = 400 , verbose_name = 'url')
    image = models.ImageField(upload_to = 'media/TeaType', default = 'media/NoImageAvailable.png', null = True)
    maintype = models.ForeignKey(MainType, blank = True, on_delete = models.CASCADE, null = True)

    class Meta:
        verbose_name = 'категория (Тип чая)'
        verbose_name_plural = 'Категории (Тип чая)'

    def __str__(self):
        return self.Type

    def get_short_name(self):
        return self.Type

    def save(self, *args, **kwargs):
        self.Type = self.Type.lower()
        return super(TeaType, self).save(*args, **kwargs)



class TeaTypeFavor(models.Model):
    Type = models.CharField(max_length = 200, verbose_name = 'аромат чая', unique = True)
    slug = models.CharField(max_length = 400 , verbose_name = 'url')

    class Meta:
        verbose_name = 'категория (аромат чая)'
        verbose_name_plural = 'Категории (аромат чая)'

    def __str__(self):
        return self.Type

    def get_short_name(self):
        return self.Type

    def save(self, *args, **kwargs):
        self.Type = self.Type.lower()
        return super(TeaTypeFavor, self).save(*args, **kwargs)



#------PRODUCT---------------
class product(models.Model):
    name = models.CharField(max_length=200, verbose_name='название', unique=True)
    slug = models.SlugField(max_length=200, verbose_name='url', unique=True)
    ProductAvt = models.ImageField(upload_to = 'media/productsAvt/', default = 'media/NoImageAvailable.png', blank=True)
    ProductMain = models.ImageField(upload_to = 'media/products/', default = 'media/NoImageAvailable.png', blank=True)
    price = models.IntegerField(verbose_name='цена')
    added = models.DateTimeField(default = datetime.datetime.now)
    available = models.BooleanField(default = True)

    country = models.ForeignKey(Country, verbose_name='страна производитель', on_delete = models.CASCADE, related_name = 'city')
    TeaType = models.ForeignKey(TeaType, verbose_name='тип/вид чая', on_delete=models.CASCADE, null = True, related_name = 'tea_type')
    TeaTypeFavor = models.ForeignKey(TeaTypeFavor, verbose_name='аромат чая', on_delete = models.CASCADE, null = True, related_name = 'type_favor')
    manufacturer = models.ForeignKey(Manufacturer, verbose_name='производитель', on_delete = models.CASCADE, null = True, default = 'собственное')

    class Meta:
        ordering = ['-added',]
        verbose_name = 'товар'
        verbose_name_plural = 'Товары'


    def __str__(self):
        return self.name

    def get_short_name(self):
        return self.name





#------PRODUCT DESCRIPTION------
class description(models.Model):
    product = models.ForeignKey(product, related_name = 'item', on_delete=models.CASCADE)
    descriptionKey = models.CharField(max_length = 100, verbose_name = 'характеристика')
    descriptionValue = models.TextField(max_length = 400, verbose_name = 'описание')
    image = models.ImageField(upload_to = 'media/productDescription/', blank = True)
    is_big = models.BooleanField(default = False, verbose_name = 'описание?')

    def __str__(self):
        return self.product.name

    def get_short_name(self):
        return self.product.name