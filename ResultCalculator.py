import sys


class ResultCalculator:
    @staticmethod
    def calculate_year_stats(one_year_readings):

        # Initializing variables needed to store result
        max_temp = -sys.maxsize - 1
        min_temp = sys.maxsize
        min_humidity = 100

        # Logic to find min,max temperature and humidity
        for month in one_year_readings:
            for read in one_year_readings[month]:
                if len(read.max_temperature_c) > 0:
                    if int(read.max_temperature_c) > max_temp:
                        max_temp = int(read.max_temperature_c)
                        max_temp_pkt = read.pkt
                if len(read.min_temperature_c) > 0:
                    if int(read.min_temperature_c) < min_temp:
                        min_temp = int(read.min_temperature_c)
                        min_temp_pkt = read.pkt
                if len(read.mean_humidity) > 0:
                    if int(read.mean_humidity) < min_humidity:
                        min_humidity = int(read.mean_humidity)
                        min_humidity_pkt = read.pkt

        result = {"max_temp": max_temp, "max_temp_pkt": max_temp_pkt, "min_temp": min_temp, "min_temp_pkt": min_temp_pkt,
                  "min_humidity": min_humidity, "min_humidity_pkt": min_humidity_pkt}
        return result

    @staticmethod
    def calculate_month_average(one_month_readings):
        # variables to store month stats
        avg_max_temp = 0
        max_temps = 0
        avg_min_temp = 0
        min_temps = 0
        avg_mean_humidity = 0
        humidity_count = 0

        # storing month stats
        for month in one_month_readings:
            for read in one_month_readings[month]:
                if len(read.max_temperature_c) > 0:
                    avg_max_temp = avg_max_temp + int(read.max_temperature_c)
                    max_temps = max_temps + 1
                if len(read.min_temperature_c) > 0:
                    avg_min_temp = avg_min_temp + int(read.min_temperature_c)
                    min_temps = min_temps + 1
                if len(read.mean_humidity) > 0:
                    avg_mean_humidity = avg_mean_humidity + int(read.mean_humidity)
                    humidity_count = humidity_count + 1
        avg_max_temp = avg_max_temp / max_temps
        avg_min_temp = avg_min_temp / min_temps
        avg_mean_humidity = avg_mean_humidity / humidity_count

        result = {"avg_max_temp": avg_max_temp, "avg_min_temp": avg_min_temp, "avg_mean_humidity": avg_mean_humidity}
        return result
