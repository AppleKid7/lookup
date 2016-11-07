from django import forms


class SearchForm(forms.Form):
    search = forms.CharField(label='',
                             attrs={'class': 'btn deep-purple',}
                             max_length=100)
