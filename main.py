import sys

import functions

# Receiving and storing Input

inp = sys.argv
dir_path = inp[1]
inp = inp[2:]
query_count = 0

# Loop to iterate report queries one by one

while query_count < len(inp):
    if inp[query_count] == '-e':
        status = functions.display_year_stats(dir_path, inp[query_count+1])
        if status is not None:
            print(status)
    elif inp[query_count] == '-a':
        status = functions.display_month_average(dir_path, inp[query_count+1])
        if status is not None:
            print(status)
    elif inp[query_count] == '-c':
        status = functions.display_month_chart(dir_path, inp[query_count+1])
        if status is not None:
            print(status)
    elif inp[query_count] == '-b':
        status = functions.display_single_line_chart(dir_path, inp[query_count+1])
        if status is not None:
            print(status)
    else:
        print("Invalid Input")
    query_count = query_count + 2
