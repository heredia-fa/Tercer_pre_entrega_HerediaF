from django import forms
from .models import  User
from django.core.exceptions import ValidationError

class User_form(forms.Form):

    name = forms.CharField(max_length=30, label='Nombre')
    lastname = forms.CharField(max_length=30, label='Apellido')
    email = forms.EmailField(label='Correo electrónico')
    age = forms.IntegerField(label='Edad')
    favorite_game = forms.CharField(max_length=30, label='Juego favorito')

class Search_user_form(forms.Form):
    name = forms.CharField(max_length=30, label='Nombre')

class New_form(forms.Form):

    title = forms.CharField(max_length=100, label= 'Titulo')
    description =  forms.CharField(label="",widget=forms.Textarea(attrs={
        'rows': 4,
        'cols': 40,
        'placeholder': 'Escribe la descripción aquí...',
    }))

#Agregar hora a la fecha
class New_table(forms.Form):
    name = forms.CharField(max_length=20,  label="Nombre de la mesa")
    description = forms.CharField(max_length=100, label="Especifique juego y reglas a usar")
    date=forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}),label="Fecha de la partida: ")
    max_players = forms.IntegerField(label="Maximo de jugadores")

class List_user(forms.Form):
    player = forms.ModelChoiceField(queryset=User.objects.all())

class Search_table_form(forms.Form):
    start_date=forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}),label="Desde: ")
    end_date=forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}),label="Hasta: ")


    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get("start_date")
        end_date = cleaned_data.get("end_date")

        if start_date and end_date:
            if end_date < start_date:
                raise ValidationError("La fecha de fin no puede ser anterior a la fecha de inicio")
        
        return cleaned_data
    


