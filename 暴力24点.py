from copy import deepcopy
from random import randint
from time import process_time
class Violent24:
    def findAllSorts_Monkey(n=4):
        out=[]
        shouldhave=1
        for i in range(2,n+1):
            shouldhave*=i
        while len(out)!=shouldhave:
            now=[]
            unused=[i for i in range(n)]
            for i in range(n):
                add=unused[randint(0,len(unused)-1)]
                now.append(add)
                unused.remove(add)
            if now not in out:
                out.append(now)       
        return out
    def seek_all(self,indexes,aim=24,sortsMode='monkey'):
        numbermy=0
        def notallequal(index,want=[4,4,4,4]):
            for i in range(len(index)):
                if index[i]!=want[i]:
                    return True
            return False
        def cheakAnswer(theTypeNow,operationsNow,aim=24):
            def calculate(a,b,operationType):
                if operationType==0:
                    return a+b
                elif operationType==1:
                    return a-b
                elif operationType==2:
                    return a*b
                elif operationType==3:
                    return a/b
            nowType=deepcopy(theTypeNow)
            for i in range(len(theTypeNow)-1):
                nowType[0]=calculate(nowType[0],nowType[1],operationsNow[i])
                nowType.pop(1)
            if nowType[0]==aim:
                return True
            else:
                return False
        numberlen=len(indexes)
        sorts=Violent24.findAllSorts_Monkey(numberlen)
        for j in range(len(sorts)):
            sortnow=sorts[j]
            typenow=[indexes[i] for i in sortnow]
            operations=[0 for i in range(numberlen-1)]
            want=[3 for i in range(numberlen-1)]
            while notallequal(operations,want):
                if cheakAnswer(typenow,operations,aim):
                    print(typenow)
                    print(operations)
                    numbermy+=1
                print(typenow)
                print(operations)
                operations[0]+=1
                for i in range(len(operations)):
                    if operations[i]>want[i]:
                        operations[i]=0
                        operations[i+1]+=1
                    else:
                        break
        return numbermy
    def seek_fuzzy(self,indexes,aim=24,sortsMode='monkey'):
        pass
a=Violent24()
print(a.seek_all([10,12,12,12]))