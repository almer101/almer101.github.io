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

# Domestic and Foreign Pricing Theory - Martingale Approach

<!--*Date Created: 28 June 2025*-->

## Introduction

In this post we will dive into the international market where we have two currencies which are connected through an exchange rate $X$. We will be referring to these markets as domestic and foreign market, where for example we can imagine the domestic market being EUR and the foreign market GBP. We will examine the relationship between the domestic and foreign martingale measures, or equivalently, domestic and foreign market prices of risk. This will allow us to get a deeper understanding of how the two are related. As a starting point for this post, we define the exchange rate $X$ as a ratio of units of domestic and foreign currency:

$$X=\frac{\text{units of domestic currency}}{\text{units of foreign currency}}$$

In the next section we will make some further assumptions and derive interesting results, let us dive into it.

## Derivation of the exchange rate expression

Let us assume that we have a domestic and foreign market with their respective short rates $r_t^d$ and $r_t^f$, which are $\mathcal{F}_t$-adapted processes.

We define three probability measures $\mathbb{P}$, $\mathbb{Q}^d$, $\mathbb{Q}^f$: objective measure, domestic martingale measure and foreign martingale measure - respectively. With that we also define three Radon-Nikodym derivatives:

$$
\begin{align}
	L_t^d = \frac{d\mathbb{Q}^d}{d\mathbb{P}}(t) \hspace{0.1cm}&\rightarrow \hspace{0.1cm} dL_t^d = L_t^d\varphi_t^d dW_t \\
	L_t^f = \frac{d\mathbb{Q}^f}{d\mathbb{P}}(t) \hspace{0.1cm}&\rightarrow \hspace{0.1cm} dL_t^f = L_t^f\varphi_t^f dW_t \\
	L_t = \frac{d\mathbb{Q}^f}{d\mathbb{Q}^d}(t) \hspace{0.1cm}&\rightarrow \hspace{0.1cm} dL_t = L_t\varphi_t dW_t^d \\
\end{align}
$$

Here $\varphi^f$, $\varphi^f$, $\varphi$ are Girsanov kernels, while market prices of risk are given by: 

$$\lambda_t^d = -\varphi_t^d \hspace{1cm} \lambda_t^f = -\varphi_t^f \hspace{1cm} \lambda_t = -\varphi_t$$

Now we want to price a foreign $T$-claim $Z^f$ in two different ways:

- Calculate the price in the foreign market and then convert the price to a domestic currency using the spot exchange rate $X_0$:

$$F^f(0) = \mathbb{E}^\mathbb{Q^f}\left[ e^{-\int_0^Tr_t^f dt} Z^f \right]$$
$$F^d(0) = X_0 F^f(0)$$

- Calculate the price of the same claim in domestic currency:

$$Z^d = X_TZ^f$$
$$F^d(0) = \mathbb{E}^\mathbb{Q^d}\left[ e^{-\int_0^Tr_t^d dt} Z^d \right] = \mathbb{E}^\mathbb{Q^d}\left[ e^{-\int_0^Tr_t^d dt} X_TZ^f \right]$$

By no-arbitrage, we know that these two ways of calculating the price need to yield the same result, i.e.:

$$\mathbb{E}^\mathbb{Q^f}\left[ X_0e^{-\int_0^Tr_t^f dt} Z^f \right] = \mathbb{E}^\mathbb{Q^d}\left[ e^{-\int_0^Tr_t^d dt} X_TZ^f \right]$$

These expectations are not taken with respect to the same probability measure, but earlier we have defined the Radon-Nikodym derivatives which allow as to change the probability measure:

$$\mathbb{E}^\mathbb{Q^d}\left[ X_0 \frac{L_T}{L_0} e^{-\int_0^Tr_t^f dt} Z^f \right] = \mathbb{E}^\mathbb{Q^d}\left[ e^{-\int_0^Tr_t^d dt} X_TZ^f \right]$$

Since $L_0=1$ and the two expressions inside expectations need to be equal we get:

$$X_0 L_T e^{-\int_0^Tr_t^f dt} = e^{-\int_0^Tr_t^d dt} X_T$$
$$X_T = X_0 L_T e^{-\int_0^T(r_u^f-r_u^d)du}$$

Finally, we get the expression for a general $t>0$:

$$
\begin{equation}
X_t = X_0 L_t e^{\int_0^t(r_u^d-r_u^f)du}
\end{equation}
$$

## Differential form for exchange rate $X_t$

From the previous expression we want to find the differential form for our exchange rate. We will do so by applying the Ito's lemma to the expression we just derived given that we know the dynamics of $L_t$. We express $X_t$ as a function of $L_t$:

$$
\begin{gather}
dL_t = L_t \varphi_t dW_t^d \\
X_t = h(t,L_t) = h(t,x) = X_0 \cdot x \cdot e^{\int_0^t (r_u^d - r_u^f) du} \\
\\
\frac{\partial h}{\partial x} = X_0 e^{\int_0^t (r_u^d - r_u^f) du} \hspace{0.5cm} \frac{\partial^2 h}{\partial x^2} = 0 \\
\frac{\partial h}{\partial t} = X_0 \cdot x \cdot (r_t^d - r_t^f) \cdot e^{\int_0^t (r_u^d - r_u^f) du} = h (r_t^d - r_t^f)
\end{gather}
$$

We plug the above into the Ito's formula and we get the dynamics for $h$:

$$
\begin{align}
	dh &= X_0L_t e^{\int_0^t (r_u^d - r_u^f) du}(r_t^d - r_t^f) dt + X_0L_t e^{\int_0^t (r_u^d - r_u^f) du} \varphi_t dW_t^d \\
	dh &= h (r_t^d - r_t^f) dt + h\varphi_t dW_t^d \\
	dX_t &= X_t (r_t^d - r_t^f) dt + X_t\sigma_t dW_t^d \\
\end{align}
$$

where $\sigma_t = \varphi_t$.

Now the thing that remains is to find the $\varphi_t$. This can be done![](data:image/jpeg;base64,LS0tCmp1cHl0ZXh0OgogIGZvcm1hdHM6IG1kOm15c3QKICB0ZXh0X3JlcHJlc2VudGF0aW9uOgogICAgZXh0ZW5zaW9uOiAubWQKICAgIGZvcm1hdF9uYW1lOiBteXN0CiAgICBmb3JtYXRfdmVyc2lvbjogMC4xMwogICAganVweXRleHRfdmVyc2lvbjogMS4xMS41Cmtlcm5lbHNwZWM6CiAgZGlzcGxheV9uYW1lOiBQeXRob24gMwogIGxhbmd1YWdlOiBweXRob24KICBuYW1lOiBweXRob24zCi0tLQoKIyBZaWVsZCBDdXJ2ZSBDb25zdHJ1Y3Rpb24KCipEYXRlIFBvc3RlZDogMTMgQXByaWwgMjAyNSoKCiMjIEludHJvZHVjdGlvbgoKSW4gdGhlIHdvcmxkIG9mIGZpeGVkIGluY29tZSB0aGUgY29uc3RydWN0aW9uIG9mIHRoZSBkaXNjb3VudCBjdXJ2ZSAoYWxzbyBjYWxsZWQgemVybyBjdXJ2ZSkgaXMgYSBmdW5kYW1lbnRhbCBzdGVwIGluIHRoZSBtb2RlbGxpbmcgZXhlcmNpc2UuIFRoZSBqb2Igb2YgYW4gaW50ZXJlc3QgcmF0ZSBtb2RlbCBpcyB0byBkZXNjcmliZSB0aGUgbW92ZW1lbnRzIG9mIHRoZSBkaXNjb3VudCBjdXJ2ZSB0aHJvdWdoIHRpbWUsIHN0YXJ0aW5nIGZyb20gYSBrbm93biBpbml0aWFsIHN0YXRlL2NvbmRpdGlvbi4gSW4gdGhlIFBpdGVyYmFyZyBib29rIChzZWUgcmVmZXJlbmNlcyksIHRocmVlIG1haW4gY2xhc3NlcyBvZiBjdXJ2ZXMgYXJlIGV4YW1pbmVkIC0gc2ltcGx5IGJvb3RzdHJhcHBlZCAkQ14wJCBjdXJ2ZXMsIGxvY2FsIHNwbGluZXMgJENeMSQsIGFuZCBmdWxsIHNtb290aGluZyBzcGxpbmVzICRDXjIkLiBUaGUgZmFtaWx5IG9mIHNwbGluZXMgd2Ugd2lsbCBleGFtaW5lIGluIHRoaXMgcG9zdCBiZWxvbmcgdG8gJENeMiQgc3BsaW5lcy4KCkp1c3QgdG8gZ2V0IGFncmVlIG9uIHNvbWUgbm90YXRpb24gYmVmb3JlIHdlIGRpdmUgaW50byBjdXJ2ZSBjb25zdHJ1Y3Rpb24gdGVjaG5pcXVlcy4gV2Ugc2F5IHRoYXQgYSBwcmljZSBvZiBhIHplcm8tY291cG9uIGJvbmQgd2l0aCBtYXR1cml0eSAkVCQgaXMgZ2l2ZW4gYnk6IAoKJCRQKDAsVCkgPSBlXnstVFxjZG90IHkoVCl9JCQKCndoZXJlICR5KFQpJCBpcyB0aGUgZGlzY291bnQgKG9yIHplcm8pIHJhdGUuIFdlIGFyZSBpbnRlcmVzdGVkIGluIGZpbmRpbmcgdGhlIGN1cnZlIHRoYXQgZ2l2ZXMgdXMgdGhlIHZhbHVlIG9mICR5KHQpJCBmb3IgZXZlcnkgJHQkIGluIG91ciBkb21haW4gKHRoaXMgY2FuIGJlIDMwLCA0MCwgNTAgeWVhcnMsIG9yIGV2ZW4gbW9yZSBpbiBzb21lIGNhc2VzKS4gSXQgd2lsbCBhbHNvIGJlIHVzZWZ1bCB0byBidWlsZCBhIGN1cnZlIG9mIGluc3RhbnRhbmVvdXMgZm9yd2FyZCByYXRlcyBmcm9tIG91ciB5aWVsZCBjdXJ2ZS4gVG8gZG8gdGhhdCB3ZSBzdGFydCBmcm9tIHRoZSBmb2xsb3dpbmcgZXF1YWxpdHk6CgokJFAoMCxUKSA9IGVeey1UXGNkb3QgeShUKX0gPSBlXnstXGludF8wXlQgZl91IGR1fS4kJAoKSXQgaXMgb2J2aW91cyB0aGF0IGZvciB0aGVzZSAyIHRoaW5ncyB0byBiZSBlcXVhbCwgdGhlIGV4cG9uZW50cyBuZWVkIHRvIGJlIGVxdWFsCgokJFRcY2RvdCB5KFQpID0gXGludF8wXlQgZl91IGR1JCQKCldlIGNhbiBub3cgdGFrZSBhIGRlcml2YXRpdmUgdy5yLnQgbWF0dXJpdHkgJFQkIGFuZCBnZXQ6CgokJGYoVCkgPSB5KFQpICsgXGZyYWN7ZCB5KFQpfXtkVH1UJCQKCldoaWNoIHRlbGxzIHVzIGhvdyB0aGUgc3BvdCBhbmQgZm9yd2FyZCByYXRlcyBhcmUgcmVsYXRlZC4gV2UgY2FuIGltbWVkaWF0ZWx5IHNlZSwgdGhhdCBpZiB3ZSB3YW50IHRvIHdvcmsgd2l0aCBpbnN0YW50YW5lb3VzIGZvcndhcmQgY3VydmVzLCBpdCB3aWxsIGJlIGltcG9ydGFudCBmb3Igb3VyIHlpZWxkIGN1cnZlICR5KHQpJCB0byBiZSBkaWZmZXJlbnRpYWJsZQoKIyMgTG9jYWwgY3ViaWMgc3BsaW5lcyAkQ14xJAoKV2l0aCBhIGdlbmVyYWwgJENeMCQgYm9vdHN0cmFwcGVkIHlpZWxkIGN1cnZlLCB3ZSBlbmQgdXAgd2l0aCBhIHBpZWNld2lzZSBsaW5lYXIgeWllbGQgY3VydmUsIHdoaWNoIHJlc3VsdHMgaW4gYSBzYXctbGlrZSBmb3J3YXJkIGN1cnZlIGFzIHRoZSB5aWVsZCBjdXJ2ZSBpcyBmdWxseSBkaWZmZXJlbnRpYWJsZS4gVG8gaW1wcm92ZSBvbiB0aGlzIHdlIGNhbiBidWlsZCBhIGN1YmljIHNwbGluZSB0aGF0IHdpbGwgcHJvZHVjZSBhIHNtb290aCB5aWVsZCBjdXJ2ZSwgYnV0IHdvdWxkIGdlbmVyYWxseSBub3QgZ2l2ZSB1cyBhIHNtb290aCBmb3J3YXJkIGN1cnZlLiBTbW9vdGggZm9yd2FyZCBjdXJ2ZSBpcyBpbXBvcnRhbnQgZm9yIHByaWNpbmcgY2VydGFpbiBpbnRlcmVzdCByYXRlIGRlcml2YXRpdmVzIHRvIHByb2R1Y2UgcmVhbGlzdGljIGFuZCBzdGFibGUgcHJpY2VzLiBUbyBpbXByb3ZlIG9uIHRoYXQsIHdlIHdhbnQgdG8gaW1wb3NlIGNlcnRhaW4gcmVzdHJpY3Rpb25zIG9uIHRoZSBzaGFwZSBvZiBvdXIgY3VydmVzIHRoYXQgd2lsbCBub3Qgb25seSBmaXQgb3VyIGRhdGEsIGJ1dCBhbHNvIHByb2R1Y2Ugc21vb3RoIGZvcndhcmQgY3VydmUuIAoKIyMgTW92aW5nIHRvd2FyZHMgJENeMiQgc3BsaW5lcwoKV2UgYXJlIHN0YXlpbmcgaW4gdGhlIHNhbWUgc3BoZXJlIG9mIGN1YmljIHNwbGluZXMsIGJ1dCB3ZSBub3cgd2FudCB0byBpbXBvc2UgdGhlIHR3aWNlIGRpZmZlcmVudGlhYmlsaXR5IHRvIHRoZSBjdXJ2ZS4gU2luY2Ugd2UgYXJlIHN0aWxsIHdvcmtpbmcgd2l0aCBjdWJpYyBzcGxpbmVzLCBpdCBpcyBuZWNlc3NhcnkgZm9yIHRoZSBzZWNvbmQgZGVyaXZhdGl2ZSB0byBiZSBwaWVjZXdpc2UgbGluZWFyLiAKCiFbUGllY2V3aXNlIGxpbmVhciBzZWNvbmQgZGVyaXZhdGl2ZV0oaW1ncy9waWVjZXdpc2VfbGluZWFyLnN2ZykKClRoYXQgbWVhbnMgdGhhdCB0aGUgc2Vjb25kIGRlcml2YXRpdmUgY2FuIGJlIGV4cHJlc3NlZCBhczoKCiQkeScnKHgpID0gXGZyYWN7eF97aSsxfSAtIHh9e3hfe2krMX0teF97aX19eV9pJycgKyBcZnJhY3t4LXhfaX17eF97aSsxfS14X2l9eV97aSsxfScnJCQKCmZvciBhbGwgJHhcaW5beF9pLCB4X3tpKzF9XSQuIFdlIGNhbiBub3cgaW50ZWdyYXRlIHRoZSBleHByZXNzaW9uIGFib3ZlIHRvIGZpbmQgdGhlIGV4cHJlc3Npb24gZm9yICR5Jyh4KSQuIEZvciBzb21lIGVhc2llciBtYW5pcHVsYXRpb24sIHdlIHdpbGwgZGVub3RlICR5X3tpfScnJCB3aXRoICRkX2kkLiAKCiQkClxiZWdpbntzcGxpdH0KCXknKHgpID0gXGZyYWN7ZF9pfXt4X3tpKzF9LXhfaX1caW50KHhfe2krMX0tdSlkdSArIFxmcmFje2Rfe2krMX19e3hfe2krMX0teF9pfVxpbnQodS14X2kpZHUgKyBDXzIgXFwKCXknKHgpID0gXGZyYWN7LWRfaX17eF97aSsxfS14X2l9XGZyYWN7MX17Mn0oeF97aSsxfS14KV4yICsgXGZyYWN7ZF97aSsxfX17eF97aSsxfS14X2l9XGZyYWN7MX17Mn0oeC14X2kpXjIgKyBDXzIKXGVuZHtzcGxpdH0KJCQKClRvIHNpbXBsaWZ5IGZ1cnRoZXIgdGhlIG5vdGF0aW9uLCB3ZSB3aWxsIGRlbm90ZSAkKHhfe2krMX0teF9pKSQgd2l0aCAkaF9pJCwgc28gdGhlbiB3ZSBoYXZlOgoKJCR5Jyh4KSA9IFxmcmFjey1kX2l9ezJoX2l9KHhfe2krMX0teCleMiArIFxmcmFje2Rfe2krMX19ezJoX2l9KHgteF9pKV4yICsgQ18yJCQKClRvIGdldCB0aGUgZXhwcmVzc2lvbiBmb3IgJHkoeCkkIHdlIGludGVncmF0ZSBhZ2FpbiB0aGUgZXhwcmVzc2lvbjoKCiQkeSh4KSA9IFxmcmFje2RfaX17NmhfaX0oeF97aSsxfS14KV4zICsgXGZyYWN7ZF97aSsxfX17NmhfaX0oeC14X2kpXjMgKyBDXzJ4ICsgQ18xJCQKCiMjIENhbGN1bGF0aW5nICRDXzEkIGFuZCAkQ18yJAoKU2luY2Ugb3VyIHN0YXJ0aW5nIHBvaW50IHdlcmUgYWN0dWFsbHkgdGhlIHBvaW50cyBvbiB0aGUgY3VydmUgKCR5X2kkKSB3ZSB3YW50IG91ciBpbnRlcnBvbGF0aW9uIHRvIGV4YWN0bHkgcGFzcyB0aHJvdWdoIHRob3NlIHBvaW50cywgb3IgbW9yZSBzcGVjaWZpY2FsbHk7CgokJHkoeF9pKSA9IHlfaSBcaHNwYWNlezAuNGNtfVx0ZXh0eyBhbmQgfVxoc3BhY2V7MC40Y219IHkoeF97aSsxfSkgPSB5X3tpKzF9JCQKClRoYXQgbWVhbnMgdGhhdCB0aGUgZm9sbG93aW5nIHR3byBlcXVhdGlvbnMgbmVlZCB0byBob2xkOgoKJCQKXGJlZ2lue3NwbGl0fQoJeSh4X2kpICY9IFxmcmFje2RfaX17NmhfaX1oX2leMyArIDAgKyBDXzJ4X2krQ18xPXlfaSBcXAoJeSh4X2kpICY9IDAgKyBcZnJhY3tkX3tpKzF9fXs2aF9pfWhfaV4zICsgQ18yeF97aSsxfStDXzE9eV97aSsxfQpcZW5ke3NwbGl0fQokJAoKU29sdmluZyB0aGUgc3lzdGVtLCB0aGlzIGdpdmVzIHVzIHRoZSBleHByZXNzaW9ucyBmb3IgJENfMSQgYW5kICRDXzIkOgoKJCQKXGJlZ2lue3NwbGl0fQoJQ18xICY9IHlfaSAtIGRfaVxmcmFje2hfaV4yfXs2fSAtIFxmcmFje3hfaX17aF9pfSh5X3tpKzF9LXlfaSkgKyAoZF97aSsxfS1kX2kpXGZyYWN7aF9peF9pfXs2fSBcXAoJQ18yICY9IFxmcmFjezF9e2hfaX0oeV97aSsxfS15X2kpIC0gKGRfe2krMX0tZF9pKVxmcmFje2hfaX17Nn0KXGVuZHtzcGxpdH0KJCQKCk5vdyB3ZSBjYW4gcGx1ZyB0aGF0IGluIHRoZSBlcXVhdGlvbiBmb3IgJHkoeCkkIHRvIGdldCB0aGUgZmluYWwgZXhwcmVzc2lvbjoKCiQkClxiZWdpbntzcGxpdH0KeSh4KSAmPSBcZnJhY3tkX2l9ezZoX2l9KHhfe2krMX0teCleMyArIFxmcmFje2Rfe2krMX19ezZoX2l9KHgteF9pKV4zICsgQ18yeCArIENfMSBcXAoJCSY9IFxmcmFje2RfaX17NmhfaX0oeF97aSsxfS14KV4zICsgXGZyYWN7ZF97aSsxfX17NmhfaX0oeC14X2kpXjMgXFwKCQkmXGhzcGFjZXswLjVjbX0rIFxmcmFje3h9e2hfaX0oeV97aSsxfS15X2kpIC0gKGRfe2krMX0tZF9pKVxmcmFje3hoX2l9ezZ9IFxcCgkJJlxoc3BhY2V7MC41Y219KyB5X2kgLSBkX2lcZnJhY3toX2leMn17Nn0gLSBcZnJhY3t4X2l9e2hfaX0oeV97aSsxfS15X2kpICsgKGRfe2krMX0tZF9pKVxmcmFje2hfaXhfaX17Nn0gXFwKCSAmPSBcZnJhY3tkX2l9ezZoX2l9KHhfe2krMX0teCleMyArIFxmcmFje2Rfe2krMX19ezZoX2l9KHgteF9pKV4zICsgKHlfe2krMX0teV9pKVxsZWZ0W1xmcmFje3h9e2hfaX0gLSBcZnJhY3t4X2l9e2hfaX1ccmlnaHRdIFxcCgkgJlxoc3BhY2V7MC41Y219KyBcZnJhY3soZF97aSsxfS1kX2kpfXs2fVsteGhfaSt4X2loX2ldICsgeV9pIC0gZF9pXGZyYWN7aF9pXjJ9ezZ9ClxlbmR7c3BsaXR9CiQkCgpXaGljaCBnaXZlcyB1cyB0aGUgZXhwcmVzc2lvbjoKCiQkeSh4KSA9IFxmcmFje2RfaX17NmhfaX0oeF97aSsxfS14KV4zICsgXGZyYWN7ZF97aSsxfX17NmhfaX0oeC14X2kpXjMgKyAoeC14X2kpXGxlZnRbXGZyYWN7eV97aSsxfS15X2l9e2hfaX0gLSAoZF97aSsxfS1kX2kpXGZyYWN7aF9pfXs2fVxyaWdodF0gLSBkX2lcZnJhY3toX2leMn17Nn0gKyB5X2kkJAoKIyMgQWRkaXRpb25hbCByZXF1aXJlbWVudHMgYW5kIHNvbHZpbmcgdGhlIHN5c3RlbQoKU2luY2Ugd2Ugb25seSBrbm93IHRoZSB2YWx1ZXMgb2YgJHlfaSQgYW5kIG5vdCB3aGF0ICR5X2knJyQgc2hvdWxkIGJlLCB3ZSBuZWVkIHRvIGNhbGN1bGF0ZSB0aG9zZSB2YWx1ZXMgaW4gb3JkZXIgdG8ga25vdyBob3cgdGhlIGZpbmFsIGN1cnZlIGxvb2tzIGxpa2UuIFRoZXJlIGlzIGFub3RoZXIgcmVxdWlyZW1lbnQgd2UgbmVlZCB0byBpbXBvc2Ugb24gb3VyIGN1cnZlIGluIG9yZGVyIGZvciBpdCB0byBiZSBjb21wbGV0ZSwgd2hpY2ggd2lsbCBhbHNvIGhlbHAgdXMgaW4gZGV0ZXJtaW5pbmcgdGhlIHZhbHVlcyBvZiAkZF9pPXlfaScnJC4KCldlIGFscmVhZHkga25vdyB0aGF0IG91ciBzZWNvbmQgZGVyaXZhdGl2ZSBpcyBjb250aW51b3VzIChvdXIgc3RhcnRpbmcgYXNzdW1wdGlvbiksIGFuZCB3ZSBoYXZlIGNhbGN1bGF0ZWQgJENfMSQgYW5kICRDXzIkIHN1Y2ggdGhhdCB0aGUgY3VydmUgd2lsbCBwYXNzIHRocm91Z2ggdGhlIGRhdGEgcG9pbnRzICR5X2kkLiBXZSBuZWVkIHRvIGVuc3VyZSB0aGF0IGFsc28gb3VyIGZpcnN0IGRlcml2YXRpdmUgKCR5Jyh4KSQpIGlzIGNvbnRpbnVvdXMsIGFuZCB3ZSBjYW4gZG8gc28gYnkgZW5zdXJpbmcgdGhhdCB0aGUgdmFsdWUgb2YgJHknKHhfaSkkIGRlZmluZWQgb24gdGhlIGludGVydmFsICRbeF97aS0xfSwgeF9pXSQgaXMgdGhlIHNhbWUgYXMgdGhlIHZhbHVlIG9mICR5Jyh4X2kpJCBkZWZpbmVkIG9uIHRoZSBpbnRlcnZhbCAkW3hfaSwgeF97aSsxfV0kLgoKTGV0IHVzIGRvIHRoYXQuIFRoZSBleHByZXNzaW9uIGZvciAkeScoeCkkIG9uIGFuIGludGVydmFsICRbeF97aS0xfSwgeF9pXSQgaXMgZ2l2ZW4gYnk6CgokJHknKHgpID0gLVxmcmFje2Rfe2ktMX19ezJoX3tpLTF9fSh4X2kteCleMiArIFxmcmFje2RfaX17Mmhfe2ktMX19KHgteF97aS0xfSleMiArIFxmcmFje3lfaS15X3tpLTF9fXtoX3tpLTF9fS0oZF9pLWRfe2ktMX0pXGZyYWN7aF97aS0xfX17Nn0kJAoKYW5kIGJ5IHNldHRpbmcgJHg9eF9pJCwgd2UgZ2V0CgokJApcYmVnaW57c3BsaXR9CnknKHhfaSkgJj0gXGZyYWN7ZF9pfXsyaF97aS0xfX1oX3tpLTF9XjIgKyBcZnJhY3t5X2kteV97aS0xfX17aF97aS0xfX0tKGRfaS1kX3tpLTF9KVxmcmFje2hfe2ktMX19ezZ9IFxcCgkmPSBcZnJhY3tkX2l9ezJ9aF97aS0xfSArIFxmcmFje3lfaS15X3tpLTF9fXtoX3tpLTF9fS0oZF9pLWRfe2ktMX0pXGZyYWN7aF97aS0xfX17Nn0KXGVuZHtzcGxpdH0KJCQKClNpbWlsYXJseSwgd2UgY2FuIGdldCB0aGUgZXhwcmVzc2lvbiBmb3IgJHknKHgpJCBvbiB0aGUgaW50ZXJ2YWwgJFt4X2kseF97aSsxfV0kOgoKJCR5Jyh4KSA9IC1cZnJhY3tkX3tpfX17Mmhfe2l9fSh4X3tpKzF9LXgpXjIgKyBcZnJhY3tkX3tpKzF9fXsyaF97aX19KHgteF97aX0pXjIgKyBcZnJhY3t5X3tpKzF9LXlfe2l9fXtoX3tpfX0tKGRfe2krMX0tZF97aX0pXGZyYWN7aF97aX19ezZ9JCQKCmFuZCBieSBzZXR0aW5nICR4PXhfaSQsIHdlIGdldAoKJCQKXGJlZ2lue3NwbGl0fQp5Jyh4X2kpICY9IC1cZnJhY3tkX3tpfX17Mmhfe2l9fWhfaV4yICsgXGZyYWN7eV97aSsxfS15X3tpfX17aF97aX19LShkX3tpKzF9LWRfe2l9KVxmcmFje2hfe2l9fXs2fSBcXAoJJj0gLVxmcmFje2Rfe2l9fXsyfWhfaSArIFxmcmFje3lfe2krMX0teV97aX19e2hfe2l9fS0oZF97aSsxfS1kX3tpfSlcZnJhY3toX3tpfX17Nn0KXGVuZHtzcGxpdH0KJCQKCk5vdywgYXMgc3RhdGVkIGVhcmxpZXIsIHRoZXNlIHR3byBleHByZXNzaW9ucyBmb3IgJHknKHhfaSkkIG5lZWQgdG8gYmUgZXF1YWwsIHRoYXQgaXM6CgokJApcYmVnaW57c3BsaXR9ClxmcmFje2RfaX17Mn1oX3tpLTF9ICsgXGZyYWN7eV9pLXlfe2ktMX19e2hfe2ktMX19LShkX2ktZF97aS0xfSlcZnJhY3toX3tpLTF9fXs2fSAmPSAtXGZyYWN7ZF97aX19ezJ9aF9pICsgXGZyYWN7eV97aSsxfS15X3tpfX17aF97aX19LShkX3tpKzF9LWRfe2l9KVxmcmFje2hfe2l9fXs2fSBcXApcZnJhY3toX3tpLTF9fXs2fWRfe2ktMX0rXGZyYWN7aF97aS0xfStoX2l9ezN9ZF9pICsgXGZyYWN7aF9pfXs2fWRfe2krMX0gJj0gXGZyYWN7eV97aSsxfS15X2l9e2hfaX0gLSBcZnJhY3t5X3tpfS15X3tpLTF9fXtoX3tpLTF9fQpcZW5ke3NwbGl0fQokJAoKRm9yIGFsbCAkaVxpblx7MiwzLC4uLixOLTFcfSQsIGFuZCB3ZSBkZWZpbmUgJGRfMT15XzEnJz0wJCBhbmQgJGRfTj15X04nJz0wJC4gVGhpcyBnaXZlcyB1cyBhIHRyaS1kaWFnb25hbCBzeXN0ZW0gdG8gc29sdmUuIE1vcmUgc3BlY2lmaWNhbGx5IGluIG1hdHJpeCBmb3JtYXQgdGhlIHByb2JsZW0gY2FuIGJlIHdyaXR0ZW4gYXM6CgokJApcYmVnaW57Ym1hdHJpeH0KICAgIFxmcmFjezF9ezN9KGhfMStoXzIpICYgXGZyYWN7aF8yfXs2fSAmIDAgJiBcY2RvdHMgJiAwICYgMCAmIDAgJiAwXFwKICAgIFxmcmFje2hfMn17Nn0gJiBcZnJhY3sxfXszfShoXzIraF8zKSAmIFxmcmFje2hfM317Nn0gJiAwICYgXGNkb3RzICYgMCAmIDAgJiAwXFwKICAgIDAgJiBcZnJhY3toXzN9ezZ9ICYgXGZyYWN7MX17M30oaF8zK2hfNCkgJiBcZnJhY3toXzR9ezZ9ICYgMCAmIFxjZG90cyAmIDAgJiAwXFwKICAgIDAgJiAgJiAgJiBcZGRvdHMgJiAgJiAgJiAwICYgMFxcCiAgICBcdmRvdHMgJiAgJiAgJiAgJiAwICYgXGZyYWN7aF97Ti0zfX17Nn0gJiBcZnJhY3sxfXszfShoX3tOLTN9K2hfe04tMn0pICYgXGZyYWN7aF97Ti0yfX17Nn0gXFwKICAgIDAgJiAwICYgXGNkb3RzICYgMCAmIDAgJiAwICYgXGZyYWN7aF97Ti0yfX17Nn0gJiBcZnJhY3sxfXszfShoX3tOLTJ9K2hfe04tMX0pClxlbmR7Ym1hdHJpeH0gXGNkb3QgClxiZWdpbntibWF0cml4fQoJZF8yIFxcIGRfMyBcXCBcXCBcXCBcdmRvdHMgXFwgXFwgXFwgZF97Ti0yfQpcZW5ke2JtYXRyaXh9ID0gClxiZWdpbntibWF0cml4fQoJXGZyYWN7eV97M30teV8yfXtoXzJ9IC0gXGZyYWN7eV97Mn0teV97MX19e2hfezF9fSBcXAoJXGZyYWN7eV97NH0teV8zfXtoXzN9IC0gXGZyYWN7eV97M30teV97Mn19e2hfezJ9fSBcXAoJXFwKCVxcCglcdmRvdHMgXFwKCVxcCglcXAoJXGZyYWN7eV97Tn0teV97Ti0xfX17aF97Ti0xfX0gLSBcZnJhY3t5X3tOLTF9LXlfe04tMn19e2hfe04tMn19IFxcClxlbmR7Ym1hdHJpeH0KJCQKCldpdGggdGhlIGV4cHJlc3Npb24gYWJvdmUsIHdlIG5vdyBoYXZlIGEgc3lzdGVtIG9mIGVxdWF0aW9ucyB0aGF0IHdlIG5lZWQgdG8gc29sdmUuIFRoaXMgc3lzdGVtIGlzIGV4cHJlc3NhYmxlIGFzOgoKJCRcbWF0aGJme019XGNkb3RcdmVje1xtYXRoYmZ7ZH19ID0gXHZlY3tcbWF0aGJme2Z9fSQkCgpUbyBzb2x2ZSBpdCB3ZSB3b3VsZCBuZWVkIHRvIGludmVydCB0aGUgbWF0cml4ICRcbWF0aGJme019JCwgYnV0IHRoaXMgY2FuIGJlIGNvc3RseS4gV2hhdCB3ZSBjb3VsZCBkbyBpbnN0ZWFkIGlzIHRvIHBlcmZvcm0gYW4gTFUgZGVjb21wb3NpdGlvbiBhbmQgc29sdmUgdGhlIHN5c3RlbSB0aGF0IHdheS4KCmBgYHtub3RlfQoqKlJlbWluZGVyKio6IExVIGRlY29tcG9zaXRpb24gaXMgYSB3YXkgb2YgcmVwcmVzZW50aW5nIGEgbWF0cml4IGFzIGEgcHJvZHVjdCBvZiBhIGxvd2VyIHRyaWFuZ3VsYXIgbWF0cml4IChMKSBhbmQgYW4gdXBwZXIgdHJpYW5nbHVhciBtYXRyaXggKFUpLiBVc3VhbGx5LCB0aGUgZWxlbWVudHMgb24gdGhlIGRpYWdvbmFsIG9mIHRoZSBsb3dlciB0cmlhbmd1bGFyIG1hdHJpeCBhcmUgc2V0IHRvICQxJDoKJFxtYXRoYmZ7TX09TFxjZG90IFUgPSBcYmVnaW57Ym1hdHJpeH0KCTEgJiAwICYgMCAmIFxjZG90cyAmIDAgXFwKCWxfezIsMX0gJiAxICYgMCAmIFxjZG90cyAmIDAgXFwKCWxfezMsMX0gJiBsX3szLDJ9ICYgMSAmIFxjZG90cyAmIDAgXFwKCVx2ZG90cyAmICYgJiBcZGRvdHMgJiBcXAoJbF97biwxfSAmIGxfe24sMn0gJiBsX3tuLDN9ICYgXGNkb3RzICYgMSBcXApcZW5ke2JtYXRyaXh9ClxiZWdpbntibWF0cml4fQoJdV97MSwxfSAmIHVfezEsMn0gJiB1X3sxLDN9ICYgXGNkb3RzICYgdV97MSxufSBcXAoJMCAmIHVfezIsMn0gJiB1X3syLDN9ICYgXGNkb3RzICYgdV97MixufSBcXAoJMCAmIDAgJiB1X3szLDN9ICYgXGNkb3RzICYgdV97MyxufSBcXAoJXHZkb3RzICYgJiAmIFxkZG90cyAmIFxcCgkwICYgMCAmIDAgJiBcY2RvdHMgJiB1X3tuLG59IFxcClxlbmR7Ym1hdHJpeH0kCmBgYAoKT24gdGhlIGJlbG93IHBsb3Qgd2UgY2FuIHNlZSB0aGUgcmVzdWx0IG9mIGJ1aWxkaW5nIHRoZSBFU1RSIGN1cnZlIGJhc2VkIG9uIHRoZSByZWFsIG1hcmtldCBkYXRhLiBUaGUgY3VydmUgaW4gcmVkIGlzIHRoZSBmaXR0ZWQgeWllbGQgY3VydmUsIHdoaWxlIGluIGdyZWVuIHdlIGNhbiBzZWUgdGhlIHNtb290aCBmb3J3YXJkIGN1cnZlLCBleGFjdGx5IGFzIHdlIHJlcXVpcmVkIGluIHRoZSBzZXR1cCBvZiBvdXIgcHJvYmxlbToKCiFbUmVzdWx0aW5nIGN1cnZlXShpbWdzL2MyX3NwbGluZS5zdmcpCgojIyBTdW1taW5nIGl0IHVwCgpXZSBoYXZlIGJyaWVmbHkgZXhwbGFpbmVkIGhvdyB0aGUgJENeMCQgYW5kICRDXjEkIHNwbGluZXMgd29yayBhbmQgd2hhdCB0aGVpciBkcmF3YmFja3MgYXJlLCB0aGVuIHdlIGhhdmUgc2hvd24gd2hhdCBpbXByb3ZlbWVudHMgdHdpY2UgZGlmZmVyZW50aWFibGUgc3BsaW5lcyBicmluZyB0byB0aGUgdGFibGUgYW5kIHdlIGhhdmUgZGVyaXZlZCB0aGUgc29sdXRpb24gZm9yIHRoZSBwcm9ibGVtLiBJdCBpcyBsZWZ0IGFzIGFuIGV4ZXJjaXNlIGZvciB0aGUgcmVhZGVyIHRvIGltcGxlbWVudCB0aGlzIGluIHRoZWlyIGZhdm9yaXRlIHByb2dyYW1taW5nIGxhbmd1YWdlIGFuZCBwdXQgdGhlIHRoZW9yeSB0byBwcmFjdGljZQoKSSBob3BlIHlvdSBlbmpveWVkIHJlYWRpbmcgdGhpcyBwb3N0IGFuZCB0aGF0IHlvdSBmb3VuZCBpdCB1c2VmdWwhCgojIyBSZWZlcmVuY2VzCgotIFtMQkcgQW5kZXJzZW4sIFZWIFBpdGVyYmFyZzogSW50ZXJlc3QgUmF0ZSBNb2RlbGluZy4gVm9sdW1lIDE6IEZvdW5kYXRpb25zIGFuZCBWYW5pbGxhIE1vZGVsc10oaHR0cHM6Ly9ib29rcy5nb29nbGUuY28udWsvYm9va3MvYWJvdXQvSW50ZXJlc3RfUmF0ZV9Nb2RlbGluZy5odG1sP2lkPW9JMmZjUUFBQ0FBSiZyZWRpcl9lc2M9eSkKCgoKCgoKCgoK) using the expressions for $L_t^d$, $L_t^f$ and $L_t$, and the fact that

$$
\begin{gather}
	dL_t^d = L_t^d\varphi_t^d dW_t \\ 
	dL_t^f = L_t^f\varphi_t^f dW_t
\end{gather}
$$

$$L_t = \frac{d\mathbb{Q}^f}{d\mathbb{Q}^d} = \frac{\frac{d\mathbb{Q}^f}{d\mathbb{P}}}{\frac{d\mathbb{Q}^d}{d\mathbb{P}}} = \frac{L_t^f}{L_t^d}$$

$$L_t = f(t,x,y) = \frac{x}{y}$$

By applying multidimensional Ito's lemma we get the expression for $dL_t$ under the objective probability measure $\mathbb{P}$. First let us define the partial derivatives needed to apply the Ito's lemma:

$$
\begin{align}
	\frac{\partial f}{\partial x} = \frac{1}	{y} \hspace{1cm} \frac{\partial f}{\partial y} = -\frac{x}{y^2} \\
	\frac{\partial^2 f}{\partial x^2} = 0 \hspace{1cm} \frac{\partial^2 f}{\partial y^2} = \frac{2x}{y^3} \\
	\frac{\partial^2 f}{\partial x \partial y} = -\frac{1}{y^2} \hspace{1cm} \frac{\partial f}{\partial t} = 0
\end{align}
$$

$$
\begin{align}
	dL_t = &\frac{1}{L_t^d}L_t^f\varphi_t^f dW_t - \frac{L_t^f}{(L_t^d)^2}L_t^d\varphi_t^d dW_t + \frac{1}{2}\cdot 0 \\ 
	&+ \frac{1}{2}\frac{2L_t^f}{(L_t^d)^3}(L_t^d)^2 (\varphi_t^d)^2dt - \frac{1}{(L_t^d)^2}L_t^d L_t^f \varphi_t^f \varphi_t^d dt \\
	dL_t = &L_t\varphi_t^f dW_t - L_t \varphi_t^d dW_t + L_t (\varphi_t^d)^2dt - L_t \varphi_t^f \varphi_t^d dt \\
	dL_t = &L_t\left( (\varphi_t^d)^2 - \varphi_t^f\varphi_t^d \right)dt + L_t (\varphi_t^f - \varphi_t^d) dW_t
\end{align}
$$

From the definition, we know that $L_t$ is a martingale under the probability measure $\mathbb{Q}^d$, that is:

$$dL_t = L_t (\varphi_t^f - \varphi_t^d) dW_t^d$$

From that we can get a nice expression for the volatility $\sigma_t$ of the exchange rate $X_t$:

$$\sigma_t = \varphi_t = \varphi_t^f - \varphi_t^d = \lambda_t^d - \lambda_t^f.$$

So our final result is 

$$dX_t = X_t (r_t^d - r_t^f) dt + X_t\sigma_t dW_t^d$$

where $\sigma_t = \lambda_t^d - \lambda_t^f$

## Conclusion

Let us now quickly revise what we have done here and that will allow as to see why the previous result is so interesting. Starting with defining domestic and foreign martingale measures and their respective Radon-Nikodym derivatives w.r.t the objective measure we have set an assumption that both the domestic and the foreign market have their risk-neutral measures.

Girsanov theorem tells us that there is a one-to-one mapping between the market price of risk and its probability measure, so we can think in terms of market prices of risk as well. What that means is if two probability measures have the same market price of risk, these two probability measures will be equal. 

Using that logic, we can see that in order for the domestic and foreign risk-neutral measure to be equal, their market prices of risk $\lambda_t^d$ and $\lambda_t^f$ need to be the same, resulting in $\sigma_t=0$. This means that the only way to make $\mathbb{Q}^d=\mathbb{Q}^f$ is to have a deterministic exchange rate $X_t$, which is usually not the case. 

## References

- [T. Bjork: Arbitrage Theory in Continuous Time](https://books.google.co.uk/books/about/Arbitrage_Theory_in_Continuous_Time.html?id=N0ImZs3HpwIC&redir_esc=y)

