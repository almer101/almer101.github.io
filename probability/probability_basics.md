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

# Discrete Probability Basics

*Date Posted: 23 January 2024*

## Introduction

Here we will introduce the basics of probability that many people cover in the undergrad studies at a university. The goal is to provide a set of the most important concepts and notions that are necessary for understanding any more advanced concepts in probability.

## Probability of an Event

In probability you will frequently hear a word event, which can be basically anything, here are some examples of events: 

- *On a single coin flip heads ($H$) appears*
- *Number 6 appeared in three consecutive 6-sided-die throws*
- *A train arrived before the 12:00h, which was the scheduled arrival time*
- *Price of the stock $S$ in one year time is be above 120 EUR*
- ...

This list is infinite, but I think it is important to have in mind what an **occurrence of an event** means. Given certain assumptions, we could calculate the probability of each of these events. A probability (often denoted by $\mathbb{P}$ or $p$) is a number in interval $[0,1]$ that is assigned to an event ($E$). *Special cases* include: 

- $\mathbb{P}(E)=0 \longrightarrow $ the event $E$ is impossible
- $\mathbb{P}(E)=1 \longrightarrow $ the event $E$ is surely happening

Let us have a look at the example of a 6-sided fair die. A die show any number from one to six, all with equal probability $p$. In the case of a fair die, the probability is $$p=\frac{1}{6}$$

Now we need a way to represent the outcome of a die throw. In order to do that we will introduce a concept of a **random variable**. *Random variable* is a way of assigning a value (most often it is an actual number) to an outcome of an experiment. A very simple random variable is exactly the outcome of a die throw, where we will assign the value of $1$ if number one appears on the die, number $2$ if the number two appears on the die, and so on. 

```{note}
My goal here is not to present these concepts in a mathematically rigorous way, but I still think that for you to be able to read other materials in the books or in the internet, it would be nice to show at least one or two examples of what it would look like to write down a die thrown outcome as a random variable. 

Let us denote with $\omega_i$ an **event** of a number $i$ appearing on the die, that is:

$$
\begin{split}
	\omega_1 &= \{\text{number 1 appears on the die}\} \\
	\omega_2 &= \{\text{number 2 appears on the die}\} \\
	&\hspace{0.2cm}\vdots \\
	\omega_6 &= \{\text{number 6 appears on the die}\}
\end{split}
$$

Then a random variable $X$ that represents the outcome of our die will simply be $X(\omega_i)=i$, that is:

$$
\begin{split}
	X(\omega_1) &= 1 \\
	X(\omega_2) &= 2 \\
	&\hspace{0.2cm}\vdots \\
	X(\omega_6) &= 6 \\
\end{split}
$$

We can also imagine a random variable $Y$ that represents the squared outcome of our die throw, that is:

$$
\begin{split}
	Y(\omega_1) &= 1^2 = 1\\
	Y(\omega_2) &= 2^2 = 4\\
	&\hspace{0.2cm}\vdots \\
	Y(\omega_6) &= 6^2 = 36
\end{split}
$$

Or even a random variable $Z$ that takes the value of $1$ if the the number on the die is even, and $0$ if the number is odd:

$$
\begin{split}
	Z(\omega_1) = Z(\omega_3) = Z(\omega_5) = 0\\
	Z(\omega_2) = Z(\omega_4) = Z(\omega_6) = 1
\end{split}
$$

```

Now that we have a good understanding of what an event $\omega$ is, what a random variable is, let us present a compact way to write down random variables (discrete random variables like the ones above):

$$
X \sim
\left(\begin{array}{cccccc}
	1 & 2 & 3 & 4 & 5 & 6 \\
	\frac{1}{6} & \frac{1}{6} & \frac{1}{6} & \frac{1}{6} & \frac{1}{6} & \frac{1}{6}
\end{array}\right)
$$

where the first row shows all the values that a random variable can take, and the second row shows the probabilities of $X$ taking that value, i.e. $\mathbb{P}(\omega_i)$. For the case of $Y$ from above, that would be:

$$
Y \sim
\left(\begin{array}{cccccc}
	1 & 4 & 9 & 16 & 25 & 36 \\
	\frac{1}{6} & \frac{1}{6} & \frac{1}{6} & \frac{1}{6} & \frac{1}{6} & \frac{1}{6}
\end{array}\right)
$$

and for $Z$:

$$
Z \sim
\left(\begin{array}{cc}
	0 & 1 \\
	0.5 & 0.5
\end{array}\right)
$$

where $0.5$ comes from the fact that any of the events $\omega_1, \omega_3, \omega_5$ can happen in order for $Z$ to take value of 0, the same goes for the even numbers. 

## Expectation and Variance

Now that we have described the concept of a random variable, it is time for us to show what does it mean to take the *expectation* or the	 *variance* of a random variable. An **expectation** (or **expected value**) of a discrete random variable is defined as follows: 

$$\mathbb{E}(X) = \sum_{i=1}^n X(\omega_i)\mathbb{P}(\omega_i) = \sum_{i=1}^n x_i p_i$$

So in other words, the expectation is the weighted sum of all possible outcomes of a random variable, weighted by the probability of those outcomes happening. Let us try to take the expectation of a random variable $X$ from above:

$$
\begin{split}
\mathbb{E}(X) &= \sum_{i=1}^6 X(\omega_i)\cdot\mathbb{P}(\omega_i) \\
\mathbb{E}(X) &= \sum_{i=1}^6 i\cdot\frac{1}{6} \\
\mathbb{E}(X) &= 1\cdot\frac{1}{6} + 2\cdot\frac{1}{6} + \cdots + 6\cdot\frac{1}{6} \\
\mathbb{E}(X) &= 3.5 
\end{split}
$$

Expected value is a very important concept in probability and probably the concept that (alongside variance) you will use the most. But what is variance? **Variance** of a random variable appears as a needed concept when you ask yourself *"How far away do I expect the random variable to be from its expected value?"*. If we want to write that mathematically (assuming we want the average of the square of the distance from the expected value) we would get:

$$Var(X) = \mathbb{E}\left( \left(X - \mathbb{E}(X)\right)^2 \right) = \mathbb{E}\left(X^2 - 2X\mathbb{E}(X) + \left( \mathbb{E}(X) \right)^2\right) = \mathbb{E}(X^2) - 2\left(\mathbb{E}(X)\right)^2 + \left(\mathbb{E}(X)\right)^2 = \mathbb{E}(X^2) - \left(\mathbb{E}(X)\right)^2$$

Where many times the last expression is very handy and could make your calculations quicker. Let us calculate the variance of our random variable $X$:

$$Var(X) = \mathbb{E}(X^2) - \left(\mathbb{E}(X)\right)^2$$

Since we have already calculated the expectation ($\mathbb{E}(X)$) we only have to calculate the $\mathbb{E}(X^2)$, and now we will show how simple that actually is. If we square a random variable, this means that we are squaring each outcome of that random variable, i.e. 

$$X^2 \sim
\left(\begin{array}{cccccc}
	1 & 4 & 9 & 16 & 25 & 36 \\
	\frac{1}{6} & \frac{1}{6} & \frac{1}{6} & \frac{1}{6} & \frac{1}{6} & \frac{1}{6}
\end{array}\right)$$

So the expected value of $X^2$ will be:

$$
\begin{split}
\mathbb{E}(X^2) &= \sum_{i=1}^6 \left(X(\omega_i)\right)^2\cdot\mathbb{P}(\omega_i) \\
\mathbb{E}(X^2) &= \sum_{i=1}^6 i^2\cdot\frac{1}{6} \\
\mathbb{E}(X^2) &= 1^2\cdot\frac{1}{6} + 2^2\cdot\frac{1}{6} + \cdots + 6^2\cdot\frac{1}{6} \\
\mathbb{E}(X^2) &=\frac{91}{6} \approx 15.1667 
\end{split}
$$

And finally the variance is: 

$$Var(X) = \mathbb{E}(X^2) - \left(\mathbb{E}(X)\right)^2 = \frac{91}{6} - (3.5)^2 = \frac{35}{12} \approx 2.91667$$

```{see-also}
There is also a notion of **covariance** and it can be calcualted as follows:

$$Cov(X,Y)=\mathbb{E}\left( (X-\mathbb{E}(X))(Y-\mathbb{E}(Y)) \right) = \cdots = \mathbb{E}(XY) - \mathbb{E}(X)\mathbb{E}(Y)$$

It is immediatelly visible that $Cov(X,X) = Var(X)$
```

## Examples with Expected Value

Let us now imagine that we throw a die 5 times in a row and we are interested in the sum of our throws. We want to calculate the expected value and the variance of that sum. We will denote the outcome of the $i$-th throw with $X_i$. All throws are *independent* (we will talk more about independence in the next chapters) and they have the same *distribution* (IID - independent identically distributed). The distribution of each throw is:

$$X_i \sim
\left(\begin{array}{cccccc}
	1 & 2 & 3 & 4 & 5 & 6 \\
	\frac{1}{6} & \frac{1}{6} & \frac{1}{6} & \frac{1}{6} & \frac{1}{6} & \frac{1}{6}
\end{array}\right)$$

We define $Y$ as the sum of our throws: 

$$Y = X_1 + \cdots + X_5 = \sum_{i=0}^5 X_i$$

We are interested in the expected value of such sum. 

```{note}
It can easily be shown that the expectation of the sum of random variables is always equal to the sum of the expectations of random variables that are included in the sum: 

$$\mathbb{E}\left( \sum_{i} X_i\right) = \sum_i \mathbb{E}(X_i)$$

This holds even if the random variables are **not independent**.
```

With this in our toolbox we can easily calculate the expected value of $Y$:

$$\mathbb{E}(Y) = \mathbb{E}\left( \sum_{i=0}^5 X_i \right) = \sum_{i=0}^5 \mathbb{E}(X_i) = 5\cdot 3.5 = 17.5$$

With variance the story is slightly different and it matters if the random variables are independent or not. 

```{note}
The full formula of the variance of the sum of random variable is as follows:

$$Var\left( \sum_{i} X_i\right) = \sum_i Var(X_i) + 2\sum_{i<j}Cov(X_i,X_j)$$

Note that the variance of the sum will be equal to the sum of variance if the random variables are **uncorrelated**, which is different from **independence**. 
```

```{important}
Independence is a stronger condition: 

$$
\begin{split}
	X,Y \text{ independent } \Rightarrow X,Y \text{ uncorrelated } \\
	X,Y \text{ uncorrelated } \nRightarrow X,Y \text{ independent }
\end{split}
$$
```

In our case, however, the $X_i$ are independent and we can easily calculate the variance of $Y$:

$$Var(Y) = \sum_{i=1}^5 Var(X_i) + 2\sum_{i<j}0 = \sum_{i=1}^5 Var(X_i) = 5 \cdot \frac{35}{12} \approx 14.58$$

<!--## Conditional probability-->

