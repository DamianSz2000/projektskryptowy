from django import forms

class NickNameForm(forms.Form):
    nickname = forms.CharField(label='nickname', max_length=50)