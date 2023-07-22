import random
dict = {
    "momo": 'MOMO',
    "zozo": 'ZOZO'
}

for _ in dict.values():
    print(_)

print(random.randrange(33000, 36000))
print(random.randrange(33000, 36000))
print(random.randrange(33000, 36000))
print(random.randrange(33000, 36000))

counter = 0
for i in range(10000000):
    if random.randrange(0, 3,1) > 0:
        counter += 1
print(counter)