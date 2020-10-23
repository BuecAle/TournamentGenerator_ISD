from django import forms
from .models import Products


class ProductCreateForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['title', 'description', 'price']

    def clean_title(self, *args, **kwargs):
        tmp = self.cleaned_data.get('title')
        if len(tmp) < 10:
            raise forms.ValidationError("This title is to short")
        return tmp


class RawProductForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField()
    price = forms.DecimalField()
