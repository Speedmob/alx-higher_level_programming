#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print('Last digit of', number, end='')
num = number % 10
if number < 0:
    num = ((-1 * number) % 10) * -1
if num == 0:
    print(' is', num, 'and is 0')
elif num > 5:
    print(' is', num, 'and is greater than 5')
else:
    print(' is', num, 'and is less than 6 and not 0')
