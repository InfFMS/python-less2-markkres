n=int(input())
for i in range(2,n+1):
    Prime=True
    for j in range(2,i):
        if i%j==0:
            Prime=False
    if Prime:
        print(i)
