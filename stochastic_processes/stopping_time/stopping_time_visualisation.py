import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from qbstyles import mpl_style

plt.style.use('bmh')
plt.style.use('dark_background')

# mpl_style(True) # True means dark

if __name__ == "__main__":
	df = pd.read_csv('simulation_output.csv')
	print(df)

	plt.plot(df['t'], df['value'])

	B = df['barrier'][0]
	plt.plot([0, max(df['t'])*1.5], [B,B], c='green', lw=1.5)
	plt.plot([0, max(df['t'])*1.5], [-B,-B], c='green', lw=1.5)

	plt.scatter([max(df['t'])], [B if max(df['value']) > B else -B], s=80, facecolors='none', edgecolors='r', lw=2)

	plt.savefig('output/sample_path.svg')
	plt.show()

	np.random.seed(22)
	dt = 0.0025
	ws = [0]
	ws2 = [0]
	ts = [0]
	T = 1.5
	N = int(T/dt)
	tau = None

	for i in range(N):
		dw = np.random.normal(0,np.sqrt(dt))
		ws.append(ws[-1]+dw)
		ts.append(ts[-1] + dt)

		if tau is None:
			ws2.append(ws2[-1]+dw)
		else:
			ws2.append(ws2[-1]-dw)

		if tau is None and ws[-1] >= B:
			tau = ts[-1]

	plt.plot([0, T], [B,B], c='green', lw=1.5)
	plt.plot([0, T], [-B,-B], c='green', lw=1.5)
	plt.plot(ts,ws2, label='Path reflected at $\\tau_b$')
	plt.plot(ts,ws, label='Original path')
	
	plt.legend()
	plt.savefig('output/reflected_path.svg')
	plt.show()
