from django import forms
from .models import Post, Comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile
from django.core.exceptions import ValidationError
import re


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

    def clean_title(self):
        """
        Custom validation for the title field.
        """
        title = self.cleaned_data.get('title')

        # Rule 1: Minimum and Maximum Length
        if len(title) < 5:
            raise ValidationError("Title must be at least 5 characters long.")
        if len(title) > 200:
            raise ValidationError("Title cannot exceed 200 characters.")
        
        # Rule 2: Prohibited Words
        banned_words = ['spam', 'advertisement', 'clickbait', 'fake']

        for word in banned_words:
            if word in title.lower():
                raise ValidationError(f"The title contains a prohibited word: '{word}'")
        
        return title
    
    def clean_content(self):
        """
        Custom validation for the content field.
        """
        content = self.cleaned_data.get('content')

        # Rule 1: Minimum Length
        if len(content) < 20:
            raise ValidationError("Content must be at least 20 characters long.")
        
        return content


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

    def clean_title(self):
        """
        Custom validation for the title field.
        """
        title = self.cleaned_data.get('title')

        # Rule 1: Minimum and Maximum Length
        if len(title) < 5:
            raise ValidationError("Title must be at least 5 characters long.")
        if len(title) > 200:
            raise ValidationError("Title cannot exceed 200 characters.")
        
        # Rule 2: Prohibited Words
        banned_words = ['spam', 'advertisement', 'clickbait', 'fake']

        for word in banned_words:
            if word in title.lower():
                raise ValidationError(f"The title contains a prohibited word: '{word}'")
        
        return title
    
    def clean_content(self):
        """
        Custom validation for the content field.
        """
        content = self.cleaned_data.get('content')

        # Rule 1: Minimum Length
        if len(content) < 20:
            raise ValidationError("Content must be at least 20 characters long.")
        
        return content
    

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


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your email address'
        })
    )

    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your password'
        }),
        help_text="Password must contain at least 8 characters, one uppercase letter, and one number."
    )

    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Re-enter your password'
        })
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your username'
            }),
        }
        labels = {
            'username': 'Username',
            'email': 'Email',
            'password1': 'Password',
            'password2': 'Confirm Password',
        }

    # ----- Custom Validations -----

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if len(username) < 4:
            raise ValidationError("Username must be at least 4 characters long.")
        if not re.match(r'^[A-Za-z0-9_]+$', username):
            raise ValidationError("Username can only contain letters, numbers, and underscores.")
        if User.objects.filter(username__iexact=username).exists():
            raise ValidationError("This username is already taken.")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email__iexact=email).exists():
            raise ValidationError("An account with this email already exists.")
        return email

    def clean_password1(self):
        password = self.cleaned_data.get('password1')

        # Length Check
        if len(password) < 8:
            raise ValidationError("Password must be at least 8 characters long.")

        # At least one uppercase letter
        if not re.search(r'[A-Z]', password):
            raise ValidationError("Password must contain at least one uppercase letter.")

        # At least one digit
        if not re.search(r'\d', password):
            raise ValidationError("Password must contain at least one number.")

        # # Optional: Help Text
        # help_texts = {
        #     'title': 'Choose a username',
        #     'content': 'Enter your email address',
        #     'password1': 'Enter your password',
        #     'password2': 'Re-Enter your password',
        # }



class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'location', 'birth_date', 'profile_picture']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Add custom styling and placeholders to form fields
        self.fields['bio'].widget.attrs.update({
            'class': 'full-width',
            'rows': 4,
            'placeholder': 'Tell us about yourself...',
            'style': 'resize: none; width:100%; padding:10px; font-size:15px; border-radius:8px; border:1px solid #ccc;',
        })

        self.fields['location'].widget.attrs.update({
            'placeholder': 'Enter your location...',
            'style': 'width:100%; padding:10px; font-size:15px; border-radius:8px; border:1px solid #ccc;',
        })

        self.fields['birth_date'].widget.attrs.update({
            'type': 'date',
            'style': 'width:100%; padding:10px; font-size:15px; border-radius:8px; border:1px solid #ccc;',
        })

        self.fields['profile_picture'].widget.attrs.update({
            'accept': 'image/*',
            'style': 'width:100%; padding:5px;',
        })