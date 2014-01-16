
total = 1000

for a in range(1,total/3+1):
    for b in range(a,total/2+1):
        c = total - a - b
        if (c > 0 and (a**2 + b**2 == c**2)):
            print(a*b*c)
        b+=1
    a+=1

