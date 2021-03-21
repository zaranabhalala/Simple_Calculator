def addition(a, b):
    return a + b

def subtraction(a, b):
    return b - a

def multiplication(a, b):
    return a * b

def division(a, b):
    c = round(b/a, 9)
    return c

def square(a):
    return a * a

def square_root(a):
    return round(a**(1/2), 8)

class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = addition(a, b)
        return self.result

    def subtract(self, a, b):
        self.result = subtraction(a, b)
        return self.result

    def multiply(self, a, b):
        self.result = multiplication(a, b)
        return self.result

    def divide(self, a, b):
        self.result = division(a, b)
        return self.result

    def square(self, a):
        self.result = square(a)
        return self.result

    def square_root(self, a):
        self.result = square_root(a)
        return self.result
