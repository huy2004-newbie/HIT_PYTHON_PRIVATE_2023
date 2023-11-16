import re

s = input()
number =  re.findall(r'-?\d+', s)
tong = sum(map(int, number))
print(tong)