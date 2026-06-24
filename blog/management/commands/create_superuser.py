from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Create a non-interactive superuser'

    def add_arguments(self, parser):
        parser.add_argument('--username', required=True)
        parser.add_argument('--email', required=True)
        parser.add_argument('--password', required=True)

    def handle(self, *args, **options):
        User = get_user_model()
        if User.objects.filter(username=options['username']).exists():
            self.stdout.write(self.style.WARNING(f"User '{options['username']}' already exists"))
            return
        User.objects.create_superuser(
            username=options['username'],
            email=options['email'],
            password=options['password'],
        )
        self.stdout.write(self.style.SUCCESS(f"Superuser '{options['username']}' created"))
