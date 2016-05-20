import random
import sys
import string
import datetime


def main():
    for i in range(5000):
        print ('('+areacode()+')'+' '+phonenumber()+"\t")


def areacode():
    keywords = ["510", "415", "208", "680", "910", "143", "213", "690", "462", "254", "612", "780", "760"]
    areacode = str(random.choice(keywords))

    return areacode

def phonenumber():
    keys = ["412-1412", "231-5124", "234-1565", "840-9014", "853-9182", "142-4132", "972-5124"]
    phonenumber = str(random.choice(keys))

    return phonenumber

if __name__ == '__main__':
    main()