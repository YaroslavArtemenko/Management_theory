import numpy as np
import matplotlib.pyplot as plt

from math import log
from scipy.integrate import odeint

def deriv(y, t, N, p, q, u, d):
    S, I, R, D = y
    dSdt = -S * p - S * u
    dIdt = S * p - q * I
    dRdt = q * I + S * u
    dDdt = I * d
    return dSdt, dIdt, dRdt, dDdt

N = 10000   # населення

r = 50          # кількість контактів
c = 0.85         # ймовірність передачі
q = 0.09         # процес одужання
u = 0.05         # вакцинування
d = 0.04      # ймовірність смертельного випадку

D0 = 0               # кількість смертей (0)
R0 = 20                # кількість індивідів з імунітетом
I0 = 97     # кількість хворих (I > 0)
S0 = 10000 - 117            # кількість здорових (S0 < N)



p = -(r*I0*log(1 - c))/N
print(p)

t = np.linspace(0, 500, 501)
t1 = np.linspace(0, 90, 91)

y0 = S0, I0, R0, D0

ret = odeint(deriv, y0, t, args=(N, p, q, u, d))
S, I, R, D = ret.T
for i in zip(t, I):
    if i[1] <= 0:
        e = int(i[0])
        print(f'Кількість смертей - {D[e]}')
        y = np.linspace(0, e, e+1)
        print(e)
        break

t2 = np.linspace(0, e, e+1)

fig = plt.figure(facecolor='w')
ax = fig.add_subplot(111, axisbelow=True)
ax.plot(t1, S[:len(t1)], 'b', alpha=0.5, lw=2, label='Susceptible')
ax.plot(t1, I[:len(t1)], 'r', alpha=0.5, lw=2, label='Infected')
ax.plot(t1, R[:len(t1)], 'g', alpha=0.5, lw=2, label='Recovered with immunity')
ax.plot(t1, D[:len(t1)], 'y', alpha=0.5, lw=2, label='Death cases')
ax.set_xlabel('Time /days')
ax.set_ylabel('Number')
ax.set_ylim(0,N)
ax.yaxis.set_tick_params(length=0)
ax.xaxis.set_tick_params(length=0)
ax.grid(b=True, which='major', c='w', lw=2, ls='-')
legend = ax.legend()
legend.get_frame().set_alpha(0.5)
for spine in ('top', 'right', 'bottom', 'left'):
    ax.spines[spine].set_visible(False)
plt.show()

fig = plt.figure(facecolor='w')
ax = fig.add_subplot(111, axisbelow=True)
ax.plot(t2, S[:len(t2)], 'b', alpha=0.5, lw=2, label='Susceptible')
ax.plot(t2, I[:len(t2)], 'r', alpha=0.5, lw=2, label='Infected')
ax.plot(t2, R[:len(t2)], 'g', alpha=0.5, lw=2, label='Recovered with immunity')
ax.plot(t2, D[:len(t2)], 'y', alpha=0.5, lw=2, label='Death cases')
ax.set_xlabel('Time /days')
ax.set_ylabel('Number')
ax.set_ylim(0, N)
ax.yaxis.set_tick_params(length=0)
ax.xaxis.set_tick_params(length=0)
ax.grid(b=True, which='major', c='w', lw=2, ls='-')
legend = ax.legend()
legend.get_frame().set_alpha(0.5)
for spine in ('top', 'right', 'bottom', 'left'):
    ax.spines[spine].set_visible(False)
plt.show()
