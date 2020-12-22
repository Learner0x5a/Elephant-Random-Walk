import numpy as np

p_ = 0.4
b = -10
T = []

def asymmetric_random_walk():
    pos = 0
    i = 0
    while True:
        Y = np.random.choice([1,-1],p=[p_,1-p_])
        pos += Y
        i += 1
        if pos == b:
            T.append(i)
            break

epochs = 2000
plot_idx = []
plot_x = []
for j in range(epochs):
    plot_idx.append(j)
    plot_x.append(np.mean(T))
    asymmetric_random_walk()

print(np.mean(T),b/(2*p_-1))
import matplotlib.pyplot as plt
plt.figure()
plt.scatter(plot_idx,T)
plt.xlabel('epoch')
plt.ylabel('T')

plt.savefig('arw.png')
plt.show()

plt.figure()
plt.scatter(plot_idx,plot_x)
plt.xlabel('epoch')
plt.ylabel('E(T)')

plt.savefig('arw1.png')
plt.show()