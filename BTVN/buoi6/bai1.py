def MyMultiple(*agr:int) -> float:
    """"
    Hàm tính tích các số truyền vào
    *agr truyền tham số chưa biết trước số lượng 
    Hàm trả về tích các số truyền vào
    """
    result = 1.0
    for x in agr:
        result *= x
    return result

print(MyMultiple(1,2,3,4))
print(MyMultiple(5,5,5))
print(MyMultiple(1.2,5))