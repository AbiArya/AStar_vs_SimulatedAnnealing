from SimulatedAnnealing import SimAnneal
import matplotlib.pyplot as plt
import time

def run():
    t0=time.time()
    numsolved=0
    nodeslist=[]
    distlist=[]
    timelist=[]
    while((time.time()-t0)<600):
        for i in range(100):#CHANGE TO 100
            print(i)
            temptime=time.time()
            nodes = []
            with open('test'+str(i)+'.txt','r') as f:
                citynum=f.readline()
                for i in range(int(float(citynum))):
                    tmpcity=f.readline()
                    firstspace = tmpcity.index(" ")
                    secondspace = tmpcity.index(' ', firstspace + 1)
                    x = float(tmpcity[firstspace + 1:secondspace])
                    y = float(tmpcity[secondspace + 1:len(tmpcity) - 1])
                    nodes.append([x,y])


            sa = SimAnneal(nodes)
            dist,nodes1,numlist,stufflist=sa.Anneal()
            distlist.append(dist)
            nodeslist.append(nodes1)
            timelist.append(time.time()-temptime)
            numsolved+=1
        if(i==99):
            break
    counter1 = 0
    counter2 = 0
    counter3 = 0
    counter4 = 0
    nodesavg1 = 0
    nodesavg2 = 0
    nodesavg3 = 0
    nodesavg4 = 0
    timeavg1 = 0
    timeavg2 = 0
    timeavg3 = 0
    timeavg4 = 0
    distavg1 = 0
    distavg2 = 0
    distavg3 = 0
    distavg4 = 0
    #plt.plot(numlist, stufflist, 'r--')
    #plt.axis([300, max(numlist), 200, 600])
    #plt.show()
    for i in range(numsolved):
        if (i < 25):
            nodesavg1 += nodeslist[i]
            timeavg1 += timelist[i]
            distavg1 += distlist[i]
            counter1 += 1
        elif (i < 50):
            nodesavg2 += nodeslist[i]
            timeavg2 += timelist[i]
            distavg2 += distlist[i]
            counter2 += 1
        elif (i < 75):
            nodesavg3 += nodeslist[i]
            timeavg3 += timelist[i]
            distavg3 += distlist[i]
            counter3 += 1
        else:
            nodesavg4 += nodeslist[i]
            timeavg4 += timelist[i]
            distavg4 += distlist[i]
            counter4 += 1

    print("avgnode1: " + str(nodesavg1 / counter1) + " avgtime1: " + str(timeavg1 / counter1) + " avgdist1: " + str(
        distavg1 / counter1))
    print("avgnode2: " + str(nodesavg2 / counter2) + " avgtime2: " + str(timeavg2 / counter2) + " avgdist2: " + str(
        distavg2 / counter2))
    print("avgnode3: " + str(nodesavg3 / counter3) + " avgtime3: " + str(timeavg3 / counter3) + " avgdist3: " + str(
        distavg3 / counter3))
    print("avgnode4: " + str(nodesavg4 / counter4) + " avgtime4: " + str(timeavg4 / counter4) + " avgdist4: " + str(
        distavg4 / counter4))

run()
