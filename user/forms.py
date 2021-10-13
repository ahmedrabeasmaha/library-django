from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth.models import User
from book.models import Book
from .models import Profile

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True,)

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        for feilds in self.visible_fields():
            feilds.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean(self):
        data = self.cleaned_data
        if User.objects.filter(username=data.get('username')).exists():
            self.add_error('username', "Username is used")
        if User.objects.filter(email=data.get('email')).exists():
            self.add_error('email', "Email is used")
        if data.get('password1') != data.get('password2'):
            self.add_error('password1', "password is not match")
        return data

class LogInForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LogInForm, self).__init__(*args, **kwargs)
        for feilds in self.visible_fields():
            feilds.field.widget.attrs['class'] = 'form-control'

class AddBookForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AddBookForm, self).__init__(*args, **kwargs)
        for feilds in self.visible_fields():
            if feilds.name == 'pic':
                feilds.field.widget.attrs['class'] = 'file-drop-input'
            elif feilds.name == 'category':
                feilds.field.widget.attrs['class'] = 'form-select me-2'
            else:
                feilds.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Book
        fields = '__all__'

class ChangePasswordForm(PasswordChangeForm):

    def __init__(self, *args, **kwargs):
        super(ChangePasswordForm, self).__init__(*args, **kwargs)
        for feilds in self.visible_fields():
                feilds.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = User
        fields = '__all__'

class ChangePicForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ChangePicForm, self).__init__(*args, **kwargs)
        for feilds in self.visible_fields():
            if feilds.name == 'pic':
                feilds.field.widget.attrs['class'] = 'file-drop-input'
            else:
                feilds.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Profile
        fields = '__all__'

