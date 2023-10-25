from .models import Serie
from . import models
from django import forms
from django.core import validators
from django.forms import ModelForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class AddSerie(ModelForm):

    class Meta:
        model=Serie
        fields=('titre','description','realisateur','annee_de_sortie','nbre_episodes')

class SignupForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model=get_user_model()
        fields=('username','email','first_name','last_name')

