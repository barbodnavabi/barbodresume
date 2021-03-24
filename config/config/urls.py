from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns
from django.urls import include, path
from resume.views import change_lang
from django.conf.urls import url


urlpatterns = [
    path('change_lang', change_lang, name='change_lang'),
]

urlpatterns += i18n_patterns(

    path('admin/', admin.site.urls),
    path('', include('resume.urls')),
)