from django  import forms
from .models import crate

class createform(forms.ModelForm):
    class Meta:
        model = crate

        fields =[
            'name',
            'mobile',
            'email',
            'birth',
        ]
