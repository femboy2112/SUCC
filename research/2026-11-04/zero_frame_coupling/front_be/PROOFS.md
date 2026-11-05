# Observer inversion, maximal boundary persistence, and the infinite-shift obstruction

**Authority:** paper proofs and separately recorded exact finite checks.
Parent #506 is pinned at `bc2d7b01b6b0a37cb79994e180758e98681aa68e`.
The four original signed poles and literal zero seed are unchanged. The
coherent example below is expressly a changed seed. No selected zero-seed
Weyl saving, Lean certificate, external referee, or novelty claim is made.

Write `e(t)=exp(2 pi i t)`, `T_n=sum_(k>=1)16^-k r_o(n+k)`, and let Z be
the actual zero-seeded radial component of U=Y+Z. Direct rational-source
expansion gives

`T_n=1/(64n²)+O(n^-3)`,
`Z_(n+ell)-Z_n=-ell/(32n²)+O_ell(n^-3)`

for every fixed signed integer ell, once all indices exist. These follow by
expanding the original rational injections and summing their exponentially
weighted future tails; no digit distribution is assumed.

## BE-01. Reciprocal observation is uniformly invertible on the maximal norm

For arbitrary complex data `v_n`, `A<=n<2A`, define

\[
M(v)=A^{-1}\max_{A\le a<b\le2A}\left|\sum_{n=a}^{b-1}v_n\right|,
\quad
M_w(v)=A^{-1}\max_{a<b}\left|\sum_{n=a}^{b-1}w_n v_n\right|,
\quad w_n=\frac{8A^3}{3n^3}.
\]

Then, for every integer `A>=1`,

\[
\boxed{M_w(v)\le\tfrac83 M(v),\qquad
 M(v)\le\tfrac38(2-1/A)^3 M_w(v)\le3M_w(v).} \tag{BE1}
\]

**Proof.** More generally, if positive weights w_n decrease, summation by
parts expresses a weighted sum on `[a,b)` as

`w_(b-1) sum_[a,b) v + sum_(k=a)^(b-2)(w_k-w_(k+1)) sum_(n=a)^k v_n`.

All coefficients are nonnegative and add to w_a, proving
`M_w<=max(w) M`. Apply the same argument with tail sums to the increasing
positive inverse weights `1/w_n`; their coefficients add to `1/w_(b-1)`.
This proves `M<=max(1/w) M_w`. Substitution yields (BE1), including A=1.
The constants are the exact operator constants on arbitrary complex data,
as witnessed by data supported at the respective endpoint.

This applies in particular to the original **coupled** signal `e(HU_n)` for
every H and every initial seed. Thus an actual maximal reciprocal-observer
saving would transfer with only a constant cost. A whole-epoch reciprocal
zero is a different hypothesis: it controls one sum, while (BE1) needs every
subinterval. This is the exact unresolved observer selection issue.

## BE-02. Every fixed nonzero smooth observer retains a maximal chirp boundary

Let w be any fixed nonzero complex C² function on `[1,2]`, and let c be any
fixed nonzero real number. Put

\[
\mathcal M_{w,c}(\Lambda)=
 \max_{1\le a<b\le2}\left|\int_a^b w(x)e(-c\Lambda/x^2)\,dx\right|,
\qquad B_w=\max_{1\le x\le2}x^3|w(x)|.
\]

As `Lambda->infinity`,

\[
\boxed{\mathcal M_{w,c}(\Lambda)
 =\frac{B_w}{2\pi|c|\Lambda}+O_{w,c}(\Lambda^{-2}).} \tag{BE2}
\]

**Uniform endpoint proof.** Twice integrating by parts gives, uniformly in
a and b,

\[
\int_a^b w(x)e(-c\Lambda/x^2)\,dx
 =\left[\frac{x^3w(x)}{4\pi i c\Lambda}
                 e(-c\Lambda/x^2)\right]_a^b
 +O_{w,c}(\Lambda^{-2}).
\]

The C² norms of w bound the twice differentiated amplitudes on the fixed
compact interval. The endpoint expression has modulus at most
`2 B_w/(4 pi |c| Lambda)`. For a matching lower bound take a point x_0
where `x³|w(x)|=B_w`. On at least one side of x_0 there is room for an
interval of length `O_c(1/Lambda)` whose exact phase change has magnitude
one half. Choose x_0 as one endpoint and that point as the other.
The two exponentials are opposite, while the two values of `x³w(x)` differ
by `O_w(1/Lambda)`. Their endpoint difference therefore has modulus
`2 B_w+O_(w,c)(1/Lambda)`. This also covers maxima at 1 or 2 by choosing the
inward interval. The displayed formula proves (BE2).

### Actual radial-relative maximal observer

For each fixed integer `ell!=0`, define

\[
M^{\mathrm{rel},w}_{A,\ell}(H)
 =A^{-1}\max_I\left|\sum_{n\in I}w(n/A)e(H(Z_{n+\ell}-Z_n))\right|.
\]

Uniformly in the interval endpoints, the source asymptotic, Riemann comparison
and rounding of continuous endpoints give, for `Lambda=H/A²>=1`,

\[
M^{\mathrm{rel},w}_{A,\ell}(H)
 =\frac{16B_w}{\pi|\ell|\Lambda}
 +O_{w,\ell}(\Lambda^{-2}+(1+\Lambda)/A). \tag{BE3}
\]

Indeed the phase is `-ell Lambda/(32(n/A)²)+O_ell(Lambda/A)`; the derivative
of the leading weighted integrand is `O_(w,ell)(1+Lambda)`.
Both errors are uniform on every interval, so the maxima differ by the same
bound. For reciprocal w, `B_w=8/3`, giving

\[
\Lambda M^{\mathrm{rel},\mathrm{rec}}_{A,\ell}(H)
 \longrightarrow\frac{128}{3\pi|\ell|}
\quad\text{if }\Lambda\to\infty,\ \Lambda^2/A\to0. \tag{BE4}
\]

This includes the prescribed critical schedule for every fixed nonzero h,
and also tuned reciprocal Fourier zeros when their growing Lambda satisfies
the stated regime. The tuned **whole-epoch** zero does not remove the
maximal-sharp boundary. A nonzero fixed compact smooth bump has `B_w>0` too:
its whole-epoch response can be superpolynomially small, while its maximal
subinterval response has precisely the nonzero `1/Lambda` leading term.

### Same-forcing coherent coupled observer: all fixed integer lags

Take the one fixed changed seed `s*=-pi/16` and assign it to the angular line,
so `Y_n^*=Y_n+16^n s*`, while the actual radial Z remains zero-seeded.
Then

\[
Y_n^*+Z_{n+\ell}=-T_n+Z_{n+\ell}-Z_n
 =-\frac{2\ell+1}{64n^2}+O_\ell(n^{-3}).
\]

For **every fixed integer ell**, `2ell+1!=0`. Applying (BE2) yields

\[
\boxed{
M^{*,w}_{A,\ell}(H)
 =\frac{32 B_w}{\pi|2\ell+1|\Lambda}
 +O_{w,\ell}(\Lambda^{-2}+(1+\Lambda)/A).
} \tag{BE5}
\]

Consequently, on the exact prescribed H_A(h), for **every fixed h!=0**,

\[
\Lambda_A M^{*,w}_{A,\ell}(H_A(h))
 \longrightarrow\frac{32B_w}{\pi|2\ell+1|}>0. \tag{BE6}
\]

For w=1 this is `256/(pi |2ell+1|)`; for reciprocal w it is
`256/(3 pi |2ell+1|)`. These are the original four-pole forcing with a
changed boundary, not an arbitrary artificial companion. Fixed integer
retiming changes the coherent obstruction's constant, not its order.
Any source-selected theorem using the literal zero seed remains possible.

## BE-03. No convergent infinite-shift reconstruction, even with finite lookback

Fix any integers `J>=0` and `N>=J+1`. There is **no** fixed sequence of
complex coefficients `a_ell`, `ell>=-J`, such that its positive-lag series
converges ordinarily and

\[
r_o(n)+\sum_{\ell=-J}^\infty
 a_\ell(Z_{n+\ell}-Z_n)=0
\qquad\text{for every integer }n\ge N. \tag{BE7}
\]

The ell=0 term is identically zero. This includes conditionally convergent
future series, any fixed finite lookback, and identities asserted only on an
eventual tail of the source. It does not prohibit n-dependent coefficients,
generalized summation procedures, or a change to the original forcing.

**Step 1: convergence forces a bounded symbol.** At any one `n_0>=N`, put
`d_ell=Z_(n0+ell)-Z_n0`. Since `Z_n0>0`, `d_ell->-Z_n0!=0`.
The differentiated tail estimate `z'(x)=O(x^-2)` shows that d_ell has finite
total variation in its tail. Its inverse is then bounded and has finite total
variation in that tail. If `sum a_ell d_ell` converges, summation by parts
against `1/d_ell` proves `sum a_ell` converges. Call its sum S and bound all
partial sums by B. For `0<q<=1`, define the partial symbols

`F_L(q)=sum_(ell=-J)^L a_ell(q^ell-1)`.

Abel summation gives `|sum_(ell=1)^L a_ell q^ell|<=B`. The finitely many
negative powers therefore give the uniform bound
`|F_L(q)|<=C(1+q^-J)`. The limiting F is analytic on the punctured unit disk,
continuous on `(0,1]`, and has at most a pole of order J at zero. Abel's
theorem supplies continuity and value zero at q=1. No absolute-convergence
assumption was inserted.

**Step 2: use the exact radial Mellin density.** Write

\[
P_o(t)=4-2t^3-t^4-t^5
      =(1-t)(t^4+2t^3+4t^2+4t+4),
\]
\[
P_r(t)=2-2t-t^2-2t^3-\tfrac12t^4-\tfrac12t^5+\tfrac14t^6,
\qquad K_z(t)=-\frac{P_r(t)}{16-t^8}.
\]

The exact source formulas are

`r_o(n)=integral_0^1 t^(8n-8) P_o(t) dt`,
`Z_n=integral_0^1 t^(8n) K_z(t) dt`.

For n>=N>=J+1, the uniform symbol bound gives an integrable majorant
`C t^(8n)|K_z(t)|(1+t^(-8J))`. Dominated convergence thus applies to each
Mellin integral of the finite stencil. Writing n=N+k, (BE7) would imply

\[
\int_0^1 t^{8k}
 \underbrace{[t^{8N-8}P_o(t)+t^{8N}K_z(t)F(t^8)]}_{W(t)}\,dt=0
 \quad(k\ge0). \tag{BE8}
\]

The bracket W extends continuously to `[0,1]`, because the worst negative
power in F is t^(-8J) and N>=J+1. Polynomials in t^8 are dense in C[0,1],
because t->t^8 is a homeomorphism and ordinary polynomials approximate
continuous functions on `[0,1]`. Equation (BE8) forces W to vanish
identically. For complex coefficients, approximate its conjugate and
integrate its squared modulus.

**Step 3: the source zero contradicts reconstruction.** At
`tau=2-sqrt(2)` in `(0,1)`, the radial logarithmic derivative is zero:

\[
\frac{P_r(t)}{16-t^8}
 =\frac18\frac d{dt}\log\frac{2-t^2}{t^2-2t+2},
\qquad K_z(\tau)=0.
\]

But `P_o(tau)>0` by the displayed positive factorization of P_o.
Consequently `W(tau)=tau^(8N-8) P_o(tau)>0`, a contradiction.
The radial zero and original nonzero density are both authentic source facts.

This explains why matching arbitrarily many endpoint source jets need not
produce a controlled infinite observer. Finite-order jets only match local
behavior near t=1. A genuine bounded future-shift symbol would have to divide
by a radial density with an interior zero. The separate front A/D analysis
quantifies how the particular canonical jet sequence fails; (BE7) rules out
all ordinarily convergent fixed coefficient sequences, even with finite lookback.

## BE-04. Exponentially accurate compensation retains a sharp variation cost

Let `P_m` and `epsilon_m` be the canonical source jets of front A/D. Its
joint-order estimate proves

`0<epsilon_n(n)<=C rho^n`, with `rho=(4 sigma)^(-1)<1`,
`sigma=1-(2-sqrt(2))^8`.

Define the actual time-varying radial compensation
`B(n)=P_n(E)Z_n=-r_o(n)+epsilon_n(n)` and its character
`w_n=e(H B(n))`. For every frequency schedule `H=A² Lambda` with
`Lambda->infinity` and `Lambda/A->0`,

\[
\boxed{\frac1\Lambda\sum_{n=A}^{2A-2}|w_{n+1}-w_n|
 \longrightarrow\frac{45\pi}{128}.} \tag{BE9}
\]

In particular this holds on the prescribed critical schedule for every fixed
nonzero h. It concerns the actual compensated source multiplier; it does not
assume anything about the angular orbit or its seed.

**Proof.** The original rational source has controlled derivative expansion
`r_o(x)=15/(64x²)+O(x^-3)`, and hence
`r_o(n)-r_o(n+1)=15/(32n³)+O(n^-4)>0` for all sufficiently large n.
The exponential residual bound gives
`|epsilon_(n+1)(n+1)-epsilon_n(n)|<=2C rho^n` after enlarging C.
Thus the increments of B are positive eventually and

`delta_n=H(B(n+1)-B(n))=O(Lambda/A)`

uniformly on the epoch. They tend to zero, so
`|e(delta_n)-1|=2 pi delta_n[1+O((Lambda/A)²)]` uniformly. The sum of
the positive delta_n telescopes exactly. Therefore the total variation is

`2 pi H [r_o(A)-r_o(2A-1)+O(rho^A)] [1+O((Lambda/A)²)]`.

Finally
`r_o(A)-r_o(2A-1)=45/(256A²)+O(A^-3)`, proving (BE9).

This pays the proposed analytic-boundary transfer rather than merely improving
its already negligible residual. The exponentially small Ward defect does not
make the multiplying observer nearly constant: its total variation still
costs a nonzero constant times Lambda. A source-specific signed correlation
could exploit more than total variation, but a plain Abel transfer through
this multiplier retains the critical-order loss.

## Attempted source-coupled improvement and remaining estimate

The positive reciprocal Jacobian itself costs only a constant on the maximal
norm, by BE-01. Hence the obstacle is not an unbounded inverse Jacobian.
The available reciprocal sinc zero is only a whole-window scalar constraint.
BE-02 proves that maximizing subintervals restores a sharp coherent boundary,
including for a smooth bump. The canonical source jets remove an already tiny
transport defect, but BE-03 prevents promoting their fixed-order spanning
property into an ordinarily convergent exact infinite future-shift identity.

An actual zero-seed improvement still requires a bound on
`max_I |sum_I e(HU_n)|`, or equivalently its reciprocal-weighted version,
using the selected numerator/carry orientation. Neither the shape of the
radial clock nor these operator identities provides that bound. No selected
little-o estimate is claimed. Original fixed-h Weyl, critical ratchet,
coarse collision energy, pi base-16 normality, and the separate RH program
remain OPEN.

## Primary-source comparison

The endpoint/nonstationary-phase calculation is classical; the explicit
maximal observer constants above are derived here without importing a theorem
about selected digit orbits. Victor Ivrii's own
[oscillatory-integral notes](https://www.math.toronto.edu/ivrii/APM-textbook/Chapter2/L2.3.html)
display the endpoint integration-by-parts expansion and distinguish endpoint
contributions from interior stationary points.

Bailey and Crandall's
[original paper](https://www.davidhbailey.com/dhbpapers/bcrandom.pdf),
Hypothesis A and Theorem 1.1, explicitly require the zero-started rational
forcing orbit and make their normality implication conditional. Lagarias's
[primary paper](https://arxiv.org/pdf/math/0101055), Theorems 3.1 and 3.3,
separates general orbit shadowing from the narrower rational-function
hypothesis. Our changed-seed observer examples do not refute that hypothesis;
they refute promotion from the stated seed-independent observer data.
