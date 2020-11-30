N = int(input())

a = []
b = []

a_in = input().split(' ')
for i in range(N):
    a.append(int(a_in[i]))
    
b_in = input().split(' ')
for i in range(N):
    b.append(int(b_in[i]))
    
min_ = pow(10, 9) + 1
for i in range(N):
    rem = b[i]/a[i]
    if(min_ > int(rem)):
        min_ = int(rem)
        
print(min_)