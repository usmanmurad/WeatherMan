# User management command class for inserting a single user


from django.core.management.base import BaseCommand
from Users.models import User


class Command(BaseCommand):
    help = "enters a user in database given username and password"

    # function to define command line arguments
    def add_arguments(self, parser):
        parser.add_argument('username', type=str, help='required username of user')
        parser.add_argument('password', type=str, help='required user password')

        # further optional arguments can also be used as in following commented part
        # parser.add_argument('first_name', type=str, nargs='?', default='', help='optional first name of user')

    # function for handling command
    def handle(self, *args, **options):
        username = options['username']
        password = options['password']
        print(options)
        user = User()
        user.username = username
        user.set_password(password)
        user.save()
        self.stdout.write(self.style.SUCCESS('Successfully created user "%s"' % username))
