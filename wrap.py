from nnet import learn,guess
from random import random as rand
import time

mult = 1
training = 1
f1 = '16-x*rand()'
f2 = 'x*rand()'

a = [[eval(f1) for x in range(16)] for i in range(10)]
b = [[eval(f2) for x in range(16)] for i in range(10)]

def calc():
    a = time.time()
    for i in range(10000000):
        pass
    print(time.time()-a)

def tlearn(g):
    global data,struct
    spec = {
        'over' : 50
        }
    a = time.time()
    learn(data,struct,going=10**10,overwrite=True,file="out"+str(g)+".txt",ending='c',spec=spec)
    print(time.time()-a)
    
if training:
    tic = time.time()
    struct = [16,6,2]
    data = [[0,i] for i in a] + [[1,i] for i in b]
    tlearn(0)
    
