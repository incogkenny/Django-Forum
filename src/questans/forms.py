from django import forms
from .models import Questions, Answers, QuestionGroups, QGroups


class QuestionForm(forms.ModelForm):

    title = forms.CharField(max_length=90, required=True)
    description = forms.CharField(required=True, widget=forms.Textarea())

    class Meta:
        # Inherits data and fields from the 'Questions' model class
        model = Questions
        # The fields that will be displayed in the form
        fields = [ 'title', 'description', 'group']





class AnswerForm(forms.ModelForm):
    class Meta:
        # Inherits data and fields from the 'Answers' model class
        model = Answers
        # The field that is displayed in the form
        fields = ['answer']