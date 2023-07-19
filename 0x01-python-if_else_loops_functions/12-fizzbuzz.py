#!/usr/bin/python3
"""
Print the numbers 1 to 100 separated by space
    For multiples of three print Fizz instead of the number
    For multiples of five print Buzz
    For numbers which are both multiple of three and five print FizzBuzz
"""


def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("{} ".format("FizzBuzz"), end="")
        elif i % 5 == 0:
            print("{} ".format("Buzz"), end="")
        elif i % 3 == 0:
            print("{} ".format("Fizz"), end="")
        else:
            print("{} ".format(i), end="")
