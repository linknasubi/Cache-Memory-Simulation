import random
random.seed(30)
MP = []#dados
MPl = []#dados a serem transferidos
MPpl = []
MC = []
c = -1 #contador de endereço
m = 1#Primeiro indice
n = 9#Ultimo indice
c2 = 0#Contador2
c1 = 0#Contador-Multiplicador
hit = int()
h = int()
o = int()

for i in range(0,4096,1):
    a = random.randint(0,1)
    if i % 8 == 0:
        h = h + 1
        c = c + 1
        d = str(c)
        b =("End:" + d)
        MP.append(b)
    MP.append(a)
    
x = len(MP)- h
for k in range(0,(x+1),1):
    if c2 % 8 == 0:
        m = 1 + (c1*9)
        n = 9 + (c1*9)
        MPl.append(MP[m:n])   
    if c2 % 8 == 0:
        c1 = c1+1
    c2 = c2 + 1  
    #print(c2)
    

del MPl[-1:]
c2 = 0
c1 = 0
for k in MPl:
    if c2 % 4 == 0:
        m = 0 + (c1*4)
        n = 4 + (c1*4)
        MPpl.append(MPl[m:n])   
    if c2 % 4 == 0:
        c1 = c1+1
    c2 = c2 + 1 

n = 0
m = 0
hit = 0 
o = 0


def MaA():    
    hit = int()
    oCount = int()
    o = int()
    for m in range(0,100):#Quantidade de tentativas que definirá o nível de taxa de sucesso
        b = random.randint(0,len(MPpl)-1)
        oCount = oCount + 1
        if oCount > 16:#Considera que as palavras utilizadas são 16 em sequência
            o = b
            oCount = 0
        else: o = o+1
        print("o:",o)
        print("oCount:",oCount)
        if o > len(MPpl)-1:
            o = 0
        if MPpl[o] in MC:
            print("Found in CM")
            hit = hit + 1
        else:
            del MC[0:-1]
            print("No Data")
            #time.sleep(1)
            print("Searching")
            #time.sleep(1)
            print("Adding Data to line:")
            if o>64:
                for i in range(0,64):##tamanho da cache
                    MC.append(MPpl[(len(MPpl)-64)+i])
            else:
                for i in range(0,64):##tamanho da cache
                    MC.append(MPpl[(o)+i])
    
            print("MPpl:",MPpl[o], "MC:",MC[i])
        #print(MC)
    a = "Hits:",hit,"/",m+1
    return a

def MaD():
    hit = int()
    oCount = int()
    o = int()
    for n in range(0,32): #Tamanho da cache
        b1 = bin(n)
        MC.append(b1) 
    for m in range(0,100):     
        b = random.randint(0,(len(MPpl)-1)) 
        o = m
        oCount = oCount +1
        if oCount<9:
            o = o + oCount
            print("Found in CM")
        elif oCount>=9: 
            o=b
            oCount = 0
        if MPpl[o] in MC:
            hit = hit + 1
        else:
            print("No Data")
            print("Searching")
            print("Adding Data to line:")
            if o<32:
                for n in range (0,32):
                    MC[n] = MPpl[n]                
            else:
                for n in range(0,32):
                    MC[n] = MPpl[n+(32*(o//32))]
    
    a = "Hits:",hit,"/",m+1
    return a


for p in range(0,3):
    if p == 0:
        print(" 1 - Mapeamento Direto")
    if p == 1:
        print(" 2 - Mapeamento Associativo ")
    if p == 2:
        print(" 3 - Método Associativo por Conjunto")

b3 = int(input("Escolha o método:"))

if b3 == 1:
    print(MaD())
if b3 == 2:
    print(MaA())
if b3 == 3:
    hit = int()
    oCount = int()
    o = int()
    for n in range(0,64): #Tamanho da cache
        b1 = bin(n)
        MC.append(b1)      
    for m in range(0,100):#Quantidade de tentativas que definirá o nível de taxa de sucesso
        b = random.randint(0,len(MPpl)-1)
        oCount = oCount + 1
        o = m
        if oCount > 16:#Considera que as palavras utilizadas são 16 em sequência
            o = b
            oCount = 0
        else: o = o+1
        print("o:",o)
        print("oCount:",oCount)
        if o > len(MPpl)-1:
            o = 0
        if MPpl[o] in MC:
            print("Found in CM")
            hit = hit + 1
        else:
            print("No Data")
            print("Searching")
            print("Adding Data to line:")
            print(o)
            if o>64:
                for i in range(0,64):##tamanho da cache
                    MC.append(MPpl[(len(MPpl)-64)+i])        
    
            else:
                for i in range (0,16):#Quantidade de conjuntos
                    for i1 in range(0,4):##Tamanho do conjunto
                        MC.append(MPpl[(o)+i1])
        a = "Hits:",hit,"/",m+1
        print(a)
