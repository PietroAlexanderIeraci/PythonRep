class ExamException(Exception):
    pass

class Diff:
    def __init__(self, ratio = 1):
        self.ratio = ratio
        if type(ratio) != int and type(ratio) != float:
            raise ExamException('Ratio must be numeric type')
        if ratio <=0:
            raise ExamException('Ratio must be positive')
    def compute(self, elements):
        self.elements = elements
        output = []
        if not self.elements:
            raise ExamException('Invalid list')
        if type(self.elements) != list:
            raise ExamException('Invalid input, must be list type')
        if len(self.elements) == 1:
            raise ExamException('Invalid list')

        for i in self.elements:
            if type(i) != int and type(i) != float:
                raise ExamException('Invalid list')
        for i in range(len(self.elements)-1):
            output.append((self.elements[i+1]-self.elements[i])/self.ratio)
        return output