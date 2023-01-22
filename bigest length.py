from random import*
def remplir(T,n):
    for i in range (n):
        b=False
        while(b==False):
            T[i]=input("T["+str(i)+"]=")
            b=verif(T[i])
def verif(ch):
    while (ch!="")and("A"<=ch[0]<="Z"):
        ch=ch[1:]
    return(ch=="")
def tri1(T,n):
    global s,sl
    ch=""
    for i in range(n):
        ch=ch+T[i]
    s=""
    sl=""
    for i in range(65,91):
        c=chr(i)
        sm=""
        for j in range(len(ch)):
            if (ch[j]==c):
                sm=sm+c
        s=s+sm
        if(len(sm)>len(sl)):
            sl=sm
def tri2(T,n,s,sl):
    b=False
    for i in range(n):
        T[i]=s[0:len(T[i])]
        s=s[len(T[i]):]
        print(T[i],end="  ")
        if (T[i].find(sl[0])>-1)and(b==False):
            p=i
            b=True
    print("\nLa séquence la plus longue est: ",sl,"commençant a la case n°: ",p)
#p.p
import numpy as np
n=5
T=np.array([str]*n)
remplir(T,n)
print(T)
tri1(T,n)
tri2(T,n,s,sl)
