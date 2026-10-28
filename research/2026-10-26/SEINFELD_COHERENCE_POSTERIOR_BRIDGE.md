# Publication addendum: the same golden–Gamma marginal can retain different Fourier futures

**Date:** 2026-10-27. **Status:** PAPER-PROVED for the declared finite-history
Pólya/Dirichlet model; independent exact rational checks accompany the proof.
This addendum uses the newly inspected [draft #314](https://github.com/femboy2112/SUCC/pull/314)
at `935c2db4c36ff56d90acd82eae30bcce15b6a053` and the
[posterior interpretation](POSTERIOR_GOLDEN_GAMMA_CONNECTION.md) in draft #315,
initially published at `2993a4e203211fae3ac1e6697bab22f9a506870e`.
The branches are siblings above #313. No #314 code is merged by this addendum.

## 1. What the latest work contributes

The [pinned #314 dossier](https://github.com/femboy2112/SUCC/blob/935c2db4c36ff56d90acd82eae30bcce15b6a053/research/2026-10-26/SEINFELD_COHERENCE_GROUPS.md)
retains formal class amplitudes in $\mathbb Q[C_{16}]$, supplies a strong
lumpability gate, and gives a symmetric sixteen-color Pólya countermodel with
unconditional empirical Fourier second moment $(N+16)/(17N)$.
Its proof dossier, implementation and validation scope were inspected.

Two precise connections follow. First, our four-field codec is a lossless
representation of its formal amplitudes. Second, its very same declared path
model contains our exact exponential/golden–Gamma posterior construction while
retaining positive future Fourier energy. The second connection can be made
under a completely specified word, not only under coarse avoidance information.

**Steelman:** a shared posterior mechanism might identify the arithmetic
information hidden by averaging and force cancellation as its log defect shrinks.
**Crucible:** retain the exact same posterior marginal under two different
selection events, then calculate the full character's future moments.
**Verdict:** the posterior mechanism is exact; sufficiency of that marginal or
its vanishing log defect for Fourier cancellation is REFUTED in this declared
model. The source-specific BBP implication remains OPEN.

## 2. Formal coherence groups and the four-field codec

The factorization into distinct rational cyclotomic polynomials gives

$$
\mathbb Q[C_{16}]=\mathbb Q[x]/(x^{16}-1)
\cong\mathbb Q\oplus\mathbb Q\oplus\mathbb Q(i)
\oplus\mathbb Q(\zeta_8)\oplus\mathbb Q(\zeta_{16}).
$$

Evaluation at $1,-1,i,\zeta_8,\zeta_{16}$ is exactly the mass and
$F_8,F_4,F_2,F_1$ packet family of our
[codec](SEINFELD_NULL_RESIDUAL_AND_FOURIER_CODEC.md).
The rational dimensions are $1+1+2+4+8=16$. Pairwise coprimality and the Chinese
remainder theorem give injectivity and surjectivity; the native antipodal
reconstruction gives the explicit inverse. This works for arbitrary signed
rational amplitude rows. A single evaluated character does not recover the
formal vector; the complete packet family does.

Preserving a present phase still need not preserve its future. For a finite
transition kernel $K$ and grouping $\kappa$, an exact quotient for **every**
initial law requires the row sums into each target class to agree:

$$
\sum_{\kappa(y)=g'}K(x,y)=\sum_{\kappa(y)=g'}K(x',y)
\quad\text{whenever }\kappa(x)=\kappa(x').
$$

This is #314's classical strong-lumpability gate. For a deterministic successor
$T$, it reduces to $\kappa(Tx)=\kappa(Tx')$. Its role here is to ensure that
discarding the labelled residual does not silently change tomorrow's observable.
It supplies a necessary and sufficient quotient criterion under the stated
all-initial-laws convention, not a signed cancellation estimate.

## 3. One explicit path law and two selection events

Let $\Theta=(\Theta_0,\ldots,\Theta_{15})$ be uniform on the probability
simplex, equivalently Dirichlet$(1,\ldots,1)$. Given $\Theta$, let the colors
$J_1,J_2,\ldots$ be iid with probabilities $\Theta_j$. For a finite word
with color counts $n_j$ and length $n$, simplex integration gives

$$
P(J_1=j_1,\ldots,J_n=j_n)
=\frac{15!\prod_{j=0}^{15}n_j!}{(n+15)!}.
$$

The Pólya rule $P(J_{t+1}=j\mid J_1,\ldots,J_t)=(1+n_j)/(16+t)$
has the same word probability by multiplying numerators and denominators.
This verifies the mixture representation directly for the declared finite law.

For every integer $r\ge0$, distinguish

$$
A_r=\{J_1,\ldots,J_r\ne0\},\qquad
B_r=\{J_1=\cdots=J_r=1\},\qquad m=15+r.
$$

$A_r$ selects a binary avoidance path, a union of full color histories.
$B_r$ selects one completely specified color word. Both have positive finite
probability, with

$$
P(A_r)=\frac{15}{15+r},\qquad
P(B_r)=\binom{r+15}{15}^{-1}.
$$

Set $T=\Theta_0$ and $Q_j=\Theta_j/(1-T)$ for $1\le j\le15$.
The simplex substitution has Jacobian $(1-T)^{14}$, so its prior density
factors as $15(1-T)^{14}\cdot14!$. Consequently
$T\sim\operatorname{Beta}(1,15)$ and $Q\sim\operatorname{Dirichlet}(1^{15})$
are independent.

The likelihood of $A_r$ is $(1-T)^r$; the likelihood of $B_r$ is
$(1-T)^rQ_1^r$. Thus both selected laws have exactly the same marginal

$$
\boxed{T\mid A_r\sim T\mid B_r\sim\operatorname{Beta}(1,m).}
$$

Their retained joint laws differ. Under $A_r$, $Q$ stays uniform Dirichlet and
independent of $T$. Under $B_r$, the full posterior is
Dirichlet$(1,r+1,1,\ldots,1)$; in particular its $Q$ distribution is tilted
toward color one. This is an exact location of information lost by passing to
the shared scalar marginal.

## 4. Identical constants bridge and shrinking defect

Under either selected law, define $X=mT$ and $Z=-m\log(1-T)$.
The beta survival function gives $P(Z>z)=e^{-z}$ for $z\ge0$, so

$$
Z\sim\operatorname{Exp}(1),\qquad
X=m(1-e^{-Z/m}),\qquad
L(s)=Ee^{-sZ}=\frac1{1+s}.
$$

Consequently $P(Z>1)=e^{-1}$, $E\log Z=-\gamma$, and the positive fixed
point $L(\lambda)=\lambda$ is $\lambda=\varphi^{-1}$. The earlier proof yields

$$
\epsilon_m=E[\log Z-\log X]=H_m-\log m-\gamma,
\qquad 0<\epsilon_m<\frac1{2m}.
$$

Both laws therefore have exactly the same oily-offset identity
$(\lambda-\gamma)-[\lambda+E\log X]=\epsilon_m$.
These are analytic identities of the declared posterior; finite rational
histories are not exact finite rational evaluations of $\gamma$ or $e$.
Here $m\ge15$, as dictated by the sixteen-color prior.

## 5. Different retained Fourier futures

Fix any integer $h$ with $16\nmid h$, write $z_j=\zeta_{16}^{hj}$, and
let $C=\sum_{j=0}^{15}\Theta_jz_j$ be the latent character mean.
The root sums satisfy $\sum_jz_j=0$ and $\sum_j|z_j|^2=16$.

Under $A_r$, put $W=\sum_{j=1}^{15}Q_jz_j$.
Dirichlet first and second moments give

$$
EW=-\frac1{15},\qquad E|W|^2=
\frac{\sum_{j=1}^{15}|z_j|^2+|\sum_{j=1}^{15}z_j|^2}{15\cdot16}
=\frac1{15}.
$$

Since $C=T+(1-T)W$, independence and the beta moments yield

$$
\boxed{E[C\mid A_r]=\frac{15-m}{15(m+1)},\qquad
v_A(m):=E[|C|^2\mid A_r]=\frac{m^2-m+30}{15(m+1)(m+2)}.}
$$

Indeed $ET^2=2/D$, $ET(1-T)=m/D$, and
$E(1-T)^2=m(m+1)/D$, where $D=(m+1)(m+2)$. Substitution proves the formula.
Moreover, for the integer domain $m\ge15$,

$$
v_A(m)-\frac1{17}
=\frac{2(m-15)(m-16)}{255(m+1)(m+2)}\ge0,
\qquad v_A(m)\longrightarrow\frac1{15}.
$$

Under the completely specified word $B_r$, the posterior parameters have total
$a=r+16$ and $\sum_j\alpha_jz_j=r z_1$. The Dirichlet moment formula

$$
E\left|\sum_j\Theta_jz_j\right|^2
=\frac{\sum_j\alpha_j|z_j|^2+|\sum_j\alpha_jz_j|^2}{a(a+1)}
$$

therefore gives

$$
\boxed{E[C\mid B_r]=\frac r{r+16}\zeta_{16}^{h},\qquad
v_B(r):=E[|C|^2\mid B_r]
=\frac{r^2+r+16}{(r+16)(r+17)}\longrightarrow1.}
$$

These moments directly govern observed future averages. If
$F_N=N^{-1}\sum_{k=1}^N\zeta_{16}^{hJ_{r+k}}$, then for either event $E=A_r,B_r$,
conditional iid sampling given $\Theta$ gives

$$
\boxed{E[|F_N|^2\mid E]=\frac1N+
\left(1-\frac1N\right)E[|C|^2\mid E].}
$$

The diagonal terms are one and each off-diagonal term is the selected second
moment of $C$. At $r=0$, this recovers #314's $(N+16)/(17N)$ exactly.
Thus the same vanishing $\epsilon_m$ and same full exponential/golden–Gamma
marginal coexist with persistent future Fourier energy; a selected constant
word can make that energy tend to one.

This is a statement about finite selected laws and future ensemble second
moments. It does not assert that every individual path is coherent, does not
identify a BBP sampling law, and does not take conditioning on a probability-zero
infinite word. Both $P(A_r)$ and $P(B_r)$ tend to zero.

## 6. Provenance, exact checks and next falsification

- **Inherited/classical:** #314's finite urn law, formal coherence groups and
  lumpability criterion; the Chinese remainder and Dirichlet identities.
- **New paper derivation in this addendum:** the two-event, same-marginal
  construction, its conditional Fourier moments, and their explicit connection
  to #315's logarithmic Euler defect.
- **Exact finite evidence:** the [stdlib oracle](seinfeld_coherence_posterior_oracle.py)
  enumerates 3,616 literal avoidance prefixes and exact two-draw predictive
  laws, checks all fifteen nontrivial modes, checks nine constant words through
  length 128, and integrates the posterior density as rational polynomials.
  Its [receipt](seinfeld_coherence_posterior_receipt.json) hashes this proof and
  the oracle. Finite checks do not prove the analytic logarithm identities.
- **Validation scope:** #314 reports isolated shim tests; this branch's native
  8,936-test result covers its own frozen production/test sources. This addendum
  changes neither production nor tests and does not import #314's code.
- **Open claim and next falsifier:** a source-derived, future-stable quotient
  retaining the joint source/phase/residual data must distinguish the authentic
  BBP path from both these controls before its signed bound can be used.
  The shared constants marginal cannot be that discriminator by itself.

Reproduce with `python research/2026-10-26/seinfeld_coherence_posterior_oracle.py --verify`.
No new Lean proof, selected $o(N)$ estimate, normality result or RH consequence is claimed.
