def chuyen_Vi_Ma_Tran(matrix):
    """
    In ra ma trận chuyển vị mà ko làm thay đổi ma trận ban đầu
    
    Intput: Truyền vào 1 ma trận kích thước bất kì
    
    Output: In ra ma trận chuyển vị
    """
    
    n = len(matrix)
    m = len(matrix[0])
    
    # in ra chuyen vi
    for j in range(m):
        for i in range(n):
            print(matrix[i][j], end=" ")    
        print("")
            
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
]

chuyen_Vi_Ma_Tran(matrix)