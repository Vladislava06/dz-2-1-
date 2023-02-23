n = int(input())
count = 0
count1 = 0
for i in range(n):
    j = int(input())
    if j == 0:
        count += 1
    else:
        count1 += 1
if count1 > count:
    print(count)
else:
    print(count1)