import random
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string
from recipes_app.models import Recipe
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Create 20 random recipes'

    def handle(self, *args, **kwargs):
        users = User.objects.all()
        if not users:
            self.stdout.write(self.style.ERROR('No users found. Please create users first.'))
            return

        for i in range(20):
            author = random.choice(users)
            title = f'Recipe {get_random_string(length=10)}'
            description = get_random_string(length=100)
            steps = get_random_string(length=10)
            cooking_time = random.randint(10, 120)
            recipe = Recipe(
                title=title,
                description=description,
                steps=steps,
                cooking_time=cooking_time,
                author=author,
            )
            recipe.save()
            self.stdout.write(self.style.SUCCESS(f'Successfully created recipe {title}'))
