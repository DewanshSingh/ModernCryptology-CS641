import fieldmath 

field = fieldmath.BinaryField(131)

def str2dec(S):
    output=[0,0,0,0,0,0,0,0]
    it=0
    for i in range(8):
        output[i] = (ord(S[it])-ord('f'))*16 + (ord(S[it+1])-ord('f'))
        it+=2
    return output

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

#all E and D possibilities

E_all = [[33,102,119],[1,19,107],[72,84,98],[36,42,49],[65,92,97],[39,106,109],[6,7,114],[53,83,118]]  
D_all = [[19,26,89],[90,46,46],[57,66,77],[36,101,33],[40,115,32],[46,100,35],[4,36,25],[118,12,78]]

#final result
#E=[85,52,38,72,116,38,66,50]
#D=[100,56,40,50,16,87,14,103]

E=[0,0,0,0,0,0,0,0]
D=[0,0,0,0,0,0,0,0]

A = fieldmath.Matrix(8, 8, field)

for p in range(8):
    for q in range(8):
        A.set(p,q,0)

#to find A(0,0),E[0],E[1],A(1,1) and A(1,0)
arr = [[0 for i in range(8)] for j in range(8)]


check=False
for i in range(3):
    E[0] = E_all[0][i]
    D[0] = D_all[0][i]
    for j in range(3):
        E[1] = E_all[1][j]
        D[1] = D_all[1][j]
        A.set(0,0,D[0])
        A.set(1,1,D[1])
        for k in range(128):
            A.set(1,0,k)    
            X0 = [6,0,0,0,0,0,0,0]  # input = [flffffffffffffff]
            Y0 = [2,0,0,0,0,0,0,0]  # input = [fhffffffffffffff]
            X1 = E_encrypt(E,X0)
            X2 = A_encrypt(A,X1)
            X3 = E_encrypt(E,X2)
            X4 = A_encrypt(A,X3)
            X5 = E_encrypt(E,X4)
            Y1 = E_encrypt(E,Y0)
            Y2 = A_encrypt(A,Y1)
            Y3 = E_encrypt(E,Y2)
            Y4 = A_encrypt(A,Y3)
            Y5 = E_encrypt(E,Y4)
            if(X5[1]==15 and Y5[1]==63):    #output = [lsfuXsjffiftksis, hpiufomigoipkrkh]
                print(1,1,k)
                arr[1][0]=k
                arr[0][0]=D[0]
                arr[1][1]=D[1]
                check=True
                A.set(1,0,k)
            if(check):break  
        if(check):break
    if(check):break        

fopen = open("input_nondiag.txt",'r')     
with fopen as f:
    input1 = f.readlines()
input1 = [x.strip() for x in input1]

fopen = open("output_nondiag.txt",'r')     
with fopen as f:
    output1 = f.readlines()
output1 = [x.strip() for x in output1]
# print(input1,output1)
it=0
for a in range(2,8):
    for b in range(a-1,-1,-1):
        check = False
        if (a-b)==1:
            # print(a,b,"yo")
            X0=str2dec(input1[it])
            Y0=str2dec(input1[it+1])
            out1=str2dec(output1[it])
            out2=str2dec(output1[it+1])
            it=it+2
            for j in range(3):
                E[a] = E_all[a][j]
                D[a] = D_all[a][j]
                    # print(E[1],D[1])
                #A.set(a,a,D[a])
                A.set(a,a,D[a])

                for k in range(128):
                    A.set(a,b,k)    
                        
                        
                    X1 = E_encrypt(E,X0)
                    X2 = A_encrypt(A,X1)
                    X3 = E_encrypt(E,X2)
                    X4 = A_encrypt(A,X3)
                    X5 = E_encrypt(E,X4)
                    Y1 = E_encrypt(E,Y0)
                    Y2 = A_encrypt(A,Y1)
                    Y3 = E_encrypt(E,Y2)
                    Y4 = A_encrypt(A,Y3)
                    Y5 = E_encrypt(E,Y4)

                    if(X5[a]==out1[a] and Y5[a]==out2[a]):    
                        check=True
                        print(a,b,k)
                        arr[a][b]=k
                        arr[a][a]=D[a]
                        A.set(a,b,k)
                        break
                    if(check):break
                if(check):break
        else:
            # print(a,b,"hehe")
            X0=str2dec(input1[it])
            Y0=str2dec(input1[it+1])
            out1=str2dec(output1[it])
            out2=str2dec(output1[it+1])
            it=it+2
            for k in range(128):
                A.set(a,b,k)    
                        # X0 = [6,0,0,0,0,0,0,0]  # input = [flffffffffffffff]
                        # Y0 = [2,0,0,0,0,0,0,0]  # input = [fhffffffffffffff]   
                X1 = E_encrypt(E,X0)
                X2 = A_encrypt(A,X1)
                X3 = E_encrypt(E,X2)
                X4 = A_encrypt(A,X3)
                X5 = E_encrypt(E,X4)
                Y1 = E_encrypt(E,Y0)
                Y2 = A_encrypt(A,Y1)
                Y3 = E_encrypt(E,Y2)
                Y4 = A_encrypt(A,Y3)
                Y5 = E_encrypt(E,Y4)

                if(X5[a]==out1[a] and Y5[a]==out2[a]):    
                    check=True
                    print(a,b,k)
                    arr[a][b]=k
                    A.set(a,b,k)
                if(check):break

print(E)          
print(arr)
# print(D[0],D[1],"lol")
