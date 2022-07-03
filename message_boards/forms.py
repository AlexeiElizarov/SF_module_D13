from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from ckeditor_uploader.fields import RichTextUploadingField
from .models import Advertsement, Category



class AdvertsementForm(forms.ModelForm):
    body = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Advertsement
        # fields = '__all__'
        fields = [
            "title",
            "body",
            "category",
            # "advertsement_category",
        ]
