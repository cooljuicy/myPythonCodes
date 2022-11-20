def factorialSorts(num):
    def getPermutation(n, k,factorial):
        an=[]
        res=[i-1 for i in range(n+1)]
        while n:
            factorial/=n
            kshang=int(k//factorial)
            k=k%factorial
            if k==0:k=factorial
            else:kshang+=1
            an+=str(res[kshang])
            res.pop(kshang)
            n-=1
        return ''.join(an)
    a=1
    for j in range(2,num+1):a*=j
    lst=[]
    for i in range(1,a+1):
        lst.append(str(getPermutation(num,i,a)))
    return lst