from django import forms
from .models import Mentor
from .options import *

class MentorAdminForm(forms.ModelForm):
    class Meta:
        model = Mentor
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'type' in self.data:
            mentor_type = self.data.get('type')
        elif self.instance.pk:
            mentor_type = self.instance.type
        else:
            mentor_type = None

        if mentor_type == 'placement':
            self.fields['field'].choices = PLACEMENT_FIELDS
        elif mentor_type == 'grad':
            self.fields['field'].choices = HIGHERSTUDIES_FIELDS
        else:
            self.fields['field'].choices = []