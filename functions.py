import os
import sys

from WeatherReading import WeatherReading
from Colors import Colors

# global dictionary variables to convert month numbers into names

FULL_MONTH_NAMES = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June",
                    7: "July", 8: "August", 9: "September", 10: "October", 11: "November", 12: "December"}
SHORT_MONTH_NAMES = {1: "Jan", 2: "Feb", 3: "Mar", 4: "Apr", 5: "May", 6: "Jun",
                     7: "Jul", 8: "Aug", 9: "Sep", 10: "Oct", 11: "Nov", 12: "Dec"}

# separate functions for each test case

def display_year_stats(dir_path, year):

    # getting and filtering names of files
    needed_files = []
    all_files = os.scandir(dir_path)
    for file in all_files:
        if year in file.name:
            needed_files.append(file.name)
    if len(needed_files) == 0:
        return "No data found for query -e " + year

    # Loading data needed to display stats
    one_month_readings = []
    one_year_readings = dict()
    for needed_file in needed_files:
        path = dir_path + needed_file
        handle = open(path, 'r')
        inp_lines = handle.readlines()
        inp_lines = inp_lines[1:]
        for i in range(len(inp_lines)):
            reading = inp_lines[i].split(',')
            reading = WeatherReading(reading)
            one_month_readings.append(reading)
        month_name = needed_file.split('_')[-1]
        month_name = month_name.split('.')[0]
        one_year_readings[month_name] = one_month_readings

    # Initializing variables needed to store result
    max_temp = -sys.maxsize - 1
    min_temp = sys.maxsize
    min_humidity = 100

    # Logic to find min,max temperature and humidity
    for month in one_year_readings:
        for read in one_year_readings[month]:
            if int(read.max_temperature_c) > max_temp:
                max_temp = int(read.max_temperature_c)
                max_temp_pkt = read.pkt
            if int(read.min_temperature_c) < min_temp:
                min_temp = int(read.min_temperature_c)
                min_temp_pkt = read.pkt
            if int(read.mean_humidity) < min_humidity:
                min_humidity = int(read.mean_humidity)
                min_humidity_pkt = read.pkt

    # Displaying Output
    print("Highest:", str(max_temp) + 'C', "on", FULL_MONTH_NAMES[int((max_temp_pkt.split('-'))[1])],
          (max_temp_pkt.split('-'))[2])
    print("Lowest:", str(min_temp) + 'C', "on", FULL_MONTH_NAMES[int((min_temp_pkt.split('-'))[1])],
          (min_temp_pkt.split('-'))[2])
    print("Humidity:", str(min_humidity) + 'C', "on", FULL_MONTH_NAMES[int((min_humidity_pkt.split('-'))[1])],
          (min_humidity_pkt.split('-'))[2])


def display_month_average(dir_path, arg_value):

    # separating month and year value
    year, month = arg_value.split('/')
    month = SHORT_MONTH_NAMES[int(month)]

    # acquiring file name needed for execution of report query
    needed_file = ''
    files = os.scandir(dir_path)
    for file in files:
        if (year in file.name) and (month in file.name):
            needed_file = file.name
            break
    if len(needed_file) == 0:
        return "No data found for query -a " + arg_value

    # loading data from file into memory
    one_month_readings = []
    path = dir_path + needed_file
    handle = open(path, 'r')
    inp_lines = handle.readlines()
    inp_lines = inp_lines[1:]
    for i in range(len(inp_lines)):
        reading = inp_lines[i].split(',')
        reading = WeatherReading(reading)
        one_month_readings.append(reading)

    # variables to store month stats
    avg_max_temp = 0
    max_temps = 0
    avg_min_temp = 0
    min_temps = 0
    avg_mean_humidity = 0
    humidity_count = 0

    # storing month stats
    for read in one_month_readings:
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

    # Output
    print("Highest Average:", str(int(avg_max_temp)) + 'C')
    print("Lowest Average:", str(int(avg_min_temp)) + 'C')
    print("Average Mean Humidity:", str(int(avg_mean_humidity)) + '%')


def display_month_chart(dir_path, arg_value):

    # separating month and year value
    year, month = arg_value.split('/')
    month_name = SHORT_MONTH_NAMES[int(month)]

    # acquiring file name needed for execution of report query
    needed_file = ''
    files = os.scandir(dir_path)
    for file in files:
        if (year in file.name) and (month_name in file.name):
            needed_file = file.name
            break
    if len(needed_file) == 0:
        return "No data found for query -c " + arg_value

    # loading data from file into memory
    one_month_readings = []
    path = dir_path + needed_file
    handle = open(path, 'r')
    inp_lines = handle.readlines()
    inp_lines = inp_lines[1:]
    for i in range(len(inp_lines)):
        reading = inp_lines[i].split(',')
        reading = WeatherReading(reading)
        one_month_readings.append(reading)

    # printing output chart

    print(FULL_MONTH_NAMES[int(month)], year)
    for read in one_month_readings:
        if (len(read.max_temperature_c) > 0) and (len(read.min_temperature_c) > 0):
            print((read.pkt.split('-'))[2], end="")
            print(Colors.red, '+' * int(read.max_temperature_c), Colors.end_c, end="")
            print(read.max_temperature_c + 'C')

            print((read.pkt.split('-'))[2], end="")
            print(Colors.blue, '+' * int(read.min_temperature_c), Colors.end_c, end="")
            print(read.min_temperature_c + 'C')


def display_single_line_chart(dir_path, arg_value):

    # separating month and year value
    year, month = arg_value.split('/')
    month_name = SHORT_MONTH_NAMES[int(month)]

    # acquiring file name needed for execution of report query
    needed_file = ''
    files = os.scandir(dir_path)
    for file in files:
        if (year in file.name) and (month_name in file.name):
            needed_file = file.name
            break
    if len(needed_file) == 0:
        return "No data found for query -b " + arg_value

    # loading data from file into memory
    one_month_readings = []
    path = dir_path + needed_file
    handle = open(path, 'r')
    inp_lines = handle.readlines()
    inp_lines = inp_lines[1:]
    for i in range(len(inp_lines)):
        reading = inp_lines[i].split(',')
        reading = WeatherReading(reading)
        one_month_readings.append(reading)

    # printing output chart

    print(FULL_MONTH_NAMES[int(month)], year)
    for read in one_month_readings:
        if (len(read.max_temperature_c) > 0) and (len(read.min_temperature_c) > 0):
            if int(read.min_temperature_c) > 0:
                red = int(read.max_temperature_c) - int(read.min_temperature_c)
            else:
                red = int(read.max_temperature_c)
            print((read.pkt.split('-'))[2], end="")
            print(Colors.blue, '+' * int(read.min_temperature_c), end="")
            print(Colors.red, '+' * red, Colors.end_c, sep="", end="")
            print(read.min_temperature_c + 'C', '-', read.max_temperature_c + 'C')
