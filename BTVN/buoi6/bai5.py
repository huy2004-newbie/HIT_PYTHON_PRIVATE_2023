def ucln(n:int, m:int) -> int:
    """
    Hàm tìm ước chung nhỏ nhất
    
    Parameter:
    n, m: hai số nguyên
    
    return
    ước chung nhỏ nhất của n, m
    """
    
    while(n != m):
        if n > m:
            n = n - m
        else:
            m = m - n
    return n

def tinh_Tich(n : int) -> int:
    tu = 1
    mau = 1
    for i in range(n):
        tu *= int(input())
        mau *= int(input())
    a = ucln(tu, mau)
    return tu/a, mau/a

n = int(input())
tu, mau = tinh_Tich(n)
print(tu, mau)

# print(ucln(15, 140))