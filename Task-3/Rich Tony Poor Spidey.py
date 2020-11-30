t = int(input())

for i in range(t):
    in1 = input().split(' ')
    in2 = input().split(' ')
    
    n = int(in1[0])
    k = int(in1[1])
    
    mon = []
    for i in range(n):
        mon.append(int(in2[i]))
    
    max_ = -1
    prod = 1
    for i in range(n):
        prod *= mon[i]
    
    for i in range(n):
        spi_mon = (prod/mon[i])*(mon[i]-k)
        if(spi_mon > max_):
            max_ = spi_mon
    
    print(int(max_))