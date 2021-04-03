from django.db import models
from django.utils.translation import gettext as _
from translated_fields import TranslatedField




class FirstPageSkills(models.Model):
    title=models.CharField(_("title"), max_length=50)
    skill=models.ForeignKey("Experiances", verbose_name=_("my skill"),on_delete=models.CASCADE)

    

    class Meta:
        verbose_name = _("FirstPageSkill")
        verbose_name_plural = _("FirstPageSkills")

    def __str__(self):
        return self.title


        category_to_str.short_description = "مهارت"
    
class Resume(models.Model):
    name=TranslatedField(models.CharField(_(" your name"), max_length=200))
    phone=models.CharField(_("phone"), max_length=200)
    description=TranslatedField(models.TextField(_("name")))
    email=models.CharField(_("name"), max_length=200)
    github=models.URLField(_("github"), max_length=200,blank=True,null=True)
    facebook=models.URLField(_("facebook"), max_length=200,blank=True,null=True)
    instagram=models.URLField(_("instagram"), max_length=200,blank=True,null=True)
    telegram=models.URLField(_("telegram"), max_length=200,blank=True,null=True)
    youtube=models.URLField(_("youtube"), max_length=200,blank=True,null=True)
    address=TranslatedField(models.CharField(_("your address"), max_length=500))
    image=models.ImageField(_("your image or your logo"), upload_to='resume')
    resume=models.FileField(_("your resume"), upload_to='resume',)
    active=models.BooleanField(_("active/deactive"))

    

    class Meta:
        verbose_name = _("Resume")
        verbose_name_plural = _("Resumes")

    def __str__(self):
        return self.name


class Projects(models.Model):
    name=TranslatedField(models.CharField(_("name"), max_length=200))
    image=models.ImageField(_("image"), upload_to='projects',blank=True,null=True)
    TypeOf=TranslatedField(models.CharField(_("Type of project"), max_length=200))
    class Meta:
        verbose_name = _("Projects")
        verbose_name_plural = _("Projects")

    def __str__(self):
        return self.name



class Favorites(models.Model):
    title=models.CharField(_("name of my hobby"), max_length=220)

    

    class Meta:
        verbose_name = _("Favorite")
        verbose_name_plural = _("Favorites")

    def __str__(self):
        return self.title

  
class ExperianceManager(models.Manager):
  def active(self):
    return self.filter(active=True)

class Experiances(models.Model):
    skill=TranslatedField(models.CharField(_("skill"), max_length=200))
    percent=models.IntegerField(_("percent of your skill"))
    active=models.BooleanField(_("active/deactive"))
    

    class Meta:
        verbose_name = _("Experiances")
        verbose_name_plural = _("Experiancess")

    def __str__(self):
        return self.skill

class Contact(models.Model):
    name=models.CharField(_("نام شما چیست"), max_length=200)
    phone=models.CharField(_("شماره شما چیست؟"), max_length=200,blank=True,null=True)
    email=models.EmailField(_("ایمیل شما چیست؟"), max_length=254,blank=True,null=True)
    subject=models.CharField(_("عنوان"), max_length=50)
    text=models.TextField(_("توضیحات خود را وارد نمایید"))
    is_read=models.BooleanField(_("خوانده شده/خوانده نشده"), default=False)
    date=models.DateTimeField(_("زمان ارسال این درخواست"), auto_now_add=True)

    

    class Meta:
        verbose_name = _("Contact")
        verbose_name_plural = _("Contacts")

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("Contact_detail", kwargs={"pk": self.pk})


