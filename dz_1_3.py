for i in range(1, 101):
    fraza = ""
    if i <= 14 and i >= 11:
        fraza = "procentov"
    elif i % 10 == 1:
        fraza = "procent"
    elif i % 10 >= 2 and i % 10 <= 4:
        fraza = "procenta"
    else:
        fraza = "procentov"
    print(i, fraza)