from django import forms
from django.forms import ModelForm
from .models import BorrowedBook

class DateInput(forms.DateInput):
    input_type = 'date'

class BorrowForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(BorrowForm, self).__init__(*args, **kwargs)
        for fields in self.visible_fields():
            fields.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = BorrowedBook
        fields = ['user', 'book', 'return_date']
        widgets = {
            'return_date': DateInput()
        }
