text = str(input("Nhap cac so cach nhau dau cach:"))
a = set(map(int, text.split()))
print(a)
l1 = []
kiemTra = 0
n = 0
for x in a:
    if(int(x) == 11):
        kiemTra += 1
    l1.append(x)
    n += 1
if kiemTra > 0:
    print("Da viet 11")
else:
    print("Sau khi them 11 vao:")
    a.add(11)    
print(a)
cap_so = ()
for i in range(n):
    for j in range(i+1, n):
        if(int(l1[i]) + int(l1[j]) == 11):
            print("cap so cong voi nhau bang 11 la:", l1[i], l1[j])
            cap_so += (l1[i], l1[j]) 
            
print("Tong cap so: ", sum(cap_so))