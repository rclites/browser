bought = []
read = []

for _i in range(int(input())):
    action = input()
    if 'BUY' in action:
        book_name = action[4:]
        bought.append(book_name)
    else:
        read.append(bought.pop())
for i in read:
    print(i)