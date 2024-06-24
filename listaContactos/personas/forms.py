from django import forms
from .models import Persona

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = [
            'nombres',
            'apellidos',
            'edad',
            'donador',
            ]
    
    def clean_nombres(selt, *args, **kwargs):
        print('paso')
        name = selt.cleaned_data.get('nombres')
        if name.istitle():
            return name
        else:
            raise forms.ValidationError('La primera letra en mayúscula')
    
    def clean_apellidos(self):
        surname = self.cleaned_data.get('apellidos')
        if not surname.istitle():
            raise forms.ValidationError('La primera letra debe estar en mayúscula.')
        if not surname.isalpha():
            raise forms.ValidationError('Los apellidos no deben contener números ni caracteres especiales.')
        return surname
    
    def clean_edad(self):
        age = self.cleaned_data.get('edad')
        if age is not None:
            if age < 0:
                raise forms.ValidationError('La edad no puede ser un número negativo.')
            if age > 120:
                raise forms.ValidationError('La edad no puede ser mayor de 120 años.')
        return age

class RawPersonaForm(forms.Form):
    nombres = forms.CharField(
        widget = forms.Textarea(
            attrs={
                'placeholder': 'Sólo tu nombre, por favor',
                'id': 'nombreID',
                'class': 'special',
                'clos': '10',
                }
            )
        )
    apellidos = forms.CharField()
    edad = forms.IntegerField(initial = 20)
    donador = forms.BooleanField()