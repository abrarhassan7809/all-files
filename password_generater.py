import random

decision = input("are you sure to reset your password : ")
if decision == 'yes':

    # this is a list
    ls_number = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    ls_letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    ls_symbol = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

    # this is input space
    numbers = int(input("how many numbers : "))
    letters = int(input("how many letters : "))
    symbols = int(input("how many numbers : "))

    pass1 = []

    # its a loop
    for char in range(1, numbers+1):
        pass1 += random.choice(ls_number)
    for char in range(1, letters+1):
        pass1 += random.choice(ls_letter)
    for char in range(1, symbols+1):
        pass1 += random.choice(ls_symbol)

    # shuffling my loop
    random.shuffle(pass1)
    full_password = ""
    for char in pass1:
        full_password += char

    # its printing my loop
    print(f"your new password is : {full_password}")

# its else conditions
elif decision == 'no':
    print("ok as you wish")
else:
    print("invalid input")
