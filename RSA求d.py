# fn = (p-1)*(q-1)
# d*e - fn*k = 1

def d(e,fn):
    p = int(input("请输入p："))
    q = int(input("请输入q："))
    e = int(input("请输入e："))
    fn = (p-1) * (q-1)
    k = 1
    while True:
        if ((fn*k)+1)%e == 0:
            (d,m)=divmod(fn*k+1,e)
            return d
        k+=1

print("d:",d(1,2))

#IPO 模式
