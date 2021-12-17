data = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

result = list()
for i in data:
    if(i.isnumeric()):
        result.append('"')
        if(int(i) < 10):
            result.append("0" + i)
        else:
            result.append(i)
        result.append('"')
    elif(i[0] == '-' or i[0] == '+'):
        result.append('"')
        if(int(i) < 10):
            x = i[0] + '0' + i[1]
            result.append(x)
        else:
            result.append(i)
        result.append('"')
    else:
        result.append(i)
print(*result)