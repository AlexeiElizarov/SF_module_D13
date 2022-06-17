from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms

from .models import Advertsement



class AdvertsementForm(forms.ModelForm):
    body = forms.CharField(widget=CKEditorUploadingWidget())


    class Meta:
        model = Advertsement
        fields = '__all__'
