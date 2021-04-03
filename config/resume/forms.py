from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].label = None
        self.fields['phone'].label = None
        self.fields['email'].label = None
        self.fields['subject'].label = None
        self.fields['text'].label = None


    class Meta:
        model = Contact
        fields=["name","phone","email","subject","text",]
