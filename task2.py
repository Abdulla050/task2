from abc import ABC, abstractmethod

class Number(ABC):
    def __init__(self, value):
        self.value = value

    @abstractmethod
    def __add__(self, other):
        pass

    @abstractmethod
    def __mul__(self, other):
        pass

    @abstractmethod
    def __gt__(self, other):
        pass

    @abstractmethod
    def __lt__(self, other):
        pass

    def showValue(self):
        return self.value

class IntegerNumber(Number):
    def __add__(self, other):
        if isinstance(other, Number):
            return self.value + other.value

    def __mul__(self, other):
        if isinstance(other, Number):
            return self.value * other.value

    def __gt__(self, other):
        if isinstance(other, Number):
            return self.value > other.value

    def __lt__(self, other):
        if isinstance(other, Number):
            return self.value < other.value

number_1 = IntegerNumber(14)
number_2 = IntegerNumber(66)

result_sum = number_1 + number_2
result_mul = number_1 * number_2
result_gt = number_1 > number_2
result_lt = number_1 < number_2

print("Sum:", result_sum)
print("Product:", result_mul)
print("Greater Than:", result_gt)
print("Less Than:", result_lt)
print("Number 1 Value:", number_1.showValue())
