# Selected BBP collisions: carry rigidity and the limits of partial source authentication

**2026-10-24. Research branch:** `research/pi-lag-carry-rigidity-2026-10-24`.
**Base:** `ea5f92bbc52468e55b597e52455f24bceedb47b3` (delivered #265).
**Authority:** paper proofs, independently implemented exact finite checks, and
certified integer intervals. No new Lean declarations. Scholarly priority unverified.
**Pi normality: OPEN. The selected collision bound: UNPROVED.**

## 1. Frontier and exact hole contract

Live main was still `b116841f12b41aaf7600da39bbb40577f25b6295`; no consolidated
inclusion manifest existed at the starting audit. This branch therefore follows
the authorized #265 fallback. The [snapshot](PI_LAG_FRONTIER_SNAPSHOT.json)
records live PR heads, ancestry, and successful donor workflows. Only #250,
#264 and #265 in that snapshot are ancestors of this base. In particular the
final #256 p-squared lift is **not** silently inherited. Both incompatible
#260/#261 `bbp_minimal_path.py` blobs remain separately pinned and hashed;
this round neither consolidates them nor claims their MP crosswalk is merged.
Claude retains the main integration and cleanup campaign.

The complete handoff, SCE dossier, supplement, production module, validation
record and exact receipts were read. The 13 inherited focused tests and
byte-identical source receipt replay passed before extension. The independent
Galois and regret oracles also passed. Source corrections from #252, signed
transport from #253, prime/p-squared scope from #256, and the #259--262
selection obstructions were read at their pinned heads. No archival original
or donor implementation is edited.

The actual source is

\[
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},\quad
y_0=0,\quad y_n=\{16y_{n-1}+r(n)\}.
\]

For every sufficiently large prime p=8u+1 with
L=ord_p(16)>sqrt(p)/log p, put Delta=3u and let M be the largest power of
16 satisfying M^5<=p^2. The target is

\[
K_p(1)=\frac M{\Delta^2}
\#\{(s,t)<\Delta:\|y_{u+1+s}-y_{u+1+t}\|_{\mathbb T}\le1/M\}
\le p^\varepsilon
\]

eventually for **each** epsilon>0, on **all** good primes (or an independently
proved sufficiently dense subfamily). The selected embedding is exactly 1.
A polylogarithmic upper bound would suffice. A single polynomial saving from
the trivial pair count is progress but does not discharge this target.

The SCE conditional implication to base-16 and base-2 normality survives the
adversarial audit. Decimal and absolute normality are not covered. The novelty
tax remains: this prescribed-scale criterion is stronger than normality; the
normal de Bruijn-repeat counterexample remains intact. Positive Poisson regret
is an equivalence, and neither Galois mean nor short source description pays
the selected-source debt.

## 2. New actual-source restrictions, and what they do not estimate

The [arithmetic proof track](PI_LAG_ARITHMETIC_TRACK.md) proves the complete
carry-retaining lag recurrence and the exact pair decomposition

\[
Q=\Delta+2\sum_{\ell=1}^{\Delta-1}
\#\{0\le s<\Delta-\ell:|\delta_{u+1+s,\ell}|\le1/M\},
\]

where delta is the centered representative of y_(n+ell)-y_n. Its integer
carry includes **both** the difference of literal source carries and the
change of centering offsets. The authentic exact regression n=1174, ell=130,
tau=1/32 has centered carry zero but source carry difference 15: both
centering offsets are 1, and 15+1-16=0. Ignoring these terms changes the process.

The positive forcing difference f_(n,ell)=r(n+1)-r(n+ell+1) is completely
monotone in n and has explicit positive beta-integral bounds. Whenever
f<=15 tau and 17 tau+f<1, a k-transition consecutive-close run occurs **if
and only if** its initial centered difference lies in

\[
\left[\sum_{i<k}16^{-i-1}f_{n+i,\ell}-\tau16^{-k},
      \sum_{i<k}16^{-i-1}f_{n+i,\ell}+\tau16^{-k}\right].
\]

This exact rational interval has width 2 tau 16^-k and retains both endpoints.
For the canonical prime windows the gates hold throughout once M>=256:
f<15/((p+8)(p+9))<15/M and 17/M+f<32/M<=1/8.
They do **not** hold at M=16. The general lag/count identity remains valid there.

Runs beginning with a nonpositive centered difference satisfy an explicit
O(log p) escape bound from the forcing's lower beta estimate. Positive runs
can shadow the exact Green difference t_n-t_(n+ell); estimating how often
the actual rational lag enters those shrinking intervals remains unpaid.
Irrationality of pi rules out an infinite such run, but supplies no uniform
count at the required scale. We claim no saving for the total pair count.

The already-known local phase multiplicity yields the useful separation:
same-local-phase pairs contribute at most M/L<p^(-1/10)log p to K_p(1).
Nonresonant pairs have p-adic valuation -1, so cannot be exact repeats.
Neither fact bounds their **near**-collisions at radius 1/M. This is a
corollary of inherited SCE arithmetic, explicitly not claimed a new major bound.

## 3. Strongest scoped impossibility result

The [hostile proof](PI_LAG_ADVERSARIAL_REVIEW.md) gives an explicit rational
construction. On a late window A,...,B at resolution M, it changes only the
initial state to a nonzero dyadic delta with 0<delta<2*16^-A. It preserves:

- the exact four-pole forcing at every time;
- every odd-prime-power primary component at every time;
- any prescribed finite odd-modulus congruences of the **unwrapped lift
  difference**, with their correct pole domain;
- a literal initial carry prefix J, subject to the proved finite cylinder bound.

Yet **all** window pairs have distance <1/M, so the scaled collision is
exactly M. It coalesces with the authentic source at an explicitly bounded
finite time K. The constructive depth cost is
K-B=ceil(log_16(2MD)), where D is the chosen odd modulus.

The prefix can grow linearly: writing Lcm(N)=lcm(1,...,N), the elementary
central-binomial argument gives Lcm(N)<16^N. Actual source denominators
through J divide Lcm(8J), so the initial carry cylinder has radius greater
than 16^(-9J). Thus J=floor((A-1)/9) always fits the required prefix margin.
On target prime windows A=u+1, this preserves floor(u/9) exact early carries.

Consequently no p^epsilon bound with fixed epsilon<2/5 holds **uniformly over
this explicitly specified observation class** on all large good primes.
This strengthens the #259 controls by retaining literal early carries;
the original dyadic/odd-primary/coalescence mechanism is credited there.

It does not refute the bound at delta=0. It does not exhibit one nonnormal
counterfeit with the entire selected source contract: each fixed control
eventually has the authentic future. It proves failure of a uniform
finite-window inference from these partial source readouts. Exact initial
zero, or sufficient later carry information that distinguishes it, must do
additional mathematical work. No PA/ZFC independence mechanism is asserted.

## 4. Parallel entropy and multiple-prime verdict

The [entropy track](PI_COLLISION_ENTROPY_TRACK.md) authenticates the common
source-free window of several primes and proves its exact joint-clock fibers.
The joint period is the **lcm**, not the product, of the orders. When this
period exceeds the window length, the clock vector identifies the time
index, so the actual cell label has conditional entropy zero at every resolution.
The genuine BBP primes (73,97), on n=13,...,36, supply an exact example.

Within each clock fiber every relative conjugate acts by a constant
translation. All circular close-pair counts inside that fiber are exactly
invariant. Cell energies differ by at most factor 2; conditional entropies
by at most log 2, with all boundary carries retained. Cross-fiber pairs are
still the unknown quantity.

On the full target p-window, R=time mod L has entropy log L. Every M-cell
label X, including the actual source's, therefore obeys

\[
H(R\mid X)\ge\log L-\log M>
\tfrac1{10}\log p-\log\log p.
\]

This forbids closing SCE by a chain-rule estimate that pays the **entire**
conditional clock entropy as an o(log p) error. It is an impossibility for
that proof architecture, not for conditional entropy methods as a whole.
The exact difference of two clock mutual informations may cancel; it remains
unbounded here, just as the signed cross-clock Fourier term remains unbounded.
No second distinct homogeneous first-birth clock covers the whole primary
p-window: a multiple-prime proof must partition it or retain later impulses.

## 5. Certified actual-source computation at the predetermined scale

The [preregistration](PI_LAG_PREREGISTRATION.md) precedes measurements.
The complete [receipt](PI_LAG_INTERVAL_RECEIPT.json) contains all cell counts,
exact counts, source hashes, interval hashes and precision budgets.

| Prime p | L | Delta | M | Exact ordered close pairs | Exact K_p(1) |
|---|---:|---:|---:|---:|---:|
| 2081 | 260 | 780 | 16 | 76544 | 5888/2925 |
| 4129 | 172 | 1548 | 16 | 300672 | 3712/1849 |
| 1048601 | 131075 | 393225 | 256 | 1208458891 | 309365476096/154625900625 |

Each prime passes the stronger exact good-prime certificate L^2>p, p>e.
No pair or cell decision is ambiguous. The last ratio is approximately
2.00073516. This is a finite observation, not a fitted exponent or proof of
the subpower bound. The same-forcing control at p2081 has all 608400 pairs
close, compared with the actual 76544.

### Integer interval proof and independent instrument

Machin's classical identity pi=16 atan(1/5)-4 atan(1/239) is algebraically
verified by the tangent addition formula and the angles' principal ranges.
For atan(1/q), truncate the alternating series after
N=ceil(B/(2 floor(log2 q))) terms. Its error is strictly less than 2^-B.
The integer binary split on [a,b) returns

\[
P=q^{2(b-a)},\quad Q=\prod_{a\le k<b}(2k+1),\quad
T=\sum_{a\le k<b}(-1)^kq^{2(b-1-k)}Q/(2k+1).
\]

Combining left/right halves uses P=P1 P2, Q=Q1 Q2,
T=T1 Q2 P2+T2 Q1. For a=0 the truncated arctangent is Tq/(QP).
If F=floor(2^B Tq/(QP)), then (F-1,F+2) is an outward enclosure in units
2^-B. Signed Machin combination yields width 60 in those units.

For last state H and local interval precision s=80, use B=4(H-1)+s+8.
Outward shifting and reduction extract 16^(n-1)pi, with wrapping retained.
Subtract a 20-term positive Green tail sum. Each rational summand is rounded
down separately; the upper endpoint adds 20 rounding units plus the ceiling
of the residual bound 16^-20/((8(n+20)+1)(8(n+20)+2)). The selected-source
identity y_n+t_n=16^(n-1)pi modulo 1 then encloses **rational y_n**, not just
the unforced pi phase. Intervals crossing the circle boundary fail closed.

After sorting intervals, strict ordering is certified. Two monotone sweeps
count directed short arcs: the lower count uses upper(endpoint)-lower(start),
and the upper count uses lower(endpoint)-upper(start). They must agree.
For radius<1/2, ordered close pairs equal Delta plus twice the directed count.
Cell endpoints must likewise agree. All operations are integer operations;
floating values appear only as explicitly approximate report summaries.

The six instrument tests independently compare direct alternating Fractions,
the four-pole rational recurrence, exhaustive all-pair counts, exact threshold
and wrap cases, and intentionally underresolved failures. A separate adversarial
oracle tests additional endpoint assignments; its source and receipt are kept.
This is certified arithmetic under the stated paper identities and software
execution assumptions, not a Lean proof or an infinite empirical inference.

## 6. Failed approaches, authority and next verdict-changing target

Refuted with explicit controls: selected<=Galois average; p-free complement
implies alignment resistance; all odd clocks plus finite lift probes and a
linear early carry prefix determine later collision behavior; small forcing
makes a smooth modulo-one orbit; enough clock conditioning creates entropy.
The stronger normal de Bruijn-repeat countermodel and all inherited SCE
hostile controls remain tested and unaltered.

Proved in this round: the selected lag run criterion and directional escape;
the stronger uniform-observation no-go; exact multiple-clock conditioning
and its quantified chain-rule obstruction; the interval algorithm's error
bounds and the listed finite certificates. Classical components include
BBP, Machin, elementary entropy, primary decomposition and binomial valuations.
Agent reviews share model/source provenance; they are not independent external
referees. Distinct evaluation algorithms are identified in the receipts.
No source-specific signed Fourier sum is newly bounded in this round.

The smallest consequential next arithmetic result is a first exponent eta>0
and a constant C for which the actual nonresonant lag visits satisfy

\[
\sum_{\substack{1\le\ell<\Delta\\L\nmid\ell}}
V_\ell(u+1,\Delta;1/M)\le C\Delta^2p^{-\eta}
\]

on all sufficiently large good primes. This would be a genuine first saving
over the trivial count; reaching Delta^2/M times p^o(1) remains the ultimate
collision target. A claim about only long consecutive runs is insufficient.
The proof must use the actual rational starting lag and its later carry
history to exclude the positive tracking cylinders often enough. Alternatively,
a signed cross-clock estimate can bypass the stronger collision requirement.

Primary references checked, without importing their conjectures:
[BBP](https://www.davidhbailey.com/dhbpapers/digits.pdf),
[Bailey--Crandall](https://www.davidhbailey.com/dhbpapers/bcnormal.pdf), and
[Bailey--Misiurewicz](https://www.davidhbailey.com/dhbpapers/dhb-mm-hotspot.pdf).
The first identifies the actual source; rational-forcing Hypothesis A in the
second is not a theorem; hot-spot criteria in the third concern actual orbit
frequencies and cannot be filled by ensemble or finite sample estimates.
