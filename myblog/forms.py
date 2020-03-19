from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
	class Meta:
		model = Feedback
		fields = ['body']
		widgets = {
            'body':forms.Textarea(attrs={'class':'fq_form',
            							 'rows':"6",
            							 'maxlength': '200'})
        }