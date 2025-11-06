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


# ----- Post Form2 -----
class PostForm2(forms.ModelForm):
    """
    This form automatically creates form fields
    based on the Post model.
    """

    class Meta:
        model = Post
        fields = ['title', 'content']
        # We exclude 'author' because we'll set it automatically

        # Optional: Customize widgets
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter post title'
            }),

            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 10,
                'placeholder': 'Enter your post content here...'
            }),
        }

        # Optional: Custom labels
        labels = {
            'title': 'Post Title',
            'content': 'Post Content',
        }

        # Optional: Help Text
        help_texts = {
            'title': 'Choose a descriptive title (max 200 characters)',
            'content': 'Write your post content using plain text or markdown',
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