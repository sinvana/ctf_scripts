list = [1,2,3,4]
lt=[]
for i in list:
    for j in list:
        for k in list:
            if i!=j and i!=k:
                if j!=k:
                    lt.append((i,j,k))
print(lt[15])
print(len(lt))
#print(lt)
input("请输入任意键推出")
