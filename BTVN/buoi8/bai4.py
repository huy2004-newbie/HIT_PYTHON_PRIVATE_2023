class Hiter:
    count = 0
    hiters = []
    def __init__(self) :
        Hiter.count += 1
        self.id = Hiter.count
        Hiter.hiters.append(self)
        
    def nhap(self):
        print("Nhập thành viên: ")
        self.ten = input("Nhập tên: ")
        self.tuoi = int(input("Nhập tuổi: "))
        self.gen = input("Nhập gen: ")
        
    def __str__(self):
        return f'ID: {self.id} || Tên: {self.ten} || Tuổi: {self.tuoi} || Gen: {self.gen}'
    
    @staticmethod
    def danhSach():
        for x in Hiter.hiters:
            print(x)


class Ban:
    def __init__(self, idBan, tenBan, truongBan: Hiter, thanhVien:list):
        self.idBan = idBan
        self.tenBan = tenBan
        self.truongBan = truongBan
        self.thanhVien = thanhVien
        
    def nhap():
        print("Nhập tt ban:")
        idBan = input("Nhập id ban: ")
        tenBan = input("Nhập tên ban: ")
        truongBan = input("Nhập truởng ban: ")
        thanhVien = []
        print("Nhập thông tin thành viên:")
        n = int(input("Nhập số luợng thành viên: "))
        for _ in range(n):
            hiter = Hiter()
            hiter.nhap()
            thanhVien.append(hiter)
        return Ban(idBan, tenBan, truongBan, thanhVien)
    
    def xuat(self):
        print("Ban: id: " + self.idBan + "\ntên: " + self.tenBan + "\ntruởng: " + str(self.truongBan) + "\nthành viên: " )
        for x in self.thanhVien:
            print(x)
        
    
    def __str__(self):
        return "Ban: id: " + self.idBan + "\ntên: " + self.tenBan + "\ntruởng: " + str(self.truongBan) + "\nthành viên: " + str(self.thanhVien)

    def dsHiter(self):
        print("Danh sách thành viên ban")
        for i in self.thanhVien:
            print(i)
            
    def addHiter(self):
        ten = input("Nhập tên hiter: ")
        tuoi = input("Nhập tuổi hiter: ")
        gen = input("Nhập gen hiter: ")
        for i in range(len(self.thanhVien)):
            if self.thanhVien[i].ten == ten:
                print("Đã ton tai")
                return
        hiter = Hiter(ten, tuoi, gen)
        self.thanhVien.append(hiter)
    def delHiter(self):
        ten = input("Nhập tên hiter xóa: ")
        for i in range(len(self.thanhVien)):
            if self.thanhVien[i].ten == ten:
                self.thanhVien.pop(i)
                print("Xóa thành công")
                return
        print("Ko tồn tại")
        
my_list = []
n = int(input("nhập số lượng: "))
for i in range(n):
    hiter = Hiter()
    hiter.nhap()
    my_list.append(hiter)
    
print("Xuất danh sách hiter")
for i in my_list:
    print(i)
    
    
m = int(input("nhập số lượng ban: "))
dsBan = []
for i in range(m):
    ban = Ban.nhap()
    dsBan.append(ban)
    
print("Xuat danh sach ban")
for i in dsBan:
    print(i.xuat())
