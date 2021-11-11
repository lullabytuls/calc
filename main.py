operation = "(15+11)*(7*3)"
result=0
vali=0
val=None
ind1=None
ind2=None
ind3=None
noparanthysis=True
stack=[]
actstack=[]
operations=[]
preop=[]
prenum=[]

def a(operation,stack,actstack,operations,preop,prenum):
    n=10    
    i=-1
    j=-1
    length=len(operation)
    for char in operation:
        if char in "0123456789":
            i=i+1;
            stack.append(int(char))
            prenum.append(i)
        elif char in "+-*/()":
            operations.append(char)
            i=i+1
            preop.append(i)
    print(stack)
    print(operations)
    print(prenum)
    print(preop)
    s=len(stack)
    print(stack.pop())
    print(s)
    z=0
    """ 
    for z in range(s-1):
        n=10
        if prenum[z]+1==prenum[z+1]:
           neu= stack[z]*n+stack[z+1]
           for z in range(s-1):
            if prenum[z+1]==prenum[z+2]:
                neu=neu*10+prenum[z+2]
           n=n*10
           actstack.append(neu)
    print(actstack)
    print(z)
    while z<=5:
        actstack.append(stack[z])
        z=z+1
    print(actstack)
    l=len(operations)
    for it in range(l):
        if operations[it]=="(":
            print("a")  """
    
a(operation,stack,actstack,operations,preop,prenum)
""" for i in range(len(preop)):
    if operations[i]!=")":
        continue
    elif operations[i]=")": """
def add(result):
    result+=stack.pop()+stack.pop()
def subtract(result):
    result-=stack.pop()-stack.pop()
def multiply(result):
    result+=stack.pop()*stack.pop()
def divide(result):
    result+=stack.pop()/stack.pop()
def lookfor(o):
    r=len(o)
    for i in range(len(o)):
        j=i+1
        while j<r:
            if o[i]==o[j] and o[i]=="(":
                noparanthysis=False
                val=j
                break
            elif o[i]==o[j] and o[i]==")":
                noparanthysis=False
                vali=vali+1




        

if operations.pop()==")":
    lookfor(operations)
    if noparanthysis==True:
        while True:
            main=operations.pop()
            if main=="+":
                add()
            elif main=="-":
                subtract()
            elif main=="*":
                multiply()
            elif main=="/":
                divide()
            if operations.isEmpty()==True:
                break

    elif noparanthysis==False:
        if vali!=0:
            for i in range(vali):
                operations.pop()
        while True:
            main=operations.pop()
            if main=="+":
                add()
            elif main=="-":
                subtract()
            elif main=="*":
                multiply()
            elif main=="/":
                divide()
            for i in range(vali-1):
                operations.pop()
    
print(result)





    