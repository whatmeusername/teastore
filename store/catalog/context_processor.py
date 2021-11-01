from .models import TeaType, MainType

def type(request):
    Dict = {}
    List = []
    for main in MainType.objects.all():
        for Type in TeaType.objects.all():
            if str(Type.maintype) == str(main.Type):
                List.append(Type)
        Dict[main] = List
        List = []
    return {'type': Dict}