import re
from django import forms
from app.models import CourseInfo

class CourseForm(forms.ModelForm):
    fee = forms.IntegerField(min_value=3000)
    class Meta:
        model = CourseInfo
        fields = '__all__'
    def clean_name(self):
        name = self.cleaned_data['name']
        res = re.findall(r'^[A-Z a-z]*$',name)
        if res:
            return res
        else:
            raise forms.ValidationError('Invalid Name-It Will Accept Only A-Z and a-z Alphabets Only')

    def clean_tutor(self):
        tutor = self.cleaned_data['tutor']
        res = re.findall(r'^[A-Z a-z]*$', tutor)
        if res:
            return res
        else:
            raise forms.ValidationError('Invalid Name-It Will Accept Only A-Z and a-z Alphabets Only')
