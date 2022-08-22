from django.forms import ModelForm
from novosite.models import Smatphone

class SmatphoneForm(ModelForm):
    class Meta:
        model = Smatphone
        fields = ['modelo','marca','ano', 'cor']