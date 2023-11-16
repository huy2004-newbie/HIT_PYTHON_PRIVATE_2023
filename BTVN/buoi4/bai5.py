l = [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]
l1 = []
for number in l:
    if type(number) != int:
        for a in number:
            l1.append(a)
    else:
        l1.append(number)

print(l1)