from django.core.management.base import BaseCommand
from faker import Faker
from employees.models import Department, Employee, Attendance, Performance
import random
from datetime import timedelta, date

fake = Faker()

class Command(BaseCommand):
    help = 'Seed database with fake employee data'

    def handle(self, *args, **kwargs):
        departments = ['HR', 'Finance', 'Engineering', 'Sales', 'Marketing']
        for dept_name in departments:
            Department.objects.get_or_create(name=dept_name)

        for _ in range(50):
            department = random.choice(Department.objects.all())
            employee = Employee.objects.create(
                name=fake.name(),
                email=fake.unique.email(),
                phone_number=fake.phone_number(),
                address=fake.address(),
                date_of_joining=fake.date_between(start_date='-2y', end_date='today'),
                department=department
            )

            # Create Attendance Records
            for _ in range(10):
                Attendance.objects.create(
                    employee=employee,
                    date=fake.date_between(start_date='-30d', end_date='today'),
                    status=random.choice(['Present', 'Absent', 'Late'])
                )

            # Create Performance Record
            Performance.objects.create(
                employee=employee,
                rating=random.randint(1, 5),
                review_date=fake.date_this_year()
            )

        self.stdout.write(self.style.SUCCESS('Successfully seeded data!'))
