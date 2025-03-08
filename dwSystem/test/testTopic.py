import random

with open('random_numbers.txt', 'w') as file:
    for i in range(1000):
        num = random.randint(0, 1000)
        file.write(str(num) + ',')

with open('random_numbers.txt', 'r') as file:
    content = file.read()
    numbers = []
    for num in content.split(','):
        if num:
            numbers.append(int(num))
    sorted_numbers = sorted(numbers)
    for num in sorted_numbers:
        print(num)