for i in range(1, 21, 2):
    print(i, end=' ')
print()
for i in range(0, 101, 10):
    print(i, end=' ')
print()
for i in range(0, 20):
    print(20 - i, end=' ')
print()

number = int(input("Number of stars: "))
for i in range(number):
    print("*", end='')
print()
for i in range(number):
    for j in range(i + 1):
        print("*", end='')
    print()
