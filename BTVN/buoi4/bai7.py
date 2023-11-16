l = list(input().split())
n = int(input())
while len(l) % n != 0:
    n = int(input())

size = len(l) // n
l2 = [l[i * size:(i + 1) * size] for i in range(n)]
print(l2)


    