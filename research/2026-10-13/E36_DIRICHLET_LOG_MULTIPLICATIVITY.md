# E36 — What the Dirichlet logarithm cancels and preserves

Independent first-generation expedition, 2026-10-13. Branch
`research/swm-e36-2026-10-13`; immutable SUCC parent
`5eb09e7cba36ec01b8f9d6834b78b5766fd93935`. No other expedition
conclusions or shared registry were consulted. Imported originals are unchanged.

## 1. Original question

Does moving a source into the Dirichlet-convolution logarithm remove
multiplicative interactions, or expose them? The faithful reading is a question
about an invertible formal coordinate, with source labels retained. Three rivals
must be separated: complete logarithm preserves the source; discarding mixed
coefficients preserves it; prime-power support identifies genuine arithmetic.
Only the first survives without additional qualifications. No physical carrier,
human computational capacity, or infinite completed observation is inferred.

## 2. Existing mathematical context

Dirichlet convolution, Bell factors, and formal logarithms are **CLASSICAL**.
[Hida, §1.14](https://www.math.ucla.edu/~hida/205a.1.19f/Lec1.pdf)
derives the formal prime-local product from coprime multiplicativity.
[Montgomery–Vaughan, §1.3, Theorems 1.8–1.9](https://personal.science.psu.edu/rcv4/personal/Publications/MNTI/05.0_pp_1_34_Dirichlet_series_I.pdf)
separates formal products from analytic rearrangements justified by absolute
convergence. These are primary author-hosted sources, browsed on this date.

Repository provenance is `provenance/IMPORT_MANIFEST.json`, originating at
FuckingRH `ba075348b7bcc66d938b3e0ca96c26e95bba340a`. Its exact Git
objects were inspected in `/home/leah/FuckingRH`: `actualization/dirichlet_lambert.py`
has blob `7f99150117c563c583be0fcc35fae1998a472162`; the frozen
`DIRICHLET_LAMBERT_SOURCE_LIFT.md` has `65f24f44369375b3cd88fc0743f60c1d5fb2a0d5`.
The originating commit object was absent in the SUCC clone (`cat-file`, exit 128),
then located and read in the original local checkout (exit 0).
The frozen `CERTIFIED_FINITE_PRIME_TRANSPORT.md` was also read. Their shared
lineage supplies context, not independent mathematical bearings.

## 3. Proposed SUCC objects

Let \(R\) be a commutative unital \(\mathbb Q\)-algebra; integral-domain
hypotheses are unnecessary. Set \(A=R^{\mathbb N_{>0}}\),

\[
(f*g)(n)=\sum_{d\mid n}f(d)g(n/d),\qquad I=\{h:h(1)=0\}.
\]

The unit is \(\delta_1\). A complete source prefix restricts to
\(A_N=R^{\{1,\ldots,N\}}\) with the same truncated product. Restriction is a
ring homomorphism. Logarithmic coordinates are

\[
b=\log_*a=\sum_{k\ge1}(-1)^{k+1}(a-\delta_1)^{*k}/k,
\quad a(1)=1.
\]

The mathematical completion \(A\cong\varprojlim_N A_N\) is coefficientwise;
it does not mean an observer has performed infinitely many causal events.
SUCC may retain the integrated source head alongside this coordinate; this probe
uses synthetic exact sources and does not exercise a physical observation journal.

## 4. Candidate theorem

**CLASSICAL; self-contained proof below.** For every such \(R\) and every normalized
\(a\in A\),

\[
a(mn)=a(m)a(n)\quad\forall\gcd(m,n)=1
\iff b(n)=0\quad\forall n\text{ having at least two distinct prime divisors}.
\]

Log and exp are inverse group isomorphisms \((\delta_1+I,*)\leftrightarrow(I,+)\).
For every \(N\ge2\), put \(L=\lfloor\log_2N\rfloor\). Then
\(I_N^{L+1}=0\), sharply when \(R\ne0\); log and exp terminate at \(L\).
The same equivalence holds for prefixes when all quantified products satisfy
\(mn\le N\). A finite successful prefix does not certify every future coefficient.

## 5. Proof attempt

Every nonzero \(k\)-fold augmentation product at \(n\) uses factors
\(n_i\ge2\). Hence \(k\le\Omega(n)\le\lfloor\log_2n\rfloor\).
This proves termination, nilpotence and restriction compatibility;
\(\delta_2^{*L}=\delta_{2^L}\ne0\) proves sharpness. Rational formal-series
identities therefore substitute legitimately, coefficient by coefficient,
giving log/exp inversion and \(\log_*(a*c)=\log_*a+\log_*c\).

For each prime let \(A_p=\delta_1+\sum_{r\ge1}a(p^r)\delta_{p^r}\).
Unique factorization makes \(a=\mathop{*}\limits_p A_p\) equivalent to
coprime multiplicativity. Each fixed coefficient of this infinite product
uses finitely many primes. Logging it yields \(b=\sum_p\log_*A_p\), supported
on prime powers. Conversely, prime-power support gives \(b=\sum_p b_p\);
exponentiation gives \(a=\mathop{*}\limits_p\exp_*b_p\), so multiplicativity
follows by unique factorization. This proves both directions, including over
rings with zero divisors. Globally all rational denominators must exist;
at horizon \(N\), invertibility of integers \(1,\ldots,L\) suffices.

## 6. Crucible

The exact path expansion retains every ordered factorization and its sign:

\[
b(6)=a(6)-a(2)a(3),\quad
b(12)=a(12)-a(2)a(6)-a(3)a(4)+a(2)^2a(3).
\]

| Hostile source or mutation | Exact receipt | Consequence |
|---|---|---|
| Zeta coefficients \(a(n)=1\) | \(b(6)=b(12)=0\) | Mixed paths cancel |
| Change only \(a(6)\) to 2 | \(b(6)=1\) | Mixed defect survives |
| Change \(a(6)=a(12)=2\) | \(b(6)=1,\ b(12)=0\) | One cancelled composite is insufficient |
| Fake composite primitive \(b=\delta_6\) | \(a=\exp_*b,\ a(2)=a(3)=0,\ a(6)=1\) | Fake place rejected |
| Average zeta with \((-1)^{v_2(n)+v_3(n)}\) | Same \(0,0,1\) at \(2,3,6\) | Two Euler sources can mix into non-Euler data |
| Consistent phase \((-1)^{v_2(n)}\) | \(b(2),b(4),b(8)=-1,1/2,-1/3\) | Support survives altered prime phases |
| Omit ordered path \((3,2)\) | \(b(6)=1/2,\ (\exp_*b)(6)=3/2\) | Broken cancellation fails reconstruction |

Within-prime interactions survive: \(b(p^2)=a(p^2)-a(p)^2/2\).
Complete multiplicativity specializes \(b(p^r)=a(p)^r/r\); ordinary
multiplicativity alone does not. Over \(\mathbb Z\), even
\(\log_*(\delta_1+\delta_2)(4)=-1/2\) exits the ring; characteristic zero
alone is insufficient. Positive characteristic does not support these unrestricted denominators.
Likewise, pointwise multiplication is not linearized: for
\(a=\delta_1+\delta_2\), \(a\cdot a=a\), but \(b(2)=1\ne2b(2)\).

## 7. Verdict

**SURVIVES / CLASSICAL:** complete log is reversible and characterizes
multiplicativity through mixed-support vanishing. **TESTED MODEL:** independent
ordered-path enumeration agrees with imported convolution operations through 64.
**REFUTED:** vanishing at one composite certifies multiplicativity; prime-power
support certifies the original prime phases; mixed projection preserves every source.
The table provides receipts. Mathematical acceptance remains with the independent
crucible and principal review; no ledger status is promoted here.

## 8. Remaining obstruction

Formal identities require no Dirichlet-series convergence. The multiplicative
source \(a(2^k)=k!\), zero at other prime powers, has no convergent analytic
half-plane: successive term magnitudes have ratio \((k+1)2^{-\sigma}\).
For complex sources an explicitly sufficient analytic bridge is
\(H_\sigma=\sum_{n\ge2}|a(n)|n^{-\sigma}<1\). The weighted convolution norm
bounds the log by \(\sum_{k\ge1}H_\sigma^k/k\), and the absolutely convergent
Dirichlet transform gives its Taylor logarithm for \(\Re s\ge\sigma\).
The finite Dirichlet polynomial is not a ring map on \(A_N\): in \(A_5\),
\(\delta_2*\delta_3=0\), while the evaluated factors multiply to \(6^{-s}\).
Truncated log coefficients must not be equated with the scalar logarithm of
a truncated source sum. Branches, continuation and
completed forms need additional work. No zeros are inputs; no RH conclusion
is licensed without conductor, half-density, phase, Gamma/poles and test domains.

## 9. Cross-domain connection with actual maps

The actual ring isomorphism into the monomial coefficient ring, completed by
integer-index restriction rather than an unspecified infinite-variable topology,
\(\Phi(f)=\sum_n f(n)\prod_pX_p^{v_p(n)}\) satisfies
\(\Phi(f*g)=\Phi(f)\Phi(g)\) by divisor enumeration. It transports log/exp
and every restriction. Let \(P\)
retain prime-power coefficients. Define \(E(a)=\exp_*P\log_*a\) and
\(c=(1-P)\log_*a\). Then

\[
a=E(a)*\exp_*c.
\]

The pair preserves source and mixed defects; \(E\) alone does not. A phase
transport \(T_\chi f(n)=\chi(n)f(n)\) with completely multiplicative unit-valued
\(\chi\) commutes with convolution and logarithm; an isolated phase change does
not. Complete two-factor measurements at coefficient 6 give interaction \(-1\) for
\(\delta_1+\delta_2+\delta_3\), but 0 for
\((\delta_1+\delta_2)*(\delta_1+\delta_3)\). This is exact non-additivity,
not a physical mechanism. κ is synthetic algebraic contact; φ is the stated
proof pathway; σ retains imported provenance; ρ risks conflating cancellation
with authenticity. No truth probability or quantum claim enters.

## 10. Deliverables

New native files: this dossier, [bounded probe](E36_dirichlet_log_probe.py),
and [exact receipt](E36_DIRICHLET_LOG_RECEIPT.json). Commands, both exit 0:

```sh
python research/2026-10-13/E36_dirichlet_log_probe.py --receipt research/2026-10-13/E36_DIRICHLET_LOG_RECEIPT.json
python scripts/verify_provenance.py
```

The receipt records hashes, path contributions, 16 source cases, 16 convolution
identities, 48 restriction checks, and every hostile control. Provenance verified
72 imports, including 17 unchanged archives. No full suite or compiler ran.
Next small lemma: prove and independently test the triangular first-defect identity
\(c(n_0)=a(n_0)-E(a)(n_0)\) when \(n_0\) is the least mixed defect, retaining
the source head and refusing missing coefficients.
