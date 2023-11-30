import math

def read_file(file_path):
    """
    Đọc tọa độ của 2 điểm từ tệp văn bản

    Parameters:
    file_path (str): Đường dẫn đến tệp văn bản chứa tọa độ

    Returns:
    tuple: Tọa độ của điểm A và B dưới dạng tuple
    """
    with open(file_path, 'r') as file:
        list = file.read().split()
        # Tìm vị trí của điểm A và B trong danh sách
        index_a = list.index('A')
        index_b = list.index('B')
        
        # Lấy tọa độ của điểm A và B
        A = (float(list[index_a + 1]), float(list[index_a + 2]))
        B = (float(list[index_b + 1]), float(list[index_b + 2]))

    return A, B

def calculate_distance(A, B):
    """
    Tính khoảng cách giữa hai điểm trên mặt phẳng tọa độ Oxy.

    Parameters:
    A (tuple): Tọa độ của điểm A.
    B (tuple): Tọa độ của điểm B.

    Returns:
    float: Khoảng cách giữa hai điểm (làm tròn đến 2 chữ số thập phân).
    """
    khoang_Cach = math.sqrt((B[0] - A[0])**2 + (B[1] - A[1])**2)
    return round(khoang_Cach, 2)

def write_output(file_path, A, B, khoang_Cach):
    """
    Ghi kết quả vào tệp văn bản.

    Parameters:
    file_path (str): Đường dẫn đến tệp văn bản output.txt.
    A (tuple): Tọa độ của điểm A.
    B (tuple): Tọa độ của điểm B.
    khoang_Cach (float): Khoảng cách giữa hai điểm.

    Returns:
    None
    """
    with open(file_path, 'w') as file:
        file.write(f"A{A} B{B} AB = {khoang_Cach}")

# Đường dẫn của tệp input và output
input_file_path = 'input.txt'
output_file_path = 'output.txt'

# Đọc tọa độ từ tệp input.txt
A, B = read_file(input_file_path)

# Tính khoảng cách AB
khoang_Cach = calculate_distance(A, B)

# Ghi kết quả vào tệp output.txt
write_output(output_file_path, A, B, khoang_Cach)