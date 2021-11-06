
from django.shortcuts import render, get_object_or_404, HttpResponse

from .models import Manufacturer, TeaType, MainType, product
from django.db.models import Max, Min
from django.db.models import Q

from .forms import PriceForm

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


from django.http import JsonResponse
from django.template.loader import render_to_string



def ViewCatalog(request, typeslug, slug):
    #--------------GETTING PRODUCTS BY URL PARAMETERS------
    maintype = MainType.objects.get(typeslug = typeslug)
    teatype = TeaType.objects.get(slug=slug, maintype = maintype)
    products = product.objects.filter(TeaType=teatype)

    #-------------INIT FORM FOR PRICE FIELDS AND SET INTIAL DATA WITH MAX AND MIN PRICE OF AVAILABLE PRODUCTS------
    initial_data = {
        'price_from': (product.objects.filter(TeaType=teatype).aggregate(Min('price'))['price__min']),
        'price_to': (product.objects.filter(TeaType=teatype).aggregate(Max('price'))['price__max'])
    }

    priceform = PriceForm(request.GET or None, initial = initial_data)


    #-------GET ALL UNIQUE COUNTRY AND FAVORS VALUES USED IN MODEL OBJECTS
    CategoriesFavor = []
    CategoriesCountry = []
    CategoriesManufacturer = []
    for categories in products:

        if str(categories.TeaTypeFavor) in CategoriesFavor and str(categories.TeaTypeFavor) != None:
            pass
        else:
            CategoriesFavor.append(str(categories.TeaTypeFavor))

        if str(categories.country) in CategoriesCountry and str(categories.country) != None: 
            pass
        else:
            CategoriesCountry.append(str(categories.country))

        if str(categories.manufacturer) in CategoriesManufacturer and str(categories.manufacturer) != None:
            pass
        else:
            CategoriesManufacturer.append(str(categories.manufacturer))


    
    #---------PAGINATE PRODUCTS FOR 9 ITEMS PER PAGE-----


    page = request.GET.get('page', 1)
    paginator = Paginator(products, 9)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)



    #----------DATA THAT WILL BE SENDED TO TEMPLATE-------
    data = {
        'URLPARAMATERS' : {'type1': typeslug, 'type2' : slug},
        'products': products,
        'price_form': priceform,
        'CategoriesCountry': CategoriesCountry,
        'CategoriesFavor':  CategoriesFavor,
        'CategoriesMan': CategoriesManufacturer,
    }
    #------RENDER----------
    return render(request, 'main/Catalog.html', data)





#----------AJAX FILTER-------------
def FilterCatalog(request):

    if request.method == 'GET' and request.is_ajax():

        maintype = MainType.objects.get(typeslug = request.GET.get('url-par1'))
        teatype = TeaType.objects.get(slug= request.GET.get('url-par2'), maintype = maintype)
        products = product.objects.filter(TeaType=teatype)

        favors = request.GET.getlist('favor[]')
        countries = request.GET.getlist('country[]')
        manufacturers = request.GET.getlist('manufacturer[]')
        price_from = request.GET.get('form-price_from')
        price_to = request.GET.get('form-price_to')

        if price_from == '' or None:
            price_from = 0
        
        if price_to == '' or None:
            price_to = 0

        products = products.filter(
            Q(price__gte = price_from) &
            Q(price__lte = price_to)
        )

        if len(favors) > 0:
            products = products.filter(TeaTypeFavor__Type__in = favors)
        if len(countries) > 0:
            products = products.filter(country__country__in = countries)
        if len(manufacturers) > 0:
            products = products.filter(manufacturer__manufacturer__in = manufacturers)

        render = render_to_string('renders_for_ajax/Product_AJAX.html', {'products': products})

        return JsonResponse({'render': render})
        
    return HttpResponse('')
