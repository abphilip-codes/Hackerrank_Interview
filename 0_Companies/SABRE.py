# Sabre Preliminary Test

s,m,l,ans=input(),0,[],[]
for i in range(len(s)):
    if(s[i].isalnum()): continue
    l.append(s[m:i])
    m=i 
l.append(s[m:i+1])
x=y=0 # Coordinates
l = [i for i in l if i]
for z in l:
    m=0
    for i in range(len(z)):
        if(z[i].isalpha()):
            if(i==0 or z[i-1].isalpha()):
                al="+1"+z[i]
                ans.append(al)
                m=i
            elif(z[i-1].isnumeric()): 
                ans.append(z[m:i+1])
                m=i 
            else: 
                al="+1"+z[i]
                ans.append(al)
                m=i
print(ans)