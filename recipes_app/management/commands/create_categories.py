from django.core.management.base import BaseCommand
from recipes_app.models import Category


class Command(BaseCommand):
    help = 'Creates 5 categories'

    def handle(self, *args, **kwargs):
        categories = ['Breakfast', 'Lunch', 'Dinner', 'Dessert', 'Snack']
        for category_name in categories:
            Category.objects.get_or_create(name=category_name)
            self.stdout.write(self.style.SUCCESS(f'Successfully created category {category_name}'))
