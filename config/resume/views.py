from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.translation import activate
from django.views.generic import CreateView
from .models import Resume,Projects,Favorites,Experiances,Contact
# Create your views here.
def index(request):
    resume=Resume.objects.filter(active=True)
    favorites=Favorites.objects.all()
    best_experiances=Experiances.objects.all()[:4]
    experiances=Experiances.objects.all()
    projects=Projects.objects.all()
    context={
        "resumes":resume,
        'experiances':experiances,
        'best_experiances':best_experiances,
        'favorites':favorites,
        'projects':projects
        
    }
    return render(request,'resume/index.html',context)



def change_lang(request):
	activate(request.GET.get('lang'))
	return redirect(request.GET.get('next'))    



class ContactCreateView(CreateView):
    model = Contact
    template_name = "resume/contact.html"
    fields=["name","phone","email","subject","text",]
    success_url = reverse_lazy('index')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['resumes'] = Resume.objects.filter(active=True)
        return context
