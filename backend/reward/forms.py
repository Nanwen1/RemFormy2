from django.forms import ModelForm
from .models import Rem


class RemForm(ModelForm):
    class Meta:
        model = Rem
        fields = '__all__'







# from django import forms
#
#
# Region_CHOICES = (
#     ("", "Choose..."),
#     ("1", "MinAus"),
#     ("2", "MinAmericas"),
#     ("3", "Petroleum"),
#     ("4", "GlobalFunction"),
# )
#
# AssetFunction_CHOICES = (
#     ("", "Choose..."),
#     ("1", "WAIO"),
#     ("2", "NiW"),
#     ("3", "OD"),
#     ("4", "Coal"),
# )
#
# grade_CHOICES = (
#     ("", "Choose..."),
#     ("1", "NA"),
#     ("4", "4"),
#     ("5", "5"),
#     ("6", "6"),
#     ("7", "7"),
#     ("8", "8"),
#     ("9", "9"),
#     ("10", "10"),
#     ("11", "11"),
#     ("12", "12"),
#     ("13", "13"),
# )
#
#
# jobfamily_CHOICES = (
#     ("", "Choose..."),
#     ("1", "SS01"),
#     ("2", "SS02"),
#     ("3", "SS03"),
#     ("4", "SS04"),
# )
#
# class RewardForm(forms.Form):
#     region = forms.ChoiceField(choices=Region_CHOICES)
#     Asset_Function = forms.ChoiceField(choices=AssetFunction_CHOICES)
#     grade = forms.ChoiceField(choices=grade_CHOICES)
#     job_family = forms.ChoiceField(choices=jobfamily_CHOICES)
#
