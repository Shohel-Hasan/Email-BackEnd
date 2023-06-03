from django.shortcuts import render, HttpResponse
from .forms import SignUpForms, LoginForms
from django.contrib.auth import login, authenticate

# Create your views here.

def SignUp(request):
    forms = SignUpForms()
    if request.method == "POST":
        forms = SignUpForms(request.POST)
        if forms.is_valid():
            forms.save()
            return HttpResponse("User Created")
    context = {
        'forms': forms
    }
    return render(request, template_name='signup.html', context=context)

def UserLogin(request):
    forms = LoginForms()
    if request.method == "POST":
        uname = request.POST['username']
        pasw = request.POST['password']
        user = authenticate(request, username=uname, password=pasw)
        if user is not None:
            return HttpResponse('Login Success')
        else:
            return HttpResponse('wrong credentials')
    context = {
        'forms': forms
    }
    return render(request=request, template_name='signin.html', context=context)
