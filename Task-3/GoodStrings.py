N = int(input())
s = input()

ones = 0
zeros = 0

for i in range(N):
    if(s[i] == '0'):
        zeros += 1
    else:
        ones += 1

if(ones != zeros):
    print(1)
else:
    print(2)