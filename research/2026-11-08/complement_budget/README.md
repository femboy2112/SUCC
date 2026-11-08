# Original folded complement: source-law restrictions and certified budget floors

**The approximation premise is now tested directly.** We prove restrictions
on models of the authentic folded complement and certify substantial finite
cost floors for a complete, specified phase menu. We do **not** obtain the
needed approximation upper bound or original-zero resonance decay.
Pi base-16 normality and RH remain **OPEN**.

This is the current handoff for this round. It continues
[`signal_frontier`](../signal_frontier/README.md) at pinned research head
`95d9860de3a52ab76c1a0719e170b609759b17b9`; the original proof baseline remains
`d32342d375f44ddf62221ad6aff2f534abdc0a03`. Fetched main is
`43a607818907120d4cdab73d240f5b4d7700b63f`. New work is confined to this folder.
The newer Fibonacci-triangle, four-pole-nine and Cayley/xi branch proofs were
read at exact pins; their contribution and limits are in
[the repository review](hostile/REVIEW.md). They supply no missing complement
decay estimate. No source contract, shared roadmap or catalog was changed.
The final fetch also found a new three-channel Poisson/Gram branch; its
[separate audit](hostile/LATEST_UPDATE_REVIEW.md) confirms that its unnormalized
matrix decays even for coherent controls. Its normalization warning is
load-bearing. The new theta-gamma branch still equals main at this fetch.

## The strongest new structural theorem

The actual folded conditional law is

    nu_r = (1/q) sum_j delta_(e(U_(n0+r+jm)-[U_(n0+r+jm)]_p)).

It obeys approximate x->16x / z->z^16 transport with an explicit forcing
cost O(L^-2) and one wrap-boundary cost2/L. Its first moment does not close:
the next first moment involves the present sixteenth moment. Replica variance
is the exact cost of replacing the law by its mean.

For a positive model with K polynomial phase branches, KD<m, branch weights
at least w_min>0, and at least one genuinely nonlinear branch,
[CBM5](model/THEOREMS.md) proves a quantitative lower bound on the model's
average chord-Wasserstein error. For fixed K and
D sqrt(p) log(p)/m->0 it gives

\[
\liminf e_{\rm law}\ \ge\ \frac{w_{\min}}{17K}.
\]

Arbitrary fixed phase anchors are permitted. Equal weights give1/(17K²).
The exact-transport version forces all branches to be homogeneous linear,
with constant weights. These proofs use polynomial root counting, the
classical Weil estimate, finite arc Fourier inversion and an explicit
layer-cake bound. [Independent review](hostile/MODEL5_REVIEW.md) checks each step.

**This is a full-law theorem, not an exclusion of arbitrary complex mixtures
approximating only B's first moment.** The inverse affine branch survives.

For a single unit-valued nonlinear chirp, [CR2](resonance/THEOREMS.md) instead
does control PR8's first-moment L1 error: its lower limit is at least1/289
when d sqrt(p)/m->0. Accurate affine unit chirps must approach a fifteenth-root
phase anchor; the resonant slope -h remains allowed. These restrictions also
hold for appropriate same-forcing controls. They do not identify literal zero.

## A direct original-source budget test

Let r=conjugate(a), W=<r,B>, E=mean|B|², and let phi_j be a declared
nonresonant atom menu with valid arithmetic costs
w_j=min(1,D_j sqrt(p)/m). Put M=max_j |<phi_j,B>|/w_j.
[CB1](THEOREMS.md) proves that **every** model

    V = R*r + sum_j c_j phi_j,     R arbitrary complex,

has

\[
\rho+\sum_j w_j|c_j|
\ \ge\ \frac{E-|W|^2}{\max(1,M)+|W|},
\qquad \rho=\mathbb E|B-V|.
\]

The dual witness B-Wr annihilates the free resonance exactly. This is a
lower bound on a sufficient method's cost; it is not a lower bound on W.

The preregistered menu includes **every** coefficient t for
e(t*x^d/p), d=1,2,3, retaining the inverse linear phase separately.
These are monomial chirps, not the entire class of mixed quadratic/cubic
polynomials. An integer-radius Bluestein FFT certifies all correlations,
with no floating FFT error assumption. Outward rational final arithmetic gives:

| Selector A | Prime p | Actual source interval | h | Magnitude upper, rounded up | rho + nonresonant cost, rounded down |
|---:|---:|---|---:|---:|---:|
|1103|4409|1103–2204|1|0.028397|0.484818|
|1103|4409|1103–2204|3|0.050799|0.463237|
|2203|8753|2189–4376|1|0.031168|0.493188|
|2203|8753|2189–4376|3|0.020826|0.482654|
|5501|21977|5495–10988|1|0.013929|0.492667|
|5501|21977|5495–10988|3|0.001936|0.498022|
|**22003 holdout**|**88001**|**22001–44000**|**1**|**0.008694**|**0.493903**|
|**22003 holdout**|**88001**|**22001–44000**|**3**|**0.004183**|**0.497946**|

The same floor applies to the nested menus of maximum degree1,2 and3 in
these runs. Every reported model is allowed an unlimited resonant coefficient.
All eight results are **finite**, not a statement that these floors persist
as A->infinity. The held-out interval is beyond the prior dossier's last
source time20017. Development windows overlap prior data.

Raw source boxes and spectrum/certificate receipts are under [results](results/).
Across the eight configurations,738,840 Fourier coefficients were evaluated;
duplicate and resonant atoms are omitted from the cost maximization as declared.
The final FFT error radii are below8e-12 after normalization. The source stays
exact; interval width is instrument uncertainty, not a source perturbation.

The first slow holdout attempt was stopped before emitting any phase result.
An equivalent literal-carry implementation removed the bottleneck and rebuilt
all development payloads identically; see [STREAM_REVIEW](STREAM_REVIEW.md).

## The most important failed shortcut

[HCB3](hostile/THEOREMS.md) constructs, for any B on the proper source coset,
an exact linear-phase fit with zero *named* resonance. Applied to B=conjugate(a),
it has rho=Rsig=0 while W=1. Its coefficient budget necessarily stays at least
one. A retained coefficient belongs to a specified representation; it cannot
be interpreted independently of that representation's error and cost.

A second source-forcing theorem gives a two-replica zero-model error floor
1/17 minus explicit boundary/forcing terms. Every split prime clock has an
even replica count; the selector does not prove that count grows. Infinitely
many selected q=2 clocks are not established. These results prevent a
law-of-large-numbers argument from being silently applied to a small fold.

## The proof chain, with the gap kept in place

1. **Original zero arithmetic -> authenticated prime/complement factorization:**
   PROVED, PE1–9 and PR1. Unwrapped states, literal carries and actual principal
   parts are retained. The clean clock ends before the next p-pole.
2. **Conditional history -> coherent signed statistic:** PROVED,
   W_I=mean a_r B_r, with exact folding and the declared common phase frame.
   The learning observer can retain the entire conditional law; CBM1–2 now
   quantify its source transport and the information lost by mean-only closure.
3. **Original folded complement -> a useful all-epoch approximation/resonance
   estimate:** **OPEN**. This round excludes certain compact models and gives
   finite cost floors; it supplies no vanishing upper bound.
4. **A valid PR8 certificate -> original-zero signed covariance decay:**
   CONDITIONAL. The required bound still charges rho, signed resonance and
   weighted nonresonant complexity separately. Alternatively a direct
   covariance estimate can bypass this stronger approximation premise.
5. **Original-zero signed covariance decay -> all-epoch Weyl decay:** PROVED
   conditionally on that decay, since
   |W_J-Cov_I(a,b)|<=eps_A+sqrt(p)/m and both displayed errors tend to zero.
   All sufficiently large epochs, and every fixed nonzero integer h, are
   required. Local good subsequences do not suffice.
6. **Weyl decay -> normality:** the existing dyadic-to-prefix and original
   Green-tail transport to {16^(n-1)pi}, followed by Weyl's criterion, are
   PROVED implications. Their input remains OPEN.

The coherent same-forcing inverse phase falsifies any attempt to remove
source selection from step3. HCB3 falsifies omitting the arithmetic cost.
The two-atom moment countermodel falsifies replacing full-law transport by
first-moment closure. Ordinary geometry and gamma calibration do not eliminate
these surviving mechanisms.

## Reproducibility and the next discriminating task

See [VALIDATION](VALIDATION.md), [PROVENANCE](PROVENANCE.json),
[claim/failure ledger](CLAIM_LEDGER.md), [root audit](resonance/ROOT_REVIEW.md),
[hostile review](hostile/REVIEW.md), and [artifact manifest](ARTIFACT_MANIFEST.json).
Independent methods include reduced-Fraction source reconstruction, direct
interval sums, exact cyclotomic counts, finite transport enumeration and a
separate interval-arithmetic implementation for the holdout maxima. Agents
share a model family and repository; this is not external scholarly refereeing.
The new analytic results have paper proofs, not new Lean kernel certification.

The next single discriminating experiment is to enlarge the complete finite
menu to a preregistered mixed-quadratic family and recompute the same **dual
cost**, without fitting only W. If the floor survives, stop demanding global
L1 reconstruction from that family and aim directly at an original-zero signed
residual estimate. A successful upper certificate would still need an
all-epoch arithmetic proof and control of the retained resonance.

**Pi base-16 normality: OPEN. RH: OPEN.**
