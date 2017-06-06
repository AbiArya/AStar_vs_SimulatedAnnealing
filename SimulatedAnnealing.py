import math
import random

class SimAnneal(object):

    def __init__(self, nodes):
        self.alpha = 0.999
        self.iteration = 1
        self.size = len(nodes)
        self.stoptemp = 0.0000000001
        self.stop = 5000000
        self.T = math.sqrt(self.size)
        self.nodes=[]


        self.distmatrix = self.makeMatrix(nodes)

        for i in range(len(nodes)):
            self.nodes.append(i)

        #self.tmpsol = self.Solution()
        self.tmpsol=self.nodes
        self.sol = list(self.tmpsol)

        self.tmpfit=sum( [ self.distmatrix[self.tmpsol[i-1]][self.tmpsol[i]] for i in range(1,self.size) ] ) + self.distmatrix[self.tmpsol[0]][self.tmpsol[self.size-1]]
        self.ifitness = self.tmpfit
        self.bfitness = self.tmpfit

        self.fitness_list = [self.tmpfit]


    def makeMatrix(self, nodes):
        n = len(nodes)
        mat = []
        for j in range(n):
            tmp = []
            for i in range(n):
                c1=nodes[i]
                c2=nodes[j]
                tmp.append(math.sqrt( math.pow(c1[0] - c2[0], 2) + math.pow(c1[1] - c2[1], 2)  ))
            mat.append(tmp)
        return mat


    def accept(self, candidate):

        candidate_fitness = sum( [ self.distmatrix[candidate[i-1]][candidate[i]] for i in range(1,self.size) ] ) + self.distmatrix[candidate[0]][candidate[self.size-1]]
        if candidate_fitness < self.tmpfit:
            self.tmpfit = candidate_fitness
            self.tmpsol = candidate
            if candidate_fitness < self.bfitness:
                self.bfitness = candidate_fitness
                self.sol = candidate

        else:
            if random.random() < (math.exp( -abs(candidate_fitness-self.tmpfit) / self.T  )):
                self.tmpfit = candidate_fitness
                self.tmpsol = candidate

    def Anneal(self):
        '''
        Execute simulated annealing algorithm
        '''
        nodes1=0
        stufflist=[]
        numlist=[]
        counter=0
        while self.T >= self.stoptemp and self.iteration < self.stop:
            nodes1+=1
            candidate = list(self.tmpsol)
            l = random.randint(2, self.size-1)
            i = random.randint(0, self.size-l)
            candidate[i:(i+l)] = reversed(candidate[i:(i+l)])
            self.accept(candidate)
            self.T *= self.alpha
            self.iteration += 1
            self.fitness_list.append(self.tmpfit)
            stufflist.append(self.bfitness)
            counter+=1
            numlist.append(counter)
        return self.bfitness,nodes1,numlist,stufflist
        #print('Improvement over greedy heuristic: ', round(( self.ifitness - self.bfitness) / (self.ifitness),4))
