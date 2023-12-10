class Pycon:
    count = 0
    sum_age = 0
    def __init__(self) -> None:
        pass
    
    def nhap(self):
        Pycon.count += 1
        self.id = self.count
        self.hoTen = input("Họ tên: ")
        self.tuoi = int(input("Nhập tuổi: "))
        Pycon.sum_age += self.tuoi
        
    def __str__(self):
        return f'ID: {self.id} || Tên: {self.hoTen} || Tuổi: {self.tuoi}'
    
    @classmethod
    def averAge(cls):
        if cls.count == 0:
            return 0
        return cls.sum_age / cls.count
    
if __name__ == '__main__':
    n = int(input())
    pycons = []
    for i in range(n):
        p = Pycon()
        p.nhap()
        pycons.append(p)
    
    for pycon in pycons:
        print(pycon)
        
    print(Pycon.averAge())
    