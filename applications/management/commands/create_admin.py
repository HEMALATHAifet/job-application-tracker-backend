from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
import os

class Command(BaseCommand):
    help = "Create admin user if it doesn't exist"

    def handle(self, *args, **kwargs):
        User = get_user_model()

        username = os.getenv("ADMIN_USERNAME", "admin")
        email = os.getenv("ADMIN_EMAIL", "admin@example.com")
        password = os.getenv("ADMIN_PASSWORD", "admin123")

        if User.objects.filter(username=username).exists():
            self.stdout.write(self.style.WARNING("Admin already exists"))
        else:
            User.objects.create_superuser(
                username=username,
                email=email,
                password=password
            )
            self.stdout.write(self.style.SUCCESS("Admin user created"))
