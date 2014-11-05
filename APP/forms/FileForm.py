from APP.models.FileModel import File
from django import forms

class FileForm(forms.ModelForm):
	class Meta:
		model = File
		fields = ['file_category', 'name', 'description', 'path']
		path = forms.FileField(
	        label='Select a file',
	        help_text='max. 42 megabytes'
    	)

