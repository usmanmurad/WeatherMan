# user management command for creating dummy users and storing datetime objects


from django.core.management.base import BaseCommand
from Users.models import User, Dates
from random import randint
from datetime import datetime
from pytz import timezone


class Command(BaseCommand):
    help = "enters dummy users in database"

    # function to define command line arguments
    def add_arguments(self, parser):
        parser.add_argument('username', type=str, help='required username for inserting dummy users')

    # function for handling command
    def handle(self, *args, **options):

        # create on hundred dummy users by extending given user name with a digit
        username = options['username']
        print(options)
        for i in range(100):
            user = User()
            user.username = username + str(i)
            user.set_password(username + str(i))
            user.save()
        self.stdout.write(self.style.SUCCESS('Successfully created hundred users !'))

        # create one hundred random datetime objects and store them in a seperate field
        for i in range(100):
            date_time = datetime(randint(2016, 2021), randint(1, 12), randint(1, 28), randint(0, 23), randint(0, 59),
                                 randint(0, 59), randint(0, 999999), tzinfo=timezone('US/Pacific'))
            date_object = Dates()
            date_object.date_time = date_time
            date_object.save()
