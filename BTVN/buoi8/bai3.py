class Matrix:
    def __init__(self, n, m, value):
        self.n = n
        self.m = m
        self.value = [value[i:i+m] for i in range(0, len(value), m)]

    def __add__(self, other):
        result = []
        for i in range(self.n):
            row = []
            for j in range(self.m):
                row.append(self.value[i][j] + other.value[i][j])
            result.append(row)
        return result
    
    def __sub__(self, other):
        result = []
        for i in range(self.n):
            row = []
            for j in range(self.m):
                row.append(self.value[i][j] - other.value[i][j])
            result.append(row)
        return result
    
    def __mul__(self, other):
        if self.m != other.n:
            raise ValueError("Không thể nhân ma trận vì không thỏa mãn điều kiện")
        result = []
        for i in range(self.n):
            row = []
            for j in range(other.m):
                element = 0
                for k in range(self.m):
                    element += self.value[i][k] * other.value[k][j]
                row.append(element)
            result.append(row)
        return result
    
    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            result = []
            for i in range(self.n):
                row = []
                for j in range(self.m):
                    row.append(self.value[i][j] / other)
                result.append(row)
            return result
        else:
            raise TypeError("Không thể thực hiện phép chia")    

    def __eq__(self, other):
        if self.n != other.n or self.m != other.m:
            return False
        for i in range(self.n):
            for j in range(self.m):
                if self.value[i][j] != other.value[i][j]:
                    return False
        return True

matrix1 = Matrix(2, 2, [3, 2, -1, 1])
matrix2 = Matrix(2, 2, [-2, -2, 0, 1])



print("matrix1 + matrix2 = " , matrix1 + matrix2)
print("matrix1 - matrix2 = " , matrix1 - matrix2)
print("matrix1 * matrix2 = " , matrix1 * matrix2)
print("matrix1 / matrix2 = " , matrix1 / matrix2)
print("matrix1 = matrix2 " , matrix1 == matrix2)