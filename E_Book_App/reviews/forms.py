from django import forms
from E_Book_App.reviews.models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['body']
        widgets = {
            'body': forms.TextInput(attrs={'placeholder': 'Leave a review...'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.label = ''


class EditReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['body',]
        widgets = {'body': forms.TextInput()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.label = ''


class DeleteReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        exclude = ['book', 'user', 'body', 'created_at', 'updated_at']
