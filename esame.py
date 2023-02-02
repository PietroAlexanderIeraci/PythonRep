class ExamException(Exception):
    pass

class CSVTimeSeriesFile:
    def __init__(self, name):
        self.name = name

    def find_file(self):
        try:
            my_file = open(self.name)
        except FileNotFoundError:
            raise ExamException("File not found")
        return my_file

    def get_data(self):
        my_file = self.find_file()
        my_list = []
        
        for line in my_file:
            elements = line.split(',')
            try:
                elements[0] = int(elements[0])
                elements[1] = float(elements[1])
                my_list.append(elements)
            except Exception:
                continue

        if not my_list:
            raise ExamException('Lista valori vuota')

        for i in range(len(my_list)-1):
            current = my_list[i]
            next = my_list[i+1]
            if next <= current:
                raise ExamException('Lista valori non valida')

        return my_list

def compute_daily_max_difference(time_series):
    output = []
    all_days = []
    current_day = []
    day_start = time_series[0][0]-(time_series[0][0]%86400)

    for element in time_series:
        if element[0]-day_start < 86400:
            current_day.append(element[1])
        else:
            day_start += 86400
            all_days.append(current_day)
            current_day = []
            current_day.append(element[1])
    all_days.append(current_day)

    for day in all_days:
        if len(day) < 2:
            output.append(None)
        else:
            output.append(max(day)-min(day))
            
    return output