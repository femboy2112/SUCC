# Existing SUCC quantum structures meet the Wilson source

**2026-11-13 continuation of [PR #613](https://github.com/femboy2112/SUCC/pull/613).**
Parent: `3929e30930438881bebcb371646389d9e66bfbde`.

## Earned result

There is a literal unitary identification between the existing SUCC successor
carrier and the central SU(2) Haar representation. Under this map, a specified
cyclic vector produces the actual one-plaquette Wilson state. A new terminating
algorithm presents any rational-polynomial Wilson observable by a finite
rational graph state with a proved error budget.

The existing Haar, typed-source and quantum-record structures also have exact
adapters. Full Haar coordinates retain the state and observable representation;
finite amplitude graphs give a constructive presentation of the declared
quantum matrix calculus; prime occupations give a literal bosonic Fock space.

These are proved mathematical representation and approximation results, with
classical attribution. The 4d Yang–Mills continuum construction and physical
mass gap are not reproduced or inferred by these adapters.

## 1. The successor is a nonabelian character-fusion graph

On the existing positive-integer carrier, S e_m=e_(m+1), S*e_1=0. Put

\[
J=(S+S^*)/2,\qquad
W e_m=U_{m-1}(x),\qquad x=\operatorname{Tr}(g)/2.
\]

Here U_n is the SU(2) spin-n/2 character, equivalently a Chebyshev polynomial
of the second kind. Normalized Haar measure induces
dnu=(2/pi)sqrt(1-x²)dx. The characters are a complete orthonormal basis of the
central Haar space, and

\[
WJW^*=M_x,\qquad
U_1U_n=U_{n+1}+U_{n-1},\quad U_{-1}=0.
\]

Thus forward/backward successor paths are exactly the fusion paths for
tensoring with the fundamental representation. In particular,

\[
\langle e_1,J^{2k}e_1\rangle
=\frac{\binom{2k}{k}}{4^k(k+1)},\qquad
\langle e_1,J^{2k+1}e_1\rangle=0.
\]

The same Haar moments obtained by integration in the parent round are now
obtained as weighted Catalan return counts. The lower boundary is structural:
the bilateral shift gives a different law, already distinguished at moment 2.

The established multiplication map also has an explicit representation:

\[
V_p e_m=e_{pm},\qquad
(WV_pW^*f)(x)=U_{p-1}(x)f(T_p(x)),
\qquad V_pJ=T_p(J)V_p.
\]

Here T_p is the first-kind Chebyshev polynomial. The weight makes this an
isometry on the full central Haar L2 space; bare composition need not even
map that space into itself. For p=2 the formula is 2x f(2x²-1). Thus both
successor and integer multiplication have concrete SU(2) character semantics.
The formula holds for composites as well as primes. Section 1.1 of the
[proof](SUCC_CHARACTER_PROOF.md) establishes the domains and adjoint; the
probe records 56 exact polynomial identities and 56 norm checks.

## 2. The Wilson source becomes a constructible graph state

For real beta, take

\[
\psi_\beta=
\frac{e^{\beta J/2}e_1}{\sqrt{\langle e_1,e^{\beta J}e_1\rangle}}.
\]

Its polynomial readings are the normalized Wilson expectations:

\[
\langle\psi_\beta,f(J)\psi_\beta\rangle
=\frac{\int f(x)e^{\beta x}\,d\nu(x)}{\int e^{\beta x}\,d\nu(x)}.
\]

The native action is 1-x; the constant exponential factor cancels. This
preserves the source, inner product and observable products. It does not assert
that an already prepared BBP or TFD vector is this Wilson vector.

### Finite constructive theorem

Given rational beta, a rational polynomial f of degree d, and rational
epsilon>0, use the finite Taylor-amplitude ray

\[
v_K=\sum_{j=0}^K\frac{(\beta J/2)^j}{j!}e_1.
\]

Its coefficients and normalized density matrix are rational. Set a=|beta|/2
and M=sum of the absolute polynomial coefficients. The normalized expectation
error is at most

\[
E_K=4M\,3^{\lceil a\rceil}\frac{a^{K+1}}{(K+1)!}.
\]

Choose K until E_K<=epsilon, which terminates, then use the graph on indices
0,...,N with N=K+floor(d/2). The exact moment-degree theorem proves that this
finite graph evaluates the Taylor-state numerator and denominator without a
hidden truncation error. The normalization is positive for every real beta
and every K.

**Executed example:** beta=3/2, f(x)=x, requested error 10^(-12).
The algorithm selects K=N=14, a **15-vertex graph**, and returns

\[
\text{expectation}=0.34414400706876060084346664701262\ldots,
\]

with exact rational error budget

\[
\frac{59049}{481517373489152000}
<1.227\times10^{-13}.
\]

The exact rational expectation is in [the receipt](probe_receipt.json).
The displayed decimal is a rounded readout, not the proof certificate.

Proof and algorithm contract: [SUCC_CHARACTER_PROOF.md](SUCC_CHARACTER_PROOF.md).

## 3. Computational graphs and ordinary QM linear algebra

The graph adapter reuses the repository's exact Gaussian-rational scalar type
and compiles its actual source_lambda and quantum_records maps. For a finite
layered graph, an input/output matrix element is the sum of the products of
edge amplitudes over all connecting paths. Matrix multiplication is graph
composition; tensor and dagger commute with this interpretation.

Every nonempty finite matrix over Q(i) has a canonical bipartite graph.
Quotienting graphs by exact denotation gives a constructive presentation of
the matrix category in positive finite dimensions. This is the precise sense
in which the finite graph and linear-algebra viewpoints represent the same
quantum calculation. It is not a claim that arbitrary recursive lambda syntax
is automatically a unitary circuit, or that a complete local rewrite calculus
has been proved.

Concrete existing adapters establish:

- Cyclic residue successor is unitary.
- Multiplication by p modulo m is unitary exactly when gcd(p,m)=1.
- A noninjective deterministic map has a reversible oracle lift when its
  original source register is retained.
- Existing exact X/Z measurement instruments compile to record-retaining
  isometries with identical Born probabilities and partial traces.

Coherent alternatives add before taking squared modulus. Distinguishable
recorded alternatives have different statistics. Beta-equivalent source
presentations cannot be counted as new physical alternatives without a
specified amplitude rule. The exact implementation uses Q(i); normalized
Hadamard entries require an algebraic extension or the weighted Haar
coordinates below. No arbitrary-complex-coefficient oracle is supplied.

Full source map and proofs: [GRAPH_QM_SEMANTICS.md](GRAPH_QM_SEMANTICS.md).

## 4. Haar is a reversible coordinate system when the source is retained

For cell masses p,q>0, the exact weighted Haar split is

\[
m=(pf_0+qf_1)/(p+q),\qquad d=f_0-f_1,
\]

\[
p|f_0|^2+q|f_1|^2=(p+q)|m|^2+\frac{pq}{p+q}|d|^2.
\]

It is a unitary in normalized amplitude coordinates. With rational weights,
the coefficients and metric can instead be retained exactly without square
roots. Applied recursively, it gives the existing complete Haar tree.

For a specified fixed-cutoff Wilson measure mu, its GNS realization is
L2(mu), cyclic vector 1, multiplication observables. Generating partitions and
all retained wavelet details reconstruct this same L2 space. The source law
sets the cell masses; shared plaquette couplings are retained. Full unitary
transport preserves every word expectation when the state **and** operators
are transported. Reflection additionally needs its positive-time domain and
reflection operator carried through the same map.

Two exact controls show why this is substantive. Uniform and biased finite
Wilson sources have the same adapted cyclic-vector coordinates (1,0), but
their transported plaquette operators retain expectations 0 and 3/5. Separately,
the two-vertex Wilson approximation has trace expectation 4/17; applying the
existing Z-measurement and discarding its record changes that expectation to 0.
Complete Haar transport preserves it. Normalization or positivity alone
would miss those source changes.

Proofs, finite-partition limits and controls:
[HAAR_SOURCE_BRIDGE.md](HAAR_SOURCE_BRIDGE.md).

## 5. Existing Fock and thermofield structures also connect

Unique factorization identifies the integer basis with the occupation basis
of bosonic Fock space over one-particle prime modes. The existing log-number
Hamiltonian is dGamma(log p), and V_p is the normalized creator
a_p^dagger(N_p+1)^(-1/2). The familiar zeta Gibbs partition is literally the
free prime-mode partition function for beta>1.

A one-particle Haar or graph unitary lifts by Gamma(U) to Fock space with
creation/annihilation relations and transported dynamics preserved. An
arbitrary Haar transform on integer states need not be such a lift. The
existing analytic xi Bargmann–Fock construction has a different source and
operator interpretation. [EXISTING_QM_ATLAS.md](EXISTING_QM_ATLAS.md) gives the
exact identifications, coefficient normalization, finite CCR boundary and
the distinction between one-copy, modular and Yang–Mills physical time.

## 6. What extends to the 4d construction, and what remains to instantiate

For a finite lattice, Peter–Weyl acts on every link. Gauge constraints require
vertex invariant tensors; a spin network records those representation labels
and tensors. Supplying the square root of the actual Wilson density gives the
source vector. Plaquette expansion and Haar integration lead to the standard
spin-foam form, with its convergent representation sums and conventions.

A finite number of SU(2) links still has a continuous configuration space and
an infinite-dimensional L2 space. A finite representation cutoff therefore
needs its own error control. The 4d continuum endpoint additionally requires
the upstream regulated fields, reflection/test domains, source family,
renormalization and uniform limit estimates. The new bridge does not replace
those estimates or turn a free arithmetic model into interacting Yang–Mills.

[QM_YM_INTERFACE.md](QM_YM_INTERFACE.md) supplies primary sources, the pinned
native action match, nonabelian link/vertex details and exact falsifiers.

## 7. Reproduction and evidence

```sh
PYTHONPATH=. python -m unittest discover -s tests -p 'test_ym_*.py' -v
python scripts/yang_mills_qm_bridge_probe.py
```

The complete Yang–Mills-focused set contains **76 passing tests**: the prior
36 plus 40 new tests, including three tests joining graph, Wilson, Haar and
existing measurement code. The paper proofs establish the universal claims;
the exact tests calibrate their implementations and boundary mutations.

The full repository suite passed **13,126 tests** with the project root on
`PYTHONPATH`. Provenance, observer-foundations and ordinal gates also passed.
The first round's original import-error run remains preserved as historical
evidence; this is the complete rerun with its diagnosed environment precondition.

See [VALIDATION.md](VALIDATION.md), [CLAIM_LEDGER.md](CLAIM_LEDGER.md),
[SOURCE_MANIFEST.json](SOURCE_MANIFEST.json) and the original
[hole contract](HOLE_CONTRACT.md). Same-family agent agreement is not counted
as blind peer review. No new Lean or full upstream Comparator replay is claimed.
