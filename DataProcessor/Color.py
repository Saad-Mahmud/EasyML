import numpy as np
def makecolor(k):
    #print('here')
    p=getcol(len(k))
    mp={k[i]:p[i]  for i in range(len(k))}
    return mp

def getcol(l):
    ret=[]
    cur=48570
    delta=int(1000000/l)
    delta=delta
    for i in range(l):
        ret.append(cur)
        cur=cur+delta
    ret2=[]
    for i in ret:
        ret2.append(con(i))
    return ret2

def con(x):
    ret='#'
    x=hex(x)
    for i in range(2,len(x)):
        ret=ret+x[i]
    for i in range(len(ret),7):
        ret=ret+'0'
    return ret