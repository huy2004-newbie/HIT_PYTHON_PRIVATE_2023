n = int(input("nhap n:"))
tapHop = set()
for i in range(n):
    gt = int(input())
    tapHop.add(gt)

l1 = list()
index = 0
for x in tapHop:
    l1.append(x)

l1.sort()
a = int(input("nhap dieu kien tong ko vuot qua cua tap con:"))
tong = 0
tapHopCon = set()
for i in range(n):
    if(tong + l1[i] <= a):
        tong += l1[i]
        tapHopCon.add(l1[i])
print("Tap hop con la:")
print(tapHopCon)
