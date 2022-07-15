print("it is loving score game : ")
your_name = input("please enter your name : ")
gf_name = input("please enter your gf name : ")

lover_combine = your_name + gf_name
lover_name = lover_combine.lower()

t = lover_name.count("t")
r = lover_name.count("r")
u = lover_name.count("u")
e = lover_name.count("e")

true = t+r+u+e

l = lover_name.count("l")
o = lover_name.count("o")
v = lover_name.count("v")
e = lover_name.count("e")

love = l+o+v+e

love_score = str(true) + str(love)
print(love_score)

if int(love_score) > 40:
    print(f"the score is 100 and your number is {love_score}")
    print("the weak chances of your love")
elif int(love_score) >= 50:
    print("the 50% chances of your love")
elif int(love_score) >= 60:
    print("the 70% chances of your love")
elif int(love_score) >= 80:
    print("the 90% chances of your love")
elif int(love_score) == 100:
    print("the 100% chances of your love")

