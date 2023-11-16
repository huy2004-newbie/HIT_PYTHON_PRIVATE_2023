n = int(input())
l = list(map(int, input().split()))
odd = 0
even = 0
for number in l:
    if number % 2 != 0:
        odd += number
    else:
        even += number
    
if odd > even:
    print("odd")
elif even > odd:
    print("even")
else:
    print("equal")