dicTongKet = {
    '01' : 2.5,
    '02' : 2.1,
    '03' : 3.5,
    '04' : 0.5,
    '06' : 0.8,
    '07' : 0.9
}
keys = list(dicTongKet.keys())
dem = 0
for key in keys:
    tb = dicTongKet.get(key)
    if(tb >= 2.5 and tb <= 3.5):
        dem += 1
print("Sinh viên có điểm tổng kết trong đoạn [2.5, 3.5] là:", dem)


tb = 0
maSinhVien = keys[0]
while( tb <=0 or tb> 10 or  maSinhVien in keys):
    maSinhVien = str(input("Nhập mã sinh viên:"))
    tb = int(input("Nhập tbm:"))
dicTongKet[maSinhVien] = tb
print(dicTongKet)

keys = list(dicTongKet.keys())
for key in keys:
    diem = dicTongKet.get(key)
    if(diem < 2.0):
        del dicTongKet[key]
print(dicTongKet)
