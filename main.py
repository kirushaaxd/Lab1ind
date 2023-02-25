from random import randint

array = []


def createArray(num):
    array = [randint(5, num * 100) for i in range(0, num+10)]
    print(array)


createArray(17)
