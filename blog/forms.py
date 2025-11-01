from django import forms
from .models import Post, Comment


# ----- Post Form -----
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        exclude = ['author']  # Author will be set automatically

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter the title'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 10,
                'placeholder': 'Enter the content'
            }),
        }


# ----- Comment Form -----
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment  # ✅ Use Comment model instead of Post
        fields = ['text']

        widgets = {
            'text': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Enter your comment'
            })
        }