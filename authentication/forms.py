from django import forms
from authentication.models import Person


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['username', 'email', 'password', 'name', 'surname',
                  'github_link', 'linkedin_link', 'instagram_link']
        widgets = {
            'password': forms.PasswordInput(), 
        }

    def save(self, commit=True):
        person = super().save(commit=False)
        if self.cleaned_data["password"]:
            person.set_password(self.cleaned_data["password"])
        if commit:
            person.save()
        return person
