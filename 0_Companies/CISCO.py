S=input()
l=list(map(str,input().split()))
ini=[]
m=0
c=0
while(m<len(S)):
    x=m
    while(x<len(S)):
        if(S[x]!=S[m]):
            break
        x+=1
    ini.append(S[m:x])
    m=x
for z in l:
    m=0
    k=[]
    while(m<len(z)):
        x=m
        while(x<len(z)):
            if(z[x]!=z[m]):
                break
            x+=1
        k.append(z[m:x])
        m=x
    allen=0
    for y in range(len(k)):
        # if(k[y]==ini[y] or k[y]*3==ini[y]): allen+=1
        if(k[y]==ini[y] or list(set(k[y]))[0]*3==ini[y]): allen+=1
    if(allen==len(k)): c+=1
print(c)