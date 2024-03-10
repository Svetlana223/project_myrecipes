from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Creates 5 users'

    def handle(self, *args, **kwargs):
        for i in range(5):
            username = f'user{i + 1}'
            email = f'user{i + 1}@example.com'
            password = 'password'
            User.objects.create_user(username=username, email=email, password=password)
            self.stdout.write(self.style.SUCCESS(f'Successfully created user {username}'))
