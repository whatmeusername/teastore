
#----DJANGO METHODS-----
from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from django.urls import reverse
from django.db.utils import IntegrityError
from django.contrib.auth import authenticate, login, logout
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.conf import settings
from django.http import Http404

#------APP MODELS AND METHODS-----
from .models import User as user_object
from .Token import TokenCreator
from .forms import LoginForm, RegisterForm
from .RegisterValidator import Validator
from .EmailDelay import Delay
#-----OTHER-------
from datetime import timedelta



#---------------USER LOGIN-----------------------------
def UserLogin(request):
    if not request.user.is_authenticated:
        data = {
            'form': LoginForm()
        }
        
        return render(request, 'main/login.html', data)
    else:
        return redirect(reverse('home:home'))

def UserLoginAuth(request):
    if request.method == 'POST' and request.is_ajax() and not request.user.is_authenticated:
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(email = email, password = password)
            if user is not None:
                login(request, user)
                return JsonResponse({'status': 1})
            else:
                return JsonResponse({'message': 'Ошибка в логине или пароле, проверьте правильность данных'})
        
    
    return HttpResponse('')

#-----USER LOGOUT------
def UserLogout(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('home:home')
    else:
        return redirect('home:home')


#--------------REGISTER--------------------
def UserRegister(request):
    if not request.user.is_authenticated:

        data = {
            'form': RegisterForm()
        }

        return render(request, 'main/register.html', data)
    else:
        return redirect(reverse('home:home'))


def UserRegisterAuth(request):
    if request.method == 'POST' and request.is_ajax():
        form = RegisterForm(request.POST)
        if form.is_valid():
            #------GETTING VARIABLES-------
            email = form.cleaned_data['email']
            FirstName = form.cleaned_data['FirstName']
            LastName = form.cleaned_data['LastName']
            password = form.cleaned_data['password']
            password_repeat = form.cleaned_data['password_repeat']
            #------VALIDATING VARIABLES-----
            validator = Validator()
            validator.validate_email(email)
            validator.validate_password(password)
            validator.validate_name(FirstName, LastName)
            validator.validate_similarity(password = password, password_repeat = password_repeat)
            #----------RESULT------
            result = validator.get_result()
            #----CHECKING IF ALL DATA PASS VALIDATIONS-----
            for value in result.values():
                if value != True:
                    return JsonResponse(result)
            else:
                #-----CHECKING IF USER WITH SAME EMAIL NOT EXISTS-----
                if user_object.objects.filter(email = email).exists():
                    result['email'] = 'Пользователь с такой почтой уже существует'
                    return JsonResponse(result)
                else:
                    #------TOKEN CREATING AND INIT DELAY----
                    delay = Delay(request)
                    token_creator = TokenCreator()
                    if delay.TimeDiff():
                        token = token_creator.CreateActivationLink(
                            email=email, 
                            password=password, 
                            FirstName=FirstName, 
                            LastName=LastName
                            )
                        #-----CREATING URL FOR MAIL-------
                        ActivationUrl = ((request.build_absolute_uri('/user/register/')) + token + '/activate/')
                        #-----SENDING EMAIL-----
                        try:
                            send_mail(
                                'Activation Link',
                                f'Activation link {ActivationUrl}',
                                settings.EMAIL_HOST_USER,
                                ['maksim.moiseev07@mail.ru']
                                )
                            delay.SetDelay()
                                
                            #------CREATING LINK FOR RESENDING PAGE-------
                            link = token_creator.CreateForReSendPage(email = email, password = password, FirstName = FirstName, LastName = LastName)
                            #------RETURNING TEMPLATE-----
                            link = str(redirect('user:RegisterSend', link = link).url)
                            return JsonResponse({'link': link})
                        except:
                            return JsonResponse({'email': 'во время отправки ссылки проищошла ошибка, проверьте правильность данных.'})


        
    return HttpResponse('')


    
def UserRegisterValidator(request):

    EmptyValues = [None, '']
    
    if request.method == 'POST' and request.is_ajax():
        #------GETTING VARIABLES-------
        email = request.POST.get('email')
        FirstName = request.POST.get('FirstName')
        LastName = request.POST.get('LastName')
        password = request.POST.get('password')
        password_repeat = request.POST.get('password_repeat')
        #------VALIDATING VARIABLES-----

        validator = Validator()

        if email not in EmptyValues:
            validator.validate_email(email)

        if password not in EmptyValues:
            validator.validate_password(password)

        if (password not in EmptyValues and 
            password_repeat not in EmptyValues):
            validator.validate_similarity(password = password, password_repeat = password_repeat)

        validator.validate_name(FirstName, LastName)
        #-----RESULT SENDING------
        result = validator.get_result()
        return JsonResponse(result)

    return HttpResponse('')



def UserRegisterActivate(request, token):
    if not request.user.is_authenticated:
        #-----UNSIGNING USER DATA------
        token_creator = TokenCreator()
        data = token_creator.UnsignToken(token)
        #-------CREATING USER IF DATA IS VALID--------
        if data:
            try:
                user = user_object.objects.create(
                    email=data['main']['email'], 
                    password=data['main']['password'], 
                    FirstName=data['Name']['FirstName'], 
                    LastName=data['Name']['LastName']
                    )
                #----LOGIN CREATED USER-----
                login(request, user)
                #-----RETURNING TEMPLATE WITH WELCOME MESSAGE----
                return render(request, 'main/Activate.html')
            #---EXPECTING ERRORS-------
            except IntegrityError and KeyError:
                raise Http404
        else:
            return redirect(reverse('home:home'))
    else:
        return redirect(reverse('home:home'))

    
def UserRegisterSend(request, link):
    if not request.user.is_authenticated:
        #------UNSIGNING USER DATA AND INIT DELAY-----
        token_creator = TokenCreator()
        delay = Delay(request)
        UserInfo= token_creator.UnsignToken(link)
        #------------AJAX REQUEST--------

        if request.method == 'POST' and request.is_ajax():
            #-----CHECKING  IF DELAY IS ENDED AND CREATING TOKEN FOR SENDING---
            if delay.TimeDiff():
                try:
                    token = token_creator.CreateActivationLink(
                            email=UserInfo['EmailSend'], 
                            password=UserInfo['PasswordSend'], 
                            FirstName = UserInfo['FirstNameSend'], 
                            LastName = UserInfo['LastNameSend']
                            )
                    #-----CREATING URL------
                    ActivationUrl = ((request.build_absolute_uri('/user/register/')) + token + '/activate/')
                    #------SENDING MAIL--------
                    try:
                        send_mail(
                            'Activation Link',
                            f'Activation link {ActivationUrl}',
                            settings.EMAIL_HOST_USER,
                            ['maksim.moiseev07@mail.ru']
                            )
                        #-----RESET DELAY-----
                        delay.SetDelay()
                        #----EXPECTING ERRORS----
                        return JsonResponse({'message': 'Ссылка успешно отправлена', 'timer': delay.GetTimeDiff()})
                    except:
                        return JsonResponse({'message': 'произошла ошибка во время отправки ссылки'})
                except:
                    raise Http404

        #---------AFTER AJAX BLOCK------

        #--CHECKING IF USER DATA STILL VALID-----
        if UserInfo == False:
            raise Http404
        else:
            data = {'time': delay.GetTimeDiff()}
            return render(request, 'main/EmailSended.html', data)
    else:
        raise Http404

