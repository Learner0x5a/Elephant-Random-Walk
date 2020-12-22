from scipy.special import loggamma
from math import gamma
import numpy as np
A = 5
# M = 5
p = 0.2
q = 0.9
direction = [1,-1]

batch_size = 10000
mem_index = []
choices = []
'''
generate random indices for memory and direction
np.random.choice is very slow for large arrays, even got stuck for some unknown reason.
'''
def batch_random():
    choices.extend(np.random.choice(direction,size=batch_size,p=[p,1-p]))
    for i in range(1,batch_size+1):
        mem_index.append(np.random.randint(0,i))
    return mem_index,choices


def sim():
    global mem_index
    global choices
    '''generate indices for the first time'''
    batch_random()
    mem = []
    X1 = np.random.choice(direction,p=[q,1-q])
    # print(X1) 
    mem.append(X1)
    pos = X1
    i = 0
    while True:
        '''use batched indices'''
        # X = np.random.choice(mem)*np.random.choice(direction,p=[p,1-p])
        # X = mem[np.random.randint(0,len(mem))]*np.random.choice(direction,p=[p,1-p])
        X = mem[mem_index[i]] * choices[i]
        mem.append(X)
        i += 1
        '''need more indices, generate another batch'''
        if i % batch_size == 0:
            batch_random()
        # print('Sampling from memory: ',i,' pos=',pos)
        pos += X 
        if pos == A:
            # print('Sampling from memory: ',i,' pos=',pos)
            '''Reached target position, reset indices.'''
            mem_index = []
            choices = []
            break
    return i





plot_idx = []
plot_x = []
plot_y = []
epochs = 20000
a_T = []
history_T = []
diff = []
print('Simulating...')
for j in range(epochs):
    T = sim()
    history_T.append(T)
    '''
    calculate gamma function for a large number will overflow
    hence we calculate the ln_gamma instead
    '''
    # res = gamma(T)*gamma(2*p)/gamma(T+2*p-1)
    res = gamma(2*p)*np.exp(loggamma(T)-loggamma(T+2*p-1))
    a_T.append(res)
    diff.append(res-(2*q-1)/A)

    if j % 2 == 0:
        print(j,(np.mean(history_T),np.mean(diff)))
        plot_idx.append(j)
        plot_x.append(np.mean(history_T))
        plot_y.append(np.mean(diff))

print((p,q,A),np.mean(a_T)-(2*q-1)/A)

import matplotlib.pyplot as plt
plt.figure()
plt.scatter(plot_idx,plot_y)
plt.xlabel('epoch')
plt.ylabel('E(diff)')

plt.savefig('erw1.png')
plt.show()

plt.figure()
plt.scatter(plot_idx,plot_x)
plt.xlabel('epoch')
plt.ylabel('E(T)')
plt.savefig('erw2.png')
plt.show()

