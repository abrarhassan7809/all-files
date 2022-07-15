
list1 = ["\U0001f600","\U0001f600","\U0001f600"]
list2 = ["\U0001f600","\U0001f600","\U0001f600"]
list3 = ["\U0001f600","\U0001f600","\U0001f600"]

total_list = [list1, list2, list3]
print(f"{list1}\n{list2}\n{list3}")

position = input("where is points : ")

horizontal = int(position[0])
vertical = int(position[1])

total_list[horizontal-1][vertical-1] = '\U0001F61C'

print(f"{list1}\n{list2}\n{list3}")
