# cron job for converting datetime objects in different timezone


from Users.models import Dates
import pytz


def change_timezone():

    # find which timezone conversion to carry on this time
    to_convert = 'UTC'
    if str(Dates.objects.all().last().date_time.tzinfo) == 'UTC':
        to_convert = 'US/Pacific'

    # get all date time objects from database
    date_times = Dates.objects.all()

    # convert 10 date time objects into different timezones using counter
    count = 0
    for date_time in date_times:
        if str(date_time.date_time.tzinfo) != to_convert:
            date_time.date_time = date_time.date_time.astimezone(pytz.timezone(to_convert))
            date_time.save()
            count = count + 1
        if count > 9:
            break
