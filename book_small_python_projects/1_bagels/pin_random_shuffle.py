import random
numbers = list('0123456789')
random.shuffle(numbers)
pin = ''.join(numbers[:4])
print(pin)