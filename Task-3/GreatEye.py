t = input()
t = int(t)

k = []
sent = []

for i in range(t):
    k.append(int(input()))
    sent.append(input().split(' '))

for i in range(t):
    sum = 0
    if(len(sent[i]) <= k[i]):
        print(-1)
    else:
        for j in range(len(sent[i][k[i]])):
            sum += ord(sent[i][k[i]][j])
        print(sum)