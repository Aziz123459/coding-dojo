def Countdown(a):
    for i in range (a,-1,-1):
        print (i)
print(Countdown(5))
def PrintandReturn(a,b):
    print (a)
    return (b)
print(PrintandReturn(2,3)) 

def firstpluslength(list):
    a=list[0]+len(list)
    return a
print(firstpluslength([1,2,3,4,5]))




def ValuesGreaterthanSecond(list):
    count=0
    new_list=[]
    for i in range (len(list)):
        if list[1]<list[i]:
            count=count+1
            new_list.append(list[i])
    print(count)
    return new_list
print(ValuesGreaterthanSecond([5,2,3,2,1,4]))

def ThisLength_ThatValue(a,b):
    list=[]
    for i in range(a):
        if i <a:
            list.append(b)
    return list
print(ThisLength_ThatValue(4,7))