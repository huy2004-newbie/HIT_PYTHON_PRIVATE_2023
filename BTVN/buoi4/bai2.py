n = int(input())
l = list(map(int, input().split()))
l1 = []
for number in l:
    a = number % 10 
    if a in [1,3,5,7,9]:
        l1.append(number)
print(len(l1))
for x in l1:
    print(x,end=" ")