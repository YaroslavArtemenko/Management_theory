from math import pi, cos, sin, radians, sqrt
import numpy as np
import matplotlib.pyplot as plt



variant = 1
s0 = variant
V = variant
l = variant
fi = (variant * pi)*150 / 25

def s(x2):
    return s0 * x2

x1_ = l * cos(radians(fi))
x2_ = l * sin(radians(fi))
print(x1_, x2_)

N = 10000
teta = (l * V)/N

def lambd(t, x1_k, x2_k):
    result = sqrt(((x1_-x1_k)-(s(x2_k))*teta)**2+(x2_-x2_k)**2)*V*teta-(V**2)*(teta**2)
    return result

def u1(t, x1_k, x2_k):
    result = ((x1_-x1_k-s(x2_k)*teta)*V*teta)/(lambd(t, x1_k, x2_k)+(V**2)*(teta**2))
    return result

def u2(t, x1_k, x2_k):
    result = ((x2_-x2_k)*V*teta)/(lambd(t, x1_k, x2_k)+(V**2)*(teta**2))
    return result

def x1(t, x1_k, x2_k):
    result = x1_k + (s(x2_k)+V*u1(t, x1_k, x2_k))*teta
    return result

def x2(t, x1_k, x2_k):
    result = x2_k + V*u2(t, x1_k, x2_k)*teta
    return result



line = np.linspace(0, 1, 10001)

all_x1 = [0]
all_x2 = [0]
for t in line:
    x1_k = all_x1[-1]
    x2_k = all_x2[-1]
    all_x1.append(x1(t, x1_k, x2_k))
    all_x2.append(x2(t, x1_k, x2_k))
    if round(all_x1[-1], 2) == round(x1_, 2) \
      and round(all_x2[-1], 2) == round(x2_, 2):
        print(t)
        time = t
        break


fig, ax = plt.subplots()
ax.plot(all_x1, all_x2)

ax.set(xlabel='x1', ylabel='x2',
       title='Trajectory of the ship')
ax.grid()
props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
textstr = str(round(time, 4)) + ' seconds'
ax.text(0.05, 0.95, textstr, transform=ax.transAxes, fontsize=14,
        verticalalignment='top', bbox=props)

plt.show()
