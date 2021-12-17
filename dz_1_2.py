spisok = list()
sum = 0
for i in range(10001):
    if i % 2 == 1:
        spisok.append(i*i*i)
for element in spisok:
    temp = str(element)
    x = 0
    for i in temp:
        x += int(i)
    if x % 7 == 0:
        sum += x

for element in spisok:
    element += 17
    temp = str(element)
    x = 0
    for i in temp:
        x += int(i)
    if x % 7 == 0:
        sum += x

print(sum)