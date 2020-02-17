a = list(map(int , input().split()))
data = 0

for i in range (len(a)) :
    if a[i] > 0:
        data += 1
    else :
        break

print (data)

