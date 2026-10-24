# Operation MINIMAL PATH — the BBP gauge, one missing prime, and the signed spectral bulk

**Research-only, 2026-10-24.** Direct parent: SUCC draft PR #256 at `0683f8f166b9106ab8405a2d6538415b5ac84ba3`; inherited source PR #254 at `fceb04645926898bb5f72346dca54f3134b06cea` and repaired PR #252. PR #253 is a sibling; no dependent Lean authority imported. Main and frozen original archives untouched. All new universal claims here have paper derivations and exact local control models; academic priority is **UNVERIFIED**. No all-horizon *pi-selected* signed cancellation bound, pi normality, RH or Weil positivity is claimed.

## 0. Steelman the minimal-path intuition, but do not promote it to a physical law

Search for a smallest source-faithful transformation or reconstruction that eliminates redundant dynamics. An admissible explanatory claim must still use the actual source and initial state and must survive counterfactual mutations. Physical nature need not satisfy a global variational principle of "simplicity": the slogan motivates an *algorithmic research criterion*, not a theorem.

The authentic BBP forcing, selected state and bounded Green future are

```
r(n)=4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2),  n>=1,
y_0=0,  y_n={16*y_(n-1)+r(n)},
t_n=sum_(k>=1) 16^-k*r(n+k),  n>=0,
16*t_(n-1)=r(n)+t_n,   t_0=pi/16,   t_n>0,  t_n=O(n^-2).
```

Here `{.}` means reduction modulo one; `{pi}` has not been declared normal. The index-variable poles, positive Hausdorff Green measure, and `Q/Z` arithmetic prime-primary torsion live in distinct domains.

## MP-01. Exact nonautonomous gauge conjugacy (DISCLOSED; classical algebra)

For **any** forcing sequence with a bounded backward Green solution `t_n`, define `H_n(y)=y+t_n mod 1` on the circle. Then

```
H_n({16*y+r(n)})={16*H_(n-1)(y)}.
```

Indeed, `r(n)+t_n=16*t_(n-1)`. The horizontal dynamics is *exactly* the ordinary base-16 circle covering in a moving coordinate. For the BBP authentic initial state, `H_0(0)=t_0=pi/16`, and the transformed trajectory is `{16^n*pi/16}`. Thus the source selects the **initial phase** but the conjugacy does not supply its statistical genericity. It is false to interpret forcing complexity alone as mixing.

For every period-L point `z=k/(16^L-1)` (including fixed points), `y_n'={16^n*z-t_n}` solves the **identical real forcing** and converges in circular distance to the periodic orbit `{16^n z}`. Its initial state is `{z-t_0}`, in general NOT zero. This proves that even the exact full forcing does not imply normality without the source-selected initial state. A rational nonzero initial change is not sufficient to arrange this example; the tuned state may be irrational.

**Important type distinction:** the existence of a bounded *real time-dependent* Green coboundary `r(n)=16t_(n-1)-t_n` does not contradict PR #252's obstruction to a *rational-function-in-index* coboundary. Different coefficient categories and admissible maps; neither result kills the other.

## MP-02. A single absent prime makes the retained local source observation nonfaithful (DISCLOSED)

For a prime q, the subgroup `Z[1/q]/Z` is dense in the real circle: at depth M, the grid of q^M points has spacing q^-M. A rational circle phase has the canonical direct-sum decomposition into p-primary torsion components (`Q/Z = direct-sum_p C_(p^infty)`). Adding a q-primary phase changes **no** p-primary component for any p != q, including arbitrarily deep p-power torsion.

That is a precise source-map nullspace. It is not a claim that all *integral p-adic values* remain unchanged: p-adic unit residues may change while the negative-valuation principal part does not. Do not conflate `Q/Z` torsion with the full p-adic field or its integral unit data.

## MP-03. Two-source indistinguishability of normality, with positivity and exponentially accurate BBP forcing (DISCLOSED, paper construction)

**Theorem.** Let q be any fixed rational prime, let K>=0, and let eps>0. There exist two rational forcing sequences `r_per(n)` and `r_norm(n)`, with source-selected rational states `y_per(0)=y_norm(0)=0`, satisfying all of the following:

1. `r_per(n),r_norm(n)>0` for all n, and for n>=2 both belong to (0,1).
2. The first K forcing samples and corresponding states agree *exactly* with the authentic BBP `r(n),y_n`.
3. For all n>=1, `|r_*(n)-r(n)| < eps*16^-n` after tightening the construction's error budget (where `*` denotes either branch). In particular every algebraic inverse-power asymptotic coefficient of the forcing agrees with BBP.
4. For every n and every p != q, the **whole p-primary torsion components** of both constructed rational states equal those of the authentic rational y_n. Likewise the p-primary torsion readouts of the forcing values agree. Equivalently, `y_*(n)-y_n` and `r_*(n)-r(n)` lie in `Z[1/q]` modulo integers.
5. The `per` selected trajectory is asymptotic to a period-L orbit of `x -> 16x mod 1` and is NOT normal (for the fixed nonzero integer Fourier mode `h=16^L-1`, the normalized character sum tends to 1).
6. The `norm` selected trajectory is asymptotic to a base-16-normal orbit and IS normal, by the classical existence of normal base-16 numbers and stability of Cesaro averages under pointwise asymptotically vanishing circular errors.

For q=3 all rational denominators can be taken **odd**, retaining the baseline denominator parity; this is the strongest easy mutation control for the BBP rational carrier.

**Proof.** Choose *either* a periodic `z` or a base-16-normal `z` arbitrarily close to `t_0=pi/16`. Periodic points are dense because the grids with denominator `16^L-1` become fine; normal points are dense because they have full Lebesgue measure (or append a base-16 Champernowne tail after an arbitrarily chosen finite prefix). Let `z_n={16^n z}` and `a_n={z_n-t_n}`. Then, regardless of which z was chosen,

```
a_n = {16*a_(n-1)+r(n)}.
```

Because `t_n->0`, the a-orbit is asymptotic to z_n. Choose z close enough to t0 that, for all n<=K, the *exact* BBP y_n is within a prescribed tiny circular tolerance eta_n of a_n; this follows from the factor `16^n*|z-t0|`. Freeze those first K states exactly. At every later index independently, exploit the density of the coset `y_n + Z[1/q]` to choose a rational state `y_*(n)` within eta_n of `a_n` in circle distance. Take `eta_n` decreasing at least as fast as `eps*16^(-n-6)`, and also less than `r(n)/100` and `(1-r(n))/100` (n>=2). Make `|z-t0|` small enough that the initial error satisfies the same forcing budget. Since all q-cosets admit arbitrarily fine rational approximants, every step is feasible.

Lift the target circular closeness to signed real errors `e_n` with `|e_n|<eta_n`, so `y_*(n)=a_n+e_n mod 1`. Then define the rational forcing as the integer lift nearest authentic r(n) of `y_*(n)-16y_*(n-1)`. The *exact* recurrence and the known Green identity give

```
r_*(n)=r(n)+e_n-16*e_(n-1),
|r_*(n)-r(n)| <= eta_n+16*eta_(n-1) < eps*16^-n.
```

For n=1 use `e_0=t0-z` (a small lift) and the same formula. Positivity follows from the strict BBP forcing lower bound and the chosen tolerances; `0<r(n)<1` for n>=2. Since `y_*(n)-y_n` is q-primary modulo 1, the forcing difference is q-primary modulo 1, so every p != q torsion trajectory/readout agrees **exactly** to all available prime-power depths. The y-orbit is asymptotic to z_n, so its limiting empirical measure is respectively periodic atomic or Haar. For the period-L target, taking h=16^L-1 makes every target phase equal 1 under e(h .), hence Cesaro tends to 1. For the normal target, each fixed character time-average converges to 0 by Weyl and pointwise vanishing error. QED.

**What the theorem does NOT preserve:** the exact four-pole *global rational-function law for every n*, the missing q-primary source, the full p-adic integral-unit readouts, or the selected real boundary mass `t0=pi/16` after perturbation. The exact authenticated original BBP still uniquely selects its own orbit, whose normality remains open. This is a **sharp source-map and access limitation**, not a refutation of pi normality.

## MP-04. Exact cyclic-time Fourier decomposition of the actual prime-window complement (DISCLOSED)

For each prime p=8m+1 use the authentic PR #256 first-birth window, local period `L=ord_p(16)|m` and B=3m/L. For any fixed integer h nonzero and p>|h|, let

```
u_s = e(4*h*16^s/p),   0<=s<L,
v_s = (1/B) sum_(b=0)^(B-1) e(h*w_(p,bL+s)),
```

where w is the **full** p-prime-to-p complement of the BBP rational phase, not a separate independently sampled clock. Normalize discrete Fourier transforms by `hat f(k)=(1/L)sum_s f_s*e(-ks/L)`. Ordinary finite Fourier inversion and Parseval show

```
W_p(h)/(3m) = sum_(k mod L) hat u(-k)*hat v(k)
            = hat u(0)*hat v(0) + sum_(k=1)^(L-1) hat u(-k)*hat v(k).
```

The constant harmonic `hat u(0)` has BGK subgroup cancellation on the good primes of PR #256; the **other L-1 modes form the exact unresolved signed interaction**. This is an operational change of common basis, not proof of stochastic independence or quantum phasors.

For k !=0 the multiplicative character `16^s -> e(-ks/L)` on H=<16> extends to Fp*. Its weighted subgroup Gauss sum is the mean of `(p-1)/L` ordinary prime-field Gauss sums after projecting onto H; each nontrivial Gauss sum has absolute value sqrt(p). Therefore

```
|hat u(k)| <= min(1,sqrt(p)/L),  k!=0.
|W_p(h)/(3m)| <= |hat u(0)| + (sqrt(p)/L)*sum_(k!=0)|hat v(k)|.
```

If an independent source-derived theorem established `sqrt(p)*sum_(k!=0)|hat v(k)|/L -> 0` along the good primes, pi would be base-16 normal for every fixed h by the PR #256 prime-window equivalence. **This spectral smallness is UNVERIFIED and numerically its naive bound is usually vacuous.** Do not silently assert that the source's complement has low Fourier complexity.

Moreover, Parseval for `|u_s|=1` says

```
sum_(k mod L)|hat u(k)|²=1,
sum_(k!=0)|hat u(k)|²=1-|hat u(0)|² ->1
```

on the good primes. BGK cancels the *zero* harmonic; it does NOT annihilate the spectral bulk. Choosing the hostile complement `v_s=conj(u_s)` makes the full average exactly 1 even if `hat u(0)` is arbitrarily small. This rules out source-blind promotion of local cancellation to global cancellation. An authentic π proof must establish **signed nonzero-mode cross-source orthogonality**, not merely small local scalar averages.

## MP-05. Minimal source-sensitive verdicts and failed routes

| Attempt | Decisive result | Status |
|---|---|---|
| Force-rich BBP dynamics guarantees mixing | Gauge conjugacy plus fixed-period initial states | REFUTED |
| Every p != 3 prime-primary readout + rational odd carrier + positive O(n^-2) forcing selects normality | One q-adic normal/nonnormal indistinguishable pair | REFUTED |
| Same exact four-pole forcing, same initial y0=0, gives two different orbits | Determinism of recurrence rules it out | REFUTED |
| BGK local zero mode suppresses all cyclic spectral modes | Parseval preserves nearly unit nonzero-mode energy | REFUTED |
| Gauss bound + small signed complementary Fourier norm suffices | Finite DFT plus classical Gauss estimate | DISCLOSED conditional; premise UNVERIFIED |
| BBP-selected signed Fourier sums are o(N) for h=1 or all h | No proof obtained; asymptotic still missing | UNVERIFIED |

The strongest viable proof instrument is now **authentic signed spectral cross-clock transport**: derive an estimate for `sum_(k!=0)hat u(-k)hat v(k)` by the *entire authenticated forcing*, not a coarse approximation class. An alternative route is a genuine direct bound on the exact BBP-selected x0=pi/16 orbit after gauge conjugacy; that should be judged by its discriminating power against nearby normal/nonnormal points.

## MP-06. Reproducibility, calibration and authority

- `observational_succ/bbp_minimal_path.py`: exact Fraction source-only rational approximation of periodic z to the BBP tail t0, q^M coset corrections and signed source lift. No pi digits.
- `tests/test_bbp_minimal_path.py`: periodic point calibration, independent CRT p-primary oracle, two choices of omitted prime, source positivity, exact frozen prefix, exponentially small forcing changes, circular Green comparison, mutation and spectral Fourier recomposition.
- `observational_succ/bbp_cyclotomic_spectral.py`: finite common-basis period DFT, complement retained from the **actual BBP source**, group mean and signed mixed term. Uses machine complex values for FINITE diagnostic comparisons only.
- `scripts/bbp_minimal_path_probe.py`: deterministic exact Fraction digest with bounded-size summaries and separately labeled approximate cyclic spectral data.

Focused tests were executed locally against an API-equivalent minimal parent `bbp_source_memory` with original four poles, exact Fraction `forcing`, `forced_step` and `tail_interval`. That is **not the complete repository**. No Lean kernel compilation or hosted final-head CI is inferred. All universal positivity/density/Gauss statements are paper mathematics, not finite-experiment proof.

### Sources (separate mathematical dependencies)

- Original exact BBP repair / tail source: SUCC PR #252, https://github.com/femboy2112/SUCC/pull/252
- Uniform full-orbit signed transfer and Green spectral representation: SUCC PR #254, https://github.com/femboy2112/SUCC/pull/254
- Authenticated p-birth and good-prime local BGK analysis: SUCC PR #256, https://github.com/femboy2112/SUCC/pull/256
- D. H. Bailey and R. E. Crandall (2001), https://doi.org/10.1080/10586458.2001.10504441
- J. C. Lagarias (2001), https://doi.org/10.1080/10586458.2001.10504456
- J. Bourgain, A. Glibichuk, S. V. Konyagin, JLMS 73 (2006) 380-398, https://doi.org/10.1112/S0024610706022721
- Classical nontrivial Gauss sums of modulus sqrt(p): Davenport, Multiplicative Number Theory I, Chapter 9; https://personal.science.psu.edu/rcv4/personal/Publications/MNTI/13.0_pp_282_325_Primitive_characters_and_Gauss_sums.pdf

## Next verdict-changing probe

1. Formalize MP-01 (exact commuting gauge square) and MP-02 (finite p-primary preservation) in Lean with no `sorry`; review all abstract density theorems separately.
2. Build a *source-specific* cyclic Fourier joint state and test whether retained holonomic two-state Green data reduce nonzero-mode spectral cross-correlations. Do not claim independence from a finite test.
3. Compare authentic BBP-selected complement Fourier vectors against normal and nonnormal q=3 matched counterfeits on held-out p windows, with explicit source mutation and exact phase bounds.
4. Seek a provable `o(1)` signed cross-mode bound or a genuinely new unbounded-horizon estimate in the exact BBP source class. Recheck all published unconditional exponential-sum bounds and their scope before invoking them.

**Final status:** π base-16/2/10 normality OPEN, RH OPEN, signed global BBP interference OPEN. This round demonstrates a new-to-SUCC minimal source-map obstruction and a precise spectral discrimination instrument, not the missing cancellation theorem.
