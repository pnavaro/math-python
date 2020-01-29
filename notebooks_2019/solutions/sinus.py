x, dx = np.linspace(0,4*np.pi,100, retstep=True)
y = np.sin(x)
plt.plot(x, y);
plt.plot(x[:-1]+dx/2, (y[1:]-y[:-1])/dx, 'k-*')
