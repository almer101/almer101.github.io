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

# Yield Curve Construction

<!--*Date Posted: 13 April 2025*-->

## Introduction

In the world of fixed income the construction of the discount curve (also called zero curve) is a fundamental step in the modelling exercise. The job of an interest rate model is to describe the movements of the discount curve through time, starting from a known initial state/condition. In the Piterbarg book (see references), three main classes of curves are examined - simply bootstrapped $C^0$ curves, local splines $C^1$, and full smoothing splines $C^2$. The family of splines we will examine in this post belong to $C^2$ splines.

Just to get agree on some notation before we dive into curve construction techniques. We say that a price of a zero-coupon bond with maturity $T$ is given by: 

$$P(0,T) = e^{-T\cdot y(T)}$$

where $y(T)$ is the discount (or zero) rate. We are interested in finding the curve that gives us the value of $y(t)$ for every $t$ in our domain (this can be 30, 40, 50 years, or even more in some cases). It will also be useful to build a curve of instantaneous forward rates from our yield curve. To do that we start from the following equality:

$$P(0,T) = e^{-T\cdot y(T)} = e^{-\int_0^T f_u du}.$$

It is obvious that for these 2 things to be equal, the exponents need to be equal

$$T\cdot y(T) = \int_0^T f_u du$$

We can now take a derivative w.r.t maturity $T$ and get:

$$f(T) = y(T) + \frac{d y(T)}{dT}T$$

Which tells us how the spot and forward rates are related. We can immediately see, that if we want to work with instantaneous forward curves, it will be important for our yield curve $y(t)$ to be differentiable

## Local cubic splines $C^1$

With a general $C^0$ bootstrapped yield curve, we end up with a piecewise linear yield curve, which results in a saw-like forward curve as the yield curve is fully differentiable. To improve on this we can build a cubic spline that will produce a smooth yield curve, but would generally not give us a smooth forward curve. Smooth forward curve is important for pricing certain interest rate derivatives to produce realistic and stable prices. To improve on that, we want to impose certain restrictions on the shape of our curves that will not only fit our data, but also produce smooth forward curve. 

## Moving towards $C^2$ splines

We are staying in the same sphere of cubic splines, but we now want to impose the twice differentiability to the curve. Since we are still working with cubic splines, it is necessary for the second derivative to be piecewise linear. 

![Piecewise linear second derivative](imgs/piecewise_linear.svg)

That means that the second derivative can be expressed as:

$$y''(x) = \frac{x_{i+1} - x}{x_{i+1}-x_{i}}y_i'' + \frac{x-x_i}{x_{i+1}-x_i}y_{i+1}''$$

for all $x\in[x_i, x_{i+1}]$. We can now integrate the expression above to find the expression for $y'(x)$. For some easier manipulation, we will denote $y_{i}''$ with $d_i$. 

$$
\begin{split}
	y'(x) = \frac{d_i}{x_{i+1}-x_i}\int(x_{i+1}-u)du + \frac{d_{i+1}}{x_{i+1}-x_i}\int(u-x_i)du + C_2 \\
	y'(x) = \frac{-d_i}{x_{i+1}-x_i}\frac{1}{2}(x_{i+1}-x)^2 + \frac{d_{i+1}}{x_{i+1}-x_i}\frac{1}{2}(x-x_i)^2 + C_2
\end{split}
$$

To simplify further the notation, we will denote $(x_{i+1}-x_i)$ with $h_i$, so then we have:

$$y'(x) = \frac{-d_i}{2h_i}(x_{i+1}-x)^2 + \frac{d_{i+1}}{2h_i}(x-x_i)^2 + C_2$$

To get the expression for $y(x)$ we integrate again the expression:

$$y(x) = \frac{d_i}{6h_i}(x_{i+1}-x)^3 + \frac{d_{i+1}}{6h_i}(x-x_i)^3 + C_2x + C_1$$

## Calculating $C_1$ and $C_2$

Since our starting point were actually the points on the curve ($y_i$) we want our interpolation to exactly pass through those points, or more specifically;

$$y(x_i) = y_i \hspace{0.4cm}\text{ and }\hspace{0.4cm} y(x_{i+1}) = y_{i+1}$$

That means that the following two equations need to hold:

$$
\begin{split}
	y(x_i) &= \frac{d_i}{6h_i}h_i^3 + 0 + C_2x_i+C_1=y_i \\
	y(x_i) &= 0 + \frac{d_{i+1}}{6h_i}h_i^3 + C_2x_{i+1}+C_1=y_{i+1}
\end{split}
$$

Solving the system, this gives us the expressions for $C_1$ and $C_2$:

$$
\begin{split}
	C_1 &= y_i - d_i\frac{h_i^2}{6} - \frac{x_i}{h_i}(y_{i+1}-y_i) + (d_{i+1}-d_i)\frac{h_ix_i}{6} \\
	C_2 &= \frac{1}{h_i}(y_{i+1}-y_i) - (d_{i+1}-d_i)\frac{h_i}{6}
\end{split}
$$

Now we can plug that in the equation for $y(x)$ to get the final expression:

$$
\begin{split}
y(x) &= \frac{d_i}{6h_i}(x_{i+1}-x)^3 + \frac{d_{i+1}}{6h_i}(x-x_i)^3 + C_2x + C_1 \\
		&= \frac{d_i}{6h_i}(x_{i+1}-x)^3 + \frac{d_{i+1}}{6h_i}(x-x_i)^3 \\
		&\hspace{0.5cm}+ \frac{x}{h_i}(y_{i+1}-y_i) - (d_{i+1}-d_i)\frac{xh_i}{6} \\
		&\hspace{0.5cm}+ y_i - d_i\frac{h_i^2}{6} - \frac{x_i}{h_i}(y_{i+1}-y_i) + (d_{i+1}-d_i)\frac{h_ix_i}{6} \\
	 &= \frac{d_i}{6h_i}(x_{i+1}-x)^3 + \frac{d_{i+1}}{6h_i}(x-x_i)^3 + (y_{i+1}-y_i)\left[\frac{x}{h_i} - \frac{x_i}{h_i}\right] \\
	 &\hspace{0.5cm}+ \frac{(d_{i+1}-d_i)}{6}[-xh_i+x_ih_i] + y_i - d_i\frac{h_i^2}{6}
\end{split}
$$

Which gives us the expression:

$$y(x) = \frac{d_i}{6h_i}(x_{i+1}-x)^3 + \frac{d_{i+1}}{6h_i}(x-x_i)^3 + (x-x_i)\left[\frac{y_{i+1}-y_i}{h_i} - (d_{i+1}-d_i)\frac{h_i}{6}\right] - d_i\frac{h_i^2}{6} + y_i$$

## Additional requirements and solving the system

Since we only know the values of $y_i$ and not what $y_i''$ should be, we need to calculate those values in order to know how the final curve looks like. There is another requirement we need to impose on our curve in order for it to be complete, which will also help us in determining the values of $d_i=y_i''$.

We already know that our second derivative is continuous (our starting assumption), and we have calculated $C_1$ and $C_2$ such that the curve will pass through the data points $y_i$. We need to ensure that also our first derivative ($y'(x)$) is continuous, and we can do so by ensuring that the value of $y'(x_i)$ defined on the interval $[x_{i-1}, x_i]$ is the same as the value of $y'(x_i)$ defined on the interval $[x_i, x_{i+1}]$.

Let us do that. The expression for $y'(x)$ on an interval $[x_{i-1}, x_i]$ is given by:

$$y'(x) = -\frac{d_{i-1}}{2h_{i-1}}(x_i-x)^2 + \frac{d_i}{2h_{i-1}}(x-x_{i-1})^2 + \frac{y_i-y_{i-1}}{h_{i-1}}-(d_i-d_{i-1})\frac{h_{i-1}}{6}$$

and by setting $x=x_i$, we get

$$
\begin{split}
y'(x_i) &= \frac{d_i}{2h_{i-1}}h_{i-1}^2 + \frac{y_i-y_{i-1}}{h_{i-1}}-(d_i-d_{i-1})\frac{h_{i-1}}{6} \\
	&= \frac{d_i}{2}h_{i-1} + \frac{y_i-y_{i-1}}{h_{i-1}}-(d_i-d_{i-1})\frac{h_{i-1}}{6}
\end{split}
$$

Similarly, we can get the expression for $y'(x)$ on the interval $[x_i,x_{i+1}]$:

$$y'(x) = -\frac{d_{i}}{2h_{i}}(x_{i+1}-x)^2 + \frac{d_{i+1}}{2h_{i}}(x-x_{i})^2 + \frac{y_{i+1}-y_{i}}{h_{i}}-(d_{i+1}-d_{i})\frac{h_{i}}{6}$$

and by setting $x=x_i$, we get

$$
\begin{split}
y'(x_i) &= -\frac{d_{i}}{2h_{i}}h_i^2 + \frac{y_{i+1}-y_{i}}{h_{i}}-(d_{i+1}-d_{i})\frac{h_{i}}{6} \\
	&= -\frac{d_{i}}{2}h_i + \frac{y_{i+1}-y_{i}}{h_{i}}-(d_{i+1}-d_{i})\frac{h_{i}}{6}
\end{split}
$$

Now, as stated earlier, these two expressions for $y'(x_i)$ need to be equal, that is:

$$
\begin{split}
\frac{d_i}{2}h_{i-1} + \frac{y_i-y_{i-1}}{h_{i-1}}-(d_i-d_{i-1})\frac{h_{i-1}}{6} &= -\frac{d_{i}}{2}h_i + \frac{y_{i+1}-y_{i}}{h_{i}}-(d_{i+1}-d_{i})\frac{h_{i}}{6} \\
\frac{h_{i-1}}{6}d_{i-1}+\frac{h_{i-1}+h_i}{3}d_i + \frac{h_i}{6}d_{i+1} &= \frac{y_{i+1}-y_i}{h_i} - \frac{y_{i}-y_{i-1}}{h_{i-1}}
\end{split}
$$

For all $i\in\{2,3,...,N-1\}$, and we define $d_1=y_1''=0$ and $d_N=y_N''=0$. This gives us a tri-diagonal system to solve. More specifically in matrix format the problem can be written as:

$$
\begin{bmatrix}
    \frac{1}{3}(h_1+h_2) & \frac{h_2}{6} & 0 & \cdots & 0 & 0 & 0 & 0\\
    \frac{h_2}{6} & \frac{1}{3}(h_2+h_3) & \frac{h_3}{6} & 0 & \cdots & 0 & 0 & 0\\
    0 & \frac{h_3}{6} & \frac{1}{3}(h_3+h_4) & \frac{h_4}{6} & 0 & \cdots & 0 & 0\\
    0 &  &  & \ddots &  &  & 0 & 0\\
    \vdots &  &  &  & 0 & \frac{h_{N-3}}{6} & \frac{1}{3}(h_{N-3}+h_{N-2}) & \frac{h_{N-2}}{6} \\
    0 & 0 & \cdots & 0 & 0 & 0 & \frac{h_{N-2}}{6} & \frac{1}{3}(h_{N-2}+h_{N-1})
\end{bmatrix} \cdot 
\begin{bmatrix}
	d_2 \\ d_3 \\ \\ \\ \vdots \\ \\ \\ d_{N-2}
\end{bmatrix} = 
\begin{bmatrix}
	\frac{y_{3}-y_2}{h_2} - \frac{y_{2}-y_{1}}{h_{1}} \\
	\frac{y_{4}-y_3}{h_3} - \frac{y_{3}-y_{2}}{h_{2}} \\
	\\
	\\
	\vdots \\
	\\
	\\
	\frac{y_{N}-y_{N-1}}{h_{N-1}} - \frac{y_{N-1}-y_{N-2}}{h_{N-2}} \\
\end{bmatrix}
$$

With the expression above, we now have a system of equations that we need to solve. This system is expressable as:

$$\mathbf{M}\cdot\vec{\mathbf{d}} = \vec{\mathbf{f}}$$

To solve it we would need to invert the matrix $\mathbf{M}$, but this can be costly. What we could do instead is to perform an LU decomposition and solve the system that way.

```{note}
**Reminder**: LU decomposition is a way of representing a matrix as a product of a lower triangular matrix (L) and an upper triangluar matrix (U). Usually, the elements on the diagonal of the lower triangular matrix are set to $1$:
$\mathbf{M}=L\cdot U = \begin{bmatrix}
	1 & 0 & 0 & \cdots & 0 \\
	l_{2,1} & 1 & 0 & \cdots & 0 \\
	l_{3,1} & l_{3,2} & 1 & \cdots & 0 \\
	\vdots & & & \ddots & \\
	l_{n,1} & l_{n,2} & l_{n,3} & \cdots & 1 \\
\end{bmatrix}
\begin{bmatrix}
	u_{1,1} & u_{1,2} & u_{1,3} & \cdots & u_{1,n} \\
	0 & u_{2,2} & u_{2,3} & \cdots & u_{2,n} \\
	0 & 0 & u_{3,3} & \cdots & u_{3,n} \\
	\vdots & & & \ddots & \\
	0 & 0 & 0 & \cdots & u_{n,n} \\
\end{bmatrix}$
```

On the below plot we can see the result of building the ESTR curve based on the real market data. The curve in red is the fitted yield curve, while in green we can see the smooth forward curve, exactly as we required in the setup of our problem:

![Resulting curve](imgs/c2_spline.svg)

## Summing it up

We have briefly explained how the $C^0$ and $C^1$ splines work and what their drawbacks are, then we have shown what improvements twice differentiable splines bring to the table and we have derived the solution for the problem. It is left as an exercise for the reader to implement this in their favorite programming language and put the theory to practice

I hope you enjoyed reading this post and that you found it useful!

## References

- [LBG Andersen, VV Piterbarg: Interest Rate Modeling. Volume 1: Foundations and Vanilla Models](https://books.google.co.uk/books/about/Interest_Rate_Modeling.html?id=oI2fcQAACAAJ&redir_esc=y)









