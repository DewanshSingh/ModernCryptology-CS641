import fieldmath

field = fieldmath.BinaryField(131)

def exp(m,n):
    n = n%127
    ans = 1
    for i in range(n):
        ans = field.multiply(m,ans)
    return ans

def E_encrypt(E,v):
    Ans = [0,0,0,0,0,0,0,0]
    for i in range(8):
        Ans[i] = exp(v[i],E[i])
    return Ans    

def A_encrypt(A,v): 
    Ans = [0,0,0,0,0,0,0,0]
    V = fieldmath.Matrix(8,1,field)
    for i in range(8):
        V.set(i,0,v[i])
    for i in range(8):
        Ans[i] = (A.multiply(V)).get(i,0)    
    return Ans

E=[102,107,72,42,65,106,6,53]
D=[26,46,57,101,40,100,4,118]

E_inv=[0,0,0,0,0,0,0,0]
for i in range(8):
    for j in range(128):
        if((E[i]*j)%127 == 1):
            E_inv[i] = j


A = fieldmath.Matrix(8, 8, field)

for i in range(8):
    for j in range(8):
        if(i==j):
            A.set(i,j,D[i])
        else:
            A.set(i,j,0)
A.set(1,0,71)   
A.set(2,1,75)  
A.set(3,2,79) 
A.set(4,3,116) 
A.set(5,4,58) 
A.set(6,5,118)
A.set(7,6,11)  
A.set(2,0,50)
A.set(3,1,0)
A.set(4,2,91)
A.set(5,3,60)
A.set(6,4,13)
A.set(7,5,13)
A.set(3,0,112)
A.set(4,1,119)
A.set(5,2,12)
A.set(6,3,15)
A.set(7,4,75)
A.set(4,0,41)
A.set(5,1,7) 
A.set(6,2,37)
A.set(7,3,4) 
A.set(5,0,120) 
A.set(6,1,112) 
A.set(7,2,106) 
A.set(6,0,11)
A.set(7,1,32)
A.set(7,0,25)  

A.invert()
ciphertext = 'fgffgnkqjfjlgrko'
#ciphertext = 'lglnkklqirlgjlkh' 
X = [0,0,0,0,0,0,0,0]   #input to be decrypted
for i in range(8):
    X[i] = (ord(ciphertext[2*i])-ord('f'))*16 + (ord(ciphertext[2*i + 1])-ord('f'))
X1 = E_encrypt(E_inv,X)
X2 = A_encrypt(A,X1)
X3 = E_encrypt(E_inv,X2)
X4 = A_encrypt(A,X3)
X5 = E_encrypt(E_inv,X4)
out =""
print(X5)
for x in X5:
    out = out+chr(x)
print(out)