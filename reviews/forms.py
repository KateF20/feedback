from django import forms

from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__' # or [with properties names], or exclude = ['']
        labels = {'user_name': 'Your name', 'text': 'Your feedback', 'rating': 'Your rating'}
        error_messages = {
            'user_name': {
                'required': 'This field can not be empty',
                'max_length': 'This name is too long'
            },
            'text': {
                'required': 'This field can not be empty',
                'max_length': 'This name is too long'
            },
            'rating': {
                'required': 'This field can not be empty',
            }
        }

