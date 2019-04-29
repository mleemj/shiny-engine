from django import forms


class MyBlogForm(forms.Form):
    id = forms.IntegerField(widget=forms.HiddenInput())
    name = forms.CharField(label="Name")
    description = forms.CharField(widget=forms.Textarea)
