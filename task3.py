a=int(input())
if a==11 or a==12 or a==13 or a==14 or a==111 or a==112 or a==113 or a==114:
    print(a,"лет")
elif a%10==1:
    print(a,"год")
elif a%10==2 or a%10==3 or a%10==4:
    print(a,"года")
else:
    print(a,"лет")
