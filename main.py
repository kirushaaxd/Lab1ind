from random import randint

array = []


def createArray(num):
    for i in range(0, num + 10):
        array.append(randint(5, num * 10))


createArray(17)
print(array)
