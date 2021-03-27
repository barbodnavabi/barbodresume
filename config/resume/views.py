from django.shortcuts import render, redirect
from django.utils.translation import activate
from django.views.generic import ListView
from .models import Resume,Projects,Favorites,Experiances
# Create your views here.
def index(request):
    resume=Resume.objects.filter(active=True)
    favorites=Favorites.objects.all()
    best_experiances=Experiances.objects.all()[:4]
    experiances=Experiances.objects.all()
    Projects=Projects.objects.all()
    context={
        "resumes":resume,
        'experiances':experiances,
        'best_experiances':best_experiances,
        'favorites':favorites
        'projects':Projects
        
    }
    return render(request,'resume/index.html',context)



def change_lang(request):
	activate(request.GET.get('lang'))
	return redirect(request.GET.get('next'))    