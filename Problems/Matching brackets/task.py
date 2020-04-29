brackets = []
for char in input():
    if char == '(':
        brackets.append(char)
    if char == ')':
        try:
            brackets.pop()
        except IndexError:
            brackets.append(char)
if brackets:
    print('ERROR')
else:
    print('OK')