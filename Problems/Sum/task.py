file = open('sums.txt', 'r', encoding='utf-8')
nums = file.readlines()
for line in nums:
    print(int(line.split(' ')[0]) + int(line.split(' ')[1]))
file.close()
