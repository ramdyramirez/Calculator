import os
import re

from functools import reduce


def greetings():
    os.system('clear')
    print("\t**********************************************")
    print("\t***  String Calculator  ***")
    print("\t**********************************************")

def Add(stringNumbers):
    negatives = re.findall(r'[-][0-9]+', stringNumbers)

    if len(negatives):
        values = ",".join(str(value) for value in negatives)
        raise Exception("Negatives not allowed %s" % values)

    if stringNumbers[0:2] == '//':
        list = formating_custom_delimiter(stringNumbers)
    else:
        list = formating_comma_delimiter(stringNumbers)
    list = map(to_int, list)
    return reduce(add, list)

def to_int(value):
    array = re.findall(r'[+]?[0-9]+', value)
    number = int(array[0])
    return number if number < 1000 else 0

def add(left, right):
    return left + right

def formating_custom_delimiter(stringNumbers):
    delimiter = stringNumbers[2]
    substr = stringNumbers[4:]
    return substr.split(delimiter)

def formating_comma_delimiter(stringNumbers):
    return stringNumbers.split(',')


### MAIN PROGRAM ###

if __name__ == "__main__":
    greetings()
    stringNumbers = input("\nEnter the string of numbers: ")
    try:
        print(Add(stringNumbers))
    except Exception as exc:
        print(exc)
