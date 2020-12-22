import numpy as np

p = 0.75
q = 0.8
# M = int(2e1)
import matplotlib.pyplot as plt
plot_idx = []
plot_x = []
plot_y = []
def sim(M):

    mem = []
    X1 = np.random.choice([1,-1],p=[q,1-q])
    mem.append(X1)
    pos = X1
    for i in range(1,int(10000)):
        X = mem[np.random.randint(0,len(mem))]*np.random.choice([1,-1],p=[p,1-p])
        # print(X,pos)
        if not len(mem) >= M:
            mem.append(X)
        pos += X 
        # if i%1==0:
            # print(pos/i)
        
        # plot_idx.append(i)
        # plot_x.append(pos/i)
    return pos/i


for k in range(1,10):
    plot_idx.append(k)

    res = []
    for j in range(100):
        print('Simulating...',j)
        res.append(sim(int(np.power(2,k))))
        # plot_idx.append(j)
        # plot_x.append(sim())
    # plt.figure()
    # plt.scatter(plot_idx,plot_x)
    # plt.xlabel('epoch')
    # plt.ylabel('S_n/n')

    # plt.savefig('erw3.png')
    # plt.show()
    # print('p=',p,' q=',q,' M=',M,' E(S_n/n)=',np.mean(plot_x),' std=',np.std(plot_x),' max-min=',max(plot_x)-min(plot_x))

    plot_x.append(np.mean(res))
    plot_y.append(np.std(res))



plt.figure()
plt.plot(plot_idx,plot_x)
plt.xlabel('M')
plt.ylabel('E(S_n/n)')

plt.savefig('erw4.png')
plt.show()

plt.figure()
plt.plot(plot_idx,plot_y)
plt.xlabel('M')
plt.ylabel('std(S_n/n)')

plt.savefig('erw5.png')
plt.show()