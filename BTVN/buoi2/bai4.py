a = 16
count = a.bit_length()
print(f'Số bit cần để biểu diễn {a}: {count}')
attributes = list(dir(a))
print("Danh sách thuộc tính và phương thức của a:")
for z in attributes:
    print(z)