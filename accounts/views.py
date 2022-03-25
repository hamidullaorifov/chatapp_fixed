from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate





# Create your views here.



def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if form.is_valid():
            if password1==password2:
                form.save()
                return redirect('accounts:login')
            # else:
            #     raise ValidationError('Password doesn\'t match')
    return render(request,'accounts/register.html',{'form':form})


def loginview(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('chat:index')
    return render(request,'accounts/login.html')
