duration = int(input("duration = "))

m = duration // 60
s = duration % 60
h = m // 60
m = m % 60
d = h // 24
h = h % 24

if(duration >= 86400):
    print("days: ", d)
    print("hours: ", h)
    print("minutes: ", m)
    print("seconds: ", s)
elif(duration >= 3600):
    print("hours: ", h)
    print("minutes: ", m)
    print("seconds: ", s)
elif(duration >= 60):
    print("minutes: ", m)
    print("seconds: ", s)
elif(duration < 60):
    print("seconds: ", duration)
