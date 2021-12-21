def thesaurus_adv(names):
    res = dict()
    for name in names:
        if(name.split()[1][0] not in res.keys()):
            res[name.split()[1][0]] = dict()
            res[name.split()[1][0]][name.split()[0][0]] = list()
        if(name.split()[1][0] in res.keys()):
            if(name.split()[0][0] in res[name.split()[1][0]].keys()):
                res[name.split()[1][0]][name.split()[0][0]].append(name)
            if(name.split()[0][0] not in res[name.split()[1][0]].keys()):
                res[name.split()[1][0]][name.split()[0][0]] = list()
                res[name.split()[1][0]][name.split()[0][0]].append(name)
    return res

initial = thesaurus_adv(["Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"])
final = {}
keys = sorted(initial)
for i in keys:
    final[i] = initial[i]
print(final)