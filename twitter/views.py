from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Twit
from django.contrib.auth.decorators import login_required
from .import forms


# Create your views here.
@login_required(login_url="/accounts/login")
def twitts_index(request):
    form = forms.CreateTwit()

    twits = Twit.objects.all().order_by('-creation_date')[:3]
    
    context = {
        'twits': twits,
        'form': form
    }
    
    return render(request,'twitter/twitts_index.html',context)

@login_required(login_url="/accounts/login")
def twit_create(request):
    if request.method == 'POST':
        form = forms.CreateTwit(data=request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('twits:twitts_index')


    else:
        form = forms.CreateTwit()

    return render(request,'twitter/twit_create.html',{'form':form})   
