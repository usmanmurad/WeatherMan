from django import forms
from Users.models import User


class RegisterForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'bio', 'phone', 'password']

    # overriding save method of ModelForm class
    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
