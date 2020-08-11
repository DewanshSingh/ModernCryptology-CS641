import fieldmath as fd

field = fd.BinaryField(131)
#131 denotes the irred. polynomial x^7 + x + 1
def exponent(m,n):
    n = n%127
    ans = 1
    for i in range(n):
        ans = field.multiply(m,ans)
    return ans

fopen = open("out.txt",'r')    
with fopen as f:
    getlines = f.readlines()
getlines = [x.strip() for x in getlines]

i=0
for a,b in zip(getlines[0::2], getlines[1::2]):
    var1 = (ord(a[2*i])-ord('f'))*16 + (ord(a[2*i + 1])-ord('f'))       
    var2 = (ord(b[2*i])-ord('f'))*16 + (ord(b[2*i + 1])-ord('f'))
    for k in range(128):
        for j in range(128):
            if(field.multiply(exponent(j,k*(k+1)),1)==var1):
                if(field.multiply(exponent(j,k*(k+1)),exponent(2,k*k*k))==var2):
                    print(i,j,k)                                        
    i=i+1
    