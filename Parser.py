import WeatherReading


class Parser:
    @staticmethod
    def parse_data(dir_path, needed_files):

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
                reading = WeatherReading.WeatherReading(reading)
                one_month_readings.append(reading)
            month_name = needed_file.split('_')[-1]
            month_name = month_name.split('.')[0]
            one_year_readings[month_name] = one_month_readings
        return one_year_readings
