from django.shortcuts import render
from django.views.generic import View, TemplateView,ListView, DetailView
from firstaid_app.forms import UserForm, LibraryForm, DiseaseForm 
from firstaid_app.models import User, Library, Disease
from . import models

from django.contrib.auth import login, authenticate, logout

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse




def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request,user)
                return render(request,'firstaid_app/index.html')

            else:
                return HttpResponse('Account not active')
        else:
            print('Someone tried to login and failed!')
            print('username: {} and password: {}'.format(username,password))
            return render(request,'firstaid_app/index.html')

    else:
        return render(request,'firstaid_app/login.html',{})

@login_required
def user_logout(request):
    logout(request)
    return render(request,'firstaid_app/index.html')
    

class Index(TemplateView):

    context_object_name = 'disease_list'
    template_name = 'firstaid_app/index.html'

    def get(self, request):
        
        args = {}

        return render(request, self.template_name, args)
        
    
    def post(self, request):
        var = request.POST.get('srchbtn')
        
        dis = Disease.objects.filter(symptoms__icontains=var)
        
        if dis != None:
            args = {'dis':dis}
            return render(request, 'firstaid_app/library_list.html',args)
        else:
            return render(request, self.template_name)


class LibraryListView(ListView):
    context_object_name = 'diseases'
    model = models.Library
    template_name = 'firstaid_app/library_list.html'

class DiseaseDetailView(DetailView):
    context_object_name = 'disease_detail'
    model = models.Disease 
    template_name = 'firstaid_app/disease_detail.html'


def register(request):

    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)

        if user_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            registered = True
        else:
            print(user_form.errors)

    else:
        user_form = UserForm()

    return render(request,'firstaid_app/register.html',
                            {'user_form':user_form,
                              'registered':registered})


