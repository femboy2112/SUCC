# Spectral purity: signed innovation, the diagonal boundary, and uniform source transport

Parent: PR #296 at `461942c0bf616518e668d236d1c6b1596665a7dd`.
Source: the unchanged four-pole BBP recurrence, with $U_0=0$ and every
unwrapped rational state retained. All theorem statements below are ordinary
classical mathematics. New-to-project quantitative transport is distinguished
from scholarly novelty, which has not been established. **π normality remains
OPEN.**

## 1. Exact finite signed innovation identity

Let $N,H\ge1$ be integers and $x_1,\ldots,x_N\in\mathbb T$. Put

$$
a_N(j)=\frac1N\sum_{n=1}^N e(jx_n),\qquad
E_{N,H}=\frac{D_{N,H}}H
=2\sum_{j=1}^{H-1}\left(1-\frac jH\right)|a_N(j)|^2.
$$

Write $F_H(t)=|\sum_{k=0}^{H-1}e(kt)|^2$ and, for $1\le m<N$,

$$q_{m,H}=\frac1m\sum_{j=1}^m F_H(x_{m+1}-x_j).$$

**Theorem SP-I1 (CLASSICAL / PAPER-PROVED / exact finite replay).**
For each finite horizon, with the same $H$ at every step,

$$
E_{N,H}=\frac{H-1}{N}+
\frac{2}{N^2H}\sum_{m=1}^{N-1}m(q_{m,H}-H).
$$

Proof: the pair kernel is symmetric, has diagonal $H^2$, and its new lower
row sums to $mq_{m,H}$. Thus the total pair energy is
$NH^2+2\sum_{m<N}mq_{m,H}$. Divide by $N^2H$, subtract one, and use
$\sum_{m<N}m=N(N-1)/2$. This is the exact sequential theorem from
[PR #296's discussion](https://github.com/femboy2112/SUCC/pull/296#issuecomment-6405132679),
now executed as an equality in $\mathbb Q[\mathbb Q/\mathbb Z]$.

**Signs matter.** At $H=2$, $x_1=0$, $x_2=1/2$, the evaluated innovation is
$q_{1,2}=0$, hence its defect is $-2$. The boundary is $1/2$ and the signed
innovation term is $-1/2$, giving $E_{2,2}=0$. This exact cyclotomic control
rejects termwise positivity and shows why the boundary is not by itself a
lower bound. Taking absolute defects loses cancellation and can give a
strictly larger finite-horizon bound; it is not needed for the signed
identity. Conversely, on the zero-forcing fixed orbit, every
$q_{m,H}=H^2$ and $E_{N,H}=H-1$.

The formal polynomial $2+2e(1/2)$ is nonzero in the free group algebra but
vanishes after cyclotomic evaluation. The program and tests retain that
distinction. No inequality is asserted merely by ordering formal coefficients.

## 2. The slow-window criterion is exactly equidistribution

**Theorem SP-I2 (CLASSICAL / PAPER-PROVED).** For any single infinite circle
sequence, the following are equivalent:

1. The sequence is equidistributed.
2. There exist integers $H_N\to\infty$ with $E_{N,H_N}\to0$.
3. For every real envelope $L_N\to\infty$, such integers can be chosen with
   $H_N\le L_N$ eventually and $H_N\le\sqrt N$ eventually.

Proof of 2 implies 1: fix $j\ge1$. Eventually $H_N\ge2j$, so the nonnegative
spectral sum gives $|a_N(j)|^2\le E_{N,H_N}$. Negative modes are conjugates;
Weyl's criterion applies.

Proof of 1 implies 3: for each integer $K\ge2$, choose strictly increasing
thresholds $n_K\ge K^2$ so that for **all** $N\ge n_K$,
$L_N\ge K$ and $|a_N(j)|^2\le K^{-2}$ for every $1\le j<K$.
Existence follows from the finitely many fixed-mode limits. Define
$H_N=\max\{K\ge2:n_K\le N\}$, taking $H_N=1$ before $n_2$.
Then $H_N\to\infty$, $H_N\le\min(L_N,\sqrt N)$ eventually, and

$$
E_{N,H_N}\le\frac{2(H_N-1)}{H_N^2}<\frac2{H_N}\longrightarrow0.
$$

The implication 3 implies 2 is immediate. This is a full diagonal argument,
not an arithmetic saving. Its thresholds depend on already knowing the
Fourier convergence; they are not obtained by retrospectively selecting
favorable finite spectra. Equidistribution alone supplies no effective
threshold for a prescribed growing window.

The rank bound yields only $H_N\le(1+o(1))N$ when $E_{N,H_N}\to0$.
The convenient $H_N=o(N)$ requirement makes the explicit boundary vanish;
it is not a necessary finite algebraic consequence of spectral purity,
because the signed term may cancel that boundary.

## 3. The exact conditional exceptional-step gate

**Theorem SP-I3 (PAPER-PROVED; finite real kernel formalized).** Let
$\eta\ge0$ and $\mathcal B\subseteq\{1,\ldots,N-1\}$. If
$q_{m,H}\le H(1+\eta)$ for $m\notin\mathcal B$, then

$$
E_{N,H}\le\frac{H-1}{N}
+\eta\frac{N-1}{N}
+\frac{2H}{N^2}\sum_{m\in\mathcal B}m.
$$

Proof: $0\le q_{m,H}\le H^2$. Off the exceptional set the signed defect is
at most $H\eta$. Everywhere it is at most
$H\eta+H^2\mathbf1_{\mathcal B}(m)$. Multiply by $m$, sum, and use SP-I1.
All these are one-sided bounds; no positivity of $q-H$ is assumed. The
finite factor $(N-1)/N$ is retained in the executable budget.

Thus $H_N\to\infty$, $H_N=o(N)$, $\eta_N\to0$, and
$\sum_{m\in\mathcal B_N}m=o(N^2/H_N)$ suffice. **The authentic arithmetic
classifier and these hypotheses are OPEN.** `exceptional_budget` explicitly
returns `good_step_premise_verified=False`; it computes a conditional budget
and does not certify a guessed good set. In particular, defining the bad set
by failed Fourier estimates would not derive a classification from the source.

## 4. A stronger source-specific theorem: spectral Green transfer throughout the sublinear range

The parent Green theorem supplies

$$
16^{n-1}\pi=U_n+T_n,\qquad
T_n=\sum_{k\ge1}16^{-k}r(n+k)>0.
$$

The original positive moment density makes $r$ decreasing. The exact
four-pole inequality $r(n+1)<15/(64n^2)$ therefore gives, for $n\ge1$,

$$
0<T_n<\frac{r(n+1)}{15}<\frac1{64n^2}.
$$

The pole inequality is not fitted: after multiplying by its positive
denominator, the difference $15/64-n^2r(n+1)$ has numerator
$5696n^3+7672n^2+2910n+225$, divided by
$64(2n+1)(4n+3)(8n+1)(8n+5)$, as proved in the parent dossier.

Let $a_N^U(j)$ and $a_N^\pi(j)$ denote the normalized characters of the two
matched histories. Using both boundedness and Lipschitz continuity gives

$$
|a_N^U(j)-a_N^\pi(j)|
\le\frac1N\sum_{n=1}^N
\min\left(2,\frac{7|j|}{64n^2}\right).
$$

Here $2\pi<7$. For any $c>0$, the decreasing function
$f(x)=\min(2,c/x^2)$ has

$$
\sum_{n=1}^{\infty} f(n)
\le\int_0^\infty f(x)\,dx
=2\sqrt{2c}.
$$

The first inequality follows separately on each interval $[n-1,n]$;
the integral is split at $\sqrt{c/2}$. Its tail is integrable, so the
infinite sum is justified by monotone limits of finite positive sums.
With $c=7|j|/64$ this proves the uniform bound

$$
\boxed{|a_N^U(j)-a_N^\pi(j)|
\le\frac{\sqrt{7|j|/8}}N.}
$$

**Theorem SP-I4 (PAPER-PROVED, original-source quantitative transfer).**
For every $N,H\ge1$,

$$
\boxed{
\left|\sqrt{E_{N,H}^U}-\sqrt{E_{N,H}^{\pi}}\right|
\le\frac1N\sqrt{\frac{7(H^2-1)}{24}}.
}
$$

Proof: apply the reverse triangle inequality to the finite vector
$\big(\sqrt{2(1-j/H)}\,a_N(j)\big)_{1\le j<H}$. Its norm is
$\sqrt{E_{N,H}}$. The squared norm of the difference is at most

$$
\frac7{8N^2}\sum_{j=1}^{H-1}2\left(1-\frac jH\right)j
=\frac{7(H^2-1)}{24N^2}.
$$

Only finite sums and a positive-tail integral are used. No exchange of
oscillatory limits, independence of prime channels, or uniform Koopman
compression is assumed.

**Corollary.** For **every prescribed** integer schedule $H_N=o(N)$,
spectral purity of the authentic rational orbit is equivalent to spectral
purity of the true π orbit along that same schedule. For example,
$H_N=\lfloor N^{3/4}\rfloor$ gives a root-energy comparison
$O(N^{-1/4})$. This theorem neither asserts nor assumes that either energy
tends to zero.

This is stronger than using only the inherited summable-tail Lipschitz
bound. That approach gives the squared root-energy error

$$
\left(\frac{119}{648N}\right)^2\frac{H(H^2-1)}6,
$$

which vanishes only in the sufficient range $H=o(N^{2/3})$. The new
clipped bound pays the transport error throughout the full sublinear
frequency range. `spectral_green_budget` improves the finite certificate
further by taking, separately at each mode, the smaller of
$7j/8$ and $(119j/648)^2$, before weighting and summing.

**Boundary.** This result makes a source-specific approximation debt smaller;
it does not bound the common spectral energy. A mutant source may also
have a small Green tail, yet its corrected seed can be nonnormal. Such a
mutant cannot use the displayed identity with π without proving that
identity. Positive source moments alone still do not control $q-H$.

## 5. Lean scope and execution

`formal/SpectralPurity.lean` formalizes a finite real symmetric pair kernel:
constant diagonal $H^2$, row sum $mq_m$, its SUCC energy update and sum,
the signed normalized telescope, and the quantitative exceptional bound.
The kernel-to-complex-Fourier interpretation is the paper proof above;
it is not silently included in the Lean claim. The source recurrence,
Weyl criterion, SP-I2 diagonal construction and SP-I4 analytic source
transport are **not Lean-formalized**.

The file also formalizes the bound for deleting a specified finite subset:
if $H\ge1$, $0\le q_m\le H^2$ and $m\le N$ on $\mathcal C$, then

$$
\left|\frac{2}{N^2H}\sum_{m\in\mathcal C}m(q_m-H)\right|
\le\frac{2H|\mathcal C|}{N}.
$$

The source-specific proof that conductor births form a sparse set is separate
in the arithmetic dossier. This lemma justifies deleting such a set once its
authentic counting theorem has been proved; it never declares the retained
steps good.

The file uses the repository pin Lean 4.14.0 and mathlib revision
`4bbdccd9c5f862bf90ff12f0a9e2c8be032b9a84`. A cached checkout at
`/home/leah/SUCC-rf/formal/mathlib_bridge` was verified against both pins
and reused for local checking. The reproducible repository command after
fetching the same pinned mathlib cache is:

```bash
cd formal/mathlib_bridge
lake exe cache get Mathlib/Data/Real/Basic.lean Mathlib/Algebra/BigOperators/Group/Finset.lean Mathlib/Algebra/BigOperators/Ring.lean Mathlib/Tactic/FieldSimp.lean Mathlib/Tactic/Linarith.lean Mathlib/Tactic/NormNum.lean Mathlib/Tactic/Positivity.lean Mathlib/Tactic/Ring.lean
lake env lean -DmaxHeartbeats=1200000 ../SpectralPurity.lean
```

The portable check, run from the repository root, is:

```bash
python scripts/check_spectral_purity_lean.py --dependency-project /home/leah/SUCC-rf/formal/mathlib_bridge --output /tmp/succ-spectral-purity-lean
```

The checker verifies every dependency Git revision against the repository's
pinned manifest, rejects tracked package changes, builds serially under a
2 GiB Lean memory cap, exports the ten actual theorem types and axiom sets,
and runs two paired negative controls. The positive controls pass; removing
the good-step premise or asserting a nonnegative antipodal defect gives an
actual Lean type mismatch. All ten theorem exports use only `propext`,
`Classical.choice`, and `Quot.sound`; none uses `sorryAx` or a custom axiom.
The actual successful observation is
[kernel-observation.json](spectral_purity_validation/lean/kernel-observation.json),
with logs and SHA256 bindings. Actual kernel status must be taken from that
receipt, not just this command listing.

This new file does not enter or modify the repository's separate formal
authority catalogue; local kernel execution and catalogue admission are
distinct claims.

The focused Python tests compare the authentic matrix code, independently
assembled Fourier energy, and pairwise Fejér energy. Exhaustive generic
holdouts cover 117 history/width combinations, and exact cyclotomic controls
include negative innovations. Source mutations alter both phase and integer
lift. Pointwise Green-tail enclosures cover times through $n=1001$ without
using digit tables or π as an input. All square-root budgets are tested by
exact rational squared inequalities.

Initial implementation failures are retained in the execution narrative:
two tests incorrectly expected a nonexistent `CyclotomicElement.is_zero`
method; one test exceeded its declared width cap; the first Lean attempt
used a post-4.14 module path. These were instrument/API failures, corrected
by using exact scalar equality, bounded test widths and the pinned module
path. The first bounded checker also exceeded its 2 GiB import budget with
all of `Mathlib.Tactic`; narrowing to the required tactics fixed that without
raising the cap. One omitted ring big-operator import was restored. Both
failed checker receipts are retained next to the successful receipt. These
were instrument/API failures, not mathematical counterexamples or passing
checks. The final Python focused run passed all 17 tests.

## 6. Claim boundaries and next falsification

| Result | Authority | What remains |
|---|---|---|
| SP-I1 signed Fejér telescope | CLASSICAL, PAPER-PROVED, EXACT FINITE; real-kernel Lean scope above | No cancellation bound |
| SP-I2 slow-window equivalence | CLASSICAL, PAPER-PROVED | No effective source threshold or prescribed schedule |
| SP-I3 exceptional sufficient bound | PAPER-PROVED; finite real-kernel Lean scope above; CONDITIONAL arithmetic application | Derive classifier and weighted exceptional estimate from original four poles |
| SP-I4 uniform sublinear source transport | PAPER-PROVED, EXACT rational budgets | Bound common energy; no analytic theorem claimed kernel-checked |
| Positive innovation defects | REFUTED | Exact antipodal control gives defect $-2$ |
| π normality | OPEN | Actual source-selected signed saving |

The next source estimate can now be posed directly at any justified
sublinear width without reopening the π/rational-orbit transport debt.
An authentic good/exceptional classifier must retain all four signed
poles and prove its own weighted count. The executable budget alone cannot
establish either premise. Any proposed proof must fail on the zero-forcing
fixed orbit, and must explain why a matched asymptotic mutant does not meet
its source hypotheses.
