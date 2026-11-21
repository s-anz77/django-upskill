from django import forms

from .models import LessonComments


class AddLessonCommentForm(forms.ModelForm):
    text = forms.CharField(
        label='Текст комментария',
        required=True,
        widget=forms.Textarea(attrs={'placeholder': 'Введите комментарий'}),
    )

    class Meta:
        model = LessonComments
        fields = ['text']
