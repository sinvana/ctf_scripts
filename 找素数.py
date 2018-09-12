x = [367]
for i in range(1,1000):
    a = 367+186*i
#    print(a)
    for j in range(2,a):
        if (a%j) == 0:
            break    
    else:
        x.append(a)

print(x[150])
