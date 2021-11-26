list = ["pizza", "falafel", "carrot cake"]
myfriend_list = list[:]
print(myfriend_list)
icecream_friend = input("icecream?")
myfriend_list.append(icecream_friend)
for i in list:
    print(f"My: {i}")
for a in myfriend_list:
    print(f"My friend: {a}")

