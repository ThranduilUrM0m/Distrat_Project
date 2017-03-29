from django import forms

class AvisForm(forms.Form):
    f_name = forms.CharField(max_length=25)
    l_name = forms.CharField(max_length=25)
    avis_text = forms.CharField(max_length=500)
    dt_created = forms.DateTimeField()

class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)