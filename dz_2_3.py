data = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
res = ""
for i in data:
    if(i.isnumeric()):
        res += ' "'
        if(int(i) < 10):
            res += ' ' + "0" + i
        else:
            res += ' ' + i
        res += ' ' + '"'
    elif(i[0] == '-' or i[0] == '+'):
        res += ' ' + '"'
        if(int(i) < 10):
            x = i[0] + '0' + i[1]
            res += ' '+x
        else:
            res += ' ' + i
        res += ' ' + '"'
    else:
        res += ' ' + i
print(res)