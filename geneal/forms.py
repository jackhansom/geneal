from django import forms
from .models import Person
from functools import partial
DateInput = partial(forms.DateInput, {'class': 'form-control',
                                      'type': 'date'})


class NameForm(forms.Form):
    first_name = forms.CharField(label='\nFirst Name', max_length=120)
    middle_names = forms.CharField(label='\nMiddle Names',
                                   max_length=120,
                                   required=False)
    last_name = forms.CharField(label='\nLast Name', max_length=120)
    born = forms.DateField(label='\nDate of Birth', widget=DateInput())
    died = forms.DateField(label='\nDate of Death', required=False,
                           widget=DateInput())
    father = forms.ModelChoiceField(label='\nFather',
                               queryset=Person.objects.all(),
                               required=False)
    mother = forms.ModelChoiceField(label='\nMother',
                               queryset=Person.objects.all(),
                               required=False)
