from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=255, label='Your Name')
    email = forms.EmailField(max_length=255, label='Your Email')
    subject = forms.CharField(max_length=255, label='Subject')
    message = forms.CharField(widget=forms.Textarea, label='Message')
