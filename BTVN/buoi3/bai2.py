n = int(input())
m = int(input())
for i in range(n):
    a = int(input())
    c = a
    b = 0
    for j in range(m):
        b += a%(10)*10**(m-1-j)
        a //= 10
    b += a*(10**m)
    print(f'Dao nguoc {m} so cuoi cua {c} la:', b)
