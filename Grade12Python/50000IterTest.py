def collatz(number):
    count = 0
    while (number != 1):
        count += 1
        if ((number % 2) == 0):
            number = number / 2
        else:
            number = (number * 3) + 1
    return count

for i in range(1, 50000):
    print collatz(i)