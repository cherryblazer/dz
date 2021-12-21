import random
def get_jokes(x):
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

    res = []

    for i in range(x):
        temp = nouns[random.randint(0, len(nouns)-1)] + " " + adverbs[random.randint(0, len(nouns)-1)] + " " + adjectives[random.randint(0, len(nouns)-1)]
        res.append(temp)
    return res

print(get_jokes(100))