X=float(10/2*3)
print(X)

Y=float(5+3*8-18/6)
print(Y)

Z=float((5+3)*(8-18)/6)
print(Z)

M=5
J= (M>5)
if J==True:
    print("(1) is true")
else: 
    print("(1) is false") 

S=2
K=10
W= (S>3 and S<2) or (K>10 or S==2)
if W==True:
    print("(2) is true")
else: 
    print("(2) is false")
    
s=9
r=5
a= not(s>9 and s<1) or (r>10 or s!=2)
b=not(s>9 and s<1) and (r>10 or s!=2)
if a==True:
    print("(3a) is true")
else: 
    print("(3a) is false")
if b==True:
    print("(3b) is true")
else: 
    print("(3b) is false")
    
P=True
Q=False
R=False
o= not(P or Q) or (not Q or P)
u=(P and R) or (Q or R) or (P and not Q)
if o==True:
    print("(4a) is true")
else: 
    print("(4a) is false")
if u==True:
    print("(4b) is true")
else: 
    print("(4b) is false")