def p(n):#print简化
    print(n)
    
def tpt(n=0):#time.process_time
    from time import process_time
    if n==0:
        p(process_time())
    elif n==1:
        return process_time()

def jstrToList(n):#str转list
    lst=[i for i in n]#列表解析式
    return lst

def jstrTofloat(n):#str转float小数
    if "." in n:
        from unicodedata import decimal
        from decimal import Decimal
        from decimal import getcontext
        li=jstrToList(n)
        place_dian=li.index('.')
        xiaoshuwei=len(li)-place_dian-1
        work_context = getcontext()
        work_context.prec = xiaoshuwei
        return Decimal(n)
    else:
        return float(n)

def calplist(n):#生成字母表
    alp="abcdefghijklmnopqrstuvwxyz"
    if n==1:
        return jstrToList(alp)
    elif n==2:
        return jstrToList(alp.upper())
    elif n==3:
        lst=[]
        for i in alp:
            lst.append(i.upper())
            lst.append(i.lower())
        return lst

def fd(a,b,xiaoshuwei):#forcediv,强制除法V3.0(被decimal秒杀呜呜呜)
    y=xiaoshuwei
    op=""
    tmp=a//b
    op+=str(tmp)
    if tmp*b!=a:
        op+="."
        nowlen=0
        while nowlen<y:
            a=a-tmp*b
            a=str(a)+"0"
            a=int(a)
            tmp=a//b
            op+=str(tmp)
            nowlen+=1
        while op[len(op)-1]=="0":
            op=op[:len(op)-1]
        if op[len(op)-1]==".":
            op=op[:len(op)-1]
    op=jstrTofloat(op)
    return op

def divanre(a,b):#商和余数
    a1=a//b
    a2=a-a1*b
    return a1,a2

def wait(n):#等待n毫秒
    from time import sleep
    sleep(n/1000)

def isprime(a):#是否为质数
    isp=False
    if a%6==1 or a%6==5:
        isp=True
        from math import sqrt
        fin=sqrt(a)
        fin=int(fin)
        for i in range(3,fin+1,2):
            if a%i==0:
                isp=False
                break
    elif a==2 or a==3:
        return True
    if isp==True and a>1 and a==int(a):
        return True
    else:
        return False

def dcopy(info):#深复制
    from copy import deepcopy
    op=deepcopy(info)
    return op

def readlastline(fname):#查看文件最后一行（知乎上抄的）
    with open(fname, 'rb') as f:  # 打开文件
    # 在文本文件中，没有使用b模式选项打开的文件，只允许从文件头开始,只能seek(offset,0)
        offset = -50  # 设置偏移量
        while True:
            f.seek(offset, 2)  # seek(offset, 2)表示文件指针：从文件末尾(2)开始向前50个字符(-50)
            lines = f.readlines()  # 读取文件指针范围内所有行
            if len(lines) >= 2:  # 判断是否最后至少有两行，这样保证了最后一行是完整的
                last_line = lines[-1]  # 取最后一行
                break
            offset *= 2
        return last_line.decode()

def gcd(a,b):#最大公约数
    x1=max(a,b)
    x2=min(a,b)
    while x2:
        x1,x2=x2,divanre(x1,x2)[1]
    return x1

def lcm(a,b):#最小公倍数
    gcdn=gcd(a,b)
    answer=fd(a*b,gcdn,0)
    return answer

def factorialSorts(num):#全部阶乘排序
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

if __name__=='__main__':#检测区
    p(
        
    )