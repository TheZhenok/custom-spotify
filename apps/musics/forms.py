# Django
from django import forms

# Local
from musics.models import Music


class TempForm(forms.Form):
    """Music form."""

    title = forms.CharField(
        max_length=100,
        label="Заголовок"
    )
    duration = forms.TimeField(
        label="Длительность",
        widget=forms.TimeInput(
            attrs={
                "type": "time"
            }
        )
    )
    description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "temp"
            }
        ),
        label="Описание",
    )


class MusicForm(forms.ModelForm):
    """Music form."""

    class Meta:
        model = Music
        fields = '__all__'
        widgets = {
            'duration': forms.TimeInput(
                attrs={'type': 'time'}
            ),
        }
