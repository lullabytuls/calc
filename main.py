stack=[]
operators=[]
final=[]
includes=False
index=0
val=1
cont=0
hold=0
enter=True
first=True
finish=True
stop1=False
add=False
result=0
none=False
notOp=False
fattempt=False
operation="((2+4)*(4/2))"
length=len(operation)

for char in operation:
    index=index+1 
    print(char)
    if char in "0123456789":
        if first==True:
            val=int(char)
            print(val)
            first=False
            notOp=True 
        elif first==False:
            val=val*10+int(char)
            notOp=True
        if index==length:
            first=True
            final.append(val)
            val=1
    elif char in "+-*/()":
        if notOp==True:
            first=True
            final.append(val)
            val=1
        if len(operators)==0:
            notOp=False
            print("aaaaaa")
            operators.append(char)
        elif len(operators)>0:
            notOp=False
            r=len(operators)
            if char=="*" or char=="/":
                if operators[r-1]=="+" or operators[r-1]=="-" or operators[r-1]=="(":
                    operators.append(char) 
                elif operators[r-1]=="*" or operators[r-1]=="/":
                    i=r-1
                    while i!=0:
                        if operators[i]=="(":
                            includes=true
                    if includes==true:
                        operators.append(char)
                    else:
                        i=r-1
                        while i!=0:
                            if operators[i]=="*" or operators[i]=="/":
                                final.append(operators[i])
                                operators.pop(i)
                            elif operators[i]=="+" or operators[i]=="-":
                                break
                            i=i-1
                        operators.append(char)
            elif char=="+" or char=="-":
                if operators[r-1]=="+" or operators[r-1]=="-" or operators[r-1]=="(" or operators[r-1]=="*" or operator[r-1]=="/":
                    i=r-1
                    while i!=0:
                        if operators[i]=="(":
                            includes=True
                    if includes==True:
                        operators.append(char)
                    else:
                        i=r-1
                        while i!=0:
                            if operators[i]=="+" or operators[i]=="-" or operators[i]=="*" or operators[i]=="/":
                                final.append(operators[i])
                                operators.pop(i)
                            i=i-1
                        operators.append(char)
                        includes=False
            elif char=="(":
                operators.append(char)
            elif char==")":
                i=r-1
                while i!=-1:
                    if operators[i]=="(":
                        hold=i
                        break
                    i=i-1
                i=r-1
                while i!=hold-1:
                    if operators[i]!="(":
                        final.append(operators[i])
                        operators.pop(i)
                    elif operators[i]=="(":
                        operators.pop()
                        break
                    i=i-1

if finish==True: #op boşaltma
    ran=len(operators)
    for i in range(ran):
        a=operators.pop()
        final.append(a)           

def add(result,z,k):
    result+=z+k
    return result
def subtract(result,z,k):
    result-=k-z
    return result
def multiply(result,z,k):
    result=z*k
    return result
def divide(result,z,k):
    result=z/k
    return result

print(final)

one=True
i=0                    
l=len(final)
while i<l:
    if final[i]=="+" or final[i]=="-" or final[i]=="*" or final[i]=="/":
        main=final[i]
        if one==True:
            if main=="+":
                result+=add(result,int(final[i-1]), int(final[i-2]))
            elif main=="-":
                result+=subtract(result,int(final[i-1]), int(final[i-2]))
            elif main=="*":
                result+=multiply(result,int(final[i-1]), int(final[i-2]))
            elif main=="/":
                result+=divide(result,int(final[i-2]), int(final[i-1]))
                print(result)
            final.pop(i)
            final.pop(i-1)
            final.pop(i-2)
            i=i-3
            l=len(final)
            one=False
        elif one==False:
            if main=="+":
                result=add(result,result, final[i-1])
            elif main=="-":
                result-=subtract(result,result, final[i-1])
                print(result)
            elif main=="*":
                result=multiply(result,result, final[i-1])
            elif main=="/":
                result=divide(result,final[i-1], result)
            final.pop(i)
            final.pop(i-1)
            print(i)
            i=i-2
            print(i)
            l=len(final)
    i=i+1

    

print(result)
print(eval(operation))
        













    