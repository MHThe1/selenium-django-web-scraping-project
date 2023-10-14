from django import forms
from .models import Board, Stat

class Boardform(forms.ModelForm):
    class Meta:
        model = Board
        fields = ['name', 'email', 'password', 'last_link']

class Statform(forms.ModelForm):
    class Meta:
        model = Stat
        fields = '__all__'

class Updateform(forms.Form):
    parent_id = forms.IntegerField()
    link = forms.CharField()
    passw = forms.CharField()