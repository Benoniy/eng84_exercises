

xmas_list = []
print("HO HO HO! What do you want for Christmas?")

user_input = ""
while True:
    user_input = input()

    if user_input.lower().count("exit") > 0:
        break

    xmas_list.append(user_input)
    print("What else would you like?")

count = 1
for item in xmas_list:
    print(f"{count}. {item.upper()}")
    count += 1
