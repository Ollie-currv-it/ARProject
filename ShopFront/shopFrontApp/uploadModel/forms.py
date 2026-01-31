from django import forms


class UploadModelFileForm(forms.Form):
    model_name = forms.CharField(max_length=255)
    model_file = forms.FileField()
    tags = forms.CharField(max_length=200, required=False)
    description = forms.CharField(widget=forms.Textarea, required=False)
    # Add other fields as necessary
    