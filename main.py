
operators=[] #operatörlerin olduğu stack
final=[] #son stack
includes=False #gelen operatörün kendisinden önce parantez içerip içermediğini belirler, içeriyorsa true içermiyorsa false
index=0 #her karakter atlanıldığında index değerinin artışı burada tutulur, özellikle birden fazla basamaklı sayılar olduğunda kullanışlı
val=1 #sayılarda işlem kolaylığı için 
hold=0 #parantezli işlemlerde parantezin bulunduğu yerin indexini tutar
first=True #bir sayının birden fazla basamaklı olup olmadığını karar vermedeki kontrol değişkeni
finish=True #işlem sonu, sonuysa operasyondaki tüm operatörler stackten çıkarılır final stackine aktarılır
result=0 #işlem sonucunun tutulduğu variable
notOp=False #önceden gelen karakterin/ mevcut karakterde operand olup olmadığını belirtir, final stack'ine atarken yardımcı
operation="((2+4)*4/2)" #bu tarz işlemlerde sorun var (yanyana birden fazla parantez, içteki parantezin sonuna kadar gidiyor fakat sonrasına devam etmiyor; kodun işleyişinde sorun yok fakat durum bu anlayamadım)
length=len(operation)

for char in operation:
    index=index+1 
    print(char)
    if char in "0123456789":
        if first==True:
            val=int(char)
            print(val) 
            first=False #sayının ilk rakamı giriş yaptı o nedenle değişken değişti
            notOp=True #sonraki gelecek eleman  öncekinin op olmadığını bilmeli
        elif first==False:
            val=val*10+int(char) #sayı birden fazla basamaklı
            notOp=True
        if index==length: #en son hanede gelen rakam ise
            first=True 
            final.append(val)
            val=1
    elif char in "+-*/()":
        if notOp==True: #önceki gelen elemanı final'e atmak için
            first=True
            final.append(val)
            val=1
        if len(operators)==0: #0 ise büyüklüğü direkt op final'e atılmalı
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

if finish==True: #op çıkarma
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
        













    