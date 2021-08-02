from Colors import Colors


# global dictionary variables to convert month numbers into names

FULL_MONTH_NAMES = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June",
                    7: "July", 8: "August", 9: "September", 10: "October", 11: "November", 12: "December"}
SHORT_MONTH_NAMES = {1: "Jan", 2: "Feb", 3: "Mar", 4: "Apr", 5: "May", 6: "Jun",
                     7: "Jul", 8: "Aug", 9: "Sep", 10: "Oct", 11: "Nov", 12: "Dec"}


class ReportGenerator:
    @staticmethod
    def generate_year_report(stats):
        # Displaying Output
        print("Highest:", str(stats["max_temp"]) + 'C', "on", FULL_MONTH_NAMES[int((stats["max_temp_pkt"].split('-'))[1])],
              (stats["max_temp_pkt"].split('-'))[2])
        print("Lowest:", str(stats["min_temp"]) + 'C', "on", FULL_MONTH_NAMES[int((stats["min_temp_pkt"].split('-'))[1])],
              (stats["min_temp_pkt"].split('-'))[2])
        print("Humidity:", str(stats["min_humidity"]) + 'C', "on", FULL_MONTH_NAMES[int((stats["min_humidity_pkt"].split('-'))[1])],
              (stats["min_humidity_pkt"].split('-'))[2])

    @staticmethod
    def generate_month_average_report(stats):
        # Output
        print("Highest Average:", str(int(stats["avg_max_temp"])) + 'C')
        print("Lowest Average:", str(int(stats["avg_min_temp"])) + 'C')
        print("Average Mean Humidity:", str(int(stats["avg_mean_humidity"])) + '%')

    @staticmethod
    def generate_month_chart(one_month_readings):
        for month in one_month_readings:
            for read in one_month_readings[month]:
                if (len(read.max_temperature_c) > 0) and (len(read.min_temperature_c) > 0):
                    print((read.pkt.split('-'))[2], end="")
                    print(Colors.red, '+' * int(read.max_temperature_c), Colors.end_c, end="")
                    print(read.max_temperature_c + 'C')

                    print((read.pkt.split('-'))[2], end="")
                    print(Colors.blue, '+' * int(read.min_temperature_c), Colors.end_c, end="")
                    print(read.min_temperature_c + 'C')

    @staticmethod
    def generate_single_line_chart(one_month_readings):
        for month in one_month_readings:
            for read in one_month_readings[month]:
                if (len(read.max_temperature_c) > 0) and (len(read.min_temperature_c) > 0):
                    if int(read.min_temperature_c) > 0:
                        red = int(read.max_temperature_c) - int(read.min_temperature_c)
                    else:
                        red = int(read.max_temperature_c)
                    print((read.pkt.split('-'))[2], end="")
                    print(Colors.blue, '+' * int(read.min_temperature_c), end="")
                    print(Colors.red, '+' * red, Colors.end_c, sep="", end="")
                    print(read.min_temperature_c + 'C', '-', read.max_temperature_c + 'C')
