# Signed-cancellation barrier: one controlled seam and three stronger obstructions

**2026-10-27. Research child of PR #324 at
`fca58d3e0289e57596dd8ca74bace325a450df31`.** Original four signed BBP poles,
zero initial condition, production modules, historical files and main are
unchanged. **Base-16 normality of pi remains OPEN.** This round proves a new
selected digit-boundary bound and decisive obstructions to three proposed
ways of amplifying the existing results. It does not improve the selected
Weyl bound `N-(log_8 N)/14+O_h(1)`.

## 1. Live frontier and dependency cut

The source throughout is

$$
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},\qquad
U_0=0,\quad U_n=16U_{n-1}+r(n).
$$

The exact future tail is positive, summable, and satisfies

$$
U_n=16^{n-1}\pi-T_n,\qquad
B=\sum_{n\ge1}T_n=\frac{R-\pi}{15}.
$$

The target remains `sum_(n<=N)e(hU_n)=o(N)` for every fixed integer `h!=0`.
The shortest existing chain is: original source and zero seed -> exact Green
transport -> **missing signed cancellation** -> Weyl normality. Arithmetic
clock bijections solve the indexing, not that missing estimate.

Live GitHub heads inspected before research:

| PR | Head | Role |
|---|---|---|
| #315 | `c094b38d399c073f5c2f9d9fe7a1a3584f5cb724` | Sibling: inverse averaging and field feedback; read, not merged |
| #316 | `239df54f5f56fdaba3bf4edfc282cdcabecea3c2` | Local compatibility and changed-seed obstruction |
| #319 | `6a187a61b19e389ed61e336a5d1c208bd21d773a` | Uniform periodic/mixed-lag logarithmic loss |
| #320 | `5ea12570aec86c3a8b555e927c10337804568a62` | Exact 2-adic clock and nonnormal source mutant |
| #321 | `eeb2a48ea1b43967ea385009a3f8ec280b2efa69` | Infinite-past zero and all-time clock |
| #322 | `73a124637444c0e51cae1ace1e70d8c65dd28eb9` | Binary state / ternary numerator CRT clock |
| #323 | `ae5dad40bfcbcd7a50676ed61c297fdc46846f37` | Uniform Green lag transport |
| #324 | `fca58d3e0289e57596dd8ca74bace325a450df31` | Nonlinear saturation, energy gate, finite spectrum control |

Main was observed at `6dd80730c3575d91f746546a25da5aedbd2e2737`.
No inherited proof-status or source passport is changed.

The active obstruction is a **pathway gap**: no source-selected signed
arithmetic estimate. It is not an access failure or a demonstrated
impossibility of proving normality. The experiments below discriminate
specific proposed mechanisms rather than voting on whether pi is normal.

## 2. Genuine positive step: fifteen cuts are controlled

Write `y_n={16^(n-1)alpha}`, `x_n={16^(n-1)alpha-T_n}` and let `C_N^+`
count visits to the fifteen windows `[a/16,a/16+T_n)`, `1<=a<=15`.
The [single-wrap theorem](PI_SINGLE_WRAP_SEAM.md) proves, uniformly over
**every real carrier alpha**, including the selected pi carrier,

$$
C_N^+\le Q+\left\lceil\frac{N-Q}{L(Q)+1}\right\rceil,
\quad L(Q)=\max\{\ell\ge0:16^{\ell+1}\le15(Q+2)^2\},
$$

for every integer `0<=Q<N`. Choosing `Q=floor(sqrt(N))` gives
`C_N^+=O(N/log N)`. A visit forces a subsequent run below the first
nonzero cut; packing these runs proves the bound without any probabilistic
assumption.

For an arbitrary digit function f, the only possible positive-density
transport error is exactly its wrap jump `f(15)-f(0)` times visits to
`[0,T_n)`. Thus every discontinuous digit statistic satisfying
`f(15)=f(0)` transports with `o(N)` error. The theorem also treats moving
nonlinear lag tuples with total internal-jump budget `o(log N)`, independently
of the lag sizes. The target under normality is the deterministic radix lag
graph, never independent product Haar.

This is stronger than the smooth-only transport of #324. Its proof uses
the authentic source bounds but is valid for a wider tail class; it is not
claimed to exploit every special arithmetic feature of the four poles.

The residual is sharp: the inherited sparse carrier
`xi=sum_(j>=0)16^(-2^j)` has **`N-Theta(log^2 N)` zero-seam visits**
against the actual original BBP tail. It has a proved elementary finite-type
bound `|xi-p/q|>1/(32q^3)`; the stronger classical exponent-two fact is
credited separately. Its same-forcing seed is `(xi-pi)/16`, not zero.
Tail summability plus finite irrationality type therefore cannot close the
remaining cut.

## 3. CRT energy can demand more than normality

The [energy dossier](PI_CRT_ENERGY_REFINEMENT_OBSTRUCTION.md) proves that
the correctly weighted conditional energy increases under nested residue
refinement, by an exact sum of squared child-mean innovations. On complete
periods this is exactly the proposed energy E. More arithmetic labels retain
more conditional bias; they do not automatically cancel it.

For the authentic source, the full moving energy itself transports:

$$
|E_U(N,M,h)-E_\pi(N,M,h)|
\le\frac{4\pi|h|B}{N}\left(1+\frac MN\right).
$$

An explicit concatenation of increasingly long repeated de Bruijn periods
is **normal to base 16 at all prefixes**, yet for a specified monotone
`M(N)=3*16^k=o(N)`, its residue energy has `limsup E=1` for every fixed h. More strongly, for
**every** prescribed schedule `M(N)->infinity`, `M(N)=o(N)`, a normal
carrier can be constructed with this maximal limsup (Theorem E5).
The maximal-energy constructions E4/E5 are **Liouville**. The strongest
new [finite-type theorem E7](PI_NORMAL_FINITE_TYPE_ENERGY_OBSTRUCTION.md)
removes that limitation: for every such prescribed schedule, one normal
carrier alpha satisfies

$$\mu(\alpha)\le4,\qquad
\liminf_{j\to\infty}E_\alpha(2^j,M(2^j),h)\ge\frac14$$

for every fixed h. Here the exponent statement means that, for each
`tau>4`, all sufficiently large q have `|alpha-p/q|>=q^(-tau)` for every p;
a uniform bound `Cq^(-4)` is not asserted. Exact finite root-of-unity second
moments select periodic words whose correlations with the old prefix are
small. Explicit digit markers simultaneously control rational approximation.
All-prefix normality, every phase error, and both determinant branches are
proved. The auxiliary word distribution is a construction device, not a
stochastic model for pi.

The simpler E6 construction is retained with its explicit eventual
`|alpha-p/q|>=2^(-10)q^(-6)` bound and energy lower limit 1/4 at N=4^j.
Thus normality **plus finite irrationality type** cannot justify an arbitrary
prescribed moving-energy gate. Each theorem's properties belong to one
carrier. Both obstructions survive the original BBP tail with a changed seed.

Quantifiers matter: fixed-M energy decay for all nonzero modes, or existence of some
sufficiently slow growing schedule, is equivalent to normality. A prescribed
growing schedule can impose strictly more uniformity. The new normal
counterexample proves this strict distinction; it does not refute the
sufficiency of E tending to zero for pi.

## 4. Growing differencing and mixing do not repair the other gates

The [moving-lag obstruction](PI_MOVING_LAG_SPARSE_OBSTRUCTION.md) proves
that one fixed same-forcing sparse selector satisfies

$$
\sup_{\substack{1\le |h|\le H_N\\\sum_i\ell_i\le d_N}}
\left|\frac1N\sum_{n=1}^N
 e\!\left(h\prod_i(E^{\ell_i}-1)V_n\right)-1\right|\longrightarrow0
$$

for **every** `d_N=o(N)` and `H_N=o(N^2)`, including growing difference
order. Its full Green debt is bounded independently of order; a sparse
neighborhood union bound tracks the coefficient norm and lag span.
At fixed h the existing finite-irrationality/logarithmic-coercivity mechanism
also applies to this control. Van der Corput is asymptotically saturated:
repeating the old deficits cannot manufacture the missing decorrelation.

The [finite-spectrum dossier](PI_MIXING_FINITE_SPECTRUM_OBSTRUCTION.md)
strengthens #324's finite-grid control to a full-support, strongly mixing,
singular invariant law. Every prescribed finite nonzero Fourier band
vanishes, but a higher mode remains nonzero. A Frostman estimate also gives
a common full-measure set of generic carriers of finite irrationality type. Thus adding mixing, density,
or finite irrationality type to a finite-band bootstrap is still insufficient.
These are changed carriers, never counterexamples to the original zero seed.

## 5. Attempts, discriminators and verdicts

| Attempt / falsifiable claim | Controls and predicted distinction | Verdict |
|---|---|---|
| Refining exact CRT labels decreases signed energy | Alternating unit signs have coarse energy 0, refined energy 1 | REFUTED as a source-free mechanism |
| Normality plus finite irrationality type forces E to vanish along any prescribed growing clock | One normal carrier has irrationality exponent <=4 and liminf endpoint energy >=1/4 | REFUTED by E7; extra uniformity identified |
| All discontinuous digit observers evade Green saturation | Functions identifying 15 and 0 have uniformly sparse remaining errors | REFUTED; exact wrap residual retained |
| Finite irrationality type forces rare zero-seam crossings | Sparse finite-type carrier has near-maximal crossings | REFUTED without zero selection |
| Existing mixed-lag losses amplify to relative cancellation | Same-forcing finite-type control stays coherent at all sublinear spans | REFUTED with stated input package |
| Finitely many nonzero modes vanishing plus mixing selects Haar | Explicit mixing singular q-lift law | REFUTED; higher spectrum matters |
| The authentic zero-selected real-phase sums satisfy o(N) | All countermodels must be excluded by new arithmetic | OPEN |

Negative results preserve the precise failed hypothesis. None says that CRT,
carry arithmetic, nonlinear statistics, or van der Corput cannot contribute
to a future source-specific proof.

## 6. Next verdict-changing proof obligation

For the boundary front, prove the genuinely weaker statement

$$
\#\{1\le n\le N:\{16^{n-1}\pi\}<T_n\}=o(N).
$$

It would extend transport to every bounded one-digit statistic. It would
**not** prove those digit frequencies uniform. Its novelty tax is paid by
being a shrinking-window problem, not Weyl normality in different notation;
for example rational carrier `alpha=1/3` has no such visits but is nonnormal.

For the signed-cancellation front, select and justify an arithmetic lemma
controlling authentic progression correlations, retaining zero selection,
the full rational states and integer branches. The exact identity is

$$
E_U=\frac MN+
\frac{2M}{N^2}\Re\sum_{j=1}^{\lfloor(N-1)/M\rfloor}
\sum_{n=1}^{N-jM}e(h(U_{n+jM}-U_n)).
$$

Any successful estimate must control the **signed** second term, with its
moving completed frequencies `h(16^(jM)-1)`, rather than substitute a
fixed-frequency theorem or add correlated logarithmic losses. The #320
mutant must fail the proposed arithmetic premise; the normal finite-type
carrier in E7 shows why the chosen moving rate cannot be silently assumed.

Bailey--Crandall Hypothesis A is still a conjectural dichotomy. Its single
authentic pi instance, after irrationality excludes the finite alternative,
is equivalent to the target. Lagarias's general Green shadowing theorem
explains why transport alone cannot discharge it. Primary-source details,
reproduction and boundaries are in the linked dossiers and
[validation record](PI_SIGNED_CANCELLATION_VALIDATION.md).

All proof audits here use the same model family. Different derivations,
exact controls, certified arithmetic and mutations offer distinct failure
modes; agent agreement is not counted as independent external evidence.
