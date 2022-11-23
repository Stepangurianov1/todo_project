from django.contrib.auth.management.commands import createsuperuser
from django.core.management import CommandError

from django.core.management.base import BaseCommand, CommandError

from users.models import MyUsers


class Command(BaseCommand):

    help = "Введите имя пользователя почту и пароль"

    def add_arguments(self, parser):
        super(Command, self).add_arguments(parser)
        parser.add_argument(
            'my_list', nargs='+',
        )

    def handle(self, *args, **options):
        data = options.get('my_list')
        if data:
            MyUsers.objects.create_user(username=data[0],
                                      email=data[1],
                                      password=data[2],
                                      is_staff=True,
                                      is_active=True,
                                      is_superuser=True)
