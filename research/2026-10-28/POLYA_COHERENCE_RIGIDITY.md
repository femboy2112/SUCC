# Source-marked Pólya coherence: minimal environment and unavoidable leakage spectrum

**Research parent:** `fec9b7a72dd6b8c7550d7915070ee8094f2b94a2`, draft PR #348.
**Authority:** paper proofs below, exact finite independent checks, and a Lean-kernel-checked
real quadratic-form core. Academic priority **UNVERIFIED**. This is finite operator
mathematics, not a quantum-device implementation, physical hbar law, RH result, or
signed BBP cancellation estimate. Original archives and source formulas are unchanged.

The main answer to the handoff is constructive and sharp. A two-dimensional environment
is sufficient and necessary at every nontrivial two-channel grade. It can return in
one fixed pure state while the marked uniform source grows coherently. For every
implementation with these locality, probability, and source-preservation properties,
the leakage probability on other inputs is the same explicit quadratic form. Its
complete spectrum is a classical Hahn spectrum. Thus the original stochastic-matrix
norm loss is not a universal cost of preserving the marked state, while source-independent
coherence preservation really is obstructed.

## 1. Definitions and exact theorem

Fix an integer `m>=1`; this is the dimension at grade `j=m-1`, not a prime.
Write `H_m=C^m`, with basis `|k>`, `0<=k<m`, and

`omega_m=m^(-1/2) sum_k |k>`.

The imported one/one Pólya birth matrix `P_m:H_m -> H_(m+1)` has

`P_m[k,k]=(m-k)/(m+1)`, `P_m[k+1,k]=(k+1)/(m+1)`.

These are probabilities. The prior handoff correctly established that applying this
same matrix to amplitudes gives `P_m omega_m=sqrt(m/(m+1)) omega_(m+1)`.

An **admissible source-marked lift** consists of a Hilbert space `E`, a unit vector
`eta in E`, and an isometry `V:H_m -> H_(m+1) tensor E` such that, for each k,

`V|k>=|k> tensor a_k + |k+1> tensor b_k`,

`||a_k||^2=(m-k)/(m+1)`, `||b_k||^2=(k+1)/(m+1)`,

and `V omega_m=omega_(m+1) tensor eta`.

The support condition is literal. Basis measurement has the original Pólya birth
probabilities; the last condition preserves the marked coherent source, including
its phase convention. No assertion of preservation on every coherent input is included.

**Theorem PCR-01 (minimal lift).** For every m an admissible lift exists. Its smallest
possible environment dimension is 1 for m=1 and exactly 2 for every m>=2. In dimension
2, with orthonormal environment vectors `e0,e1`, one such lift has `eta=e0` and

```
a_k = [(m-k)e0 + sqrt(k(m-k))e1] / sqrt(m(m+1)),
b_k = [(k+1)e0 - sqrt((k+1)(m-k-1))e1] / sqrt(m(m+1)).
```

**Theorem PCR-02 (universal accepted channel and sharp leakage).** For *every*
admissible lift, with any environment dimension, the accepted operator

`K0=(I tensor <eta|)V`

is forced to be

`K0=sqrt((m+1)/m) P_m`.

Consequently, for every `psi in H_m`, the squared norm outside the returned source
environment ray equals

```
Leak_m(psi) = ||(I tensor (I-|eta><eta|))V psi||^2
           = 1/[m(m+1)] sum_(l=1)^(m-1) l(m-l)|psi_l-psi_(l-1)|^2.
```

For normalized psi this is the probability of an auxiliary outcome orthogonal to eta;
for general psi it is the corresponding homogeneous quadratic form. Its spectrum is

`{r(r+1)/[m(m+1)] : r=0,...,m-1}`,

with each eigenvalue simple. For m>=2, putting
`psi_perp=psi-<omega_m,psi>omega_m`, the sharp inequalities are

```
2/[m(m+1)] ||psi_perp||^2 <= Leak_m(psi)
                            <= (m-1)/(m+1) ||psi_perp||^2.
```

Equality on the left holds on the first nonconstant Hahn mode, and equality on the
right on its highest-degree mode, together with any added uniform component. Leakage
vanishes exactly on the span of omega_m. This is a finite spectral uncertainty statement
between deviation from the marked source and disturbance of its auxiliary record.
It contains no physical unit or hbar.

## 2. Proof of minimality, construction, and universality

Two adjacent source columns share precisely one target row. Isometry therefore forces

`<b_(l-1),a_l>=0`, for `1<=l<m`.

If E is one-dimensional and m>=2, both factors are nonzero and this is impossible.
At m=2 its phase-independent squared overlap is `1/9`. Nonadjacent source columns have
disjoint target supports. This proves the lower bound for every possible choice of
edge phases, without a positivity assumption on the amplitudes.

For the displayed two-dimensional construction, direct calculation gives the specified
edge norms, and

`<b_(l-1),a_l>=[l(m-l)-l(m-l)]/[m(m+1)]=0`.

Each column has norm one, so V is an isometry. In every target row the two incoming
environment vectors sum to `sqrt(m/(m+1))e0`, with the single-parent boundary rows
having the same value. Hence `V omega_m=omega_(m+1) tensor e0`. For m=1 all e1
coefficients vanish and the environment can be discarded. This proves PCR-01.

Now consider any admissible lift, not just that construction. Set
`c=sqrt(m/(m+1))`. Source preservation gives

`a_0=c eta`, `a_l+b_(l-1)=c eta` (`1<=l<m`), `b_(m-1)=c eta`.

Taking inner products of the middle identity with its orthogonal summands forces

`<eta,a_l>=||a_l||^2/c=(m-l)/sqrt(m(m+1))`,

`<eta,b_(l-1)>=||b_(l-1)||^2/c=l/sqrt(m(m+1))`.

The boundary values obey the same formula. Thus the projection onto eta is uniquely
K0, even when the remaining environment coordinates differ. Since V is an isometry,
the rejected squared norm is `||psi||^2-||K0 psi||^2`; it is implementation-independent
under the stated conditions. This is a stronger assertion than one successful example.

For the constructed lift the second Kraus operator has zero boundary rows and

`(K1 psi)_l=sqrt(l(m-l)/[m(m+1)])(psi_l-psi_(l-1))`.

It gives the displayed leakage formula and the exact identity `K0* K0+K1* K1=I`.
The channel `rho -> K0 rho K0*+K1 rho K1*` is consequently trace preserving and
completely positive. This describes a mathematical channel, without claiming a
physical implementation or cost-free preparation of its input.

## 3. Independent spectral proof and Lean boundary

Let L be the real symmetric m-by-m path Laplacian with edge weight `l(m-l)`.
For any polynomial p, at node k it acts as

```
(Lp)(k)=k(m-k)[p(k)-p(k-1)]
       +(k+1)(m-k-1)[p(k)-p(k+1)].
```

The boundary weights vanish, so no value outside the grid is read. On monomial `k^r`,
the degree `r+1` terms cancel; the degree r coefficient is
`2r+r(r-1)=r(r+1)`, and all other terms have smaller degree. For r=0 it vanishes.
Evaluation of polynomials of degree less than m on the m distinct grid points is an
isomorphism. Thus in the monomial-evaluation basis L is triangular with diagonal
`r(r+1)`, `0<=r<m`. These values are distinct. Symmetry supplies an orthogonal
eigenbasis and gives the sharp two-sided inequalities in PCR-02. This proof does
not assume a table of eigenvalues.

As an independent exact representation, the tests evaluate

`Q_r(k)=sum_(t=0)^min(r,k) (-1)^t binom(r,t)binom(r+t,t)binom(k,t)/binom(m-1,t)`.

They verify the full eigenvector equation. The separate SymPy oracle instead constructs
the radical isometry, extracts K1, and factors its characteristic polynomial.
The identification with `Q_r(k;0,0,m-1)` is classical Hahn theory, with the same
difference equation in [DLMF 18.22.10–11](https://dlmf.nist.gov/18.22#E10).

[`formal/PolyaCoherence.lean`](../../formal/PolyaCoherence.lean) proves, for **all**
natural m and all real coordinate functions v, the finite quadratic identity

```
sum_(i=0)^m {[(m-i)v_i+i v_(i-1)]^2+i(m-i)(v_i-v_(i-1))^2}
  =m(m+1) sum_(i=0)^(m-1) v_i^2.
```

At i=0 the coefficient of the previous coordinate is zero; Lean's truncated natural
subtraction is therefore harmless. At i=m the extra coordinate also has zero weight.
The proof derives the row identity by ring algebra and proves the all-m summation
identity. The degree-one Hahn eigenvalue identity is also kernel checked. Applying
the real identity separately to real and imaginary parts proves the complex quadratic
identity on paper. The full complex-channel construction, all-degree spectral theorem,
and source uniqueness are **not** claimed as Lean formalizations.

Executed with Lean 4.14.0 and mathlib
`4bbdccd9c5f862bf90ff12f0a9e2c8be032b9a84`; reported dependencies of the main
theorems are only `propext`, `Classical.choice`, and `Quot.sound`. There are no added
axioms, admitted goals, or analytic placeholders. These are ordinary Lean foundational
dependencies, not new mathematical premises.

## 4. Full-x Oily source covariance

**Theorem PCR-03.** Let `mu_k>0`, `sum mu_k=1`, and let `0<p_k<1` for `0<=k<m`
be any nearest-neighbor birth law. Let `nu=P mu`. Write the square-root marked sources
as `omega_mu=sum sqrt(mu_k)|k>` and `omega_nu=sum sqrt(nu_l)|l>`.
There is an isometry with exactly these edge probabilities, supported on k and k+1,
mapping `omega_mu` to `omega_nu tensor eta`. For m>=2 its minimal environment dimension
is exactly two. Every such lift has the same accepted operator

`K0[l,k]=P[l,k] sqrt(mu_k/nu_l)`.

**Proof.** In target row l let `x=mu_l(1-p_l)` and `y=mu_(l-1)p_(l-1)`, omitting
missing boundary parents, so `t=x+y=nu_l>0`. Define weighted environment vectors

```
A_l=(x e0+sqrt(xy)e1)/sqrt(t),
B_l=(y e0-sqrt(xy)e1)/sqrt(t).
```

They are orthogonal, have squared norms x and y, and sum to `sqrt(t)e0`. Divide A_l
by `sqrt(mu_l)` and B_l by `sqrt(mu_(l-1))` to obtain the edge vectors. Unique shared
target rows give column orthogonality; the prescribed column probabilities sum to one.
The weighted row sum gives marked-source transfer. Conversely, isometry forces
orthogonality in each shared row, and inner products against the marked row sum force
the stated K0. The scalar obstruction is identical to PCR-01. This proves the theorem.

Apply it to the actual imported `conditional_split(x,j,k)` and
`unique_local_birth_probability(x,j,k)` for **every real `0<x<=1` and every j>=0**.
All probabilities are strictly positive, and the prior CDF proof gives `nu=mu_(j+1)`.
The code checks rational x exactly; the proof's real parameter domain is not inferred
from those finite samples. At x=0 there is no reachable birth, and no uniqueness or
dimension requirement is asserted for unreachable states. A single x-independent
channel is not inferred: the marked source and channel are transported together.

More generally, prescribed diagonal phase gauges `D_in,D_out` transport a lift as
`V'=(D_out tensor I)V D_in*`. This proves covariance of a *marked* source. It cannot
produce unknown phases: the gauges must already be supplied and retain their provenance.
In particular, inserting original BBP phases into these gauges does not estimate their
signed sum or select the zero seed.

## 5. Higher-rank prime fibers and exact environment requirement

**Theorem PCR-04.** Fix integers `c>=2`, `j>=0`. On the weak compositions
`k_1+...+k_c=j`, use the c-channel Pólya transitions

`k -> k+e_i` with probability `(k_i+1)/(j+c)`.

The uniform distribution on grade j is sent to the uniform distribution on grade j+1.
Among support-preserving isometries realizing these basis probabilities and preserving
the corresponding uniform pure marked sources, the smallest environment dimension is

`min(c,j+1)`.

Moreover the projection onto the returned marked environment state is forced to be
`K0=sqrt((j+c)/(j+1))P` for every such lift.

**Proof.** There are `M_j=binom(j+c-1,c-1)` source states. For a target composition l,
the sum of incoming transition probabilities is `(sum_i l_i)/(j+c)=(j+1)/(j+c)`;
`M_(j+1)/M_j=(j+c)/(j+1)`, proving uniform-source preservation.

Distinct source compositions can share at most one target: if `k+e_i=k'+e_h` and
`k!=k'`, the ordered pair `(i,h)` is uniquely determined by `k'-k`. Hence isometry
forces the environment edge vectors entering any given target to be mutually
orthogonal. The number of parents of l is the number of its positive coordinates.
Its maximum is `d=min(c,j+1)`, attained by distributing the j+1 units among as many
coordinates as possible. Since every edge probability is positive, `dim E>=d`.

For sufficiency, in each target row independently, enumerate its q<=d parents and
let `t_i=mu_parent P[row,parent]` be their incoming probability fluxes. In `C^d`, pad
`u=(sqrt(t_i/nu_row))_i` with zeros. Choose a unitary U_row carrying u to a fixed
unit vector eta (a Householder reflection suffices over the reals). Assign the edge
vector `sqrt(P[row,parent_i]) U_row e_i`. Edge norms and pairwise orthogonality are
correct, and the weighted row sum is `sqrt(nu_row)eta`. The unique-shared-row property
then yields an isometry. Finally, projecting the marked row sum onto each orthogonal
summand forces `K0[row,parent]=P[row,parent]sqrt(mu_parent/nu_row)`, as before.

For an actual prime power `p^j`, these labels are its ordered c-factor splittings.
They carry the classical `Sym^j(C^c)` representation. The theorem needs neither a
new SU(c) dynamical law nor physical hbar. Treating composite 6 as a primitive prime
breaks the source fiber: even for c=2, `d(6^j)=(j+1)^2`, not j+1. The local algebra
alone is not a test of primality, and attaching a false label does not authenticate it.
No multivariate spectral formula is claimed here.

## 6. Strengthened terminal-law uniqueness and a concrete countermodel

**Theorem PCR-05.** Consider Markov compilers whose entire visible state is `(j,k)`,
starting at `(0,0)`, with only births `(j,k)->(j+1,k)` or `(j+1,k+1)`, and stopping
with probability `s_j` independent of k. Suppose the almost-sure terminal law is the
full authenticated Oily law

`t_(j,k)=(1-u)(1-v)u^k v^(j-k)`, `u=x-x^2/2`, `v=x^2/2`, `0<x<=1`.

Then both the stopping hazard and every birth probability are unique. Prescribing
the conditional marginal at every reached grade is a redundant extra assumption.

**Proof.** Every realized path visits grade j exactly when its terminal grade J is at
least j. Thus arrival mass is `C_j=Pr(J>=j)`. Since `q_j=Pr(J=j)>0`, the hazard is
forced to be `s_j=q_j/C_j>0`. Terminal mass is arrival-state mass times s_j, so the
conditional arrival law is already `mu_j(k)=t_(j,k)/q_j`. Finally nearest-neighbor
CDF conservation forces

`mu_j(k)a_(j,k)=sum_(i<=k)mu_j(i)-sum_(i<=k)mu_(j+1)(i)`.

Positivity determines every a uniquely; the imported compiler supplies the valid
solution. No unobserved internal state or history-dependent policy is included in the
uniqueness statement. Such refinements can change microhistory while retaining a
coarse transition law.

**Countermodel when split-independent stopping is removed.** At x=1 the original
root terminal mass is 1/4, arrivals at `(1,0),(1,1)` are `(3/8,3/8)`, their terminal
masses are each 1/8, and all three grade-two arrivals equal 1/6. Replace only these flows:

| Edge | Original flow | Modified flow |
|---|---:|---:|
| `(0,0)->(1,0)` | 3/8 | 5/12 |
| `(0,0)->(1,1)` | 3/8 | 1/3 |
| `(1,0)->(2,1)` | 1/12 | 1/8 |
| `(1,1)->(2,1)` | 1/12 | 1/24 |

The other grade-one outgoing edges remain 1/6. Every node still conserves probability;
all terminal masses remain unchanged, and the grade-two arrival distribution is restored
exactly. Continue with the original compiler from grade two onward. This gives the
**entire same terminal law at every grade**, but the grade-one hazards are now 3/10 and
3/8. The root birth probability changes from 1/2 to 4/9. This is an explicit exact
counterexample to terminal-law uniqueness without its stopping assumption.

This also repairs a possible overreading of the parent dossier: dropping only the
separately stated reached-grade marginal condition does *not* produce ambiguity if
the full terminal law, the Markov state, and grade-only stopping remain fixed.

## 7. Composition preservation: exact classical criterion

**PCR-06 (CLASSICAL).** Let J be an isometry, `P=JJ*`, and `C(T)=J*TJ` on bounded
operators. For a unital star subalgebra A, C is multiplicative on A if and only if
`ran J` reduces every `T in A`, equivalently `[P,T]=0` for every T in A.

Indeed

`C(AB)-C(A)C(B)=J*A(I-P)BJ`.

If C is multiplicative, taking `(A,B)=(T*,T)` gives

`0=J*T*(I-P)TJ=((I-P)TJ)*((I-P)TJ)`,

so `(I-P)TJ=0`. Applying the same argument to T* gives reduction. Conversely reduction
makes the displayed defect zero for every pair. More generally

`||C(AB)-C(A)C(B)|| <= ||(I-P)A*J|| ||(I-P)BJ||`.

The positive T*T defect is exactly leakage squared, so the constant one is sharp in
the vector quadratic-form identity. A particular ordered pair may have zero defect
without a reducing subspace; the theorem deliberately quantifies over a star algebra.
This is the standard compression/multiplicative-domain mechanism, independently
proved here, not a new theorem attributed to SUCC. Bibliographic anchor: M.-D. Choi,
*A Schwarz inequality for positive linear maps on C*-algebras*, Illinois J. Math. 18
(1974), 565–574, [DOI](https://doi.org/10.1215/ijm/1256051007). The publisher page was
not retrievable by the browsing tool in this run; the elementary proof above is complete
and does not rely on accessing that paper.

## 8. Adversarial boundaries, sources, and next tests

The same-population phase-flipped input `(1,-1)/sqrt(2)` at m=2 has leakage 1/3 and
reduced output purity 5/9 in the explicit lift, whereas omega_2 has zero leakage and
pure output. Probability agreement therefore does not imply coherent-source agreement.
On the marked trajectory the auxiliary system returns exactly to eta at each grade;
there is no theorem requiring a growing retained history for that specific trajectory.
This is not preservation of all quantum information, an entropy-production result,
or a free physical erasure claim.

The following source distinctions remain load-bearing:

* `U_0=0` and the exact signed four-pole forcing are unchanged and not replaced by an
  Oily endpoint. This theorem concerns a constructed observer prior.
* The seeds `1/15` and `-pi/16` leave the forcing and Oily compiler unchanged. No theorem
  here can authenticate the zero seed from that compiler. Global phase also leaves
  leakage invariant; phase covariance requires the source labels to be supplied.
* Altered four-pole forcing may still admit an abstract channel of this form. Local
  channel existence therefore does not certify the original BBP forcing.
* The ordinary one-mode zeta stopping and balanced Oily stopping differ by
  `(j+1)(1-q)`. Coherifying their common allocation does not turn their global
  normalizers `zeta(beta)` and `zeta(beta)^2` into the same source.
* A diagonal/no-coupling implementation fails the required positive births; replacing
  probabilities by their square roots without an environment fails column orthogonality.
* Fake composite primitive primes fail the actual divisor-fiber dimension test.
* No finite spectrum or positive leakage estimate supplies signed Weyl cancellation.

Primary provenance is `observational_succ/oily_prime_growth_compiler.py` at the pinned
parent, SHA256 `d027ef10175c4f6fa0064fcd5405722a7a25f389874344a6679489374b1c8dcd`;
the observer source is `origin_fiber_arithmetic_observer.py`, SHA256
`c58186b834a84586082e5de104261b346fbd5aec6436c9dba64ada9cdcf575e2`.
The independent implementations share that source contract, but not the numerical
spectral algorithm. They are implementation bearings, not independent original sources.

The relevant prior literature includes Korzekwa, Czachorski, Puchala and Zyczkowski,
[*Coherifying quantum channels*](https://arxiv.org/abs/1710.04228), New J. Phys. 20
(2018), 043028. That work studies preserving a classical transition matrix while
increasing channel coherence, including the unitary/unistochastic boundary. Our
rectangular, nearest-neighbor, marked-input constraints differ, and the proof here
derives their consequences directly. The search does **not** establish academic novelty
of this special construction. The Hahn spectrum is explicitly classical, not new.

| Local claim | Status | Exact boundary | Next falsification target |
|---|---|---|---|
| PCR-01 | PAPER-PROVED; exact radical tests | support and basis probabilities fixed | relax support; scalar obstruction may disappear |
| PCR-02 | PAPER-PROVED; real energy core LEAN KERNEL; full spectrum exact finite tests | universal only over marked-source-preserving lifts | change phase mark without transporting channel |
| PCR-03 | PAPER-PROVED; exact rational full-x source and radical tests | positive mu and births; two-parent geometry | multi-overlap graphs can cancel across rows |
| PCR-04 | PAPER-PROVED; exact finite composition tests | uniform c-channel Pólya and fixed origin labels | source-dependent nonuniform higher-rank classification |
| PCR-05 | PAPER-PROVED with explicit relaxed-assumption countermodel | visible Markov state and grade-only hazard | hidden memory refinements and lumpability |
| PCR-06 | CLASSICAL, elementary reproof | bounded operators; whole star algebra | quantitative source-specific nonreducing algebras |
| Global coherent preservation by scalar Pólya lift | REFUTED | m>=2; every edge phase | positive overlap witness |
| Unavoidable growing retained history on the marked source | REFUTED in this finite channel model | two-dimensional returned environment suffices | physical resource model would need separate assumptions |
| Signed zero-seeded BBP cancellation from these bounds | UNVERIFIED / no implication established | selected signed phase gate remains open | genuinely signed source-labelled transfer inequality |

Reproduce the finite checks with

```
PYTHONPATH=. python -m unittest tests.test_polya_coherent_observer -v
python scripts/polya_coherence_oracle.py --output /tmp/polya-coherence-oracle.json
```

The committed oracle receipt records 18 actual-radical source-transfer/isometry cases,
characteristic polynomials for m=1 through 10, and the phase-flipped counterexample.
These finite ranges are exact checks, not the proof of the universally quantified
theorems. Consolidated run receipts and hosted CI are recorded separately by the
parent research delivery.
