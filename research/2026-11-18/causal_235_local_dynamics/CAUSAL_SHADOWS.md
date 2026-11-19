# Causal audit: simultaneous 2/3 observations and the retained source boundary

Audit of SUCC main `81be6b897ae980b801a3b9de9e22ef81e8360bfb`.
User-facing date: 2026-11-18 (America/New_York).

## Earned result

**PROVED ELEMENTARY EXTENSION:** every finite carry-residue word can coexist
with arbitrarily deep simultaneous 2-adic and 3-adic agreement with the authentic
BBP orbit, the identical forcing, and the identical chronological clock, after
changing its rational seed. This includes every finite adaptive transcript whose
state-dependent inputs are finite local reports. It does not include an exact
zero-seed certificate or an observed real carry. The theorem extends the existing
A-FS witness; it is not a counterexample to the fixed-zero pi problem.

**REUSED POSITIVE INTERFACE:** bounded-height rational reconstruction converts
sufficiently deep joint local observations back into the actual rational carrier.
This is already in SUCC as DZ3, not a new theorem here. The useful distinction is
between local clock dynamics, height-qualified state recovery, and asymptotic
signed phase cancellation. They are three separate contracts.

## 1. Exact mixed-place finite-shadow theorem

Use the unmodified four-pole source

\[
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},\quad
P_n=\sum_{j=1}^n16^{-j}r(j),\quad
U_n(s)=16^n(s+P_n).
\]

For every integer `N>=1`, `a>=2`, `b>=1`, and every word
`c=(c_1,...,c_N)` in `{0,1,2,3}^N`, define

\[
D=\sum_{n=1}^N(4+c_n)16^{N-n},\qquad
\beta=\frac{D}{16^N-1},\qquad A=2^a3^b,
\]
\[
Q=256 A16^N+1,\qquad
m=\left\lfloor\frac{(\beta-P_{N+1})Q}{A}+\frac12\right\rfloor,
\qquad s=\frac{Am}{Q}.
\]

Then, with reduced rational height `H(s)=max(|num(s)|,den(s))`,

1. `0<s<1`, the denominator of `s` is coprime to 6, and `H(s)<=Q`;
2. for every `n>=0`,
   \[
   U_n(s)-U_n(0)=16^ns,\quad
   v_2(U_n(s)-U_n(0))\ge a+4n,\quad
   v_3(U_n(s)-U_n(0))\ge b;
   \]
3. for every `1<=n<=N`,
   \[
   \lfloor U_n(s)\rfloor\equiv c_n\pmod4.
   \]

All computations constructing `s` use finite rational source data. No decimal
pi, unknown digit, or infinite future observation is used.

### Proof

`Q` is 1 modulo 6, so the valuation assertions follow immediately from the
seed formula and the exact affine recurrence. Rounding gives

\[
\left|s-(\beta-P_{N+1})\right|\le\frac A{2Q}
<\frac{16^{-N}}{512}.
\]

The periodic base-16 expansion of `beta` has digits `4+c_n` between 4 and 7.
Consequently every shifted fractional part belongs to `[4/15,7/15]`, and
`floor(16^n beta) mod4=c_n` for the stated times.

For a source-only bound, write

\[
r(n)=\int_0^1 t^{8n-8}(1-t)H(t)\,dt,\quad
H(t)=4+4t+4t^2+2t^3+t^4.
\]

On `[0,1]`, `0<H(t)<=15`. Thus `r(n)` is positive and decreasing and, for
`n>=1`,

\[
r(n+1)\le\frac{15}{(8n+1)(8n+2)}<\frac{15}{64n^2}.
\]

It follows that

\[
0<16^n(P_{N+1}-P_n)<\frac1{64n^2}\quad(1\le n\le N).
\]

The exact identity

\[
U_n(s)=16^n\beta
-16^n(P_{N+1}-P_n)
+16^n\big(s-(\beta-P_{N+1})\big)
\]

therefore changes no integer part: the lower fractional margin is at least
`4/15-1/64-1/512 =1913/7680>0`, and the upper is at most
`7/15+1/512 =3599/7680<1`. This proves the desired word without even invoking
the completed pi identity.

Finally `P_(N+1)<47/240+1/1024<1/5`, while `4/15<=beta<=7/15` and the rounding
error is smaller than `1/8192`. Hence `0<s<1`. Its unreduced positive numerator
is smaller than `Q`, so the reduced height is at most `Q`. This completes the
universal paper proof. Finite tests below audit the construction, not its
universal quantifiers.

## 2. Finite adaptive causal observers

Let a deterministic observer run for a finite horizon. It receives the exact
time, the source description and any finite source values. Its only queries of
the unknown carrier state are cosets

\[
U_n+2^{k_2}\mathbb Z_2,\qquad U_n+3^{k_3}\mathbb Z_3,
\]

at finitely many nonnegative integer depths. The 3-adic report includes the
actual polar part; it is not a silently reduced cleared numerator. Its query
choice and internal-memory update may depend arbitrarily on its preceding
transcript.

Run this observer on the zero-seed source and record its finite query depths.
Choose

\[
a\ge\max(2,\max(k_2-4n)),\qquad b\ge\max(1,\max k_3).
\]

Apply the theorem to any prescribed carry word through the largest queried
time. Every queried report agrees. By induction the observer chooses the same
next query, has the same internal memory and produces the same transcript.
Yet the prescribed real carry word can differ arbitrarily.

This is an explicit, source-preserving obstruction to an inference based only
on finite local histories. It does **not** cover exact equality tests for the
seed, exact rational state reports, or observed real carries. It also does not
cover a theorem whose premise is the authenticated initial condition `U_0=0`:
the constructed seed is positive and deliberately violates that premise.

The actual source's forcing-derived 3-adic polynomial clock is unchanged
identically. Any lawful Fibonacci observer factored through the finite 2/3
clock labels therefore survives this control. Exact clock intertwining alone
cannot supply the missing carry count.

## 3. Quantified boundary debt

Suppose a proposed positive-drift inequality applies to all these seeds,

\[
\sum_{n=1}^N1_{\lfloor U_n(s)\rfloor\bmod4\in\{1,2\}}
\ge\delta N-B(s),\qquad \delta>0,
\]

with a finite seed-dependent boundary term and uniform horizon quantifier.
The all-zero word forces `B(s_N)>=delta N`, although

\[
H(s_N)\le256 A16^N+1.
\]

In particular a uniformly bounded debt is impossible. More quantitatively,

\[
B(s_N)\ge\frac\delta{\log16}
\big(\log(H(s_N)-1)-\log(256A)\big).
\]

For a shell `[B,2B)`, use the all-zero prefix of length `2B`; the corresponding
coefficient is `delta/(2 log16)`. These are necessary constraints on a proposed
seed-uniform potential, not lower bounds on the authentic zero-seed count.
They supply a concrete adversarial calibration for any proposed zero-boundary
potential. Height-dependent costs or an exact-zero-only theorem remain possible.

## 4. Positive recovery boundary already in SUCC

If rationals `x=a/b`, `y=c/d` have positive denominators and heights at most `H`,
and `v_2(x-y)>=k`, `v_3(x-y)>=l` for nonnegative integers `k,l`, then
`2^k3^l` divides `ad-bc`. If

\[
2^k3^l>2H^2,
\]

the bound `|ad-bc|<=2H^2` forces equality. This proof also permits denominators
divisible by 3 when the finite report includes their polar part; the denominator
valuation only strengthens the numerator divisibility. Existence is supplied
by the real source; bounded enumeration supplies an exact finite decoder.

SUCC already has this classical height-qualified repair in
`research/2026-10-12/DIAGONAL_ADELIC_ZETA_SOURCE.md` (DZ3), and a source-specific
2-adic finite decoder in `research/2026-11-02/carrier_hbar_bridge/PROOFS.md`.
This audit uses them as the positive control, not as new discoveries.

## 5. What the forward-moving observer changes

The legal carrier chronology is `n -> n+1`; an algebraic inverse used in an
internal calculation does not enact a backward carrier step. Observation cycles
must retain elapsed time and whatever memory the declared prediction task needs.
The clock/source/initial-boundary certificate may itself be a sufficient model;
unbounded append-only history is not forced for every task.

For sample-driven finite differences of stride `d`, the `k`th forward null
filter based at `n` uses `r(n),...,r(n+kd)` and becomes observable at `n+kd`.
The same expression can be calculated earlier from a known deterministic source
law, but its status is then a model prediction rather than a future measurement.

The moving linear defect is

\[
D_n=P_{n+1}K_n-B_nP_n.
\]

Its noncommutative telescoping identity follows by insertion of the intermediate
projections. These descent/minimax/error statements are already established in
`docs/principia_observatoris/02_causality_geometry.md` and
`research/2026-11-14/tenacious_d/DEFECT_AND_GAUGE.md`; a change to moving coordinates
does not independently prove a new source-selected cancellation estimate.

## 6. Probe, truth state and next dependency cut

`test_mixed_causal_shadow.py` ran successfully: 4 unittest methods, all 1,364
words of lengths 1 through 5, exact long patterns at horizons 7, 19 and 48, an
adaptive local observer through time 33, a broken dyadic report mutant, an
exact-zero predicate discriminator and bounded-height reconstruction controls.
These are **OBSERVED FINITE** checks of the **PROVED PAPER** construction.

The smallest still-live pi route is a bound on the actual signed real carry or
phase statistic with exact zero ancestry and a source-dependent height or
boundary potential. The joint local observer supplies an instrument and a
falsifier; it does not supply that bound. Existing R0 and full pi-normality
remain open. No implication to Collatz termination or RH is claimed.

Primary project provenance:

- Main `docs/MAIN_XXVI_SOURCE_PHASE_INTERFACE.md`, especially CI-CG2 and CI-CG3.
- Main `research/2026-11-15/three_count_hail_mary/ADVERSARY_NOTES.md`, Theorem A-FS.
- Main `research/2026-10-12/DIAGONAL_ADELIC_ZETA_SOURCE.md`, DZ3.
- Main `research/2026-11-02/carrier_hbar_bridge/PROOFS.md`, bounded-height BBP decoder.
- The source description and zero-seed contract remain those of `docs/PI_NORMALITY_FRONTIER.md`.

No imported code or archival dossier was modified. This proof was developed
in a separate research task and audited before integration in this dossier.
