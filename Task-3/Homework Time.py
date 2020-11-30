N = int(input())

a = []
for i in range(N):
    a.append(int(input()))

F = []
F.append(1)
F.append(2)
F.append(3)

for i in range(1000000):
    if(i > 2):
        F.append((F[i-1]+F[i-2]+F[i-3])%(pow(10, 9) + 7))

for i in range(N):
    str_ = str(F[a[i]-1])
    rev_str = str_[::-1]
    rev_int = int(rev_str)
    print(rev_int)