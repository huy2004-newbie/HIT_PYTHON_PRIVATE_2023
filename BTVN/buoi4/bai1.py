dd, mm, yyyy = map(int, input().split("/"))

check_hop_le = not (1 <= dd <= 31 and 1 <= mm <= 12 and yyyy >= 1000)

while(check_hop_le):
    print("Xin moi nhap lai")
    dd, mm, yyyy = map(int, input().split())

# Kiem tra nam nhuan
check_nam = False
if yyyy % 4 == 0 & yyyy % 100 != 0:
    check_nam = True

# Kiem tra thang 2
check_t2 = False
if mm == 2:
    if check_nam:
        check_t2 = dd>29
    else:
        check_t2 = dd>28

# kiem tra nhung thang co 30 ngay va 31 ngay
check_thang_31ngay = False
check_thang_30ngay = False
if mm!=2:
    if mm in [1,3,5,7,8,10,12]:
        check_thang_31ngay = not(True)
    else:
        check_thang_30ngay = not (dd == 31)

Check_ngay_hop_le = check_thang_31ngay or check_thang_30ngay

while(Check_ngay_hop_le or check_t2):
    print("Xin moi nhap lai")
    d, m, y = map(int, input().split())

if check_nam:
    ngay_trong_thang = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
else:
    ngay_trong_thang = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


dem_ngay = ngay_trong_thang[mm-1] - dd + 1

if mm != 12:
    for i in range(mm + 1, 13):
        dem_ngay += ngay_trong_thang[i-1]

print(dem_ngay)
