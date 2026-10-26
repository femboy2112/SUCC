# Odd-denominator resonance controls and the sharp uniform-initial-state boundary

**Status:** PROVED PAPER for the finite statements and stated asymptotic; exact
finite code and adversarial tests. Scholarly novelty is UNVERIFIED. Authentic
zero-initial BBP cancellation and pi normality remain OPEN.

**Baseline:** PR #296, `461942c0bf616518e668d236d1c6b1596665a7dd`.
This work owns no Gram-purity or Fejer-innovation estimate. It isolates what
an arithmetic prime-window bound can infer without the selected initial state.

## Hole contract and provenance

The proposed shortcut is a vanishing upper bound for the first prime-window
sum, uniform over rational trajectories having odd denominators, the genuine
p-primary first-birth clock, and the exact signed BBP recurrence. The cheapest
falsifier is a rational initial state chosen from a finite future endpoint.
The construction below refutes this uniform statement while preserving those
properties. It does **not** refute a theorem retaining `U_0=0`.

The novelty tax is explicit. [CSI-04 and CSI-08](../2026-10-24/CYCLOTOMIC_SELECTED_INTERFERENCE.md)
already construct dyadic shifted initial states with authentic forcing and
near-coherent finite windows, preserving every odd-primary component; CSI-05
classifies their eventual coalescence. [MP.GAUGE-01 and MP.GAUGE-03](../2026-10-24/BBP_MINIMAL_PATH_GAUGE_AND_MISSING_PRIME.md)
already establish Green conjugacy and much stronger modified-forcing controls.
Those ideas are inherited, not rediscovered. The additions here are:

- an entirely finite rational endpoint construction whose initial and all
  state denominators are **odd**, and whose p-primary clock is unchanged;
- an explicit **modulus deficit of order m^-4**, with its exact
  asymptotic coefficient, to match a forcing-variation lower bound of that order;
- a quantified distinction between inexpensive independent anti-phase rounding
  and expensive coherence for a single homogeneous rational clock.

Changing an odd initial denominator can change other odd-primary components.
We claim preservation of the selected p-primary component, not all odd clocks.

## 1. Pointwise p-free approximation is inexpensive

Let p=8m+1 be prime, L=ord_p(16), Delta=3m and
`a_t = 4*16^t mod p`. For any odd q coprime to p choose s_t nearest to
`-q*a_t/p` and put `w_t=s_t/q`. Then

\[
\left|\frac{a_t}{p}+w_t\right|\le\frac1{2q}.
\]

The sequence is L-periodic, its complementary denominators divide q and are
p-free, and for every integer h,

\[
\frac1\Delta\Re\sum_{t<\Delta}e\left(h\left(\frac{a_t}{p}+w_t\right)\right)
\ge 1-\frac{242h^2}{49q^2}.
\]

**Proof.** Apply nearest-grid approximation and
`cos(2*pi*x) >= 1-2*pi^2*x^2 >= 1-(968/49)*x^2`, using pi<22/7.
The residues repeat after L, so the deterministic rounding repeats too. QED.

Taking q=2p+1 gives near-perfect coherence with q only linear in p. Consequently
even a polynomial denominator bound alone does not exclude high-period
anti-phase imitation. This construction **fails the exact BBP recurrence**;
the code records its homogeneous recurrence defects rather than assigning it
an authentic source label. The collision branch's authentic-conductor-grid
control can impose a stronger denominator schedule; it has the same recurrence
boundary.

## 2. Exact forcing and odd denominators still allow almost complete resonance

Retain the complete original forcing for every n:

\[
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},
\qquad U_0=0,\quad U_n=16U_{n-1}+r(n).
\]

For each prime p=8m+1 set N=4m and

\[
q=2pm^2 16^N+1,\qquad
A_N=\frac{U_N}{16^N}=\sum_{k=1}^{N}16^{-k}r(k).
\]

Let c be a nearest point of `(1/q) Z` to `-A_N`. Thus
`epsilon=c+A_N` has absolute value at most `1/(2q)`. Define

\[
X_0=c,\qquad X_n=16X_{n-1}+r(n)=U_n+16^n c.
\]

**Finite theorem.** For n=m+1,...,4m:

1. The forcing is exactly the original four-pole forcing at every step.
2. All X_n have odd rational denominators. Their p-primary numerators are
   exactly `4*16^(n-m-1) mod p`; their complementary phase is p-free and odd.
3. `|X_n| < 1/(32m^2)`.
4. For h nonzero, with `W'_p(h)=sum_(n=m+1)^(4m) e(h X_n)`,

\[
\boxed{
0\le 1-\frac{|W'_p(h)|}{3m}
 < \frac{121h^2}{6272m^4}.
}
\]

**Proof.** Every quantity selecting c is finite rational arithmetic. Since
q is odd and congruent to 1 modulo p, c has an odd p-free denominator.
The two apparently even source terms combine as

\[
-\frac2{8n-4}-\frac1{8n-2}
=-\frac{3n-1}{(2n-1)(4n-1)},
\]

so the forcing, U_n, and X_n have odd denominators. The difference
`X_n-U_n=16^n c` is p-integral, hence changes no p-primary component.
The established first-birth theorem supplies the claimed nonzero residue.

Expanding the exact recurrence backwards from N yields

\[
X_n=-\sum_{k=n+1}^{N}16^{n-k}r(k)+16^n\epsilon.
\tag{1}
\]

The finite positive sum is bounded by the inherited Green-tail bound
`T_n < beta_n = 1/((8n+1)(8n+2))`. Therefore

\[
|X_n|<\beta_n+\frac{16^n}{2q}
<\frac1{64m^2}+\frac1{4pm^2}
\le\frac1{m^2}\left(\frac1{64}+\frac1{68}\right)
<\frac1{32m^2}.
\]

Here p>=17 for the declared prime family. Applying the same cosine inequality
and averaging gives

\[
\frac{|W'_p(h)|}{3m}\ge\frac{\Re W'_p(h)}{3m}
>1-\frac{968h^2}{49}\frac1{1024m^4}
=1-\frac{121h^2}{6272m^4}.
\]

The lower deficit bound is the triangle inequality. QED.

The control's **only failure of the supplied finite authentic history** is
`X_0=c != 0`. Indeed A_N>=47/240 and q is large enough that its nearest
negative grid point is nonzero. The source history validator checks initialization
and every exact forcing step separately, rejecting this control for precisely
the initialization error. Its labels cannot be mistaken for a genuine BBP passport.

The quantifier order is

\[
\text{for every p-window there exists a rational }c_p.
\]

There is no assertion that a single fixed rational initial state stays coherent
on all windows. Unlike the dyadic controls, these odd shifts need not coalesce
with the original orbit. Their global normality is not determined here.

## 3. The m^-4 deficit is attained with an exact limiting coefficient

For the controls of section 2 and each fixed nonzero integer h,

\[
\boxed{
\lim_{\substack{p=8m+1\to\infty\\p\text{ prime}}}
m^4\left(1-\frac{|W'_p(h)|}{3m}\right)
=\frac{3\pi^2h^2}{131072}.
}
\]

**Proof.** The inherited sharp beta bracket gives
`T_n=1/(64n^2)+O(n^-3)` uniformly for n>=m. Equation (1) can be written

\[
X_n=-T_n+16^{n-N}T_N+16^n\epsilon.
\tag{2}
\]

Uniformly over the window, `m^2*16^n*epsilon=O(m^-1)` because
`q>2pm^2 16^N` and p=8m+1. The terminal correction
`m^2*16^(n-N)*T_N` is bounded and its mean absolute value is O(m^-1):
sum the finite geometric series. Thus it has vanishing mean and second
moment, even though it is non-negligible at the final few indices. This
explicit boundary term cannot be dropped pointwise.

Consequently the first two empirical moments of m^2 X_n converge by ordinary
Riemann sums to those of `-1/(64s^2)` with s uniform on [1,4]. Direct integration
gives

\[
\mathbb E(s^{-2})=\frac14,\qquad
\mathbb E(s^{-4})=\frac7{64},\qquad
\mathrm{Var}(s^{-2})=\frac3{64}.
\]

It follows that `m^4 Var(X_n) -> 3/262144`. To pass to the complex mean,
expand its **squared modulus** by pairs:

\[
\left|\frac1{3m}\sum_n e(hX_n)\right|^2
=\frac1{(3m)^2}\sum_{n,k}\cos(2\pi h(X_n-X_k))
=1-4\pi^2h^2\mathrm{Var}(X_n)+O_h(m^{-8}).
\]

The remainder is uniform because `|X_n|<1/(32m^2)`; the fourth-order cosine
remainder suffices. Divide the squared-modulus deficit by one plus the modulus,
which tends to 2. This gives the displayed coefficient. QED.

This is a sharpness result for estimates **uniform over the initial-state
family**. It neither supplies a lower bound for the actual zero-initial
window nor weakens its source-selection requirement. When combined with a
proved universal forcing-variation gap of order m^-4, it establishes the
correct order of that universal gap, while showing that it cannot approach
the requested cancellation bound.

## 4. A finite prefix and an unchanged forcing tail still do not authenticate the source

Fix K with 0<=K<m. Start at zero, preserve the first K authentic forcing
values, and change only the next one by

\[
\widetilde r(K+1)=r(K+1)+16^{K+1}c.
\]

All other values equal r(n). The resulting state equals U_n through K and
equals X_n for all n>=K+1. Thus the same near-coherent p-window occurs with
zero initial state, the same initial K observations, and an **identical
forcing tail**, hence identical asymptotics to every inverse-power order.
The impulse is p-free and occurs before p-birth. It can be large or negative;
positivity is not claimed. The exact global four-pole law fails at precisely
the recorded index K+1, and the validator rejects it there.

This finite-tail control is simpler and weaker than MP.GAUGE-03's carefully
positive exponentially small all-time perturbations. It is included as an
executable mutation test, not a novel source-indistinguishability theorem.

## 5. Homogeneous time consistency has an exponential denominator cost

Let `x=a/p+b/q` have a nonzero p-primary component, gcd(p,q)=1. Suppose the
centered lifts z_t of `16^t x`, for t=0,...,H-1, all satisfy
`|z_t|<=rho<1/17`. Then

\[
\boxed{q\ge\frac{16^{H-1}}{p\rho}.}
\]

**Proof.** The integer `z_(t+1)-16z_t` has absolute value at most 17rho<1,
so is zero. Hence `z_t=16^t z_0`. The nonzero p-primary part ensures z_0 is
nonzero, and its rational denominator divides pq, so `|z_0|>=1/(pq)`.
Use `|z_(H-1)|<=rho`. QED.

This explains why independent polynomial-q anti-phase rounding is inexpensive
while a single homogeneous q-clock shadowing zero for H steps costs
exponentially many denominator units. The lemma **does not apply** to the
inhomogeneous BBP recurrence; section 2 retains its forcing and uses the
backward source-tail correction explicitly.

## 6. Inverse theorem: near-maximal resonance lies in explicit exponentially narrow seed arcs

The preceding controls describe actual resonant examples. The converse below
classifies **every sufficiently near-maximal window**, with exact finite
source-dependent centers. It concerns deficit of size at most O(1/D); it
does not classify a window whose normalized character magnitude is, for
example, 1/2. Ordinary expanding-map cylinder geometry is classical; the
addition here is an explicit conversion from character-mean deficit to
one common integer branch, with authenticated rational BBP centers and
constants suitable for exact rejection tests. Academic novelty remains
UNVERIFIED.

Let D>=2, T=D-1, h be a nonzero integer, and consider any real trajectory

\[
X_{t+1}=16X_t+r_{t+1},\qquad 0\le t<T.
\]

Write `r_min=min_(1<=j<=T) r_j`, `r_max=max_(1<=j<=T) r_j` and

\[
S_T=\sum_{j=1}^{T}16^{-j}r_j.
\]

Choose a positive radius a satisfying

\[
34a+|h|(r_{\max}-r_{\min})<1.
\tag{3}
\]

**Finite inverse theorem.** If

\[
1-\left|\frac1D\sum_{t=0}^{T}e(hX_t)\right|\le\frac{8a^2}{D},
\tag{4}
\]

then X_0 modulo one lies in the union of **15|h| explicit circle arcs**

\[
\boxed{
\left\{x:\left\|x-\left(\frac{j}{15|h|}-S_T\right)\right\|\le R\right\},
\quad 0\le j<15|h|,
\qquad
R=\frac{32a+|h||r_T|}{15|h|16^T}.
}
\tag{5}
\]

**Proof.** Put `M=D^-1 sum e(hX_t)` and `epsilon=1-|M|`. Condition (3)
forces a<1/34, so (4) ensures M is nonzero. Choose theta with
`e(theta)=M/|M|`. The exact mean-center identity is

\[
\sum_t|e(hX_t)-e(\theta)|^2=2D\epsilon\le16a^2.
\]

For circle distance, `|e(x)-1|>=4||x||`. Thus every hX_t has a unique
lift `y_t=theta+q_t`, where `|q_t|<=a`. Define

\[
d_t=q_{t+1}-16q_t-hr_{t+1}.
\]

All d_t are congruent to 15theta modulo one. They occupy a real interval
of length at most `34a+|h|(r_max-r_min)<1`. Consequently they are all the
same real b: distinct congruent values would differ by a nonzero integer.
There is one integer `k=b-15theta`, and

\[
y_{t+1}=16y_t+hr_{t+1}+k.
\]

Set `f=-k/15`. The translated trajectory satisfies
`y_(t+1)-f=16(y_t-f)+hr_(t+1)`. Telescoping gives

\[
y_0-f+hS_T=16^{-T}(y_T-f).
\tag{6}
\]

The final step yields a tighter terminal estimate than an arbitrary
supremum bound:

\[
y_T-f=q_T+\frac b{15}
=\frac{16(q_T-q_{T-1})-hr_T}{15},
\qquad
|y_T-f|\le\frac{32a+|h||r_T|}{15}.
\]

Insert this in (6), remember `y_0=hX_0 mod 1`, and divide by h. The possible
values of f/h modulo the frequency-lift ambiguity form the grid of
15|h| points in (5). QED.

For the authentic prime window, substitute D=3m, X_t=X_(m+1+t), and
`r_j=r(m+1+j)`. Strict source monotonicity makes the forcing spread
`r(m+2)-r(4m)`. All arc centers, radii and hypotheses are rational for
rational a. If the actual zero-initial start U_(m+1) lies **outside** these
arcs, the contrapositive gives the genuine finite lower bound

\[
1-\frac{|W_p(h)|}{3m}>\frac{8a^2}{3m}.
\]

The executable oracle reports membership and this threshold separately;
it does not claim that membership implies coherence. Tests verify that the
same-forcing controls of section 2 lie inside the arcs at p=41,73,97,193,
while the authentic starts lie outside those particular certified arcs.
Tests also cover all 15|h| frequency/fixed-point lifts at h=-2 and h=3.

For an order-m^-4 deficit, one may take a of order m^-3/2 (with its constant
large enough for (4)). The arc radius is then
`O_h(16^(-(3m-1))*m^(-3/2))`. This identifies the exact finite source seeds
whose exponentially precise approximation is necessary for this extreme
resonance. The source-specific seed exclusion for **all growing p** is not
proved. A very small union of arcs is not a probability statement about the
deterministically selected zero initialization, and this inverse result does
not address the broader nonvanishing-resonance regime needed for normality.

## Executable receipt and verdict

Artifacts: `observational_succ/bbp_resonance_controls.py` and
`tests/test_bbp_resonance_controls.py`.

The focused suite checks independent direct four-pole identities, exact
backward terminal sums, odd denominators and p-primary residues through p=193,
typed rejection of p=3,5 and composites, a changed signed coefficient, the
single-impulse boundary, the inverse seed-arc theorem's hypotheses and fixed-point
lifts, and a certified rational Machin/Taylor phase enclosure of the modulus-loss
control at p=17. These finite tests audit implementation;
the universal and asymptotic statements derive from the proofs above.

**Verdict:** source shape and recurrence alone permit order-m^-4 near-resonance
in an odd rational selected-initial-state family. This is a precise obstruction
to a uniform-in-initial-state arithmetic proof and an order-sharp calibration
for finite nonflatness estimates. The missing lamp is an estimate that uses
the exact zero initialization and full source history to exclude these tuned
selectors without assuming the desired signed cancellation.
