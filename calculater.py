import os


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operation = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculater():

    num1 = float(input("enter first value : "))
    for symbol in operation:
        print(symbol)
    can_continue = True

    while can_continue:
        operator = input("enter the symbol : ")
        num2 = float(input("enter second value : "))

        calculation_func = operation[operator]
        ans = calculation_func(num1, num2)
        print(f"{num1} {operator} {num2} = {ans}")

        again_start = input(f"type 'y' to continue this calculation type 'again' to continue other calculation "
                            f"other wise 'n' : ")
        if again_start == "y":
            num1 = ans
        elif again_start == "again":
            calculater()
        else:
            print("game over")
            can_continue = False


calculater()
