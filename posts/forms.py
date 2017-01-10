from django import forms

from pagedown.widgets import PagedownWidget

from .models import Post
from .models import Likes


class PostForm(forms.ModelForm):
    content = forms.CharField(widget=PagedownWidget(show_preview=False))
    publish = forms.DateField(widget=forms.SelectDateWidget)
    class Meta:
        model = Post
        fields = [
            "title",
            "content",
            "image",
            "draft",
            "publish",
        ]

class QuestionForm(forms.ModelForm):
    def save(self, user = None, force_insert = False, force_update = False, commit = True):
        q = super(QuestionForm, self).save(commit = False)
        q.user = user
        if commit:
            q.save()
        return q

    class Meta:
        model = Likes
        exclude = ('user',)
