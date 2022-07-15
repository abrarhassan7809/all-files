import menu as menu
import tabel as tabel
# from prettytable import PrettyTable
#
# table = PrettyTable()
# table.add_column("pokemon name",["pikachu", "squirrel", "charmander"])
# table.add_column("type", ["electric", "water", "fire"])
# table.align = "l"
# print(table)

# -----------------------------


def latte():
    pro_list = {"milk is": "100ml",
                "water is": "150ml",
                "coffee is": "100ml"
                }
    return pro_list


class Coffee_Machine:
    def Menu(self):
        serve = {"latte" : "$30",
                 "espresso": "$50",
                 "cappuccino": "$60"
                 }
        return serve

    def latte(self):
        pro_list = {"milk is": "100ml",
                    "water is": "150ml",
                    "coffee is": "100ml"
                    }
        return pro_list

    def latte(self):
        pro_list = {"milk is": "100ml",
                    "water is": "150ml",
                    "coffee is": "100ml"
                    }
        return pro_list


obj = Coffee_Machine()
is_on = True
while is_on:
    choice = input("what would you like : ")
    if choice == "off":
        is_on = False
    elif choice == "menu":
        print(obj.Menu())
    elif choice == "latte":
        payment = input(input("please enter $30 : "))
        if payment == 30:
            print(latte())
    elif choice == "espresso":
        payment = input(input("please enter $50 : "))
        if payment == 50:
            print("milk is : 150ml")
            print("water is : 100ml")
            print("coffee is : 150ml")
        else:
            print("invalid espresso")
    elif choice == "cappuccino":
        payment = input(input("please enter $60 : $"))
        if payment == 60:
            print("milk is : 200ml")
            print("water is : 100ml")
            print("coffee is : 200ml")
        else:
            print("invalid cappuccino")

