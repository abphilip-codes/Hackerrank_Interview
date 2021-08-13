# Udaan Preliminary Test

database = {}                          # User is key, appointment is value
for T in range(int(input())):
    l = list(input().split())
    if(l[0]=="add-user"):               # Input Command Taken
        if(l[1] in database): print("failure")
        else: 
            print("success")
            database[l[1]]=[]
    elif(l[0]=="create-event"):          # Input Command Taken
        b = 0
        for z in range(int(l[4])):
            if(b==1): break
            l[2:4] = list(map(int,l[2:4]))
            for i in range(len(database[l[5+z]])):
                k1,k2 = database[l[5+z]][i][1],database[l[5+z]][i][2]
                if(l[1]==database[l[5+z]][i][0]):
                    if(any(x in range(k1,k1+k2) for x in range(l[2],l[2]+l[3]))): 
                        print("failure")
                        b = 1
        else: 
            for z in range(int(l[4])):
                database[l[5+z]].append(l[1:])
            print("success")
    elif(l[0]=="show-events"):            # Input Command Taken
        for z in database[l[2]]:
            if(z[0]==l[1]):
                print("{}-{}".format(z[1],z[1]+z[2]),end=" ")
                print(*z[4:])
    elif(l[0]=="suggest-slot"):           # Input Command Taken
        m = list(range(int(l[2]),int(l[3])))
        for z in l[6:]:
            for y in database[z]:
                if(y[0]==l[1]): 
                    for a in range(y[1],y[1]+y[2]):
                        if a in m: m.remove(a) 
        for ele in m:
            nr=0
            for q in range(ele,ele+int(l[4])):
                if q not in m: nr=1
            if(nr==0): 
                print(ele)
                break
        else: print("none")