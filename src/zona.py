import random

firstnumber = random.randint(0, 1000000000)
secondnumber = random.randint(0, 1000000000)

multiplayer = 0

if firstnumber < 1000000000 * 0.06:
    multiplayer = 1.00
else:
    multiplayer = 1000000000 / secondnumber

print(multiplayer)
