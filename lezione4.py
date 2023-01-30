class ExamException(Exception):
    pass

class CSVFile:
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
            if elements[0] == 'Date':
                continue
            else:
                elements[1] = elements[1].replace('\n','')
                my_list.append(elements)
        return my_list
