from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_user')
    created_at = models.DateTimeField(auto_now_add=True) # Automatic Timestamp
    updated_at = models.DateTimeField(auto_now=True) # Updates automatically

    def __str__(self):
        """
        This is what displays when you print a Post Object
        """

        return f"{self.title} - {self.author}"


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment_user')
    text = models.TextField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Comment by {self.author.username}'
    

