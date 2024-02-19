---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.11.5
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Bond prices under the Ornstein Uhlenbeck mean-reverting process


## Introduction
The OU mean-reverting process is often used to model interest rates and for this reason we will call our stochastic process $r$. This process is characterized by the following stochastic differential equation (SDE):

$$dr_t = k(m-r_t)dt + \sigma dW^\mathbb{P}_t$$

where $W^\mathbb{P}$ is the $\mathbb{P}$-standard Brownian motion and $\mathbb{P}$ is the historical probability. The parameters above represent: 

- $k$ characterizes the speed of mean reversion
- $m$ is the long-run mean of the rate $r_t$ 
- $\sigma$ is the volatility of the interest rate


## Bond price

A differential equation that describes the change in the value of a riskless asset (in our case we will assume that bonds are riskless) is given by:

$$\frac{dB(t)}{B(t)} = r_t dt$$

where we usually set an initial condition $B(0)=1$. This differential equation is easily solved and gives us the expression for the value of 1 unit of the riskless asset at any time $t$:

$$B(t) = B(0)\exp{\left(\int_0^t r_u du\right)} = \exp{\left(\int_0^t r_u du\right)}$$

```{note}
Keep in mind that in case that $r$ is constant, this formula collapses to $B(t)=e^{rt}$, but that is not very interesting, and we will now try to tame the stochastic process and see the expression for calculating the bond price when we have a stochastic interest rate. 
```

With the formula above we also know the expression for the present value of a 1 unit of money being paid at time $t$: 

$$B(0) = \exp{\left(-\int_0^t r_u du\right)}$$

Since an integral of a stochastic process is a random variable, we can calculate the today's price $p(0,t)$ of 1 unit maturing at time $t$ as a risk-neutral expectation of the above expression, that is:

$$p(0,t) = \mathbb{E}^\mathbb{Q}\left( e^{-\int_0^t r_u du} \right)$$

The goal of this post will be the calculation of that expected value. Here we have 2 problems to tackle: 

- Finding the risk-neutral probability measure
- Finding the distribution of $(e^{-\int_0^t r_u du})$


## Risk neutral probability measure $\mathbb{Q}$

Risk neutral probability measure is usually obtained such that we look at the discounted gain process of a risky security in the market and adjust the drift of $W^\mathbb{P}$ to obtain $W^\mathbb{Q}$. Here we, of course, rely on the [Girsanov theorem](https://en.wikipedia.org/wiki/Girsanov_theorem) that states that given a Brownian motion under $\mathbb{P}$, if we can find an adapted process $\nu_t$ such that [Novikov condition](https://en.wikipedia.org/wiki/Novikov%27s_condition) holds, then the following process is a Brownian motion under the new probability measure $\mathbb{Q}$: 

$$dW_t^\mathbb{Q} = \nu_t dt + dW_t^\mathbb{P}$$

This is a very powerful result, and it allows us to price financial products. We will assume here that the market price of risk is 

$$\nu_t = \nu = \frac{\mu_S-r}{\sigma_S}$$

where $\mu_S,r,\sigma_S$ are constants which results in our $\nu$ being a constant as well. For constants, the Novikov condition holds: 

$$\begin{gather}
\mathbb{E}\left[ \exp\left( \int_0^T \nu^2ds \right)\right] < +\infty \\
\mathbb{E}\left[ \exp\left( \nu^2 (T-0) \right)\right] < +\infty \\
e^{\nu^2 T} < +\infty \\
\end{gather}
$$

Then we know that $W_t^\mathbb{P}$ can be written as: 

$$dW_t^\mathbb{P} = -\nu dt + dW_t^\mathbb{Q}$$

## Solving the SDE
Let us now plug that in the initial SDE: 

$$\begin{gather}
dr_t = k(m-r_t)dt + \sigma(-\nu dt + dW_t^\mathbb{Q}) \\
dr_t = k(m-\frac{\sigma\nu}{k}-r_t)dt + \sigma dW_t^\mathbb{Q}
\end{gather}
$$

where we denote with $\vartheta=(m-\frac{\sigma\nu}{k})$ the long-run mean of the interest rate $r_t$ under the risk neutral probability measure $\mathbb{Q}$:

$$dr_t = k(\vartheta-r_t)dt + \sigma dW_t^\mathbb{Q}$$

This SDE has a famous solution that is achieved when assuming a transformation of the initial process $f(t, r_t)=r_t\cdot e^{kt}$, and an initial condition of $r(0)=r_0$. This is left to the reader as an exercie, but the solution will be provided down in the Appendix, in case this is one of the first times you are encountering SDEs. Anyhow, the solution for this process can be obtained and is:

$$r_t=e^{-kt}(r_0-\vartheta) + \vartheta + \sigma \int_0^t e^{-k(t-u)}dW_u^\mathbb{Q}$$

```{note}
The stochastic integral we have in the end is just a **random variable**. This seems silly to mention, but when I was studying stochastic processes, this really helped me to view them just as random variables.
```

In fact this is a very tamable version of a stochastic integral, because thanks to **Ito's isometry** we know that the distribution of this integral is normal under $\mathbb{Q}$:

$$\int_0^t e^{-k(t-u)}dW_u^\mathbb{Q} \sim \mathcal{N}\left(0, \int_0^t \left(e^{-k(t-u)}\right)^2 du\right) \sim \mathcal{N}\left( 0, \frac{1-e^{-2kt}}{2k} \right)$$

Let us denote that stochastic integral as a random variable $Y_t$:

$$Y_t=\int_0^t e^{-k(t-u)}dW_u^\mathbb{Q}$$

Then our final expression for the process $r_t$ looks like this:

$$r_t=e^{-kt}(r_0-\vartheta) + \vartheta + \sigma Y_t$$

## Working our way there...

First we need to find out the distribution of our stochastic integral $\left(\int_0^t r_u du\right)$. Let us do that step by step:

$$
\begin{split}
	\int_0^t r_u du &= r_0\int_0^t e^{-ku}du + \vartheta \int_0^t(1-e^{-ku})du + \sigma\int_0^t Y_u du \\
	&= -r_0\frac{1}{k}(e^{-kt}-1) + \vartheta t + \vartheta\frac{1}{k}(e^{-kt}-1) + \sigma\int_0^t Y_u du\\ 
	&= \frac{1}{k}(e^{-kt}-1)(\vartheta - r_0) + \vartheta t + \sigma\int_0^t Y_u du
\end{split}
$$

Since $Y_t$ are normally distributed, their sum would also be normally distributed, and since integral is an infinite sum, the element $\left( \int_0^t Y_u du \right)$ is also **normally distributed**. Moreover, we know that the mean of $Y_t$ is zero, so the mean of the integral will also be zero. Before jumping in the calculation of variance, let us calculate the covariance between two $Y_u$ and $Y_s$:

$$
\begin{split}
	Cov^\mathbb{Q}(Y_u, Y_s) &= \mathbb{E}^\mathbb{Q}\left( Y_uY_S\right) -  \mathbb{E}^\mathbb{Q}\left( Y_u \right) \mathbb{E}^\mathbb{Q}\left( Y_s \right) \\
	&= \mathbb{E}^\mathbb{Q}\left( Y_uY_S\right) - 0 \\
	&= \mathbb{E}^\mathbb{Q}\left( \int_0^u e^{-k(u-g)}dW_g^\mathbb{Q} \int_0^s e^{-k(s-h)}dW_h^\mathbb{Q} \right) \\
	&= e^{-k(u+s)}\mathbb{E}^\mathbb{Q}\left( \int_0^u \int_0^s e^{kg} e^{kh}dW_g^\mathbb{Q} dW_h^\mathbb{Q} \right)
\end{split}
$$

It is known that $dW_g^\mathbb{Q} dW_h^\mathbb{Q}=0, \forall h\neq g$, so those parts of the integral will disappear, while parts where $h=g$ will be equal to $dt$. This leads us to the following conclusion: 

$$
\begin{split}
	Cov^\mathbb{Q}(Y_u, Y_s) &= e^{-k(u+s)}\mathbb{E}^\mathbb{Q}\left( \int_0^{\min(u,s)} e^{2kh} dh \right) \\
	Cov^\mathbb{Q}(Y_u, Y_s) &= e^{-k(u+s)} \frac{1}{2k}(e^{2k\min(u,s)} - 1)
\end{split}
$$

With this result in place, we can proceed with our calculation of the variance:

$$
\begin{split}
	Var^\mathbb{Q}\left(\int_0^t Y_u du\right) &= \mathbb{E}^\mathbb{Q}\left( \int_0^t Y_u du \int_0^t Y_s ds \right) - \mathbb{E}^\mathbb{Q}\left( \int_0^t Y_u du\right)\mathbb{E}^\mathbb{Q}\left( \int_0^t Y_s ds \right) \\
	&= \mathbb{E}^\mathbb{Q}\left( \int_0^t Y_u du \int_0^t Y_s ds \right) - 0 \\
	&= \mathbb{E}^\mathbb{Q}\left( \int_0^t  \int_0^t Y_u Y_s du ds \right) \\
	&= \int_0^t \int_0^t \mathbb{E}^\mathbb{Q}\left(Y_u Y_s\right) du ds \\
	&= \int_0^t \int_0^t Cov^\mathbb{Q}(Y_u, Y_s) duds \\
	&= 2\int_0^t \int_0^s Cov^\mathbb{Q}(Y_u, Y_s) duds
\end{split}
$$

Notice that in the last step we changed only the limits of the second integral and added 2 in front to avoid calculating each covariance twice, but also to eliminate that $\min(u,s)$ function, because now we know that $u$ is always going to be smaller than $s$ if the limits of the integral are set up like this. Let us continue:

$$
\begin{split}
	Var^\mathbb{Q}\left(\int_0^t Y_u du\right) &= 2\int_0^t \int_0^s e^{-k(u+s)} \frac{1}{2k}(e^{2ku} - 1) duds \\
	&= \frac{1}{k}\int_0^t e^{-ks}\int_0^s e^{-ku}(e^{2ku} - 1)duds \\
	&= \frac{1}{k}\int_0^t e^{-ks}\int_0^s (e^{ku} - e^{-ku})duds \\
	&= \frac{1}{k}\int_0^t e^{-ks} \left( \frac{1}{k}\left(e^{ks}-1\right) + \frac{1}{k}\left(e^{-ks}-1\right) \right) ds \\
	&= \frac{1}{k^2}\int_0^t \left(1-e^{-ks}+e^{-2ks}-e^{-ks}\right) ds \\
	&= \frac{1}{k^2}\left( \int_0^t ds -2\int_0^t e^{-ks}ds + \int_0^t e^{-2ks}ds \right)\\
	&= \frac{1}{k^2}\left( t + \frac{2}{k} \left( e^{-kt} - 1 \right) - \frac{1}{2k} \left( e^{-2kt} - 1 \right) \right)\\
	&= \frac{1}{2k^2} \left( 2kt-3+4e^{-kt}-e^{-2kt} \right)
\end{split}
$$

And with this we have calculated the variance. So with this result now, we know the exact distribution of our $\left(\int_0^t r_u du\right)$. Let use the following notation

$$R_t = \int_0^t r_u du$$

And then we can write the expression from above once again:

$$R_t = \frac{1}{k}(e^{-kt}-1)(\vartheta - r_0) + \vartheta t + \sigma\int_0^t Y_u du$$

Now we can calculate the mean and the variance of $(-R_t)$:

$$\mathbb{E}^\mathbb{Q}(R_t) = \frac{1}{k}(e^{-kt}-1)(\vartheta - r_0) + \vartheta t = \mu_R$$

$$Var^\mathbb{Q}(R_t) = \sigma^2 \cdot Var^\mathbb{Q}\left( \int_0^t Y_u du\right)  = \frac{\sigma^2}{2k^2} \left( 2kt-3+4e^{-kt}-e^{-2kt}  \right) = \sigma_R^2$$

So to put it compactly:

$$R_t \sim \mathcal{N}\left(\mu_R, \sigma_R^2\right)$$

## Calculating the bond price

As we have stated in the beginning, the today's price of one unit of money that is paid at time $t$ is given by:

$$p(0,t) = \mathbb{E}^\mathbb{Q}\left( e^{-\int_0^t r_u du} \right) = \mathbb{E}^\mathbb{Q}\left( e^{-R_t} \right)$$

But since $R_t$ is normally distributed, we know how to calculate the expected value of a function where a normal random variable is the exponent:

$$
\begin{gather}
	p(0,t) = \mathbb{E}^\mathbb{Q}\left( e^{-R_t} \right) = e^{\mu_R+\frac{1}{2}\sigma_R^2} \\
	p(0,t) = \exp\left( \frac{1}{k}(e^{-kt}-1)(\vartheta - r_0) + \vartheta t + \frac{\sigma^2}{4k^2} \left( 2kt-3+4e^{-kt}-e^{-2kt}  \right) \right)
\end{gather}
$$

So given the current level of the rate $r_0$, and the parameters $k,\sigma,\vartheta$ we can calculate the risk neutral price of our bond. So for example, if our bond A pays 100 in two years time, the current price of the bond would be:

$$P_A = 100\cdot p(0,2) = 100\cdot \exp\left( \frac{1}{k}(e^{-2k}-1)(\vartheta - r_0) + 2\vartheta + \frac{\sigma^2}{4k^2} \left( 4k-3+4e^{-2k}-e^{-4k}  \right) \right)$$

## Concluding notes

This is a very interesting experience in my opinion, because it shows how to calculate the expression of a risk-neutral bond price. Often you do not actually have the parameters at hand, but rather you need to calculate them from the data. This would then be an optimization problem where you want to find $\hat{\Theta} = (k,\sigma,\vartheta)$, such that it minimizes the squared distances of market prices of bonds and the theoretical prices calculated with the formula above. More specifically, the problem would be: 

$$
\begin{split}	
	\hat{\Theta} := \arg \min_\Theta \sum \left( p_{market} - p_{theoretical} \right)^2
\end{split}
$$

where $p_{theoretical}$ is the theoretical price obtained with the formula for $p(0,t)$.

## References

- [The Trending Ornstein-Uhlenbeck process: A technical note](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3263789)
- Bocconi Lectures on Computational Methods in Finance