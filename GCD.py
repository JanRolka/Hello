def GCD(a,b):
    while b!=a:
        if a>b:
            a=a-b
        else:
            a,b=b,a
            a=a-b 
    print(a)

GCD(900,150)