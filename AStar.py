from random import randint
import networkx as nx
from Node import Node
import random
import math
import time

def makeFiles():
    for amount in range(100):#CHANGE TO 100
        fileobj = open("test" + str(amount) + '.txt', 'w')
        if (amount<25):
            cities=10
        elif(amount<50):#this lets the makefiles run once, and it'll make all 100 files, and automatically change the city#
            cities=25
        elif(amount<75):
            cities=50
        else:
            cities=100
        fileobj.write(str(cities) +'\n')
        xpresent=[]
        ypresent=[]
        for i in range(101):
            xpresent.append(1)
            ypresent.append(1)
        for city in range(cities):# will make the necessary number of cities
            xtmp=randint(0,100)
            ytmp=randint(0,100)
            if(xpresent[xtmp]==0 and ypresent[ytmp]==0):#checks to see if a city is already made at that particular location
                while(xpresent[xtmp]==0 and ypresent[ytmp]==0):#keep generating cities till u hit an empty spot
                    xtmp=randint(0,100)
                    ytmp=randint(0,100)
            xpresent[xtmp]=0
            ypresent[ytmp]=1
            str1=str(city)+ ' ' + str(xtmp) + ' ' + str(ytmp)
            fileobj.write(str1 +"\n")

def findDistance(a,b):
    dist = (((a.x - b.x)**2) + ((a.y - b.y)**2)) ** (.5)
    dist = math.sqrt(math.pow(a.x - b.x,2) + math.pow(a.y - b.y,2))
    return dist

def run():
    t0=time.time()
    numsolved=0
    nodeslist=[]
    distlist=[]
    timelist=[]
    while((time.time()-t0)<600):
        t0=time.time()
        for i in range(100):#CHANGE TO 100
                temptime=time.time()
                fileobj=open('test'+str(i)+'.txt','r')#CHANGE TEST0 TO A VAR, SO IT CYCLES ALL FILES
                if((time.time()-t0)>600):
                    break
                #fileobj=open('test78.txt','r')
                numcities=fileobj.readline()
                cities=[]
                closed=[]
                notclosed=[]
                dist=0
                nodes=0

                #this reads the files, turns all the cities into nodes, and puts them in the notclosed list
                for d in range(int(float(numcities))):
                    tmp=fileobj.readline()
                    firstspace=tmp.index(" ")
                    secondspace=tmp.index(' ',firstspace+1)
                    cities.append((tmp[firstspace+1:secondspace],tmp[secondspace+1:len(tmp)-1]))
                    tmpNode=Node()
                    tmpNode.x=float(tmp[firstspace+1:secondspace])
                    tmpNode.y=float(tmp[secondspace+1:len(tmp)-1])
                    tmpNode.num=float(tmp[:firstspace])
                    nodes+=1
                    notclosed.append(tmpNode)

                closed.append(notclosed[0])
                notclosed.remove(closed[0])
                start=closed[0]
                curr=start
                tmpcity=closed[0]
                distances=[]
                if((time.time()-t0)>600):
                    break
                while(notclosed and (time.time()-t0<600)):
                #while(notclosed):
                    maxdist=999999
                    maxnode=None
                    for a in notclosed:#iterates through all the nodes, to see which one to add next

                        graph = nx.Graph()
                        hn=0
                        hn=dist+hn+findDistance(a,curr)
                        for g in range(len(notclosed)):
                            if(notclosed[g]!=a):
                                distances.append(findDistance(a,notclosed[g]))
                            for e in range(len(notclosed)+1):
                                if(g!=len(notclosed)):
                                    if(e==len(notclosed)):
                                        if (notclosed[g].x != a.x and notclosed[g].y != a.y):
                                            dist1=findDistance(notclosed[g],start)
                                            graph.add_edge(g,'c',weight=dist1)
                                            nodes+=1
                                        if ((time.time() - t0) > 600):
                                            break
                                    else:
                                        if((notclosed[g].x!=a.x and notclosed[g].y!=a.y) and (notclosed[e].x!=a.x and notclosed[e].y!=a.y)):
                                            dist1=findDistance(notclosed[g],notclosed[e])
                                            graph.add_edge(g,e,weight=dist1)
                                            nodes+=1
                                        if ((time.time() - t0) > 600):
                                            break
                        adddist=0
                        for c in notclosed:
                            if(a!=c):
                                adddist+=findDistance(c,start)
                        hn+=adddist
                        mst=nx.prim_mst(graph)#changed tree to edges
                        for node in mst.edges(data=True):
                            hn+=node[2]['weight']#adds up the distances from the mst
                        hn+=findDistance(a,start)+min(distances)#adds the distance from the a node to start node
                        if(hn<maxdist):
                            maxdist=hn
                            maxnode=a
                        if ((time.time() - t0) > 600):
                            break
                    closed.append(maxnode)
                    notclosed.remove(maxnode)
                    dist+=findDistance(maxnode,curr)
                    curr=maxnode
                distlist.append(dist)
                nodeslist.append(nodes)
                print(time.time()-temptime)
                print("iter: " + str(i) + " dist: " + str(dist))
                timelist.append(time.time()-temptime)
                numsolved+=1

    print(time.time()-t0)
    print(numsolved)
    print(dist)
    counter1=0
    counter2=0
    counter3=0
    counter4=0
    nodesavg1=0
    nodesavg2=0
    nodesavg3=0
    nodesavg4=0
    timeavg1=0
    timeavg2=0
    timeavg3=0
    timeavg4=0
    distavg1=0
    distavg2=0
    distavg3=0
    distavg4=0

    for i in range(numsolved):
        if(i<25):
            nodesavg1+=nodeslist[i]
            timeavg1+=timelist[i]
            distavg1+=distlist[i]
            counter1+=1
        elif(i<50):
            nodesavg2+=nodeslist[i]
            timeavg2+=timelist[i]
            distavg2+=distlist[i]
            counter2+=1
        elif(i<75):
            nodesavg3+=nodeslist[i]
            timeavg3+=timelist[i]
            distavg3+=distlist[i]
            counter3+=1
        else:
            nodesavg4+=nodeslist[i]
            timeavg4+=timelist[i]
            distavg4+=distlist[i]
            counter4+=1

    print("avgnode1: " + str(nodesavg1/counter1) + " avgtime1: " + str(timeavg1/counter1) + " avgdist1: " +str(distavg1/counter1))
    print("avgnode2: " + str(nodesavg2/counter2) + " avgtime2: " + str(timeavg2/counter2) + " avgdist2: " +str(distavg2/counter2))
    print("avgnode3: " + str(nodesavg3/counter3) + " avgtime3: " + str(timeavg3/counter3) + " avgdist3: " +str(distavg3/counter3))
    print("avgnode4: " + str(nodesavg4/counter4) + " avgtime4: " + str(timeavg4/counter4) + " avgdist4: " +str(distavg4/counter4))


#makeFiles()
run()
