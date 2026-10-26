# Sharp clock transport and finite local agreement without the zero anchor

**Source passport.** The primary source is unchanged:
$U_0=0$, $U_n=16U_{n-1}+r(n)$, with the original four signed BBP poles.
The countermodel below changes the initial state and is explicitly rejected
as an authentic replacement. No imported source file is modified.

This work narrowly extends the clock and seed results in
[PR #299](https://github.com/femboy2112/SUCC/pull/299), exact
commit `1d5df4509c6e2042406e3067991b33b8b9fd41fe`. That sibling's
`mobius_refined_matrix.py` is **not imported**, because another branch uses
that module name for a different implementation. The definitions and proofs
here stand on the parent Fourier carrier and exact original forcing.

## 1. A sharp target-specific transport inequality

For a circle probability measure $\mu$ and integer $H\ge2$, write

$$
E_H(\mu)=2\sum_{j=1}^{H-1}\left(1-\frac jH\right)|\widehat\mu(j)|^2.
$$

For empirical measures this is precisely the normalized excess $D/H$.
Let $\delta=\|\mu-\nu\|_1$ be the total variation **norm**, with range
$[0,2]$ for differences of probability measures. On a labelled finite
timeline, $\sum_n|w_n-v_n|$ is also a valid upper bound; coincident circle
points may make the pushforward measure norm smaller.

**Theorem CT-1 (PAPER-PROVED).**

$$
\boxed{\left|\sqrt{E_H(\mu)}-\sqrt{E_H(\nu)}\right|
\le\sqrt{H/2}\,\delta.}
$$

The constant is sharp, even for finitely supported positive measures.
At $H=1$ both sides' energy terms are identically zero; the implementation
returns zero rather than a spurious positive dimension bound.

**Proof.** Define the finite Hilbert-space feature map

$$
\Phi_H(x)=\left(\sqrt{2(1-j/H)}\,e(jx)\right)_{1\le j<H}.
$$

Its mean has squared norm $E_H(\mu)$. With the unnormalized Fejér kernel
$F_H(t)=|\sum_{k=0}^{H-1}e(kt)|^2$, direct expansion gives

$$
\|\Phi_H(x)-\Phi_H(y)\|^2
=2H-\frac2H F_H(x-y)\le2H.
$$

The signed measure $\mu-\nu$ has total mass zero. If $\delta>0$, its
Jordan decomposition is $(\delta/2)(P-Q)$ for probability measures $P,Q$.
Thus

$$
\left\|\int\Phi_H\,d(\mu-\nu)\right\|
\le\frac\delta2\iint\|\Phi_H(x)-\Phi_H(y)\|\,dP(x)dQ(y)
\le\delta\sqrt{H/2}.
$$

All functions are continuous and bounded in a finite-dimensional space, so
the integral and norm steps require no infinite-frequency exchange. The
reverse triangle inequality proves the result. The case $\delta=0$ is immediate.

**Exact sharpness control.** Let $\nu$ be uniform on the $H$-grid, and
let $\mu=\nu+t\delta_0-t\delta_{1/H}$, where $0<t<1/H$.
Both measures are positive, $E_H(\nu)=0$, $\delta=2t$, and

$$E_H(\mu)=2Ht^2=(H/2)\delta^2.$$

The executable test checks this in the exact cyclotomic quotient for every
$H=2,\ldots,12$. It also rejects the falsely strengthened squared constant
$H/4$. Formal nonzero in $\mathbb Q[\mathbb Q/\mathbb Z]$ is not used as
a test for nonzero cyclotomic evaluation.

The dependence on dimension is necessary in order as well. For
$\mu=(1-t)\nu+t\delta_0$ with the same grid-uniform $\nu$,

$$E_H(\mu)=(H-1)t^2,\qquad\|\mu-\nu\|_1=2t(1-1/H).$$

Taking $t$ of order $H^{-1/2}$ keeps the energy away from zero even though
the measure distance tends to zero. A dimension-free transport claim fails.

## 2. More clock depth can be transported back to the selected source

Fix $N\ge Q\ge1$. Let $m_a$ count times $1\le n\le N$ in residue $a$
modulo $Q$. On the same observed source states define

$$\mu_n=1/N,\qquad\beta_n=1/(Qm_{n\bmod Q}).$$

Every residue exists; the tool rejects $N<Q$. No synthetic phase is added.
With $r=N\bmod Q$, the exact timeline distance is

$$\delta_{N,Q}=\frac{2r(Q-r)}{NQ}\le\frac Q{2N}.$$

**Corollary CT-2 (PAPER-PROVED; EXACT rational budgets).**

$$
\boxed{|\sqrt{E_H(\mu)}-\sqrt{E_H(\beta)}|^2
\le\frac H2\delta_{N,Q}^2\le\frac{HQ^2}{8N^2}.}
$$

Consequently, along a prescribed schedule, the balanced and original
spectral-purity limits are equivalent when $\sqrt{H_N}Q_N=o(N)$.
This improves the sufficient condition $H_NQ_N=o(N)$ obtained in PR #299
by directly bounding the trace difference. It is a stronger **transport
theorem**, not a proof that either energy is small. The exact error is zero
whenever $Q\mid N$, so neither sufficient schedule is a necessary condition.

The [previous source-authentic Green result](SPECTRAL_PURITY_INNOVATION.md) gives, for the original
unweighted rational orbit and the true π orbit,

$$
|\sqrt{E^U_{N,H}}-\sqrt{E^\pi_{N,H}}|
\le\frac{\sqrt{7(H^2-1)/24}}N.
$$

Triangle inequality therefore transports from the balanced **authentic
rational** clock to the true π orbit with total root-energy error at most

$$
\boxed{\frac{\sqrt{7(H^2-1)/24}}N
+\sqrt{H/2}\,\delta_{N,Q}.}
$$

Both costs retain their distinct source maps. A sufficient joint schedule is
$H=o(N)$ and $\sqrt H Q=o(N)$. No Koopman outgoing boundary is discarded.

## 3. Exact forcing and arbitrary finite local state agreement still permit coherence

PR #299 constructs rational wrong seeds with denominators coprime to a
chosen prime set. The following stronger construction also makes their
**numerators** satisfy arbitrary specified local seed precisions. It thus
matches the actual states modulo those precisions, not merely the forcing
pole masks or denominator exclusions.

Fix integers $N\ge m\ge1$, a finite set of genuine primes $P$, and integer
depths $k_p\ge1$. Put

$$
M=\prod_{p\in P}p^{k_p},\quad
q_*=-\sum_{j=1}^N16^{-j}r(j),\quad
D=1+128m^2M16^N,
$$

$$
\boxed{\xi=\frac MD\left\lfloor\frac{Dq_*}{M}+\frac12\right\rfloor.}
$$

The empty prime set is allowed, with $M=1$. Let $V_0=\xi$ and
$V_n=16V_{n-1}+r(n)$, using the original forcing without any change.

**Theorem CT-3 (PAPER-PROVED; exact finite witnesses).**

1. $\xi\ne0$, $D$ is odd, and $\gcd(D,M)=1$.
2. For every $p\in P$ and every integer $n\ge0$,
   $$v_p(V_n-U_n)\ge k_p+n\,v_p(16).$$
3. For every $m\le n\le N$,
   $$|V_n|<\frac5{256m^2}.$$

**Proof.** Rounding to the nearest integer gives

$$
|\xi-q_*|\le\frac M{2D}<\frac1{256m^2 16^N}.
$$

The denominator is $1$ modulo $M$ and odd. The rounded integer is nonzero:
$q_*\le-r(1)/16=-47/240$ and $D/M>128m^216^N\ge2048$, so its argument
before rounding is strictly below $-1/2$. The numerator is a multiple of
$M$, and cancellation with the $p$-free denominator cannot remove a factor
$p\mid M$. Hence $v_p(\xi)\ge k_p$. Subtracting the two exact recurrences
gives $V_n-U_n=16^n\xi$ for every $n$, proving the local assertion.

The finite future-tail identity is

$$
V_n=16^n(\xi-q_*)-\sum_{j=n+1}^N16^{n-j}r(j).
$$

The authentic positive decreasing four-pole source obeys
$r(n+1)<15/(64n^2)$. Its finite tail is less than
$r(n+1)/15<1/(64n^2)$. The rounding term is less than
$1/(256m^2)$ for $n\le N$, proving the claimed radius.

The p-adic assertion concerns **the valuation of the difference**. It does
not illegally reduce a nonintegral individual state modulo a positive
prime power. Dyadic precision improves by $4n$; at odd primes the original
requested precision remains. All forcing differences are exactly zero.

This is a horizon-dependent family. It neither proves a fixed infinite
nonnormal rational seed nor provides a counterexample to π normality.
It violates the exact initial condition $U_0=0$ and can introduce denominator
places outside the authentic conductor. An exact zero anchor or the exact
allowed conductor can therefore reject it. Finite local congruence checks
alone cannot reject it, even when every selected precision is imposed at
every observed time.

## 4. Uniform obstruction for all partitions, all positive weights, and a growing matrix

Take **any** nonnegative probability weights on the window $m,\ldots,N$;
strict positivity is permitted but unnecessary. For a nonzero integer $h$,
write $z_n=e(hV_n)$. The total variance bounds the entire gain of every
nested partition hierarchy:

$$
0\le\text{total conditional gain}
\le1-|\sum_nw_nz_n|^2
\le\sum_nw_n|z_n-1|^2.
$$

This is the finite conditional-expectation Pythagoras identity. Zero-mass
cells are omitted, and no independence of prime masks is used. Since
$|e(x)-1|\le2\pi|x|<7|x|$, CT-3 gives

$$
\sum_nw_n|z_n-1|^2
<\frac{1225h^2}{65536m^4}
<\frac{5h^2}{128m^4}.
$$

**Corollary CT-4 (PAPER-PROVED; matrix form).** For every integer $H\ge1$
and all such weights,

$$
\boxed{0\le(H-1)-E_H(V,w)
\le\frac{5H(H^2-1)}{768m^4}.}
$$

The same upper bound controls the weighted sum of the partition gains over
all $1\le h<H$. To check the constant, sum the individual caps against
$2(1-h/H)$ and use

$$\sum_{h=1}^{H-1}2(1-h/H)h^2=\frac{H(H^2-1)}6.$$

Thus for $H=o(m^2)$ the ratio $E_H/(H-1)$ tends to one for these finite
controls, regardless of the weighting or partition hierarchy. This includes
balanced CRT weights. The result is a quantitative obstruction to uniform
innovation claims over all locally compatible seeds; it does not concern
the uniquely specified authentic seed after its exact zero anchor is imposed.

## 5. Execution, controls, and authority

Implementation: `observational_succ/bbp_clock_transport.py`.
Focused tests: `tests/test_bbp_clock_transport.py`.

The focused suite passed 17 tests. It includes exact cyclotomic sharpness
for widths $2$ through $12$, a false-constant mutation, 196 antipodal
measure comparisons, every balancing clock with $1\le Q\le N\le30$,
and independent combined-rational forcing checks. Fresh seed cases use
$(N,m)=(8,3),(16,8),(37,19)$, primes through $17$, and depths through $8$.
Outward rational character intervals check the all-weight partition and
matrix bounds. Integer-lift, forcing, zero-anchor label and authority
mutations are rejected. The code never labels a counterfeit as the original
source and never labels a transport budget as a cancellation proof.

CT-1 through CT-4 are **PAPER-PROVED**, with **EXACT FINITE** instruments and
controls. No Lean authority is claimed for these complex/analytic results.
The separately checked finite selected-phase core has its own explicit
theorem scope and receipt below. π normality and the balanced energy
estimate remain **OPEN**.

## 6. Separately executed finite Lean core for the selected-phase argument

`formal/SelectedPhase.lean` was actually checked with Lean 4.14.0 and
mathlib `4bbdccd9c5f862bf90ff12f0a9e2c8be032b9a84`. Its eight declarations
formalize integer branch uniqueness at strict gap less than one, the
inhomogeneous backward recurrence telescope, its endpoint bound, finite
summation of supplied block deficits, and the exact rational margins
$919/1600<1$ and $1648007/4704000<1$.

The scalar aggregation explicitly assumes every block estimate and the
triangle/cover equations. It does not derive those hypotheses from the
original BBP source. Complex chord geometry, the source integral, π's
irrationality measure, the logarithmic block count, CT-1 through CT-4,
and normality are **not formalized** in this file.

The serial checker verifies every dependency revision and source cleanliness,
uses a 2 GiB Lean memory cap, exports the eight actual theorem types and
their axiom sets, and runs three paired controls. Correct controls pass;
wrong forcing sign, overcounted block loss, and a false integer equality
each fail with a Lean type mismatch. All exports use only `propext`,
`Classical.choice`, and `Quot.sound`. The first direct elaboration exposed
an omitted ordered-sum import; adding that import resolved it before the
successful checker run.

Actual receipt: [kernel-observation.json](selected_phase_validation/lean/kernel-observation.json).
The existing historical formal sources and their receipt hashes are unchanged.

```bash
python scripts/check_selected_phase_lean.py \
  --dependency-project /home/leah/SUCC-rf/formal/mathlib_bridge \
  --output /tmp/succ-selected-phase-lean
```

The dependency path is an observed compatible local cache; callers may use
the repository's own `formal/mathlib_bridge` after fetching the same pinned
dependencies. This local kernel observation does not modify the separate
formal authority catalogue or assert a hosted run has passed.
