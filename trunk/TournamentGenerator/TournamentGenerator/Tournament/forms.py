from django import forms
from .models import Tournament


# Create your forms here
class TournamentCreateForm(forms.ModelForm):

    class Meta:
        model = Tournament
        fields = ['TournamentName', 'TournamentSize']

    def clean_title(self):
        tmp = self.cleaned_data.get('TournamentName')
        if len(tmp) < 5:
            raise forms.ValidationError('This Tournamentname is too short')
        return tmp



class RawTournamentForm(forms.Form):
    TournamentName = forms.CharField()
    TournamentSize = forms.CharField()
