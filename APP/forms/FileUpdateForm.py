from APP.models.FileModel import File
from django import forms


class FileUpdateForm(forms.ModelForm):

    class Meta:
        model = File
        fields = ['file_category', 'name', 'description']
        widgets = {
            'file_category': forms.Select(attrs={
                'class': 'form-control'
            }),
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter name'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter description',
                'rows': '3'
            })
        }
