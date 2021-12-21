def thesaurus(names):
    res = dict()
    for name in names:
        if(name[0] not in res.keys()):
            res[name[0]] = []
        res[name[0]].append(name)
    return res

print(thesaurus(["Иван", "Мария", "Петр", "Илья"]))