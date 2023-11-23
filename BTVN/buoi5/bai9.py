import random
n = 0
while(n < 10 or n > 100000):
    n = int(input("Nhập số lượng:"))
sinhVien = dict()
tenNganh = ["CNTT", "KHMT", "KTPM", "HTTT"]
maSinhVien_list = []    # lưu mã sinh viên để không cho người dùng nhập trùng
for i in range(n):
    key = 'Account' + str(i+1)
    print(key)
    sinhVien[key] = dict()
    maSinhVien = 0
    if(i == 0):    # lấy mã sinh viên đầu tiên vào trong maSinhVien_list
        while(maSinhVien < 1000000000 or maSinhVien > 10000000000):
            maSinhVien = int(input("Nhập mã sinh viên:"))
            maSinhVien_list.append(maSinhVien)
    if(i != 0):
        # sau khi đã có một phần tử trong maSinhVien_list thì không cho người dùng nhập msv đã có
        while(maSinhVien < 1000000000 or maSinhVien > 10000000000 or maSinhVien in maSinhVien_list):
            maSinhVien = int(input("Nhập mã sinh viên:"))
            maSinhVien_list.append(maSinhVien)        
    sinhVien[key]['Username'] = maSinhVien 
    pass_Word = random.choice(tenNganh) + str(maSinhVien)
    sinhVien[key]['Password'] = pass_Word
print(sinhVien)