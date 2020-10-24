from django import forms
from .models import Teams


class TeamCreateForm(forms.ModelForm):
    class Meta:
        model = Teams
        fields = ['TeamName', 'NrOfPlayer']

    def clean_title(self, *args, **kwargs):
        tmp = self.cleaned_data.get('TeamName')
        if len(tmp) < 10:
            raise forms.ValidationError("This Teamname is to short")
        return tmp


class RawTeamForm(forms.Form):
    TeamName = forms.CharField()
    NrOfPlayer = forms.DecimalField()
