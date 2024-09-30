a,b=map(int,input().split())
c,d=map(int,input().split())
if d<a or c>b:
    print("Пустое множество")
elif d==a:
    print(a)
elif c==b:
    print(b)
else:
    if c<a and d>b:
        print("[",a,",",b,"]")
    elif c<a and d<b:
        print("[",a,",",d,"]")
    elif c>a and d<b:
        print("[",c,",",d,"]")
    elif c>a and d>b:
        print("[",c,",",b,"]")
