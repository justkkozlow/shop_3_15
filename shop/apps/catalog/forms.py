from django import forms


class ContactForm(forms.Form):
    subject = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control',
                                                                      'placeholder': "Тема"}))

    content = forms.CharField(label='', widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5,
                                                                     'placeholder': 'Напишите нам...'}))



