# Cambrian E: arithmetic transport and its source-identification boundary

Date: 2026-10-13 UTC. Executor: one research worker, `/root/arithmetic`,
executing assignments 25–30 sequentially in the isolated worktree
`e_arithmetic`. These are six actual investigations, not six claimed
independent agents. Base: `5eb09e7cba36ec01b8f9d6834b78b5766fd93935`.
Branch: `research/cambrian-e_arithmetic-2026-10-13`.

The main result is a **bounded source-identification theorem**: four rational
queries to the causal prime-side ramp recover each finite Dirichlet-log
coefficient through certified intervals. Formal convolution inversion then
recovers the original normalized arithmetic prefix. The method distinguishes
fake-six, nonunit Euler weights, altered event phase, and wrong half-density.
It uses no nontrivial zero locations. This is an elementary proved
instrument, new to this project; mathematical priority is not claimed.

The complementary obstruction is sharp: compatible finite p-adic clock
weights need not define a bounded Q_p-valued measure, and an entire family
of normalized positive Fourier-self-dual real tests produces additional
off-line strip zeros while keeping the genuine finite Euler source. Neither
finite clock coherence nor self-dual completion supplies Weil positivity.

## Baseline, provenance, and hole contract

Before construction, the worker froze these hypotheses independently of
other workers: affine SUCC/FUCC covariance should survive but not authenticate
weights; p-adic extension needs compatibility and continuity; continuous
additive Z_p-to-R transport is trivial; Gaussian sieve coverage does not
certify prime connectivity; compact-log prime transport can be exact while
completion ambiguity survives; and finite prime-side Weil data should admit
source-sensitive inversion without global positivity.

Read: `AGENTS.md`, `docs/METHOD.md`, `docs/RH_HANDOFF.md`,
`provenance/IMPORT_MANIFEST.json`, the immutable source dossiers for the
finite prime certificates, and current Mahler, diagonal-adele, and Gaussian
research. The imported source commit is
`ba075348b7bcc66d938b3e0ca96c26e95bba340a` in `femboy2112/FuckingRH`.
No imported module, archival original, shared ledger, README, CI file,
architecture, or roadmap was modified. All changes are additive and
namespaced `cambrian_e_*`.

**Exact target.** Identify a normalized finite arithmetic source from a
bounded Archimedean causal observable, preserving its genuine index,
Dirichlet-log coefficient, log phase, and half-density. This is strictly
weaker than constructing a completed Weil-positive form.

**Weakest sufficient form.** Recover each coefficient b(n) from four
queries to a sound ramp oracle, with an explicit stability bound. The
missing edge closed is `finite connected source -> causal response ->
identifiable source prefix`. The oracle's physical authenticity remains
an independent assumption.

**Cheapest falsifiers.** Fake composite impulse at 6, multiplicative
nonunit Euler coefficient at 2, moved log(2) phase, wrong half-density,
large measurement errors, and ending the observation exactly at the last
event. All have explicit receipts or a proof below.

**Truth boundary.** Paper proofs below are PROVED LOCAL / DISCLOSED under
their displayed mathematical assumptions. Executable Fraction interval
tests are finite verified instances. No Lean kernel check, RH proof,
physical source authentication, new Gaussian all-step theorem, or
universal completed positivity is claimed.

## E25 — Arithmetic SUCC/FUCC algebra

**Typed question.** On the algebraic finite-support span of the basis
`e_n`, n>=0, define S e_n=e_(n+1) and V_m e_n=e_(mn), m>=1.
Which covariance survives prime valuation and finite residue observation?

**Positive hypothesis:** exact affine covariance and authentic prime
valuation shifts. **Rival:** the same identities survive arbitrary
dilations, so they do not select Euler weights or the von Mangoldt source.
Both are true within their distinct domains.

**E25.1 (CLASSICAL / PROVED LOCAL).** For every m>=1,

\[
V_m S=S^m V_m,\qquad V_mV_l=V_{ml}.
\]

Both sides send e_n to e_(mn+m), respectively e_(mln). For m>1,
S V_m and V_m S disagree on every basis vector: their target indices are
mn+1 and mn+m. For genuine prime p and n>=1, unique factorization gives
nu(pn)=nu(n)+e_p. The successor nu(n+1) need not be an independent shift
in prime coordinates. No Hecke algebra identity is inferred.

**Finite clock obstruction.** Multiplication by p on Z/p^r Z has image
p Z/p^r Z and exactly p elements in each nonempty fiber. It is not
invertible on that clock. Proof: pn=pa mod p^r iff n=a mod p^(r-1).
The fresh receipt uses p=3,r=3: image size 9, each fiber size 3. The
unrestricted dilation on integer basis vectors is injective; the residue
quotient loses one digit. These are different representations.

**Weight countermodel.** Set a(n)=2^(v_2(n)). It is completely
multiplicative. Its Euler factor at 2 is (1-2*2^-s)^-1 in its convergence
region, and its Dirichlet log has b(2^k)=2^k/k while the other prime towers
retain b(p^k)=1/k. This preserves the carrier covariance and prime-power
support while violating the genuine zeta weights. Tests recover b(2)=2,
b(4)=2,b(8)=8/3. Composite-supported anomalies are empty; weight anomalies
are present. **Verdict:** exact algebra survives; algebra implies genuine
zeta source is REFUTED. Next lamp: a source law deriving the weights,
not another covariance diagram.

## E26 — p-adic clocks and bounded completion

**Typed question.** Given projectively compatible rational cylinder
weights mu_r(a) on Z/p^r Z, do they define a bounded functional on
C(Z_p,Q_p) with supremum p-adic norm?

**Positive hypothesis:** compatibility plus uniform p-adic boundedness
supports continuous integration. **Rival:** compatibility alone does not.

**E26.1 (PROVED LOCAL, sharp obstruction).** For every prime p, the
uniform assignment mu_r(a)=p^-r is normalized and projectively compatible,
since p*p^-(r+1)=p^-r. Nevertheless it has unbounded p-adic norm:
|mu_r(a)|_p=p^r. Were I a bounded Q_p-linear functional agreeing with these
cylinders, their indicator functions would have supremum norm 1 but
|I(1_(a+p^r Z_p))|_p=p^r. No finite bound for I exists. This does not
deny ordinary real-valued Haar probability on Z_p: the scalar codomain
has changed.

**Positive repair.** If the compatible weights satisfy a uniform bound
|mu_r(a)|_p<=C, define I on locally constant f by
sum_a f(a)mu_r(a). Compatibility makes this independent of refinement.
The ultrametric inequality gives |I(f)|_p<=C||f||_infty. Locally constant
functions are dense in C(Z_p,Q_p): continuous functions on compact Z_p
are uniformly continuous, so a sufficiently fine cylinder partition
approximates uniformly. Thus I extends uniquely and boundedly. Conversely,
any bounded functional bounds every cylinder weight by its norm. This is
an exact necessary-and-sufficient bounded integration criterion, not a
construction of zeta moments or Kummer congruences.

Mahler's null-coefficient criterion supplies a separate classical function
completion. The original 1958 paper and its 1961 correction were opened;
the latter corrects a differentiability proof and must accompany any use
of that original theorem. No differentiability theorem is needed here.
**Verdict:** compatibility-alone completion is REFUTED; bounded integration
is DISCLOSED with its missing uniform-bound hypothesis restored. Next
lamp: an arithmetic measure with justified corrected-zeta moments.

## E27 — Finite, adelic, and Archimedean transport

**Typed question.** Can a continuous additive map carry an isolated
p-adic integer source directly to the real carrier while preserving
integer addition, or must transport retain an additional source lift?

**E27.1 (CLASSICAL / PROVED LOCAL).** Every continuous additive homomorphism
f:Z_p->R is zero. Its image is a compact additive subgroup of R. A subgroup
containing x!=0 contains all integer multiples nx and is unbounded, hence
cannot be compact. This does not prohibit nonlinear continuous
finite-residue observations, circle-valued characters, or a shared
diagonal rational source embedded separately at all places.

The existing normalized product formula and additive reciprocity are
replayed at q=7/30. They use actual rational index lifts; no map from
an arbitrary finite residue to a uniquely determined real address is
introduced. In particular the two embeddings preserve a common source,
not the isolated topologies of Z_p and R.

**E27.2 (PROVED LOCAL, bounded analytic bridge).** For the finite source
defined in E30, the causal ramp has the Laplace transform

\[
\int_0^\infty e^{-zt}F_b(t)\,dt
=-\frac1{z^2}\sum_{n=2}^N
 b(n)\log n\;n^{-(z+1/2)},\qquad\Re z>0.
\]

Proof: the sum is finite and
integral_(log n)^infty exp(-zt)(t-log n)dt=n^-z/z^2, by one translation
and integration by parts. This transport preserves genuine log phase,
half-density, and finite Dirichlet-log coefficients. It is not Tate's
entire local-to-global distributional framework or Gamma completion.
For the full genuine source, absolute convergence at Re z>1/2 permits
the classical -zeta'/zeta(z+1/2) identity; no continuation into the
critical strip follows from this finite proof.

**Verdict:** a direct nontrivial continuous additive Z_p-to-R bridge is
REFUTED; rational-lift and bounded-log-source transport survives. Next
lamp: a complete standard source/domain representation, followed by an
independent sign theorem.

## E28 — Gaussian prime coverage and the source firewall

**Typed question.** Does a translation witness in the periodic norm sieve
for finitely many primes certify an infinite actual Gaussian-prime walk?

**Positive hypothesis:** authentic sieve containment plus zero-displacement
potential certificates yields finite prime-component bounds. **Rival:**
sieve leakage alone permits composite points and proves no prime walk.

Replayed the existing P={2,5,13}, D^2=2 confinement certificate and exact
finite-exception transport. Its source-relative bound is 580; no
optimality claim is made. At D^2=4 the same periodic sieve has an 82-step
closed quotient walk translating by (0,130). The witness is correctly
labeled as periodic-sieve escape only.

**Fresh decisive source falsifier:** z=1+30i belongs to this sieve, since
N(z)=901=17*53 is divisible by none of 2,5,13, but z is not a Gaussian
prime. Therefore a sieve-allowed path is not by that fact an actual
Gaussian-prime path. This also exhibits how increased finite coverage
can fail to identify the original source predicate.

The pinned OpenAI manuscript and source manifest remain the provenance
for the imported all-step existence theorem. This campaign used its
stored source metadata and mathematical interface, and opened its pinned
GitHub paper/scope URLs. The web reader exposed the GitHub shell rather
than manuscript text; raw-content retrieval returned DisabledError.
No fresh source-file hash verification or Lean v4.34.1 rebuild is claimed.
The finite certificates replay without importing all-step existence.

**Verdict:** the finite source-preserving certificate survives; sieve
escape implies prime escape is REFUTED. A uniform all-D source-derived
certificate construction remains UNVERIFIED. Next lamp: the actual
finite-sieve existence argument or a new source-specific construction,
not quotient finiteness alone.

## E29 — Euler/Gamma/theta completion controls

Replayed genuine local Euler factors, standard Lambda(2) rational enclosure,
deleted Euler factor p=3, DZ8, and DZ9. These are different checks. The
standard Gaussian is declared explicitly; it is not inferred from
self-duality alone.

**E29.1 (PROVED LOCAL family, classical Gaussian Fourier premise).** Fix
an integer k>=2 and a positive rational w with

\[
2<kw<k+k^{-1},\qquad r=k^2.
\]

The positive normalized Schwartz function

\[
f(x)=\frac{wG_1(x)+G_{r^2}(x)+r^{-1}G_{r^{-2}}(x)}{w+1+r^{-1}},
\quad G_a(x)=e^{-\pi a x^2},
\]

is Fourier self-dual, with f(0)=integral f=1, by the classical Gaussian
Fourier identity. Its Mellin multiplier relative to the standard real
factor is

\[
C(s)=\frac{w+r^{-s}+r^{s-1}}{w+1+r^{-1}}
=C(1-s),\quad C(0)=C(1)=1.
\]

With y=r^(s-1/2), its zeros satisfy y^2+kw*y+1=0. The strict lower
bound kw>2 gives two negative real roots with distinct reciprocal
moduli R,R^-1, R>1. The function R+R^-1 is strictly increasing for
R>1; kw<k+k^-1 gives R<k. Hence the added zeros are

\[
s=\tfrac12\pm\frac{\log R}{\log(k^2)}
+\frac{(2j+1)\pi i}{\log(k^2)},\quad j\in\mathbb Z,
\]

strictly inside 0<Re s<1 and off Re s=1/2. Multiplying the same genuine
finite zeta Euler source by this different real test produces C(s)xi(s)
with those extra zeros; actual xi is unchanged. No unknown zeta zeros
entered construction or proof.

**Fresh holdout:** k=3,w=4/5,r=9. The quadratic is
y^2+(12/5)y+1, discriminant 44/25, and
R=(6+sqrt(11))/5 lies between 1 and 3. The strict boundaries have
separate negative controls: kw=2 does not give off-line roots, and
kw=k+k^-1 puts them at the strip boundary. The construction is a
generalization of the already recorded DZ9 mechanism, not independent
new evidence against actual RH.

**Verdict:** functional equation, pole normalization, source positivity,
and Fourier self-duality do not force the standard completion or RH.
The implication is REFUTED by an explicit source mutation. Next lamp:
standard completion identification across an adequate source/test family,
then positivity of that exact Weil form.

## E30 — Source tomography and the Weil/Suzuki interface

Let a(1)=1 and a(2),...,a(N) lie in Q. On arithmetic prefixes define
(u*v)(n)=sum_(d|n)u(d)v(n/d). Write a=delta_1+h. Since h(1)=0,
h^*r(n)=0 for 2^r>n. Define

\[
b=\log_*a=\sum_{r\ge1}(-1)^{r+1}h^{*r}/r,
\quad
F_b(t)=-\sum_{n=2}^N\frac{b(n)\log n}{\sqrt n}(t-\log n)_+.
\]

These are finite algebraic sums. For the genuine prefix a(n)=1,
Euler factorization gives b(p^j)=1/j and b(n)=0 at other n>1;
then b(n)log n=Lambda(n).

**E30.1 (PROVED LOCAL source-identification theorem).** If T>log N,
F_b restricted to [0,T] determines b(2),...,b(N), and therefore the
entire normalized arithmetic prefix a(1),...,a(N). It is linear in b,
though the initial a-to-b transformation is nonlinear.

Proof: in distributions on (0,T),
F_b''=-sum_n b(n)log n/sqrt n * delta_(log n). Distinct log n are
distinct points in (0,T), so a test bump around each isolates its
coefficient. Every normalization log n/sqrt n is nonzero. In the finite
nilpotent convolution algebra, exp_* and log_* are inverse by the
ordinary formal power series identities (which truncate in each
coordinate). Thus b recovers a. The implementation independently
computes exp_* and tests 25 signed rational prefixes from a fixed fresh
random seed, across five horizons, against the existing log adapter.

**Sharp horizon countermodel.** At T=log N, adding c!=0 to b(N) changes
no response value on [0,T], since (t-log N)_+=0 there. More generally,
events beyond the measured horizon are invisible. Strict horizon and
source-support assumptions cannot be silently dropped.

**E30.2 (PROVED LOCAL four-query inversion and stability).** Choose
u_-<v_- strictly in (log(n-1),log n) and u_+<v_+ strictly in
(log n,log(n+1)); log1=0. On either gap F_b is affine, so

\[
D_-:=\frac{F_b(v_-)-F_b(u_-)}{v_--u_-},\quad
D_+:=\frac{F_b(v_+)-F_b(u_+)}{v_+-u_+},\quad
b(n)=-\frac{D_+-D_-}{\log n/\sqrt n}.
\]

If every query has absolute error <=epsilon, the coefficient error is at
most

\[
\frac{2\epsilon}{\log n/\sqrt n}
\left(\frac1{v_+-u_+}+\frac1{v_--u_-}\right).
\]

Proof: each slope uses two errors, whose difference has magnitude
<=2epsilon; add the two slope bounds and divide by the positive weight.
Thus the event-gap width is a real conditioning cost, not merely a
formatting choice. The machine implementation encloses logs and square
roots by existing proven Fraction bounds, picks rational thirds inside
certified gaps, and propagates all four query intervals outward. For
two distinct reduced rationals with positive denominator <=D, their
distance is at least 1/D^2. An enclosure of width <1/D^2 contains at
most one such coefficient, conditional on the denominator prior. It
does not prove that a candidate exists or that the prior is valid.

Controls recover genuine prime powers and zero composite coefficients;
fake a(6)=2 yields b(6)=1; a(n)=2^(v_2(n)) yields weight anomalies;
wrong n^-1 half-density recovers 1/sqrt2 instead of b(2)=1; moving the
log2 impulse to log3 yields b(2) near zero under the declared clock;
and large sound noise intervals refuse the denominator uniqueness test.
The second ramp implementation is different code but shares the rational
log/sqrt primitives. This is implementation triangulation, not a blind
external witness.

**Precise completed-form interface.** Suzuki's explicit prime term for
the standard zeta Weil functional is

\[
W_{\rm prime}(f)=-\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
\{f(\log n)+f(-\log n)\}.
\]

For a compactly supported test f, only finitely many terms enter, so the
source-identification result recovers this arithmetic distribution on
any bounded log window. For f=v*tilde(v), v in C_c^infty(-a,a), its
support lies in [-2a,2a]; the required prime prefix ends at exp(2a).
The pole and Gamma contributions remain separate. A mutation's ramp is
a deliberately zeta-normalized diagnostic, not the Weil distribution
of an arbitrary L-function.

One can state a bounded operator consequence without positivity:
on L^2(-a,a), extending functions by zero, let T_l v(x)=v(x-l).
The compact prime term is the finite self-adjoint operator

\[
B_a=-\sum_{\log n\le2a}w_n(T_{\log n}+T_{-\log n}),\quad
w_n=\Lambda(n)/\sqrt n,
\quad\|B_a\|\le2\sum_{\log n\le2a}|w_n|.
\]

The adjoint of the compressed shift is its opposite compressed shift;
each has norm <=1. This proves the norm bound. **When a>log2/2**, two
smooth equal bumps fit inside (-a,a) with centers separated by log2.
Choose their width small enough to avoid every other active prime shift;
they yield a nonzero off-diagonal 2x2 prime form with eigenvalues of
opposite signs. For 2a<=log2 the compressed prime operator is instead
zero (the equality endpoint has zero overlap in L2). Auditor F exposed
the previously omitted window hypothesis with a=1/4. The original worker
commit and this correction are retained separately. Such a prime-only result is
consistent with the existing isolated impulse obstruction. Gamma/pole
coupling must be handled before asking for completed sign.

**Verdict:** bounded source identification and finite arithmetic
distribution transport are DISCLOSED under their source-law and oracle
assumptions. Universal full-Weil positivity remains UNVERIFIED. The
missing lamp is an exact standard completion/domain representation and
a source-specific positivity argument; the tomography result does not
secretly assume or reproduce RH.

## Evidence and reproducibility

New evidence: `scripts/cambrian_e_arithmetic_probe.py`,
`observational_succ/cambrian_e_arithmetic_transport.py`,
`tests/test_cambrian_e_arithmetic_transport.py`, and
`CAMBRIAN_E_ARITHMETIC_RECEIPT.json`. The receipt records the execution
head, immutable base, Python version, and SHA-256 hashes of code, probe,
and tests. Because a commit cannot contain its own hash, the execution
head records the pre-commit state; content hashes identify exactly the
executed files. The integration report must record the resulting commit.

Executed validation:

```sh
python -m unittest discover -s tests -p 'test_cambrian_e_arithmetic_transport.py'
python -m unittest discover -s tests -p 'test_diagonal_adele_zeta.py'
python -m unittest discover -s tests -p 'test_adelic_theta_completion.py'
python -m unittest discover -s tests -p 'test_source_prime_certificates.py'
python scripts/cambrian_e_arithmetic_probe.py --output research/2026-10-13/CAMBRIAN_E_ARITHMETIC_RECEIPT.json
python scripts/verify_provenance.py
python scripts/diagonal_adelic_zeta_probe.py
python scripts/gaussian_moat_probe.py
python scripts/observer_foundations_probe.py
python scripts/ordinal_succ_report_probe.py
```

The new suite has 11 passing tests. Existing suites have 22, 14, and 7
passing tests respectively. Provenance verifies 72 items, including
17 byte-identical archived research files. The baseline foundational and
ordinal probes also passed. Full-suite/CI and formal
verification are integration duties, not claimed by these targeted runs.

## Primary sources inspected and priority boundaries

1. Masatoshi Suzuki, *Weil's quadratic form via the screw function*,
   arXiv:2606.09096v3 (23 September 2026),
   <https://arxiv.org/html/2606.09096v3>. Opened the actual text, including
   the introduction's arithmetic Weil formula and distributional section
   2.5. These specify the completed domain and prime distribution used
   for the interface above. The paper's spectral limiting statement
   remains a conjecture; self-adjoint finite operators do not settle RH.
2. Masatoshi Suzuki, *Aspects of the screw function corresponding to the
   Riemann zeta function*, arXiv:2206.03682,
   <https://arxiv.org/abs/2206.03682>. Opened primary abstract record.
   Existing project formulas were not promoted merely from this abstract.
3. Kurt Mahler, *An interpolation series for continuous functions of a
   p-adic variable*, J. Reine Angew. Math. 199 (1958), 23–34,
   <https://carmamaths.org/resources/mahler/docs/139.pdf>, and its 1961
   correction, <https://carmamaths.org/resources/mahler/docs/145.pdf>.
   Rendered pages 1–2 of the original and page 1 of the correction.
   The p-adic bounded-functional criterion above is independently proved.
4. NIST DLMF §25.4,
   <https://dlmf.nist.gov/25.4>, exact standard completion/reflection
   normalization. The self-dual mutant formulas are derived above from
   the declared Gaussian Fourier premise, rather than read off zeta zeros.
5. OpenAI, *Bounded-Step Walks on Gaussian Primes*, pinned source
   <https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Bounded-Step-Walks-on-Gaussian-Primes-September-26-2026/paper.pdf>.
   Use the precise retrieval boundary in E28; no newly executed external
   formalization or re-audited all-step proof is asserted.

The closest novelty statement supported here is **new-to-project certified
four-query source tomography and the combined arithmetic control suite**.
Volterra ramp inversion, Dirichlet convolution exp/log, compact-group
obstructions, bounded p-adic integration, and Gaussian completion
nonuniqueness are classical or elementary constructions. An independent
academic theorem has not been established in this cluster.

## Integration recommendation and next discriminator

Accept the additive source-tomography instrument and paper theorem;
retain all positive and negative controls. Keep the E29 family explicitly
as completion-source mutation, and E26 as a codomain-sensitive obstruction.
Do not promote any claim to RH, physical observation, or full completed
Weil positivity. The next useful experiment is a rigorous standard
Gamma/pole interval oracle on a compact smooth test family, independently
checked against Suzuki's exact distributional normalization and these
mutants. Extending only the finite prime window would enlarge the source
receipt but would not close the sign gap.
