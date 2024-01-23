import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
import random
plt.style.use('bmh')

def simulate_path(k, theta, sigma, r_0=None):
	r_0 = theta if r_0 is None else r_0

	T = 1
	n = 1000
	ts = np.linspace(0,T,n+1)
	rts = []
	dt = T/n

	for t in ts:
		if len(rts) == 0: 
			rts.append(r_0)
			continue
		rt = rts[-1]
		dW = np.random.normal(loc=0, scale=np.sqrt(dt))

		# dr_t = k(theta - r_t)dt + sigma dW^Q
		dr = k*(theta - rt)*dt + sigma * dW
		rts.append(rt+dr)

	return ts, rts

k = 20
theta = 0.02
sigma = 0.02
cmap = plt.get_cmap('plasma')

ts, path = simulate_path(k=k, theta=theta, sigma=sigma, r_0=0.022)

plt.plot(ts, path, c=cmap(0))
plt.ylim(0,0.04)
plt.legend()
plt.show()
