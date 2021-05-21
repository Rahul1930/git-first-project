def mod_pow(x,y,M):
    if (y==0):
        return 0
    elif (y%2==0):
        res=pow(x,y/2)%M
        return (res * res)%M
    else:
        return (((x%M)*pow(x,y-1)%M)%M)
p=mod_pow(2,3,5)
print(p)
