stack=[]
operators=[]
final=[]
index=0
val=1
cont=0
hold=0
enter=True
first=True
stop1=False
add=False
result=0

operation="15+3"
length=len(operation)

for char in operation: 
    if index>0 and cont!=index-1 and enter==True:
        cont+=1
        continue
    if char in "0123456789":
        enter=True
        while index<length-1:
            str=operation[index+1]
            if str.isdigit():
                if first==True:
                    val=int(operation[index])*10+int(operation[index+1])
                    first=False
                elif first==False:
                    val=val*10+int(operation[index+1])
            elif index+2==length:
                first=True
                final.append(val)
                val=1
                index=index+1
                break
            else:
                first=True
                final.append(val)
                val=1
                index=index+1
                break
            index=index+1
    elif char in "+-*/()":
        index=index+1
        enter=False
        if len(operators)==0:
            operators.append(char)
        elif len(operators)>0:
            r=len(operators)
            if char=="*" or char=="/":
                if operators(r-1)=="+" or operators(r-1)=="-" or operator(r-1)=="(":
                    operators.append(char) 
                elif operators(r-1)=="*" or operators(r-1)=="/":
                    i=r-1
                    while i!=0:
                        if operators[i]=="*" or operators[i]=="/":
                            final.append(operators[i])
                            operators.pop(i)
                        elif operators[i]=="+" or operators[i]=="-" or operators[i]=="(":
                            break
                        i=i-1
                    operators.append(char)
            elif char=="+" or char=="-":
                if operators(r-1)=="+" or operators(r-1)=="-" or operators(r-1)=="(" or operators(r-1)=="*" or operators(r-1)=="/":
                    i=r-1
                    while i!=0:
                        if operators[i]=="+" or operators[i]=="-" or operators[i]=="*" or operators[i]=="/":
                            final.append(operators[i])
                            operators.pop(i)
                        elif operators[i]=="(":
                            break
                        i=i-1
                        operators.append(char)
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
                    i=i-1
def add(result,i,j):
    result+=i+j
def subtract(result,i,j):
    result+=i-j
def multiply(result,i,j):
    result+=i*j
def divide(result,i,j):
    result+=i/j

one=True
i=0                    
l=len(final)
while i<l:
    if final[i]=="+" or final[i]=="-" or final[i]=="*" or final=="/":
        main=final[i]
        if one==True:
            if main=="+":
                add(result,final[i-1], final[i-2])
            elif main=="-":
                subtract(result,final[i-1], final[i-2])
            elif main=="*":
                multiply(result,final[i-1], final[i-2])
            elif main=="/":
                divide(result,final[i-1], final[i-2])
            final[i-1].pop()
            final[i-2].pop()
            final[i].pop()
            one=False
            j=i-2
            l=l-3
            while i!=l-1:
                final[j]=final[i+1]
                i+=1
                j=j+1
            i=-1
        elif one==False:
            if main=="+":
                add(result,result, final[i-1])
            elif main=="-":
                subtract(result,result, final[i-1])
            elif main=="*":
                multiply(result,result, final[i-1])
            elif main=="/":
                divide(result,result, final[i-1])
            final(i-1).pop()
            final(i).pop()
            j=i-1
            temp=i
            l=l-2
            while i!=l-1:
                final[j]=final[i+1]
                i+=1
                j=j+1
            i=-1
    i=i+1

    

print(result)
        













    