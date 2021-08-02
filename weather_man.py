import os

import Parser
import ResultCalculator
import ReportGenerator


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

    one_year_readings = Parser.Parser.parse_data(dir_path, needed_files)
    stats = ResultCalculator.ResultCalculator.calculate_year_stats(one_year_readings)
    ReportGenerator.ReportGenerator.generate_year_report(stats)


def display_month_average(dir_path, arg_value):

    # separating month and year value
    year, month = arg_value.split('/')
    month = SHORT_MONTH_NAMES[int(month)]

    # acquiring file name needed for execution of report query
    needed_file = []
    files = os.scandir(dir_path)
    for file in files:
        if (year in file.name) and (month in file.name):
            needed_file.append(file.name)
            break
    if len(needed_file) == 0:
        return "No data found for query -a " + arg_value

    one_month_readings = Parser.Parser.parse_data(dir_path, needed_file)
    stats = ResultCalculator.ResultCalculator.calculate_month_average(one_month_readings)
    ReportGenerator.ReportGenerator.generate_month_average_report(stats)


def display_month_chart(dir_path, arg_value):

    # separating month and year value
    year, month = arg_value.split('/')
    month_name = SHORT_MONTH_NAMES[int(month)]

    # acquiring file name needed for execution of report query
    needed_file = []
    files = os.scandir(dir_path)
    for file in files:
        if (year in file.name) and (month_name in file.name):
            needed_file.append(file.name)
            break
    if len(needed_file) == 0:
        return "No data found for query -c " + arg_value

    one_month_readings = Parser.Parser.parse_data(dir_path, needed_file)

    # printing output chart

    print(FULL_MONTH_NAMES[int(month)], year)
    ReportGenerator.ReportGenerator.generate_month_chart(one_month_readings)


def display_single_line_chart(dir_path, arg_value):

    # separating month and year value
    year, month = arg_value.split('/')
    month_name = SHORT_MONTH_NAMES[int(month)]

    # acquiring file name needed for execution of report query
    needed_file = []
    files = os.scandir(dir_path)
    for file in files:
        if (year in file.name) and (month_name in file.name):
            needed_file.append(file.name)
            break
    if len(needed_file) == 0:
        return "No data found for query -b " + arg_value

    one_month_readings = Parser.Parser.parse_data(dir_path, needed_file)
    # printing output chart

    print(FULL_MONTH_NAMES[int(month)], year)
    ReportGenerator.ReportGenerator.generate_single_line_chart(one_month_readings)
