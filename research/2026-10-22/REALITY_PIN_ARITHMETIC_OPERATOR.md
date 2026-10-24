# Reality Pin: an infinite arithmetic boundary operator with certified horizons

**Date:** 2026-10-22. **Parent:** spectral-boundary PR #243 at
`d2f760ab9d9a11719e950caeb2d54bfa5114f495`. **Status:** paper proofs plus independent
exact finite controls; no Lean certificate for these operator theorems, no physical
measurement, no claim of independent academic novelty.

## Hole contract and provenance

The exact hole is whether the *actual* additive and multiplicative source operators
can produce a well-defined boundary resolvent with a certified finite observation
budget. The target is deliberately weaker than physical spacetime identification:
existence, convergence, source-sensitive return coefficients, and a precise limit
on the authority of a single boundary vector. The cheapest falsifiers are a
non-summable prime perturbation, an incorrectly merged `S`/`V_2` channel, an omitted
horizon term, a fake composite primitive, and transport of the old Gibbs state to a
new Hamiltonian without checking stationarity.

Inherited sources inspected: `AGENTS.md`, `docs/FOUNDATIONS.md`, `docs/METHOD.md`,
`provenance/IMPORT_MANIFEST.json` (original foundation import commit
`ba075348b7bcc66d938b3e0ca96c26e95bba340a`),
`PRIME_BRIDGE_ONE_SHOT.md` (PR #234),
`SUCC_FUCC_RECIPROCAL_PASCAL_BRIDGE.md` (PR #236), and their source implementations.
No frozen archival source is changed. The operators and affine/reciprocal laws
below are inherited; the explicit two-horizon error bounds and certified
transcendental finite evaluator are new to this branch.

The classical analytic tools are the bounded-perturbation, spectral, resolvent and
min-max theorems. A primary author-hosted source checked in this round is Gerald
Teschl, *Mathematical Methods in Quantum Mechanics* (2009 online edition),
[Theorem 6.4, Lemma 6.5, Theorem 4.10](https://www.mat.univie.ac.at/~gerald/ftp/book-schroe/schroe.pdf).
The application below is derived explicitly; it is not attributed as a new version
of Kato–Rellich or an original compact-resolvent theorem.

## ARITH-1. Source domain, self-adjointness, compactness and thermal threshold

Let `H=ell²(N_{>=1})`, with its authenticated integer basis, and let

\[
 D e_n=(\log n)e_n,\quad
 \mathcal D(D)=\{x:\sum_n(\log n)^2|x_n|^2<\infty\},
\]
\[
 S e_n=e_{n+1},\qquad V_p e_n=e_{pn},\qquad
 T=\lambda(S+S^*)+\sum_{p\ \mathrm{prime}}p^{-\sigma}(V_p+V_p^*),
 \quad\lambda\in\mathbb R,\quad\sigma>1.
\]

(The subscript means genuine rational primes.) Define

\[
 b=2|\lambda|+\frac{2}{\sigma-1},\qquad c=b+\delta,
 \qquad\delta>0,\qquad K=D+T+cI.
\]

**Theorem.** The prime series converges absolutely in operator norm, `T` is bounded
self-adjoint with `||T||<=b`, and `K` is self-adjoint on `D(D)` with the finitely
supported sequences as a core. It satisfies `K>=delta I`, has compact resolvent,
and has a complete eigenbasis with eigenvalues `E_j` counted with multiplicity
obeying

\[
 \log j+c-b\le E_j\le\log j+c+b.
\]

Consequently, for real `beta>0`, `exp(-beta K)` is trace class exactly when
`beta>1`; in that regime

\[
 e^{-\beta(c+b)}\zeta(\beta)
 \le\operatorname{Tr}(e^{-\beta K})
 \le e^{-\beta(c-b)}\zeta(\beta).
\]

**Proof.** Every `S,V_p` is an isometry. The prime sum is bounded by
`2 sum_p p^-sigma <= 2 sum_{n=2}∞ n^-sigma <= 2/(sigma-1)` by the integral test.
Its adjoint is its norm-limit adjoint. The real diagonal multiplication operator
`D` is self-adjoint, and adding bounded symmetric `T+cI` preserves its domain and
self-adjointness (equivalently, apply the bounded case of Kato–Rellich). Truncation
of a vector and of `Dx` proves the finite-support core statement; bounded
perturbation gives equivalent graph norms. The lower bound follows from
`D>=0` and `T>=-bI`.

For real `s>=0`, put `R_0=(D+c+s)^-1`. This diagonal operator is compact since its
entries tend to zero. The norm of `R_0 T` is at most `b/(c+s)<1`, so

\[
 (K+s)^{-1}=(I+R_0T)^{-1}R_0
\]

is compact. The resolvent identity extends compactness to every resolvent point;
self-adjointness guarantees all nonreal points, and the lower bound guarantees
`-s` for real `s>-delta`. Min-max applied to
`D+(c-b)I <= K <= D+(c+b)I` proves the eigenvalue inequalities. Exponentiating the
scalar inequalities and summing gives the trace assertions, including divergence
for `0<beta<=1`. QED.

**Boundary observable.** `m(s)=<e_1,(K+s)^-1 e_1>` is therefore defined for `s>=0`,
positive and at most `(s+delta)^-1`. It is the Stieltjes transform of the actual
source vector's spectral measure. No physical choice of `lambda,sigma,c` follows
from this construction, and changing `c` between candidate models changes the
observable. Candidate comparisons below keep one common shift fixed.

## ARITH-2. Certified norm-resolvent source horizon

Let `P_N` project onto source labels `1,...,N`; put `K_N=P_N K P_N` as an operator
on `P_N H` and embed its resolvent by zero on the complement:

\[
 R_N(s)=P_N(K_N+sI_{P_NH})^{-1}P_N.
\]

**Theorem.** For every integer `N>=1` and real `s>=0`,

\[
\boxed{
 \|(K+s)^{-1}-R_N(s)\|
 \le \frac{(1-b/(c+s))^{-2}}{\log(N+1)+c+s}.
}
\]

Thus the authentic finite source prefixes converge in **operator norm at the
resolvent level**, even though certain compressed source identities have
operator-norm-one horizon defects.

**Proof.** Let `R_{0,N}=P_N R_0 P_N`. Because `P_N` commutes with `D`,
`(I+R_{0,N}T)^-1 R_{0,N}` has range `P_N H` and is exactly `R_N(s)`: projecting its
linear equation gives `(K_N+s)x=P_N y`. Both Neumann inverses have norm at most
`(1-b/(c+s))^-1`. Multiplication verifies the identity

\[
 (K+s)^{-1}-R_N(s)
 =(I+R_0T)^{-1}(R_0-R_{0,N})(I+TR_{0,N})^{-1}.
\]

Finally `||R_0-R_{0,N}||=(log(N+1)+c+s)^-1`. QED.

**Sharper one-port bound.** For the scalar `m_N(s)=<e_1,R_N(s)e_1>`,

\[
\boxed{
 0\le m(s)-m_N(s)
 \le\frac{b^2}{(s+\delta)^2(\log(N+1)+s+\delta)}.
}
\]

**Proof.** Decompose `K+s` into `P_N` and `Q_N=I-P_N` blocks `A,B;B*,E`.
The exterior block is self-adjoint on the restricted diagonal domain and has
`E>=log(N+1)+s+delta`; the off-diagonal block has norm at most `b` because the
unbounded diagonal has no cross block. Schur elimination gives
`P_N(K+s)^-1P_N=(A-B E^-1 B*)^-1`. Its difference from `A^-1` is positive;
the inverse identity bounds its norm by
`(s+delta)^-2 ||B E^-1 B*||`. This yields the displayed estimate. The Schur
identity follows directly by solving the two block equations, so no bounded
interior-domain assumption is hidden. QED.

**Independent prime horizon.** Define `K^(P)` by retaining genuine primes
`p<=P` and keeping the same `c`. For integer `P>=1`,

\[
 \|(K+s)^{-1}-(K^{(P)}+s)^{-1}\|
 \le\frac{2P^{1-\sigma}}{(\sigma-1)(s+\delta)^2}.
\]

This is the second resolvent identity and the integral tail bound for integers
strictly greater than the integer cutoff. The integer restriction is essential:
for a real cutoff just below 2 and large sigma, the remaining prime 2 can exceed
the proposed integral bound; a real cutoff must use its floor instead. In the exact
finite matrix `K_N`, every prime `p>N` is already absent because it has no pair
`n,pn<=N`; therefore its exact construction needs no infinite prime enumeration.
The source-prefix and prime-tail limits both have explicit budgets. The bounds
are conservative, not an assertion that the slow logarithmic estimate is optimal.

## ARITH-3. All source return moments exist; the first jets retain channel identity

`e_1` belongs to every power domain of `K`. To see this without assuming a bounded
Hamiltonian, use the common smooth space
`D_infty=intersection_{r>=0} D((1+D)^r)`. On its weighted seminorms, `S` and `S*`
are bounded by constants depending on `r`; `V_p` costs at most
`(1+log p)^r`, while `V_p*` decreases the weight. The series
`sum_p p^-sigma(1+log p)^r` converges for every fixed `r`. Hence `T` maps
`D_infty` to itself, `D` does also, and the assertion follows by induction.
This validates every `mu_k=<e_1,K^k e_1>` as a finite mathematical moment.

Write `a_p=p^-sigma`, `b_2=lambda+a_2`, `b_p=a_p` for odd primes, and

\[
 q=\lambda^2+2\lambda 2^{-\sigma}+\sum_p p^{-2\sigma}.
\]

Then

\[
\boxed{\mu_1=c,\quad \mu_2=c^2+q,}
\]
\[
\boxed{
 \mu_3=c^3+3cq+(\lambda+2^{-\sigma})^2\log2
 +\sum_{p>2}p^{-2\sigma}\log p
 +2\lambda(\lambda+2^{-\sigma})3^{-\sigma}.
}
\]

**Proof.** `K e_1=c e_1+w`, with `w=sum_p b_p e_p`. Thus
`mu_2=c²+||w||²`. Expanding the third moment gives
`c³+3c||w||²+<w,Dw>+<w,Tw>`. Distinct prime labels have no multiplicative edge
between them. The only adjacent pair of primes is `(2,3)`, accounting for the
last cross term. Every series converges absolutely. QED.

The `2 lambda 2^-sigma` term is a source collision: `S` and `V_2` both carry the
boundary source `1` to `2`. Summing amplitudes is required; overwriting one
channel or adding squared amplitudes without the cross term is incorrect. This
is an actual source-sensitive return calculation, not a chosen toy spectrum.

**Fake primitive control.** Fix any composite `q>=4` and nonzero real `eta`, and
compare `K` to `K+eta(V_q+V_q*)` with one common shift sufficiently large for both.
The first moment agrees, while the second moment increases by exactly `eta²`,
since `e_q` is orthogonal to all genuine prime boundary targets. The affine
identity `V_q S=S^q V_q` nevertheless holds for this composite. It therefore
cannot authenticate a generator's claim to be a *primitive prime*. The direct
composite injection is detected by this particular boundary test. This does not
prove that every counterfeit, with arbitrary retuning of other coefficients, is
separated by `mu_2`.

## ARITH-4. Scalar cyclicity versus source-controlled tomography

For a self-adjoint compact-resolvent operator, `e_1` is spectrally cyclic iff every
eigenspace is one-dimensional and its projection of `e_1` is nonzero. Indeed the
spectral subspace generated by `e_1` intersects each eigenspace in at most the
line spanned by that projection, and the spectral projections exhaust `H`.
**We have not established these two properties for the full `K_(lambda,sigma)`
family.** Connected nonzero off-diagonal entries alone do not prove them; the
connected antisymmetric-mode example in PR #243 remains a valid warning.
Polynomial Krylov cyclicity can require additional moment-determinacy/density
work for an unbounded operator and is not silently substituted for spectral
cyclicity here.

**Final-round refinement:** [GAC-1](REALITY_PIN_GENERIC_ARITHMETIC_CYCLICITY.md)
now proves spectral cyclicity for each fixed nonzero lambda and every sigma>1
outside an at-most-countable exceptional set. This does not certify sigma=2,
lambda=0, polynomial density, or uniform spectral visibility. The full-family
assertion above remains unresolved; the generic result has analytic paper-proof
authority and is not inferred from the finite moment tests.

There is, however, a complete source-labelled alternative that does not assume
scalar cyclicity.

**Controlled-response theorem.** Suppose an observer may prepare every
`S^j e_1=e_(j+1)` and obtain every complex matrix element

\[
 R_{ij}(s)=\langle S^i e_1,(K+s)^{-1}S^j e_1\rangle,
 \qquad i,j\ge0,
\]

at one known `s>=0`. Then these data determine the self-adjoint operator `K`, its
domain and all source-labelled matrix coefficients uniquely in the fixed source
basis. Gauge freedom consists only of simultaneous changes of representation
that preserve all source preparations and readouts; such a unitary is the
identity on the dense basis span.

**Proof.** The matrix elements determine the bounded resolvent on the dense
finite span, hence everywhere by continuity. Its injective inverse has domain
its range, which is exactly `D(K)`, and `K=R(s)^-1-sI`. A source-preserving unitary
fixes every `S^j e_1`, hence the whole Hilbert space. QED.

If only diagonal readings are available, coherent superposition preparations and
polarization are an additional assumption, not a free capability: real and
imaginary off-diagonal elements require the `(e_i+e_j)` and `(e_i+i e_j)`
experiments with their calibrated normalization. Finite `i,j` access only yields
partial information; the uniform source-horizon bound supplies the stated limit
under the declared model. No real experiment is asserted.

This separates three geometries: the unlabelled scalar spectral quotient; the
source-labelled action graph; and any physical geometry. `S^(n-1)` already
reaches every basis label. Prime words shorten some routes and satisfy the
actual `V_p S=S^p V_p` relation, but that word metric is a cost of permitted
source operations, not a physical proper distance. Source-labelled access is a
strictly stronger probe language than one passive scalar response.

## ARITH-5. Reciprocal horizon defects coexist with resolvent convergence

The inherited full-space law is `V_p* S^p=S V_p*`. In the prefix source, with
`S_N=P_N S P_N` and `V_(p,N)=P_N V_p P_N`, for `N>=p` one obtains

\[
 V_{p,N}^* S_N^p-S_N V_{p,N}^*
 =-|\lfloor N/p\rfloor+1\rangle\langle p\lfloor N/p\rfloor|.
\]

**Proof.** On a basis vector `e_n`, both terms vanish unless `p|n`. Away from the
largest multiple `p floor(N/p)`, both allowed paths reach `e_(n/p+1)`. At that
largest multiple, the forward `p`-shift exits the source prefix and is discarded,
while division followed by one successor remains inside. This leaves precisely
the displayed negative rank-one channel. QED.

Its norm is one for every `N>=p`, but its source input moves to infinity; it tends
strongly to zero. This is **not** a contradiction with ARITH-2: multiplication by
the resolvent suppresses high source energy, while an unsmoothed source-action
identity retains the sharp exit amplitude. Horizon preservation must specify the
topology and observable, rather than declaring all truncations coherent.

## ARITH-6. The old arithmetic Gibbs state is not equilibrium for the new operator

Let `rho_beta=diag(n^-beta/zeta(beta))`, `beta>1`, be the inherited `H_0` Gibbs
state. It does **not** commute with this interacting `K`, for any real `lambda`:

\[
 [K,\rho_\beta]_{1,3}
 =3^{-\sigma}\frac{3^{-\beta}-1}{\zeta(\beta)}\ne0.
\]

This follows from the source edge `(1,3)`; neither `S` nor a diagonal shift
contributes there. Thus preserving the Gibbs **threshold** `beta=1` does not
preserve the Gibbs **state**, old thermofield double, or old prime mirror factor
under a change of dynamics. Use `K` as an observable while retaining `H_0` as
modular dynamics, or construct the new Gibbs state `exp(-beta K)/Tr(exp(-beta K))`
and derive its mirror anew. The companion quantum analysis develops the latter
boundary. No KMS or signed Weil conclusion follows from ordinary positivity.

## Exact evaluator, controls and authority

`observational_succ/reality_pin_arithmetic.py` implements `sigma` restricted to
integers at least two and exact rational `lambda,s`; the universal paper theorem
allows real `sigma>1`. It evaluates the true logarithm by a rational enclosure,
not a floating-point substitution. After range reduction, for `z=(x-1)/(x+1)`:

\[
 2\sum_{j=0}^{L-1}\frac{z^{2j+1}}{2j+1}
 \le\log x\le
 2\sum_{j=0}^{L-1}\frac{z^{2j+1}}{2j+1}
 +\frac{2z^{2L+1}}{(2L+1)(1-z^2)}.
\]

The upper bound follows by bounding every remaining denominator below by
`2L+1` and summing a geometric series. Hence diagonal lower and upper matrices
sandwich `K_N` in Loewner order. Their inverse entries bound `m_N`, and the
proved horizon tail bounds the **infinite** `m`. Exact matrix inversion is an
independent oracle for the moment formulas; it is not proof by numerical fit.
The bound can be wide for small `N`; no practical identifiability is claimed from
a wide enclosure.

Controls preserve channel collisions, the fake composite, wrong primitive
passport, incorrect affine prime test, reciprocal horizon rank, negative Laplace
parameters, floating inputs, interval precision refinement, source-prefix
comparison, and the nonstationary old Gibbs state. The controlled tomography
finite inverse test validates matrix algebra only, not access to physical
superposition preparations.

**Remaining missing theorem:** certify a specified source such as (lambda,sigma)
=(1,2), classify GAC-1's exceptional set, or produce an explicit genuine dark
eigensector. The lambda=0 case remains separate. Establish the full-family result with
quantitative spectral weights if stable passive identification is wanted. A
separate missing contact is a physical source whose permitted interventions and
calibrated response realize these operators. Neither gap is filled by selecting
attractive constants or by the already-proved analytic existence theorem.
