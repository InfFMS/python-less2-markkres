a,b=map(int,input().split())
c,d=map(int,input().split())
if abs(a-c)==abs(b-d) or a==c or b==d:
    print("YES")
else:
    print("NO")
