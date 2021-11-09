operation = "15+11*7*3"

def a(operation):
    stack=[]
    actstack=[]
    operations=[]
    preop=[]
    prenum=[]
    n=10
    i=-1
    j=-1
    length=len(operation)
    for char in operation:
        if char in "0123456789":
            i=i+1;
            stack.append(int(char))
            prenum.append(i)
        elif char in "+-*/":
            operations.append(char)
            j=i+1
            i=i+1
            preop.append(i)

    print(stack)
    print(operations)
    print(prenum)
    print(preop)
    s=len(stack)
    print(s)
    z=0
    for z in range(s-1):
        n=10
        if prenum[z]+1==prenum[z+1]:
           neu= stack[z]*n+stack[z+1]
           n=n*10
           print(neu)
           actstack.append(neu)
    print(actstack)
a(operation)
