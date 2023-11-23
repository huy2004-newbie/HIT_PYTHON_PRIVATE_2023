n = int(input("Nhap so sv dien ban 1:"))
A = set()
for i in range(n):
    a = input()
    A.add(a)
print(A)

m = int(input("Nhap so sv dien ban 2:"))
B = set()
for i in range(m):
    b = input()
    B.add(b)
print(B)

print("\nRUN","\n")
giaoNhau = A&B    
if giaoNhau != set():
    print("SV dang ki ca 2 ban co MSV la:")
    for msv in giaoNhau:
        print(msv, end = " ")
else:
    print("Ko sv nao dk 2 ban")
print("")
hopNhau = (A - giaoNhau) | B
print("Danh sach msv cua 2 ban:")
for msv in hopNhau:
    print(msv, end = " ")
print("")
A_Hieu_B = A - B
if A_Hieu_B != set():
    print("SV dk ban 1 ma ko dk ban 2 la:")
    for msv in A_Hieu_B:
        print(msv, end = " ")
else:
    print("ko co SV dk ban 1 ma ko dk ban 2")
print("")
A_Khac_Biet_Doi_Xung_B = hopNhau - giaoNhau
if A_Khac_Biet_Doi_Xung_B != set():
    print("SV chi dk 1 ban co msv la:")
    for msv in A_Khac_Biet_Doi_Xung_B:
        print(msv, end = " ")    
else:
    print("ko co SV chi dk 1 ban")