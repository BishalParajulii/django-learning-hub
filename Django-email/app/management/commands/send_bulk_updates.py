from django.core.management.base import BaseCommand
from django.core import mail
from templated_email import get_templated_mail


class Command(BaseCommand):
    help = 'Sends bulk email updates to all users'

    def handle(self, *args, **options):

        connection = mail.get_connection()
        connection.open()

        users = [
            'j.wilson88@gmail.com',
            'schen_dev@outlook.com',
            'm.thorne.92@yahoo.com',
        ]

        messages = []

        for user in users:

            msg = get_templated_mail(
                template_name='welcome',
                from_email='abc@example.com',
                to=[user],
                context={
                    'username': 'bishal',
                    'full_name': 'Bishal',
                    'signup_date': '14 May 2026'
                }
            )

            messages.append(msg)

        connection.send_messages(messages)

        connection.close()

        self.stdout.write(
            self.style.SUCCESS(
                f'Successfully sent {len(messages)} emails'
            )
        )