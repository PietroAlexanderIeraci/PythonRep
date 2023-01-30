class ExamException(Exception):
    pass

class MovingAverage:
    def __init__(self, windowsize):
        self.windowsize = windowsize
        if type(self.windowsize) != int or self.windowsize <= 0:
            raise ExamException('Invalid window size')
        
    def compute(self, elements):
        self.elements = elements
        if type(elements) != list:
            raise ExamException('Invalid input, must be list type.')
        for i in elements:
            if type(i) != int and type(i) != float:
                raise ExamException('Invalid list, must contain only int or float type elements.')

        output = []
        start = 0
        finish = self.windowsize

        if finish > len(self.elements):
            raise ExamException('Window size too large for selected list')

        while finish <= len(self.elements):
            avg = 0
            for i in list(range(start,finish)):
                avg += self.elements[i]
            avg = avg/self.windowsize
            output.append(avg)
            start += 1
            finish += 1
        return output