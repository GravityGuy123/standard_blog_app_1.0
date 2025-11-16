from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta
from .models import UserProfile

class Command(BaseCommand):
    help = 'Permanently delete accounts deactivated for more than 30 days'

    def handle(self, *args, **options):
        # Calculate cutoff date (30 days ago)
        cutoff = timezone.now() - timedelta(days=30)

        # Find old deactivated accounts
        old_deactivated = UserProfile.objects.filter(
            is_deactivated = True,
            deactivated_at__lt=cutoff
        )

        count = old_deactivated.count()

        # Permanently delete
        for profile in old_deactivated:
            username = profile.user.username
            profile.user.delete() # This also deletes the profile (CASCADE)
            self.stdout.write(f'Deleted {username}')
        
        self.stdout.write(
            self.style.SUCCESS(
                f'✅ Permanently deleted {count} accounts deactivated for 30+ days'
            )
        )