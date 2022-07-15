# def function(f_name, age):
#     name = f_name.title()
#     age = age
#     print(f"your name is {name} and your age is {age}")
#
#
# f_name = input("enter your name : ")
# age = int(input("enter your age : "))
# function(f_name, age)

# --------- above is a function -----------
# -------- this is a leap year program ------------
from datetime import date
year = int(input("Enter the leap year : "))
user = input("if you try to calculate your age please enter : yes / no\n")

today = date.today()
if user == "yes":
    print(f"the current date is : {today}")
    print("please weight program is executing ->\n")

    birth_year = int(input("enter your year : "))
    birth_month = int(input("enter your month : "))
    birth_date = int(input("enter your date : "))

    # ------------------------
    current_year = int(input("enter current year : "))
    current_month = int(input("enter current month : "))
    current_date = int(input("enter current date : "))

    month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if birth_date > current_date:
        current_month = current_month - 1
        current_date = current_date + month[birth_month - 1]
    if birth_month > current_month:
        current_year = current_year - 1
        current_month = current_month + 12

    # ----------calculate date, month, year
    calculated_date = current_date - birth_date
    calculated_month = current_month - birth_month
    calculated_year = current_year - birth_year

    # print present age
    print("Present Age")
    print(f"Years: {calculated_year} Months: {calculated_month} Days: {calculated_date}\n\n")
    print(f"{year} is leap year")

    # if year % 4 == 0 and year % 100 != 0:
    #     print(f"this is a leap year : {year}")
    # elif year % 400 == 0 and year % 100 == 0:
    #     print(f"this is a leap year : {year}")
    # else:
    #     print(f"this is a not leap year : {year}")

    # ---------------------------------------------------
if user == "yes":
    if year % 4 == 0 and year % 100 != 0:
        print(f"this is a leap year : {year}")
    elif year % 400 == 0 and year % 100 == 0:
        print(f"this is a leap year : {year}")
    else:
        print(f"this is a not leap year : {year}")

elif user == "no":
    if year % 4 == 0 and year % 100 != 0:
        print(f"this is a leap year : {year}")
    elif year % 400 == 0 and year % 100 == 0:
        print(f"this is a leap year : {year}")
    else:
        print(f"this is a not leap year : {year}")
else:
    print("invalid input")
