from django import forms
from .models import Team


# Create your forms here
class TeamCreateForm(forms.ModelForm):

    class Meta:
        model = Team
        fields = ['TeamName', 'NrOfPlayer', 'Manager', 'Captain', 'Tournament']

    def clean_title(self, *args, **kwargs):
        tmp = self.cleaned_data.get('TeamName')
        if len(tmp) < 10:
            raise forms.ValidationError('This Teamname is too short')
        return tmp


# Teamform with its fields
class RawTeamForm(forms.Form):
    TeamName = forms.CharField()
    NrOfPlayer = forms.DecimalField(min_value=5, max_value=30)
    Manager = forms.CharField()
    Captain = forms.CharField()
    Tournament = forms.CharField()
