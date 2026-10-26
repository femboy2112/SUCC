# Collision route: exact quantitative bridge and a same-carrier counterfeit

Date: 2026-10-25. Baseline: PR #296, `461942c0bf616518e668d236d1c6b1596665a7dd`.
This is the independent collision bearing of Operation FUCC THE RESONANCE.
**Base-16 pi normality remains OPEN.** No source-selected collision saving is
claimed. The code uses the original four-pole BBP recurrence with `U_0=0`.

## Hole contract and verdict

Let `y_n={U_n}`, `U_n=16U_(n-1)+r(n)`, with the unchanged four signed
poles, and let `E_(N,d)=M sum_j p_j^2`, `M=16^d`, for the first N actual
rational states `y_1,...,y_N`. The required collision count includes self-pairs.
At `d_N=floor((2/5)log_16 N)`, the attached plan asks for
`E_(N,d_N)=o(log N)`. The condition is **sufficient and UNVERIFIED**.

The shorter dependency cut already present in the repository is weaker:

$$
\frac{\log E_{N,d_N}}{d_N}\longrightarrow0,
\qquad\text{equivalently }E_{N,d_N}=N^{o(1)}.
$$

With the positive BBP tail, one-cell carry transfer, and a vanishing unsafe
prefix, the inherited entropy proof suffices. It does not need the stronger
`o(log N)` hypothesis. The trimmed version is weaker still. A bound at one
unspecified slowly adapted depth is qualitatively equivalent to normality;
a bound at the prescribed logarithmic depth has additional quantitative content.
Neither is an established estimate for the authentic source. The frontier contract's
"or equivalently" wording must not be read as a literal equivalence between
untrimmed and trimmed hypotheses: the inherited rare-hotspot example separates
them. Both are sufficient routes, with different strength.

The new results below are (i) a finite explicit Fourier bound for the plan's
stronger premise, and (ii) an adversarial exclusion of a stronger conductor-only
argument. The first is a **quantitative bridge, not a new arithmetic saving**.
The second is a **refutation with a concrete source-labelled countercontrol**.
The missing lamp is a bound on the actual numerators/carries correlated across
time under the exact recurrence and its zero initial condition.

## 1. Exact audit of the inherited entropy criterion

Read directly from:

- [PI_SOURCE_COLLISION_ENTROPY.md](../2026-10-24/PI_SOURCE_COLLISION_ENTROPY.md),
  SCE-02, SCE-04, SCE-06 and SCE-07;
- [PI_TRIMMED_JOINT_ENTROPY.md](../2026-10-24/PI_TRIMMED_JOINT_ENTROPY.md);
- [PI_HYPOTHESIS_A_SYNTHESIS.md](../2026-10-24/PI_HYPOTHESIS_A_SYNTHESIS.md),
  sections 4--5.

For an actual infinite digit word and its N consecutive starts, `k<=d`,
`q=floor(d/k)` and `d/N<=1/2`, the proved finite bound is

$$
D(p_{N,k}\Vert u_{16^k})
\le \frac{\log C_{N,d}}{q}
+h_2(d/N)+(d/N)\log(16^k-1).
$$

The d-block distribution includes the required future digits at the last
start. Arbitrary trimming is handled by decomposing the full start law;
shift invariance is never imposed on the retained subset. For retained mass
`1-delta` and its collision `C_G`, the numerator becomes
`delta*d*log(16)+(1-delta)*log(C_G)`.

For the rational BBP source, the exact positive tail satisfies

$$
\{16^{n-1}\pi\}=y_n+T_n\pmod1,
\qquad 0<T_n<[(8n+1)(8n+2)]^{-1}.
$$

At depth d discard the at-most `ceil(sqrt(M)/8)+1` early indices where the
one-cell condition is not certified. The safe source subset has collision
at most `E/(1-delta)^2`; its true-circle collision is at most twice this.
For `M<=N^(2/5)`, `delta=O(N^(-4/5))`. Thus

$$
\log C_G\le\log2+\log E-2\log(1-\delta),
$$

and `log E=o(d)` supplies every fixed-block limit through the inherited
finite bound. This verifies all-prefix sufficiency without an assumed
boundary avoidance count. For prime windows, SCE-07 separately requires
coverage of all sufficiently large good primes; its stated good-order
threshold is `L_p>sqrt(p)/log p`, and its collision variable is the scaled
small-ball pair count `K_p(1)`, which dominates cell collision. The fixed
modulus PNT supplies relative-scale coverage. These are different scopes;
a finite family of favorable primes or a merely sparse subsequence is not enough.

## 2. RCL-01: a finite collision-to-Fourier ladder inequality

**PROVED PAPER.** For integers `N,d,J>=1`, nonzero integer h, put
`M=16^d`, `Q=|h|16^(J-1)`, and require **Q<M**. Define

$$
c_N(q)=\frac1N\sum_{n=1}^N e(qy_n),\qquad e(x)=\exp(2\pi i x),
$$

and the exact source cell collision E as above. Then

$$
\boxed{
|c_N(h)|\le\sqrt{\frac{E-1}{J}}+\epsilon_{N,M,J,h},
}
$$

where the completely explicit rational error is

$$
\epsilon_{N,M,J,h}
=\frac{2(J-1)}N
+\frac{11|h|(16^{J-1}-1)}{56N}
+\frac{44|h|16^{J-1}}{7M}.
$$

In particular the entirely rational consequence

$$
|c_N(h)|^2\le\min\left(1,
\frac{2(E-1)}J+2\epsilon_{N,M,J,h}^{\,2}\right)
$$

can be computed without complex evaluation.

### Proof

The authentic recurrence and a shift of N consecutive terms give

$$
|c_N(16q)-c_N(q)|
\le\frac2N+\frac{44|q|}{7N}\sum_{n=1}^N r(n+1).
$$

The source-specific all-n inequality already proved in
[SUCC_INTERNAL_MATRIX_WALK.md](SUCC_INTERNAL_MATRIX_WALK.md) is
`0<r(n+1)<15/(64n^2)`. The elementary integral bound
`sum_(n>=1) n^(-2)<2` gives `sum r(n+1)<15/32`. Telescoping the exact
frequency ladder therefore gives, for `0<=j<J`,

$$
|c_N(h16^j)-c_N(h)|
\le\frac{2j}{N}
+\frac{11|h|(16^j-1)}{56N}.
$$

Replace each y_n by the left endpoint `a_n/M` of its actual cell. Since the
replacement displacement is less than `1/M`, its Fourier mean `b_N(q)` obeys
`|b_N(q)-c_N(q)|<=44|q|/(7M)`. Exact finite cyclic Parseval gives

$$
\sum_{q=0}^{M-1}|b_N(q)|^2=M\sum_a p_a^2=E,
\qquad b_N(0)=1.
$$

The hypothesis Q<M makes `h16^j mod M`, `0<=j<J`, distinct and nonzero.
Thus their squared Fourier means sum to at most E-1. Each differs from
`c_N(h)` by at most epsilon. The Euclidean triangle inequality in J
coordinates gives `sqrt(J)|c_N(h)|<=sqrt(E-1)+sqrt(J)*epsilon`, as claimed.
The squared consequence is `(a+b)^2<=2a^2+2b^2` and `|c_N(h)|<=1`.

### Quantifiers and novelty tax

Fix h. Choose `J=max(1,floor(d_N/2))`. Then J is asymptotic to a positive
constant times log N, Q<M eventually, and epsilon tends to zero. Consequently
`E=o(log N)` implies the authentic selected Fourier limit. Green transport
then gives the true pi limit. The statement holds for each fixed nonzero h;
no uniformity over arbitrarily growing h is asserted.

The code computes E from the genuine finite source, but provides no upper
bound on E beyond the measured finite prefix. This is a classical finite
Bessel argument combined with a paid, original-source recurrence error.
It is not a new theorem that the desired asymptotic holds. The entropy
criterion in section 1 is strictly more permissive as a sufficient condition.

## 3. RCL-02: a maximally colliding counterfeit inside every allowed conductor

The familiar p-free countercontrol can be sharpened without introducing
any new denominator prime. Let `p=8m+1`, `n=m+1+t`, `0<=t<Delta=3m`,
and write the authentic split

$$
y_n=\frac{a_t}{p}+w_t\pmod1,\qquad
1\le a_t<p,\quad Q_t=\mathrm{den}(w_t).
$$

The canonical source decomposition implies

$$
\mathrm{den}(y_n)=pQ_t,\qquad p\nmid Q_t.
$$

Indeed, if `y_n=A/(pQ)` is reduced, subtracting its p-primary phase gives
`(A-a_t Q)/(pQ)=B/Q`, and `gcd(B,Q)=1` because `gcd(A,Q)=1` and p is a
unit modulo Q. Define the counterfeit on **this exact allowed grid**:

$$
\widetilde w_t
=\frac{\left\lceil Q_t(1-a_t/p)\right\rceil}{Q_t}\pmod1,
\qquad \widetilde y_t=\frac{a_t}{p}+\widetilde w_t\pmod1.
$$

Then all of the following hold for every window:

1. `den(tilde w_t)` divides Q_t. No new prime, larger prime power, or larger
   conductor is introduced at any individual time.
2. Its p-primary phase is still exactly the authentic `a_t/p`.
3. Because `p` is coprime to Q_t and `a_t` is nonzero,
   `0<tilde y_t<1/Q_t` strictly.
4. With `Q_min=min_t Q_t`, every cell count at any integer `M<=Q_min` lies
   in cell zero, so `E_tilde=M` and the ordered small-ball count is
   `Delta^2` at radius `1/M` (for the usual `M>2` domain).
5. For every integer h,

$$
\left|\frac1\Delta\sum_t e(h\widetilde y_t)-1\right|
<\frac{44|h|}{7Q_{\min}}.
$$

**Proof:** ceiling changes the target by a number strictly between zero
and `1/Q_t`. Rational reduction only removes denominator factors. The
p-primary component is unchanged by adding a p-free fraction. The cell and
phase bounds follow directly. This proof uses no stochastic model.

### The obstruction survives a growing window

The inherited authentic height theorem PH-10 in
[PI_PASCAL_PRIME_HEIGHT.md](../2026-10-24/PI_PASCAL_PRIME_HEIGHT.md) proves
`log den(U_n)>=(3+o(1))n`, using the ordinary PNT in fixed classes modulo 8.
The circle and unwrapped state have the same denominator. Hence for every
fixed epsilon>0, all sufficiently large eligible primes satisfy

$$
Q_{\min}\ge\frac{\exp((3-\epsilon)(m+1))}{p}.
$$

In particular the fake collision is maximal at every prescribed polynomial
scale M in p, while its normalized Fourier mean approaches 1 exponentially
fast. This is a theorem derived from the authentic source's allowed grids,
not an extrapolation from the finite examples.

**Exact scope of refutation:** allowed denominator divisibility, absence of
new places, authentic local p-clock, and the upper conductor schedule do not
force real-circle decorrelation. The construction need not retain the exact
reduced denominator after rounding, nor the original other-prime numerators,
nor the four-pole recurrence, nor its initial condition. It is **not** a
counterexample to a fully authenticated BBP statement. The tests deliberately
reject it against the actual recurrence. The stronger same-forcing,
altered-initial-condition countercontrol belongs to
[BBP_RESONANCE_OBSTRUCTIONS.md](BBP_RESONANCE_OBSTRUCTIONS.md).

This strengthens the earlier arbitrary-q p-free counterfeit only in the
explicit conductor-divisibility sense. It does not claim to preserve all
primary observations, which would determine the exact rational circle phase.

## 4. Why exact distinctness or denominator size does not finish counting

If a rational difference has nonzero p-primary component and p-free
complement denominator Q, its distance to the nearest integer is at least
`1/(pQ)`. That is an exact separation statement. Its right side decreases
when Q grows. It therefore supplies no exclusion at the much coarser
polynomial radius `1/M` when the complementary denominator is exponential.
The construction in section 3 gives a concrete witness that even retaining
the actual allowed denominators leaves every pair in one small cell.

The difference identity

$$
U_{n+k}-U_n=(16^k-1)U_n+
\sum_{j=1}^k16^{k-j}r(n+j)
$$

is source-exact, but the main state and the forcing sum can cancel modulo
one. Counting their denominators or proving they are unequal does not bound
how often their real distance is below `M^(-1)`. No source-selected upper
bound for that near-collision count has been established in this bearing.

## 5. Reproducibility and authority

Files:

- `observational_succ/bbp_resonance_collision.py`: exact ladder error budget
  and same-allowed-conductor anti-phase construction;
- `tests/test_bbp_resonance_collision.py`: independently summed BBP source
  cells, forcing-bound holdouts, no-new-conductor checks, original p-primary
  reconstruction, maximal collisions, and actual recurrence rejection.

Executed locally: `python -m unittest tests.test_bbp_resonance_collision -v`:
**5 tests passed**. The counterfeit controls cover p=17,41,73,97,113 and
M=16,64,256. The infinite claims are supported by the displayed proofs and
explicitly named inherited height theorem, not by those finite cases.
No new Lean declaration is claimed. Full-tree validation is reported by the
principal separately.

| Claim | Status | Boundary |
|---|---|---|
| RCL-01 finite ladder inequality | PROVED PAPER; finite exact budget tested | Does not estimate authentic E asymptotically |
| RCL-02 same-allowed-conductor counterfeit | PROVED PAPER; exact controls tested | Changes complementary residues and recurrence |
| RCL-03 exponentially fine counterfeit alignment | PROVED conditional on imported PH-10/PNT | Does not preserve exact reduced denominators |
| Authentic `E=o(log N)` or `E=N^{o(1)}` | UNVERIFIED | Requires new source-selected temporal counting |
| Pi normality / mathematical undecidability | OPEN / NOT ESTABLISHED | No infinite completion is inferred |
