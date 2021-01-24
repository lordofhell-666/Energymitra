from django import forms

SPECTRUM = (
    ('', 'Choose...'),
    ('HLS', 'Home Lighting System'),
    ('OFGS', 'Off Grid System'),
    ('ONS', 'On Grid System'),
)

class Contactform(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    category = forms.ChoiceField(choices=SPECTRUM)
    message = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Write your message'})
        )
