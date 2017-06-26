from django import forms
from .models import data

class dataform(forms.Form):
    file = forms.FileField()
    training = forms.IntegerField()
    testing = forms.IntegerField()
    describe = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)

class adddata(forms.ModelForm):
    class Meta:
        model = data
        fields = '__all__'
