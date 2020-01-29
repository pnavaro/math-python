x, dx = np.linspace(-6,6,100, retstep=True)
f = np.exp(-x**2)
plt.plot(x, f)

0.5 * dx * np.sum(f[:-1] + f[1:]), np.trapz(f, x)
