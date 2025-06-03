from django import forms
from .models import Logger


#Primer formulario definido
class miFormulario(forms.Form):
    nombre = forms.CharField()
    edad = forms.IntegerField()



class LogForm(forms.ModelForm):
	class Meta:
		model = Logger
		fields = "__all__"
		widgets = {
			'hora_llegada': forms.TimeInput(attrs={'type':'time'}),
        }