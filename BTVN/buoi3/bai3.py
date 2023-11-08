n = int(input())
for i in range(n):
    Name = input()
    Test1 = float(input())
    Test2 = float(input())
    check = Test1 + Test2
    print(i+1, Name, end=" ")
    if check < 100:
        print("Yếu")
    elif check < 150:
        print("Khá")
    elif check < 190:
        print("Giỏi")
    else:
        print("Xuất sắc")