import math
x1, y1, x2, y2, x3, y3 = map(int, input().split())
d12 = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
d13 = math.sqrt((x1 - x3)**2 + (y1 - y3)**2)
d23 = math.sqrt((x2 - x3)**2 + (y2 - y3)**2)
print(((d12+d23>d13 and d12*d23*d13 != 0)  and "Tam giac") or "Ko la tam giac")