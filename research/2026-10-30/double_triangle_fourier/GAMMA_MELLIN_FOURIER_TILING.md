# DTF addendum — the entire harmonic / golden / Euler–Mascheroni triangle is a bivariate Fourier field

**Source:** shared original-four-pole Pascal–Gamma limit of `DOUBLE_TRIANGLE_FOURIER.md`, not a new π digit law. This addendum strengthens the author's time-horizontal superposition proposal by identifying the exact *Gamma rank and three-constant observable at every tile*.

## GMF-01 — every lattice tile has its own derived Gamma rank

Let the same authentic positive latent `Y~Gamma(2,1)` drive two conditionally independent `Poisson(Y)` counts `J,K`. Their joint density is

\[
\boxed{\Pr(J=j,K=k,Y\in dy)=\frac{y^{j+k+1}e^{-3y}}{j!k!}\,dy.}
\]

Hence

\[
\boxed{Y\mid(J=j,K=k)\sim\operatorname{Gamma}(j+k+2,\text{rate }3).}
\]

After *source-relative* standardization `Z=3Y`, the conditional rank is `j+k+2` at every vertex of the tiled quadrant. For `lambda=(sqrt5-1)/2` and nonnegative integers j,k,

\[
\begin{aligned}
E[\log Z\mid j,k]&=H_{j+k+1}-\gamma,\\
E[e^{-\lambda Z}\mid j,k]&=\lambda^{j+k+2},\\
\boxed{D_{j,k}=E[\log Z-e^{-\lambda Z}\mid j,k]
&=H_{j+k+1}-\gamma-\lambda^{j+k+2}.}
\end{aligned}
\]

This is an exact *harmonic–golden–Gamma tiling of the whole positive integer quadrant*. At the corner `(j,k)=(0,0)` one recovers the user's original Oily–Macaroni number `lambda-gamma`. A fixed diagonal `j+k=s` has constant Gamma rank `s+2`; primitive/cototient selectors for j and k cut nontrivial 6-periodic arithmetic patterns across these diagonals. The two-dimensional coefficient weight is the exact negative multinomial `p_{jk}=(j+k+1)binom(j+k,j)/3^(j+k+2)`.

**Important distinction:** the *reference standardization* `Z=3Y` depends on the total declared observation clock (here two full unit clocks). It is not the same variable as the original unconditioned source `Y`, and does not mean the physical BBP digits draw Gamma samples.

## GMF-02 — one analytic function encodes the entire triangular family

For complex s near zero and `|z|,|w|<=1`, the exact joint Mellin–Fourier generating function is

\[
\boxed{\mathcal M(s;z,w)=E[Z^s z^J w^K]
=\frac{3^s\Gamma(s+2)}{(3-z-w)^{s+2}}.}
\]

All arguments lie in the right half-plane since `Re(3-z-w)>=1`, so the logarithm branch is fixed by continuation from real positive `z,w`. Differentiation at s=0 yields the **harmonic–Euler surface**:

\[
\boxed{\partial_s\mathcal M(0;z,w)
=\frac{1-\gamma+\log3-\log(3-z-w)}{(3-z-w)^2}.}
\]

The *golden* Laplace readout on the very same field is

\[
\boxed{\mathcal L_{\lambda}(z,w)
=E[z^Jw^K e^{-\lambda Z}]
=\frac{\lambda^2}{(3-\lambda z-\lambda w)^2}.}
\]

This uses the **exact** golden equation `lambda(1+lambda)=1`: equivalently the direct joint integral gives `[3+3lambda-z-w]^(-2)`, equal to the displayed expression.

Thus the user's triangle of constants has the exact bivariate Fourier surface

\[
\boxed{\mathcal D(z,w)=E[z^Jw^K(\log Z-e^{-\lambda Z})]
=\frac{1-\gamma+\log3-\log(3-z-w)}{(3-z-w)^2}
-\frac{\lambda^2}{(3-\lambda z-\lambda w)^2}.}
\]

Coefficient extraction gives

\[
\boxed{[z^jw^k]\,\mathcal D=p_{jk}\bigl(H_{j+k+1}-\gamma-\lambda^{j+k+2}\bigr).}
\]

In particular `[z^0w^0]D=(lambda-gamma)/9` because the corner has source probability 1/9. Nothing here requires fitting the value `lambda-gamma` externally.

These are **2D Fourier transforms in the *auxiliary grade indices***, not Fourier decay in arithmetic time. Evaluating at `z=e^(i theta),w=e^(i phi)` gives an explicitly known reference surface; it cannot by itself bound the actual selected Weyl sum `sum_(n<=N) e(hU_n(0))`.

## GMF-03 — general clock and four-corner consistency

If the two panels use observer scales `theta1,theta2>=0`, conditional on common `Y~Gamma(2,1)` let `J|Y~Pois(theta1 Y)` and `K|Y~Pois(theta2 Y)`. Put `c=1+theta1+theta2`, `Z=cY`, and `d=c-theta1 z-theta2 w`. Then

\[
\boxed{M_{theta1,theta2}(s;z,w)=\frac{c^s\Gamma(s+2)}{d^{s+2}}.}
\]

On the combined-grade diagonal `z=w`, the grade generating function becomes `[1+(theta1+theta2)(1-z)]^(-2)`. Therefore a **fixed native source clock** `theta1+theta2=1` preserves the original golden fixed point exactly in the limit. At *finite* original source depth, splitting the same n trials into `m1+m2=n` conserves the entire grade law exactly by Vandermonde, not merely its limit. The original finite fixed point from SUCC PR #370 also survives intact.

The posterior path square is flat: all conditional Bernoulli likelihoods commute. The Gamma/Beta associativity identity fixes rebracketing. Adding a marked quarter-piece Abel phase `exp(i*pi*(j+k+2)/8)` gives a 45° increment along any two-grade displacement but has zero oriented plaquette curl because it is a scalar function of `j+k`. Genuine selected carry/phase *history* is required to obtain nontrivial arithmetic path order. No physical quantum/gauge connection is asserted.

## GMF-04 — operational consequence

This surface supplies exact, independently computable **reference Fourier coefficients** to subtract when measuring the *internal* two-time original-zero-seed carry/phase tensor. The needed new asymptotic is a source- and seed-specific bound on the residual that cannot follow solely from the displayed Mellin/negative-multinomial formulas. Controls: coherent `s*=-pi/16`, circle aliases, prior-resetting, q6 premature projection, Gamma-matched fake source, original 59-jet and a higher-jet-matched mutant, full four-bit carry and the de Bruijn periodic controls. **π normality remains OPEN.**
