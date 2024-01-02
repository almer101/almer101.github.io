import matplotlib.pyplot as plt
plt.style.use('bmh')

def plot_data(x,y, label=None):
	if label is None:
		plt.plot(x,y, marker='o')
	else:
		plt.plot(x,y, marker='o', label=label)

	ax = plt.gca()
	ax.spines['bottom'].set_color('gray')
	ax.spines['left'].set_color('gray')
	ax.tick_params(axis='x', colors='gray')
	ax.tick_params(axis='y', colors='gray')
	ax.xaxis.label.set_color('gray')
	ax.yaxis.label.set_color('gray')



x = [1,2,3,5,10,20,30]
y = [2,2.35,2.5,2.56,2.6,2.65,2.67]
plot_data(x,y)
plt.ylim(1.8, 3)
plt.ylabel('$YTM (\%)$')
plt.xlabel('Maturity')

plt.savefig('../imgs/yc.png', transparent=True)
plt.show()

x = [1,2,3,5,10,20,30]
y_ts = [2,2.37,2.53,2.6,2.67,2.77,2.85]
plot_data(x,y_ts)
plt.ylim(1.8, 3)
plt.ylabel('Zero rate')
plt.xlabel('Maturity')

plt.savefig('../imgs/ts.png', transparent=True)
plt.show()

plot_data(x,y, label='Yield curve')
plot_data(x,y_ts, label='Term structure')
plt.ylim(1.8, 3)
plt.ylabel('Zero rate')
plt.xlabel('Maturity')
plt.legend()
plt.savefig('../imgs/yc_ts.png', transparent=True)
plt.show()

