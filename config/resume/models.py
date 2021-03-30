from django.db import models
from django.utils.translation import gettext as _

class Resume(models.Model):
    name=models.CharField(_("name"), max_length=200)
    phone=models.CharField(_("phone"), max_length=200)
    description=models.TextField(_("name"))
    email=models.CharField(_("name"), max_length=200)
    github=models.URLField(_("github"), max_length=200,blank=True,null=True)
    facebook=models.URLField(_("facebook"), max_length=200,blank=True,null=True)
    instagram=models.URLField(_("instagram"), max_length=200,blank=True,null=True)
    telegram=models.URLField(_("telegram"), max_length=200,blank=True,null=True)
    youtube=models.URLField(_("youtube"), max_length=200,blank=True,null=True)
    address=models.CharField(_("your address"), max_length=500)
    image=models.ImageField(_("your image or your logo"), upload_to='resume')
    resume=models.FileField(_("your resume"), upload_to='resume',)
    active=models.BooleanField(_("active/deactive"))

    

    class Meta:
        verbose_name = _("Resume")
        verbose_name_plural = _("Resumes")

    def __str__(self):
        return self.name


class Projects(models.Model):
    name=models.CharField(_("name"), max_length=200)
    image=models.ImageField(_("image"), upload_to='projects',blank=True,null=True)
    TypeOf=models.CharField(_("Type of project"), max_length=200)
    class Meta:
        verbose_name = _("Projects")
        verbose_name_plural = _("Projectss")

    def __str__(self):
        return self.name



class Favorites(models.Model):
    title=models.CharField(_("name of my hobby"), max_length=220)

    

    class Meta:
        verbose_name = _("Favorite")
        verbose_name_plural = _("Favorites")

    def __str__(self):
        return self.title

  

class Experiances(models.Model):
    skill=models.CharField(_("skill"), max_length=200)
    percent=models.IntegerField(_("percent of your skill"))
    

    class Meta:
        verbose_name = _("Experiances")
        verbose_name_plural = _("Experiancess")

    def __str__(self):
        return self.skill

class Contact(models.Model):
    name=models.CharField(_("what is your name?"), max_length=200)
    phone=models.CharField(_("what is your phone?"), max_length=200,blank=True,null=True)
    email=models.EmailField(_("what is your email?"), max_length=254,blank=True,null=True)
    subject=models.CharField(_("subject"), max_length=50)
    text=models.TextField(_("enter your text"))
    is_read=models.BooleanField(_("read/not read"), default=False)
    date=models.DateTimeField(_("when this massage send?"), auto_now_add=True)

    

    class Meta:
        verbose_name = _("Contact")
        verbose_name_plural = _("Contacts")

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("Contact_detail", kwargs={"pk": self.pk})
