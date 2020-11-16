from django import forms
from .models import Teams, Tournament


class TeamCreateForm(forms.ModelForm):
    class Meta:
        model = Teams
        fields = ['TeamName', 'NrOfPlayer', 'Manager', 'Captain']

    def clean_title(self, *args, **kwargs):
        tmp = self.cleaned_data.get('TeamName')
        if len(tmp) < 10:
            raise forms.ValidationError("This Teamname is too short")
        return tmp


class RawTeamForm(forms.Form):
    TeamName = forms.CharField()
    NrOfPlayer = forms.DecimalField()
    Manager = forms.CharField()
    Captain = forms.CharField();


class TournamentCreateForm(forms.ModelForm):
    class Meta:
        model = Tournament
        fields = ['TournamentName', 'TournamentSize']

    def clean_title(self, *args, **kwargs):
        tmp = self.cleaned_data.get('TournamentName')
        if len(tmp) < 5:
            raise forms.ValidationError("This Tournamentname is too short")
        return tmp


class RawTeamForm(forms.Form):
    TournamentName = forms.CharField()
    TournamentSize = forms.CharField();
