for i in range(100,1000):
    n=len(str(i))
    if i==int(str(i)[0])**n+int(str(i)[1])**n+int(str(i)[2])**n:
        print(i)
