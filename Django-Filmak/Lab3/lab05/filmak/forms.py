from django import forms

class LoginForm(forms.Form):
	username=forms.CharField(label='Erabiltzaile izena:')
	password=forms.CharField(label='Erabiltzaile pasahitza:')