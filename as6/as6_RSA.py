#!/usr/bin/env python
# coding: utf-8

# In[25]:


import time
from sage.crypto.util import *


# In[26]:


def coppersmith_howgrave_univariate( modulus, M1, loop):
    print("For size of unknown message:")
    for k in range(loop):
        M2 = M1 << k
        P.<x> = PolynomialRing(ZmodN) #, implementation='NTL')
        pol = (M2 + x)^e - C
        dd = pol.degree()


        # Tweak those
        beta = 1                              # b = N
        epsilon = beta/10                      # <= beta / 10
        mm = ceil(beta**2 / (dd * epsilon))     # optimized value
        tt = floor(dd * mm * ((1/beta) - 1))    # optimized value
        XX = ceil(N**((beta**2/dd - epsilon)))  # optimized value

        dd = pol.degree()
        nn = dd * mm + tt

        if not 0 < beta <= 1:
            raise ValueError("beta should belongs in (0, 1]")



        if not pol.is_monic():
            raise ArithmeticError("Polynomial must be monic.")

        polZ = pol.change_ring(ZZ)
        x = polZ.parent().gen()

        gg = []
        for ii in range(mm):
            for jj in range(dd):
                gg.append((x * XX)**jj * modulus**(mm - ii) * polZ(x * XX)**ii)

        for ii in range(tt):
            gg.append((x * XX)**ii * polZ(x * XX)**mm)

        BB = Matrix(ZZ, nn)
        for ii in range(nn):
            for jj in range(ii+1):
                BB[ii, jj] = gg[ii][jj]

        

        BB = BB.LLL()
        new_pol = 0

        for ii in range(nn):
            new_pol += x**ii * BB[0, ii] / XX**ii

        potential_roots = new_pol.roots()
        roots = []

        for root in potential_roots:
            if root[0].is_integer():
                result = polZ(ZZ(root[0]))
                if gcd(modulus, result) >= modulus^beta:
                    roots.append(ZZ(root[0]))

        
        if len(roots) == 0:
            print(k,"No roots found")
        else:
            print(k,roots)
            break
    return 


# In[27]:



length_N = 1024  # size of the modulus
e = 5
N = 84364443735725034864402554533826279174703893439763343343863260342756678609216895093779263028809246505955647572176682669445270008816481771701417554768871285020442403001649254405058303439906229201909599348669565697534331652019516409514800265887388539283381053937433496994442146419682027649079704982600857517093
C = 58851190819355714547275899558441715663746139847246075619270745338657007055698378740637742775361768899700888858087050662614318305443064448898026503556757610342938490741361643696285051867260278567896991927351964557374977619644763633229896668511752432222528159214013173319855645351619393871433455550581741643299
ZmodN = Zmod(N)
str1 = "This door has RSA encryption with exponent 5 and the password is "
M1 = Integer(str(ascii_to_bin(str1)),base=2)
loops = 200 # size of unknown part of message # length of 1/5th root of N 

coppersmith_howgrave_univariate( N, M1, loops)

