from django.core.management.base import BaseCommand
from faker import Faker
from django.utils import timezone
from hangarinproj.models import Task, Note, SubTask, Priority, Category

fake = Faker()

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        for _ in range(10):
            task = Task.objects.create(
                title=fake.sentence(nb_words=5),
                description=fake.paragraph(nb_sentences=3),
                deadline=timezone.make_aware(fake.date_time_this_month()),
                status=fake.random_element(elements=["Pending","In Progress","Completed"]),
                category=Category.objects.order_by('?').first(),
                priority=Priority.objects.order_by('?').first(),
            )
            Note.objects.create(task=task, content=fake.paragraph(nb_sentences=2))
            SubTask.objects.create(
                parent_task=task,
                title=fake.sentence(nb_words=4),
                status=fake.random_element(elements=["Pending","In Progress","Completed"])
            )
