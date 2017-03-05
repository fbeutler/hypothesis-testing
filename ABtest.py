
#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import t as student_t
from scipy.stats import norm

'''
This program goes through the different steps of an A/B test analysis
'''

def main():

	mu = 0
	variance = 1
	sigma = np.sqrt(variance)
	x = np.linspace(-10, 10, 1000)
	linestyles = ['-', '--', ':', '-.']
	dofs = [1, 2, 4, 30]

	# plot the different student t distributions
	for dof, ls in zip(dofs, linestyles):
		dist = student_t(dof, mu)
		label = r'$\mathrm{t}(dof=%1.f, \mu=%1.f)$' % (dof, mu)
		plt.plot(x, dist.pdf(x), ls=ls, color="black", label=label)

	plt.plot(x,norm.pdf(x, mu, sigma), color="green", linewidth=3, label=r'$\mathrm{N}(\mu=%1.f,\sigma=%1.f)$' % (mu, sigma))
	
	plt.xlim(-5, 5)
	plt.xlabel('$x$')
	plt.ylabel(r'$p(x|k)$')
	plt.title("Student's $t$ Distribution approximates Normal")

	plt.legend()
	plt.show()

	print "The 90%% confidence interval is = (%0.2f %0.2f)" % (norm.interval(0.9, loc=0, scale=1))
	download_rate_estimate = 0.02
	sigma_s = download_rate_estimate*(1. - download_rate_estimate)
	N = 5.3792*sigma_s/(0.1*download_rate_estimate)**2
	print "estimate of N = %d" % round(N)

	# Calculate the t value given the measured download fractions 
	download_fractions = [0.0187, 0.0210]
	print "t_A = %0.2f (for a measured download rate of 2.1%%)" % t_test(N, download_fractions[1], N, download_fractions[0])

  	return 


# function to calculate the t value
def t_test(N_A, p_A, N_0, p_0):
	variance_A = p_A*(1. - p_A)
	variance_0 = p_0*(1. - p_0)
	return (p_A - p_0)/np.sqrt(variance_A/N_A + variance_0/N_0)

if __name__ == '__main__':
  main()
