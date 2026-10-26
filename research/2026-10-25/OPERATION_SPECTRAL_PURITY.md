# Operation Spectral Purity: removing conductor births and testing source selection

**Result:** no proof of base-16 normality of pi was obtained. This round proves
an arithmetic removal theorem for the original source, a stronger spectral
Green transfer, and a simultaneous prefix/jet/positivity countermodel. It also
kernel-checks the finite sequential and exceptional-step core. The remaining
signed estimate is stated below on a strictly smaller, independently defined
set of source steps. No academic priority claim is made.

**Provenance:** isolated branch `research/spectral-purity-2026-10-25`, based on
the live PR [#296](https://github.com/femboy2112/SUCC/pull/296) head
`461942c0bf616518e668d236d1c6b1596665a7dd`. The parent remains a draft, based
on [#293](https://github.com/femboy2112/SUCC/pull/293). Main and imported
source artifacts are unchanged. The baseline receipt records live heads,
discussion, and adjacent [#294](https://github.com/femboy2112/SUCC/pull/294)
and [#295](https://github.com/femboy2112/SUCC/pull/295).

## 1. One source, explicit domains

For integers $n\ge1$, retain exactly

$$
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},
\qquad U_0=0,\qquad U_n=16U_{n-1}+r(n).
$$

All finite states are unwrapped rationals. Their real-circle characters are
$e(x)=\exp(2\pi i x)$. The source's monotone common conductor is

$$
Q_n=\operatorname{lcm}_{1\le j\le n}\operatorname{den}(r(j))
=\operatorname{lcm}_{0\le j\le n}\operatorname{den}(U_j).
$$

It must not be replaced by the last state's reduced denominator. The matrix
is $G_{N,H}=\sum_{n=1}^Nv_nv_n^*$, $A=G/N$, with
$v_n=(e(kU_n))_{0\le k<H}$, and $D_{N,H}=\operatorname{tr}(A^2)-H$.
Throughout one horizon $N$, every innovation uses the **same** width $H$.

Formal identities live in $\mathbb Q[\mathbb Q/\mathbb Z]$. Cyclotomic traces
hold after root-of-unity evaluation. Real inequalities are established by
paper proofs or outward rational intervals, never by ordering formal symbols.

## 2. The arithmetic saving actually proved

Let $\mathcal C_N=\{1\le n\le N:Q_n>Q_{n-1}\}$ and select, before any data,

$$
H_N=\max\left(2,1+\left\lfloor\sqrt{\lfloor\log_2N\rfloor}\right\rfloor\right).
$$

Each conductor-growth time introduces a previously unseen odd prime-power
layer $p^a\le8N$. Distinct times receive distinct layers. Elementary
Chebyshev counting therefore proves $|\mathcal C_N|=O(N/\log N)$.
Since $0\le q_{m,H}\le H^2$ and $H\ge2$,

$$
\boxed{
\left|\frac{2}{N^2H_N}
\sum_{\substack{1\le m<N\\Q_{m+1}>Q_m}}m(q_{m,H_N}-H_N)\right|
\le\frac{2(H_N-1)|\mathcal C_N|}{N}\longrightarrow0.}
$$

This is an unconditional source-specific bound on a defined part of the
actual innovation sum. It uses no Galois averaging, independence, or Weyl
cancellation. The arithmetic dossier supplies a log-free rational bound
valid at finite $N$, and an exact executable source-conductor certificate.

Consequently define only the remaining, conductor-flat signed sum

$$
J_N^{\rm flat}=\frac{2}{N^2H_N}
\sum_{\substack{1\le m<N\\Q_{m+1}=Q_m}}m(q_{m,H_N}-H_N).
$$

The exact sequential identity gives

$$
\boxed{\frac{D_{N,H_N}}{H_N}=J_N^{\rm flat}+o(1).}
$$

The error has an explicit source-independent kernel bound and an authentic
prime-power count. Thus the next precise sufficient statement is
$\limsup_{N\to\infty}J_N^{\rm flat}\le0$. Nonnegativity of $D$ then forces
$J_N^{\rm flat}\to0$ and spectral purity. **That statement is OPEN.**
The flat steps have weight asymptotic to $N^2/2$, so this is a real removal
of one arithmetic class, not a claim that most of the statistical problem
has disappeared. A prescribed-width purity condition can be stronger than
qualitative equidistribution; no converse at this particular rate is asserted.

For $t=\lfloor\log_2N\rfloor\ge64$, the known removal error is at most
$130/\sqrt t$. Thus $N\ge2^{\lceil\max(64,(130/\varepsilon)^2)\rceil}$
is an explicit sufficient cutoff for that error to be at most any given
$\varepsilon>0$. It supplies no estimate on the remaining signed sum.

Full proof: [arithmetic dossier](SPECTRAL_PURITY_ARITHMETIC.md), AR-3--AR-5.

## 3. A sharper source transfer, and the equivalence check

The original Green tail satisfies $0<T_n<1/(64n^2)$ and
$U_n+T_n=16^{n-1}\pi$. Saturating the character error before summing gives

$$
\left|\frac1N\sum_{n\le N}[e(hU_n)-e(h(U_n+T_n))]\right|
\le\frac{\sqrt{7|h|/8}}N.
$$

Indeed $|e(hT_n)-1|\le\min(2,7|h|/(64n^2))$, and the decreasing summand's
sum is at most its integral on $(0,\infty)$, equal to $\sqrt{7|h|/8}$.
Weighted Euclidean reverse triangle in the Fourier energy identity yields

$$
\boxed{
\left|\sqrt{D^U_{N,H}/H}-\sqrt{D^\pi_{N,H}/H}\right|
\le\frac1N\sqrt{\frac{7(H^2-1)}{24}}.}
$$

Every prescribed sublinear width $H=o(N)$ therefore transports spectral
purity in both directions. This is a source-derived approximation estimate;
neither energy is thereby shown to be small.

The [innovation dossier](SPECTRAL_PURITY_INNOVATION.md) also gives the
required explicit diagonal proof: equidistribution is equivalent to purity
along **some** arbitrarily slowly growing window, even with an imposed
divergent sublinear upper envelope. Thus the unrestricted window criterion
is not an independent arithmetic saving. The same dossier proves the exact
signed sequential identity and the conditional good/exceptional inequality.

## 4. Two routes that failed, with receipts

**New prime channels.** The relative cyclotomic trace of an arriving matrix,
fixing the complete past and the other prime channels, is exactly $I_H$ at
a higher $p$ layer when $H\le p$. At a first $p$ layer it is
$(pI_H-ww^*)/(p-1)$, retaining the complementary source phase in $w$.
These are exact matrix restrictions on conjugates. They do not bound the
selected embedding: on the actual BBP source, $n=2,H=p=3$ has traced
innovation $3$ and selected innovation $>5$. A separate $n=14,p=109,H=4$
holdout also violates the tempting selected upper bound. Both are certified
by rational Machin/Taylor intervals. Above the $H\le p$ boundary, frequency
aliases survive explicitly. Moreover, declaring only conductor births good
leaves exceptional weight $\sim N^2/2$ and fails Target B.

**Finite source jets plus positive carriers.** For every fixed finite prefix
$M$ and finite jet order $K$, the [multiscale dossier](SPECTRAL_PURITY_MULTISCALE.md)
constructs a different, positive rational forcing with $U_0^*=0$, odd
denominators at every integer time, exactly the original first $M$ source
steps, strict Hausdorff/Pascal signs of every order, and the prescribed BBP
endpoint jets. Its rational selected seed is periodic under multiplication
by 16, so it is nonnormal. Quantified finite-difference bounds preserve all
fixed derivative critical-band limits. Thus these observations, even
together, cannot establish a universal high-to-low cancellation theorem.
The changed source fails the **exact global four-pole identity**; the
authentic source remains unique. No one counterfeit matches all exact
moments or the entire endpoint jet. Limits in prefix, jet order, and source
time are not interchanged.

The earlier Source Genesis dossiers already refute finite tail jets alone
and certain non-coboundary variants. The strengthening here is simultaneous
exact arbitrary finite source-prefix matching, arbitrary jets, positivity,
and global odd denominators, with a constructive exact certificate.

**Zero relations and positive carriers.** The forward recurrence, backward
Green equation, Gram update and Pascal differences give compatible exact
zero relations. Their algebraic compatibility is also satisfied by the
changed sources, with their own explicitly labelled forcing. The new
relative matrix trace is an additional arithmetic relation, but the
selected-embedding counterexample prevents promoting it to the needed
inequality. Likewise, positive Gamma comparisons and all-size moment Hankel
positivity do not constrain the missing signed temporal average. The
Walsh control retains the top interaction explicitly. No commuting diagram,
scalar positivity statement, or incomplete prime marginal is used as an
unproved source-selection theorem.

## 5. Mandatory hostile controls and the failed assumption

| Control | What it defeats / exact assumption that fails |
|---|---|
| Zero forcing, fixed zero orbit | $q=H^2$ and $D/H=H-1$; symmetry and Gram positivity do not imply innovation saving. The authentic forcing is absent. |
| Rational periodic seed | At a denominator multiple the Fourier mean is 1; the required signed estimate fails. |
| Sparse transcendental seed $\sum_{k\ge1}16^{-k!}$ | Liouville approximation gives transcendence; nonzero digits have density zero, so the orbit has empirical limit $\delta_0$. Irrationality is insufficient; the selected BBP seed is absent. |
| Simultaneously matched positive mutant | Matches any chosen finite prefix and jet, all Hausdorff signs, odd denominators, and moving critical limits; exact global BBP poles/residues fail. |
| Even-parity four-bit histogram | Walsh masks 1--14 vanish, mask 15 equals 1. Full interaction control is missing. |
| Haar averaging of starting points | Spatial squared Weyl sum integrates to $N$ even for the selected fixed zero orbit with squared sum $N^2$. Selected-point comparison is missing. |
| Re-gauged unimodular shift | Bare spectra erase source phase labels; the selected source matrix elements are missing. Unit-norm outgoing boundary is retained. |
| Authentic new-layer trace | Actual $q_{1,3}>5$ versus trace 3. Pointwise domination by relative algebraic averaging is false. |
| Same entire conductor tower | $U_n^*=16^n-1/Q_n$ has exactly the authentic common conductors and positive forcing, but every fixed character tends to 1. The four-pole law and carry history fail. |

The sparse-digit assertion follows by excluding the at most $L$ positions
before each nonzero digit: their density tends to zero for every fixed $L$.
All remaining shifted values are at most $16^{-L}/(1-1/16)$, and then
$L\to\infty$. This argument supplies the occupation claim, independently
of the Liouville transcendence argument.

## 6. Proof authority and operational boundaries

The [claim supplement](../../docs/CLAIM_SUPPLEMENT_SPECTRAL_PURITY.md)
separates CLASSICAL, PAPER-PROVED, EXACT FINITE, LEAN KERNEL, CONDITIONAL,
REFUTED, and OPEN. The Lean file formalizes finite symmetric-kernel
accumulation, sequential normalization, and the conditional exceptional
bound over the reals. The complex Fourier representation, Green analytic
estimate, arithmetic density proof, countermodel existence theorem, and
infinite normality implication remain paper proofs, not Lean declarations.

The workers used different derivations and instruments but share one model
family and repository lineage. This is not independent external refereeing.
Contact is the exact four-pole source (kappa); algebraic and interval checks
are the survival tests (phi); mutant/source and trace/embedding distinctions
are the source-map checks (sigma); commitment to the desired normality
conclusion supplies no evidence (rho). There is no physical quantum claim.

The reproducible [validation receipt](SPECTRAL_PURITY_VALIDATION.md) records
commands, versions, failures, hashes, finite holdouts, and exact commits.
The [handoff](SPECTRAL_PURITY_HANDOFF.md) preserves the remaining flat-step
obligation. Neither a finite matrix identity nor this new partial arithmetic
removal is a proof of pi normality.
