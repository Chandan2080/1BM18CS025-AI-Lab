from collections import defaultdict
 
class Graph:
    def __init__(self,vertices):
         self.V=vertices
         self.graph=defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)
    
    def DLS(self,src,target,limit):
        
        if(src==target):
            return True
        
        if(limit<=0):
            return False
        
        for i in self.graph[src]:
            if(self.DLS(i,target,limit-1)):
                return True

        return False

    def IDDFS(self,src,target,limit):
        for i in range(limit):
            if(self.DLS(src,target,i)):
                return True
        return False



k=input("Enter the number of edges: \n")
g=Graph(int(k))
print("Enter the u and v values for "+str(k)+" edges:")
for i in range(int(k)-1):
    j=1
    
    u,v = input("-> ").split()
    g.addEdge(int(u),int(v))
    j = j+1

target = input("Target?  ")
maxDepth = input("Maximum Depth?  ")
src = input("Source?  ")

#target,maxDepth,src = input("Enter the Target, maximum depth & the source: \n").split()
if g.IDDFS(int(src), int(target), int(maxDepth)) == True: 
    print ("---->Target is reachable from source " +
        "within the given max depth") 
else : 
    print ("---->Target is NOT reachable from source " +
        "within the given max depth!")