import random
import matplotlib.pyplot as plt;
import numpy as np
from time import sleep

def score (score_list):
    
    score_list[1].remove(max(score_list[1]))
    return sum(score_list[1]);

def sailor_pos (data):
    temp=sorted (data,key=data.get,reverse=True)
    return (temp)
    

def perf_value (data):
    dictionary = {}
    random.seed()
    [ dictionary.update({x: random.normalvariate(data[x][0],data[x][1])}) for x in data]
    return dictionary

    
def read_data (filename):
    f=open (filename,'r')
    rawdata = f.read().splitlines()
    ndata = [x.replace(',',' ') for x in rawdata]
    data = [x.split() for x in ndata [1:len(ndata)]]
    dictionary = {}
    [dictionary.update ({x[0]: (float(x[1]),float(x[2]))}) for x in data]
    return dictionary

def test (filename):
    info=read_data(filename)
    results = {}
    scores = {}
    [results.update ({x:[]}) for x in info]
    win_count = {}
    [win_count.update ({x:0}) for x in info]
    for race in range (0,1000):
        for x in range (0,6):
            temp = perf_value(info)
            pos= sailor_pos (temp)
            for i in range (0,len(pos)):
                temp [pos[i]] = i+1;
            [results[x].append(temp[x]) for x in temp]
        sleep (.01)
        [scores.update({x: score ((x,results[x])) }) for x in results]
        rank = sorted(scores,key=scores.get)
        win_count[rank[0]]+=1;
    return win_count
temp = test ("file.csv")
sailors=[]
wins=[]
[sailors.append(x) for x in temp]
[wins.append(temp[x]) for x in temp]
y_pos = np.arange(len(sailors))
print (wins)
error = np.random.rand(5)

plt.bar(y_pos, wins, xerr=error, align='center', alpha=0.4)
plt.xticks(y_pos, sailors)
plt.ylabel('Wins')
plt.title('player wins for 1000 races')

plt.show()


