from django.db import models
from django.utils.translation import gettext as _

class Resume(models.Model):
    name=models.CharField(_("name"), max_length=200)
    phone=models.CharField(_("phone"), max_length=200)
    description=models.TextField(_("name"))
    email=models.CharField(_("name"), max_length=200)
    github=models.URLField(_("github"), max_length=200)

    

    class Meta:
        verbose_name = _("Resume")
        verbose_name_plural = _("Resumes")

    def __str__(self):
        return self.name


class Projects(models.Model):
    name=models.CharField(_("name"), max_length=200)
    image=models.ImageField(_("image"), upload_to='projects')
    TypeOf=models.CharField(_("Type of project"), max_length=200)
    class Meta:
        verbose_name = _("Projects")
        verbose_name_plural = _("Projectss")

    def __str__(self):
        return self.name



class Favorites(models.Model):
    name=models.CharField(_("name of my hobby"), max_length=220)

    

    class Meta:
        verbose_name = _("Favorite")
        verbose_name_plural = _("Favorites")

    def __str__(self):
        return self.name

  

class Experiances(models.Model):
    skill=models.CharField(_("skill"), max_length=200)
    percent=models.IntegerField(_("percent of your skill"))
    

    class Meta:
        verbose_name = _("Experiances")
        verbose_name_plural = _("Experiancess")

    def __str__(self):
        return self.name