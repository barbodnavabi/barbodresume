from django.shortcuts import render, redirect
from django.utils.translation import activate

# Create your views here.
def index(request):
    context={
        
    }
    return render(request,'resume/index.html',context)



def change_lang(request):
	activate(request.GET.get('lang'))
	return redirect(request.GET.get('next'))    