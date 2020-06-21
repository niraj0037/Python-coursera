import re
x = open('regex_sum_368747.txt')
sum = 0
count = 0
for line in x:
    f = re.findall('[0-9]+', line)
    for num in f:
            count = count + 1
            sum = sum + int(num)

print('There are', count, 'values with a sum =', sum)