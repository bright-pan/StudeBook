from APP.models.SoftwareModel import Software
from django import forms


class SoftwareForm(forms.ModelForm):

    class Meta:
        model = Software
        fields = ['name', 'description', 'url']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter name'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter description',
                'rows': '3'
            }),
            'url': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter URL'
            })
        }
