from django.core.management.base import BaseCommand
from Users.models import Dates
import pytz

class Command(BaseCommand):
    help = "test command"

    def add_arguments(self, parser):
        parser.add_argument('first_name', type=str, nargs='?', default='', help='optional first name of user')

    def handle(self, *args, **options):

        # find which timezone conversion to carry on this time
        to_convert = 'UTC'
        print("last object tz is ", Dates.objects.all().last().date_time.tzinfo)
        if str(Dates.objects.all().last().date_time.tzinfo) == 'UTC':
            to_convert = 'US/Pacific'
        print('to convert is ', to_convert)
        # get all date time objects from database
        date_times = Dates.objects.all()

        # convert 10 date time objects into different timezones using counter
        count = 0
        for date_time in date_times:
            print('date time value is', date_time.date_time)
            if str(date_time.date_time.tzinfo) != to_convert:
                date_time.date_time = date_time.date_time.astimezone(pytz.timezone(to_convert))
                print('converted date time value is', date_time.date_time)
                date_time.save(force_update=True)
                count = count + 1
            if count > 9:
                break
