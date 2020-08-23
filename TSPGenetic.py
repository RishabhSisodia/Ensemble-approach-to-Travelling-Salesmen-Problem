from random import randrange as rr

from math import sqrt

import timeit

def distance(l):
    s=0
    for i in range(1,len(l)):
        x1,y1=dic[l[i-1]][0],dic[l[i-1]][1]
        x2,y2=dic[l[i]][0],dic[l[i]][1]
        s+=sqrt((x2-x1)**2+(y2-y1)**2)    
    return s
def dist(i,j):
    return float(format(sqrt((i[1]-j[1])**2+(i[0]-j[0])**2),".1f"))

dic={}
siz=int(input())
for _ in range(siz):
    inp=list(map(float,input().strip().split()))
    dic[int(inp[0])]=(inp[1],inp[2])

dic[siz+1]=dic[1]

l=[i+1 for i in range(siz)]
l=l+[siz+1]
#l=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
cities=list(l)
len_c=len(cities)
len_c-=1

population=len_c*6
# permutations

paths=[]
i=0
while i<population:
    r1=rr(1,len_c)
    r2=rr(1,len_c)
    while r1==r2:
        r1=rr(1,len_c)
        r2=rr(1,len_c)
    cities[r1],cities[r2]=cities[r2],cities[r1]
    if cities not in paths:
        paths.append(list(cities))
        i+=1
ll=list(l)
"""
# grredy cell------------------------++++++++++++++++++++++++++++++++++++++++

for i in range(0,len_c-1):
    c=distance([l[i],l[i+1]])
    jj=i+1
    for j in range(i+2,len_c-1):
        if distance([l[i],l[j]])<c:
            jj=j
            c=distance([l[i],l[j]])
    l[i+1],l[jj]=l[jj],l[i+1]

            
paths.append(list(l))
l=list(ll)
# grredy cell------------------------++++++++++++++++++++++++++++++++++++++++



#b & b -----------------------------------------++++++++++++++++++++++++++++

n=len(l)
n-=1
costm=[]

for i in range(1,n+1):
    te=[]
    for j in range(1,n+1):
        if i==j:
            te.append("inf")
        else:
            te.append(dist(dic[i],dic[j]))
    costm.append(te)


def reduc(matr,n):   
    cost=0
    for i in range(n):
        min_num=10000000
        for j in range(n):
            if matr[i][j]!='inf':
                if min_num>matr[i][j]:
                    min_num=matr[i][j]
                        
            
        if min_num!=0 and min_num!=10000000:
            for j in range(n):
                if matr[i][j]!='inf':
                    matr[i][j]-=min_num
            cost+=min_num

            
    for i in range(n):
        min_num=10000000
        for j in range(n):
            if matr[j][i]!='inf':
                if min_num>matr[j][i]:
                    min_num=matr[j][i]
        if min_num!=0 and min_num!=10000000:
            for j in range(n):
                if matr[j][i]!='inf':
                    matr[j][i]-=min_num
            cost+=min_num

    return cost

cost1=reduc(costm,n)



def makeinf(m,n,x,y):
    for i in range(n):
        m[x][i]='inf'
        m[i][y]='inf'
    m[y][0]='inf'
    

for i in range(0,n-1):
    mij=costm[l[i]-1][l[i+1]-1]
    newmat=[list(costm[_]) for _ in range(n)]
    makeinf(newmat,n,l[i]-1,l[i+1]-1)
    if mij=='inf':
        mij=100000
    costmin=cost1+reduc(newmat,n)+ mij
    z=i+1
    
    confmat=[list(newmat[_]) for _ in range(n)]
    for j in range(i+2,n):
        mij=costm[l[i]-1][l[j]-1]
        if mij=='inf':
            mij=100000
        newmat=[list(costm[_]) for _ in range(n)]
        makeinf(newmat,n,l[i]-1,l[j]-1)
        curcost=(cost1+reduc(newmat,n)+ mij)

        if curcost<costmin:
            costmin=curcost
            z=j
            confmat=[list(newmat[_]) for _ in range(n)]
    cost1=costmin
    costm=[list(confmat[_]) for _ in range(n)]
    l[i+1],l[z]=l[z],l[i+1]
    
print(l)
paths.append(l)
l=list(ll)

"""
#b&b----------------------------------------------------------++++++++++++++++++++
#crossovers
def crossover():
    j=0
    crossovers=[]
    parents=[]
    while j<population//2:
        r1=rr(0,population)
        r2=rr(0,population)
        while r1==r2 and r1 in parents and r2 in parents:
            r1=rr(0,population)
            r2=rr(0,population)
        parents.append(r1)
        parents.append(r2)
        p1=list(paths[r1])
        p2=list(paths[r2])
        
        r1=rr(1,len_c)
        r2=rr(1,len_c)
        while r1==r2:
            r1=rr(1,len_c)
            r2=rr(1,len_c)
        p1[r1:r2+1],p2[r1:r2+1]=p2[r1:r2+1],p1[r1:r2+1]

        xtra=list(set(l)-set(p1))
        len_x=len(xtra)
        for i in range(len(p1)):
            if p1.count(p1[i])>1:
                x=0#rr(0,len_x)
                p1[i]=xtra[x]
                del xtra[x]
                len_x-=1
                
        xtra=list(set(l)-set(p2))
        len_x=len(xtra)
        for i in range(len(p2)):
            if p2.count(p2[i])>1:
                x=0#rr(0,len_x)
                p2[i]=xtra[x]
                del xtra[x]
                len_x-=1
        
        if p1 not in crossovers and p2 not in crossovers and p1 not in paths and p2 not in paths:
            crossovers.append(list(p1))
            crossovers.append(list(p2))
            j+=1


    #mutation       
    mutations=[]
    i=0
    while i<(population):
        mutagens=list(crossovers[i])
        r1=rr(1,len_c)
        r2=rr(1,len_c)
        while r1==r2:
            r1=rr(1,len_c)
            r2=rr(1,len_c)
        mutagens[r1],mutagens[r2]=mutagens[r2],mutagens[r1]
        if mutagens not in paths and mutagens not in crossovers and mutagens not in mutations:
            mutations.append(list(mutagens))
            i+=1

    ultimatelist=paths+crossovers+mutations
    distances={}
    for i in range(len(ultimatelist)):
        distances[distance(ultimatelist[i])]=ultimatelist[i]
    
    
    dissort=sorted(distances.keys())
    print(dissort[0])
    
    for i in range(min(population,len(dissort))):
        paths[i]=distances[dissort[i]]

    c=distance(paths[0])

    for i in range(len_c-1,0,-1):
        jj=i
        for j in range(1,len_c):
            paths[0][i],paths[0][j]=paths[0][j],paths[0][i]
            if distance(l)<c:
                jj=j
                c=distance(paths[0])
            paths[0][i],paths[0][j]=paths[0][j],paths[0][i]
        paths[0][i],paths[0][jj]=paths[0][jj],paths[0][i]
    
    

generations=int(input())
start=timeit.default_timer()
while generations>0:
    crossover()
    generations-=1
print(paths[0])
stop=timeit.default_timer()
print(stop-start)
