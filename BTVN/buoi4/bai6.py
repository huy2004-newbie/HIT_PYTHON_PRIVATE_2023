# l = list(map(int, input().split()))
l = [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
l.sort()
l1 = []
a = l[0]
l2 = []
for number in l:
    if number == a:
        l2.append(number)
    else:
        l1.append(l2)
        a = number
        l2 = []
        l2.append(number)
print(l1)
    