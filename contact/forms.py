from django import forms
from django.core.exceptions import ValidationError

from contact.models import Contact


class ContactForm(forms.ModelForm):
  first_name = forms.CharField(
    widget=forms.TextInput(
      attrs={
        'class': 'classe-a classe-b',
        'placeholder': 'Escreva aqui',
      },
    ),
    label="Primeiro None",
    help_text="Texto de ajuda para seu unuário"
  )

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)

    # self.fields['first_name'].widget.attrs.update({
    #   'class': 'classe-a classe-b',
    #   'placeholder': 'Veio do init',
    # })

  class Meta:
    model =  Contact
    fields = (
      'first_name',
      'last_name',
      'phone',
      'email',
      'description',
      'category',
    )
    # widgets = {
    #   'first_name': forms.TextInput(
    #     attrs={
    #       'class': 'classe-a classe-b',
    #       'placeholder': 'Escreva aqui',
    #     }
    #   )
    # }

  def clean(self):
    # cleaned_data = self.cleaned_data
    
    # self.add_error(
    #   None,
    #   ValidationError(
    #     'Mensagem de erro 2',
    #     code='invalid'
    #   )
    # )

    return super().clean()
  
  def clean_first_name(self):
    first_name = self.cleaned_data.get('first_name')

    if first_name == 'ABC':
      self.add_error(
        'first_name',
        ValidationError(
          'Veio do add_error',
          code='invalid'
        )
      )

    return first_name