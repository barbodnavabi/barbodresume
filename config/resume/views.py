from django.shortcuts import render, redirect
from django.utils.translation import activate
from django.views.generic import ListView
from .models import Resume,Projects,Favorites,Experiances
# Create your views here.
def index(request):
    resume=Resume.objects.filter(active=True)
    favorites=Favorites.objects.all()
    context={
        "resumes":resume,
    }
    return render(request,'resume/index.html',context)






class AboutListView(ListView):
    model = Favorites
    template_name = "resume/about.html"
    queryset=Favorites.objects.all()
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['resumes'] = Resume.objects.all()
        context['experiances'] = Experiances.objects.all()[:4]
        return context
    



class ExperianceListView(ListView):
    model = Experiances
    template_name = "resume/experiance.html"

def change_lang(request):
	activate(request.GET.get('lang'))
	return redirect(request.GET.get('next'))    