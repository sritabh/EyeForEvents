#UserCreationForm to create users
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError

#create signup form with extra field
class SignUpForm(UserCreationForm):

    #creating email field,required,widget used to represent html element
    email = forms.EmailField(label="",widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}),)
    
    #creating 1st name field max length= 100 char,required
    first_name = forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}),)

    #creating last name field max length= 100 char,required
    last_name = forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}),)
    
    #function to prevent duplicate email
    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.count():
            raise  ValidationError("Email already exists")
        return email
    
    #function for checking empty password & if pass1 = pass2 
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("Password don't match")

        return password2

    #creating form with extra fields 
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2',)

    #*args for any no of args **kwargs for dictionary args
    def __init__(self, *args, **kwargs):
	    super(SignUpForm, self).__init__(*args, **kwargs)

	    self.fields['password1'].widget.attrs['class'] = 'form-control'
	    self.fields['password1'].widget.attrs['placeholder'] = 'Password'
	    self.fields['password1'].label = ''
	    self.fields['password1'].help_text = '<ul class="form-text text-muted small" style="text-align:left;"><li>Your password must contain at least 8 characters.</li></ul>'

	    self.fields['password2'].widget.attrs['class'] = 'form-control'
	    self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
	    self.fields['password2'].label = ''
	    self.fields['password2'].help_text = '<span class="form-text text-muted" style="text-align:left;"><small>Enter the same password as before, for verification.</small></span>'
  

