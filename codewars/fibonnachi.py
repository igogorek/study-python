__author__ = 'igogor'

def productFib(prod):
    (a, b) = (0, 1)
    while True:
        if a * b >= prod:
            return [a, b, a*b == prod]
        (a, b) = (b, a+b)


