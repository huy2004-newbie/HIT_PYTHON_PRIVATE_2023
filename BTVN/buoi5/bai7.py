str_1 = input("Nhập xâu: ")  # Không cần chuyển đổi input thành str, vì input luôn trả về str
print(str_1)
list_1 = list(str_1)
i = 0
while i < len(list_1)-1:
    if list_1[i] == ' ':
        del list_1[i]
    else:
        i += 1

list_2 = []  # list lưu keys
list_2.append(list_1[0])
for x in list_1:
    if x not in list_2:
        list_2.append(x)

list_3 = []  # list lưu số lần xuất hiện
for key in list_2:
    dem = list_1.count(key)
    list_3.append(dem)

print(list_3)

dic = dict()
# thêm key và val vào dic
for i in range(len(list_2)):
    dic[list_2[i]] = list_3[i]

print(dic)