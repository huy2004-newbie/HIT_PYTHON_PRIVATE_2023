def input_arr(n:int):
    """
    Nhập mảng có n số từ người dùng
    Input: size của arr
    Output: List
    """
    arr = []
    for i in range(n):
        arr.append(float(input()))
    return arr

def calculate_sum_until_position(arr, x):
    
    """
    Hàm tính tổng từ đầu đến vị trí x của list
    Input: List, x
    Output: Tổng 0->x của List 
    """
    if x<1 or x>len(arr):
        return "Ko hợp lệ"
    else:
        return sum(arr[:x])
    
n = int(input())
a = input_arr(n)
print("Nhập số lần: ", end="")
so_Lan = int(input())
for i in range(so_Lan):
    print("Nhập x: ", end="")
    print(calculate_sum_until_position(a, int(input())))