import sys
import re


import weather_man


def validate_month_input(inp):
    if not re.match("[0-9]{4,4}/[0-9]{1,2}$", inp):
        print("Invalid Input")
        exit()
    if int((inp.split('/'))[1]) < 1 or int((inp.split('/'))[1]) > 12:
        print("Invalid Month Value")
        return False
    return True


# Receiving and storing Input

inp = sys.argv
dir_path = inp[1]
inp = inp[2:]
query_count = 0

# Loop to iterate report queries one by one

while query_count < len(inp):
    if inp[query_count] == '-e':
        if not re.match("[0-9]{4}$", inp[query_count+1]):
            print("Invalid Input")
            exit()
        status = weather_man.display_year_stats(dir_path, inp[query_count+1])
        if status is not None:
            print(status)
    elif inp[query_count] == '-a':
        if validate_month_input(inp[query_count+1]):
            status = weather_man.display_month_average(dir_path, inp[query_count+1])
            if status is not None:
                print(status)
    elif inp[query_count] == '-c':
        if validate_month_input(inp[query_count+1]):
            status = weather_man.display_month_chart(dir_path, inp[query_count+1])
            if status is not None:
                print(status)
    elif inp[query_count] == '-b':
        if validate_month_input(inp[query_count+1]):
            status = weather_man.display_single_line_chart(dir_path, inp[query_count+1])
            if status is not None:
                print(status)
    else:
        print("Invalid Input")
        break
    query_count = query_count + 2
