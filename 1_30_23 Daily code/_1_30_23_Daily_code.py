import matplotlib.pyplot as plt
import random
q = random.randint(1,100)
w = random.randint(1,100)
e = random.randint(1,100)
r = random.randint(1,100)
t = random.randint(1,100)
a = random.randint(1,100)
s = random.randint(1,100)
d = random.randint(1,100)
f = random.randint(1,100)
g = random.randint(1,100)
x = [q, w, e, r, t]
y = [a, s, d, f, g]

#for i in range(100):
#    y.append(i*5-20)
#for i in range(100):
#    y.append(i*-3+10)
#for i in range(100):
#    y.append(i*.5-3) 
plt.plot(y)
plt.show()