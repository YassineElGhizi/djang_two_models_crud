from django import forms


class AddBrandForm(forms.Form):
    name = forms.CharField(required=True)


class AddStoreForm(forms.Form):
    name = forms.CharField(required=True)
    brand = forms.IntegerField(required=True)
