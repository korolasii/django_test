from django.core.management.base import BaseCommand
from first_app.models import Employee


class Command(BaseCommand):
    help = 'Activate all employees (set is_active=True)'

    def handle(self, *args, **options):
        updated_count = Employee.objects.update(is_active=True)
        self.stdout.write(self.style.SUCCESS(f'Successfully activated {updated_count} employees.'))
