
target = 1000
added = 0 
for i in range(1,target):
    if (i % 3 == 0) or (i % 5 == 0):
        added += i

print(added)
