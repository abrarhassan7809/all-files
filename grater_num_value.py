import random
print("Sorry this is strong password generator ->")
number = ['1','2','3','4','5','6','7','8','9','0']
letter = ['a','b','c','d','e','f','g','h','i','j']
symbols = ['!','@','#','$','%','^','&','*','(',')']

ls_number = int(input("Enter any numbers form 0 to 9 : "))

ls_letter = int(input("Enter how much letter : "))

ls_symbols = int(input("Enter how much symbols : "))

before_password = []

for char in range(1, ls_number+1):
    before_password.append(random.choice(number))

for char in range(1, ls_letter+1):
    before_password.append(random.choice(letter))

for char in range(1, ls_symbols+1):
    before_password.append(random.choice(symbols))

random.shuffle(before_password)

print(f"Your new password is : {before_password}")

password = ""
for char in before_password:
    password += char
print(f"Your new password is : {password}")
