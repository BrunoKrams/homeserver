
class DigitSplitter:

    def __init__(self, number:int):
        self.number = number

    def get_nth_digit(self, index:int):
        tmp = 10**index
        return (self.number % (tmp*10)) // tmp
