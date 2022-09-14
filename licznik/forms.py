from django import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.core.validators import FileExtensionValidator
from django.forms import DateInput, PasswordInput


# class UserForm(forms.ModelForm):
class UserForm(UserCreationForm):

    email = forms.EmailField(max_length=254, help_text='Wymagany.')
    # password = forms.CharField(widget=PasswordInput())



    class Meta:
        model = User
        fields = ['first_name','second_name','last_name','email','pesel','username']


class KandydatForm(forms.ModelForm):
    class Meta:
        model = Kandydat
        fields = ['clas','internat','j_pol_egz','mat_egz','j_obcy_egz','j_pol_oc','mat_oc','biol_oc',
                  'inf_oc','sw_wyr']

class UserFormAdmin(forms.ModelForm):

    firstname = forms.CharField()
    secondname = forms.CharField()
    lastname = forms.CharField()
    pesel = forms.CharField()
    username = forms.CharField()
    # password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = '__all__'


class KandydatFormAdmin(forms.ModelForm):

    user_firstname = forms.CharField()
    user_secondname = forms.CharField()
    user_lastname = forms.CharField()
    user_pesel = forms.CharField()
    user_username = forms.CharField()

    class Meta:
        model = Kandydat
        # fields = '__all__'
        exclude = ["user"]



class UploadForm(forms.Form):
    docfile = forms.FileField(
        label='Dołącz plik csv',
        help_text='max. 1MB',
        validators=[FileExtensionValidator(allowed_extensions=['csv'])])


class StatusForm(forms.ModelForm):


    class Meta:

        # dt = statobj.datastart
        model = Status
        fields = ['status', 'datastart','dataend']
        widgets = {
            'datastart': DateInput(attrs={'type': 'date', 'value':datetime.datetime.today().strftime("%d-%m-%Y")}),
            'dataend': DateInput(attrs={'type': 'date'})
        }
