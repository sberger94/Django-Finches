from django.forms import ModelForm
from .models import Spotted

class SpottedForm(ModelForm):
    class Meta:
        model = Spotted
        fields = ['date', 'location']