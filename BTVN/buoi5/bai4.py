n = int(input("Nhap so luong phan tu trong mang: "))
a = []
for i in range(n):
    x = input(f"Nhap phan tu thu {i+1}: ")
    a.append(x)
b = tuple(a)
dem = 0 
print("Cac phan tu trong tuple:")
for x in b:
    print(x, end=" ")
    if (x.isdigit()):
        dem += 1
print("")
print("Trong b co", dem,"phan tu la so.")