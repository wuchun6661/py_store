print('100-999的所有水仙花数为：')
count = 0
for a in range(100,1000):
    if ((a%10)**3) + ((a//100)**3) + ((a%100-a%10)/10)**3 == a:
        count += 1
print(count,'个')
