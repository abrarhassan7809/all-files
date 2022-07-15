num1 = 0
num2 = 1

for x in range(0, 20):
    if x == 0:
        print(num1)
    if x == 1:
        print(num2)
    total = num1 + num2
    num1 = num2
    num2 = total

    print(total)
