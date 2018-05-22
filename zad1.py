import random
import numpy as np
import matplotlib
import math
import matplotlib.pyplot as plt

def checkIfInside(arr, val):
    if val in arr:
        return True
    return False

def createForest(_p=0.5,_x = 10,_y = 10): #create forest
    tabForest= []
    for i in range (1,_x+1):
        for j in range (1,_y+1):
            if random.uniform(0,1) < _p:
                tabForest.append({'x':i,'y':j,'tree':True,'fire':False,'burned':False})
    return tabForest
def findTree(_dict,_x,_y): #find tree by position
    for element in _dict:
        if element['x'] == _x and element['y'] == _y:
            return element
def makeFire(_dict,_x,_y): #fire tree by position
    for element in _dict:
        if not element['burned'] and element['x'] == _x and element['y'] == _y:
            element['fire'] = True

def startFire(_dict): #start fire
    for element in _dict:
        if element['x'] == 1:
            element['fire'] = True

def returnFire(_dict): #lista podpalonych drzew
    tabFire = []
    for element in _dict:
        if element['fire'] and not element['burned']:
            tabFire.append([element['x'],element['y']])
    # print tabFire
    return tabFire

def findNextFire(_arr,_dict,_size): #znajdywanie kolejnych drzew do podpalenia
    tabMove = [[-1,-1],[0,-1],[1,-1],[-1,0],[1,0],[-1,1],[0,1],[1,1]]
    for element in _arr:
        for move in tabMove:
            x = element[0] + move[0]
            y = element[1] + move[1]
            if x >= 1 and y >= 1 and x <= _size and y <= _size:
                for d in _dict:
                    if d['x'] == x and d['y'] == y and not d['burned']:
                        d['fire'] = True


def makeBurned(_dict,_newdict): #wypalic palace sie drzewa
    for element in _dict: 
        if element['fire'] and not element['burned']:
            element['burned'] = True
            _newdict.append(element) #list of burned trees
            # _dict.remove(element)
            # remove i dodac do innej listy  CZY TO COS PRZYSPIESZY??

def isBurning(_dict): 
    a = 0
    for element in _dict:
        if element['fire'] and not element['burned']:
            a =  a + 1
        
    if a > 0:
        return False
    else:
        return True
def showForest(_dict):
    for element in _dict:
        print element
def countAllTrees(_dict):
    counter = 0
    for element in _dict:
        counter = counter + 1
    print counter

def policzSrednia(_wyniki,_size):
    print("Srednia dla roznych prawdopodobienstw: ")
    for wynik in _wyniki:
        a = 0
        for i in wynik:
            if(i < 1):
                print i,":"
            if(i > 1):
                a = a + i
        print(a / float(_size))        

def main(_N=100,_size = 10):  #zmienne prawdopodobienstwo
    wynik = []
    for j in range (0,10):
        nn = j/10.0
        wynik2 = []
        wynik2.append(nn)
        for j in range (0,_N):
            forest = createForest(nn,_size,_size)
            counter = 0
            isEnd = False
            burnedList = []
            startFire(forest)
            while(not isEnd):
                counter = counter + 1
                fireList = returnFire(forest)
                makeBurned(forest,burnedList)
                findNextFire(fireList,forest,_size)
                if isBurning(forest):
                    isEnd = True
                    wynik2.append(counter)
        wynik.append(wynik2)
    policzSrednia(wynik,_size)
    # print(wynik); 


def main2(_p = 0.7,_N=10, _size = 10): #jedno prawdopodobienstwo 
    wynik = []
    for j in range (0,_N):
        forest = createForest(_p,_size,_size)
        counter = 0
        isEnd = False
        burnedList = []
        startFire(forest)
        while(not isEnd):
            counter = counter + 1
            fireList = returnFire(forest)
            makeBurned(forest,burnedList)
            findNextFire(fireList,forest,_size)
            if isBurning(forest):
                isEnd = True
        wynik.append(counter)
    print(wynik); 

def main3(): #check function
    nn = 0.2
    forest = createForest(nn,10,10)
    burnedList = []
    countAllTrees(forest)
    startFire(forest)
    fire = returnFire(forest)
    print("Pierwszy ogien")
    print(fire)
    makeBurned(forest,burnedList)
    print(burnedList)
    findNextFire(fire,forest,10)
    fire = returnFire(forest)
    print("Drugi ogien")
    print(fire)
    makeBurned(forest,burnedList)
    print(burnedList)
    findNextFire(fire,forest,10)
    fire = returnFire(forest)
    print("Trzeci ogien")
    print(fire)
    print(burnedList)

# main2(0.5,1,50)
main()
