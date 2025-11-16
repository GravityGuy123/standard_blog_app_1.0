from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone


# -----------------------------
# Post Model
# -----------------------------
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_user')
    created_at = models.DateTimeField(auto_now_add=True)  # Automatic Timestamp
    updated_at = models.DateTimeField(auto_now=True)      # Updates automatically

    def __str__(self):
        """This is what displays when you print a Post Object"""
        return f"{self.title} - {self.author.username}"


# -----------------------------
# Comment Model
# -----------------------------
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment_user')
    text = models.TextField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Comment by {self.author.username}'


# -----------------------------
# UserProfile Model
# -----------------------------
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    bio = models.CharField(max_length=300, blank=True)
    location = models.CharField(max_length=100, blank=True)
    birth_date = models.DateTimeField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True)

    # Track soft deletion
    is_deactivated = models.BooleanField(default=False)
    deactivated_at = models.DateTimeField(null=True, blank=True)
    deactivated_reason = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return f'Profile of {self.user.username}'

    def deactivate(self, reason=''):
        """
        Soft delete - deactivate account
        """

        self.is_deactivated = True
        self.deactivated_at = timezone.now()
        self.deactivation_reason = reason
        self.user.is_active = False
        self.user.save()
        self.save()

    def reactivate(self):
        """
        Restore deactivated account
        """

        self.is_deactivated = False
        self.deactivated_at = None
        self.deactivation_reason = ''
        self.user.is_active = True
        self.user.save()
        self.save()


# -----------------------------
# Signals to create/update profile
# -----------------------------
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        # Create profile only for newly created users
        UserProfile.objects.create(user=instance)
    else:
        # For existing users, only save if profile exists
        if hasattr(instance, 'user_profile'):
            instance.user_profile.save()