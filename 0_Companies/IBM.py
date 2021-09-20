# IBM Preliminary Test

direction,floor,floor_requests,z = input(),int(input()),sorted(list(map(int,input().split())),reverse=True),0
if(floor_requests[-1]>=0 and floor_requests[0]<=15 and (direction=="UP" or direction=="DN")): 
    while(floor_requests[z]>floor): z+=1
    print(*(floor_requests[:z][::-1]+floor_requests[z:]),sep="\n") if(direction=="UP") else print(*(floor_requests[z:]+floor_requests[:z][::-1]),sep="\n")
else: print("Invalid")