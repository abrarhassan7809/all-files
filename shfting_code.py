list1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
         'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
         'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
         'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("type 'encode' to encrypt, type 'decode' to decrypt : ")
user_msg = input("type your message : ").lower()
shift = int(input("type the shift number : "))


def encode(user_message, shift_amount):
    final_msg = ""
    for x in user_message:
        y = list1.index(x)
        new_y = y + shift_amount
        final_msg += list1[new_y]
    print(f"the value is : {final_msg}")


def decode(final_msg, shift_amount):
    last_msg = ""
    for x in final_msg:
        y = list1.index(x)
        new_y = y - shift_amount
        last_msg += list1[new_y]
    print(f"the value is : {last_msg}")


if direction == "encode":
    encode(user_message=user_msg, shift_amount=shift)
elif direction == "decode":
    decode(final_msg=user_msg, shift_amount=shift)
else:
    print("invalid input")
