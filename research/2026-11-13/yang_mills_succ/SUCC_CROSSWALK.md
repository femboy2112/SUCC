# Yang–Mills and SUCC: source, observable and dynamics crosswalk

**Research date:** 2026-11-13. **SUCC baseline:** Main XXV,
`db9fb4b84672050efa79b13377f1e73364598a14`.

**Status:** repository audit, classical reconstruction interface, elementary
operator counterexample, and 65 reproduced finite implementation tests. This
document neither reproduces the full external Yang–Mills proof nor establishes
a Yang–Mills mass gap, π normality, RH or Goldbach. No mathematical priority
claim is made. The external result's status and formal verification evidence
require their own source audit; this document addresses the SUCC side.

## 1. The strongest faithful research question

Can SUCC express the authenticated finite observables, gauge identifications,
positive states and limiting operations used in a four-dimensional Yang–Mills
construction, preserving enough structure to reproduce a specific theorem?
Can a separately identified estimate from that construction then apply to an
actual arithmetic SUCC operator?

The first question has a concrete algebraic interface. The second requires an
additional mathematical bridge. A Hilbert-space encoding, noncommuting pair of
operators, positive covariance, or existence of a continuum object does not by
itself imply the source-selected signed estimate in the current π program.
These are distinct dependency edges, not an argument that such a bridge is
impossible.

The maintained baseline is
[Main XXV π frontier](https://github.com/femboy2112/SUCC/blob/db9fb4b84672050efa79b13377f1e73364598a14/docs/PI_NORMALITY_FRONTIER.md).
It retains the exact source

\[
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},
\qquad U_0=0,\qquad U_n=16U_{n-1}+r(n),
\]

and the completed orbit

\[
Y_n=U_n+T_n=16^n(\pi/16).
\]

Source authentication and source-to-orbit transport are established interfaces.
The all-scale selected signed statistical estimate remains **OPEN**.

## 2. Actual reusable machinery and its boundaries

All local paths in this table refer to the pinned Main XXV baseline.

| Existing source | What it actually supplies | What remains to apply it to Yang–Mills |
|---|---|---|
| [holonomy_proof_transport.py](../../../observational_succ/holonomy_proof_transport.py) and [tests](../../../tests/test_holonomy_proof_transport.py) | Exact finite `GL(2,F2)` oriented transports. A path-blind target descends exactly when it is invariant under the declared relative holonomy. | An actual gauge group, lattice source, state, observable algebra and limit construction. The finite model is not a physical curvature measurement. |
| [Local-to-global gluing, LG4](../../2026-10-12/LOCAL_GLOBAL_YONEDA_GLUE_2026-10-12.md) and [nonabelian_local_global.py](../../../observational_succ/nonabelian_local_global.py) | For any group, connected local torsor sections glue iff the ordered overlap-cycle products are identity. An exact `S3` commutator is invisible to its sign character. | This is flat-section gluing. Yang–Mills integrates over nonflat configurations too; making every plaquette flat would change the intended model. |
| [Arithmetic thermofield foundations, A1–A5](../../2026-10-22/ARITHMETIC_ER_EPR_FOUNDATIONS.md) and [arithmetic_tfd.py](../../../observational_succ/arithmetic_tfd.py) | Paper construction of arithmetic shifts, prime multiplication, a Gibbs purification for beta greater than one, a cyclic/separating state and explicit modular operators. | The dossier explicitly constructs a type-I representation. It supplies no verified identification with a Yang–Mills local observable net, Wilson origin, four-dimensional locality or physical time translations. |
| [weil_gns_gate.py](../../../observational_succ/weil_gns_gate.py) and [tests](../../../tests/test_weil_gns_gate.py) | Exact rational principal-minor checks for declared finite symmetric forms, including positive, indefinite and unobserved-negative-direction controls. | Identification with the required complete source form and positivity on its entire domain. A generic auxiliary positive form is not the signed Weil form or a Yang–Mills reflection form. |
| [Infinite-qubit next target](../../2026-11-05/infinite_qubit_field/NEXT.md) and [cluster/GHZ tests](../../../tests/test_infinite_qubit_source_cluster.py) | Source-labelled quasilocal graph-state constructions and finite controls. The dossier explicitly identifies the unchanged signed Weyl obligation. | A source-derived chronological dynamical estimate. Encoding a phase into a state does not prove that its time average cancels. |
| [Fourier–Yoneda pinbed theorems](../../2026-11-07/fourier_yoneda_pinbed/THEOREMS.md) | A complete Bernoulli observable surface for circle probability laws, an explicit distributional inverse, and exact affine intertwining. | Statistical approach to Haar for the authenticated orbit. Completeness of an observable representation is not decay of its response. |
| [Carrier/Tate/Weil audit](../../2026-10-15/RH_CARRIER_TATE_WEIL_FUNCTOR.md) | Separates expression of a target, its computable specification, analytic realization, and proof-sufficient positivity. | A new identification or positivity theorem must be supplied at the relevant edge; the names of the carrier objects do not supply it. |

The circle-valued BBP characters form an abelian arithmetic observable family.
That family alone does not instantiate a compact nonabelian simple gauge group,
a four-dimensional Wilson plaquette law, a running coupling, or the hypotheses
of an Osterwalder–Schrader reconstruction. The presence of noncommuting SUCC/FUCC
operators does not establish these additional structures.

Conversely, nothing prevents SUCC from defining a new source-indexed model of
the external lattice construction. Such a model must preserve the actual
source law and quantify its own analytic limits. Its provenance must distinguish
imported Yang–Mills theorems from newly proved adapter statements.

## 3. Current gauge corrections must be preserved

The following are **unmerged sibling research inputs**, read at exact commits.
They are not silently imported into Main XXV.

- [PR #611](https://github.com/femboy2112/SUCC/pull/611), commit
  `7306e766c0bc212af1d93bb349358bebb579ff42`:
  [lag completeness](https://github.com/femboy2112/SUCC/blob/7306e766c0bc212af1d93bb349358bebb579ff42/research/2026-11-13/joint_time_lag_response/LAG_COMPLETENESS.md)
  and
  [anchored inverse stability](https://github.com/femboy2112/SUCC/blob/7306e766c0bc212af1d93bb349358bebb579ff42/research/2026-11-13/joint_time_lag_response/INVERSE_STABILITY.md).
- [PR #612](https://github.com/femboy2112/SUCC/pull/612), commit
  `2128708b14d45493a2a8e48d967b098299b2556d`:
  [gauge-complete normality dossier](https://github.com/femboy2112/SUCC/blob/2128708b14d45493a2a8e48d967b098299b2556d/research/2026-11-13/gauge_complete_normality/README.md).

### 3.1 Complete relative observations can characterize normality

Let \(T(x)=16x\bmod1\), let \(\lambda\) be Haar probability on the circle,
and fix **one** integer lag \(\ell\ge1\). Define full-shell lag laws

\[
\nu^Y_{B,\ell}=\frac1B\sum_{n=B}^{2B-1}
\delta_{\{Y_{n+\ell}-Y_n\}},\qquad
\nu^U_{B,\ell}=\frac1B\sum_{n=B}^{2B-1}
\delta_{\{U_{n+\ell}-U_n\}}.
\]

The observations include states through \(2B-1+\ell\); they are not
zero-padded truncated autocorrelations. Exactly,

\[
Y_{n+\ell}-Y_n=(16^\ell-1)Y_n.
\]

JTLC-01 proves that if a \(T\)-invariant probability \(\mu\) has
\(q_*\mu=\lambda\) for a nonzero integer \(q\), then \(\mu=\lambda\).
One proof first obtains \(\mu\le |q|\lambda\), then combines Fourier decay
of its \(L^1\) density with invariance. The invariance hypothesis matters.

Combining this with the characteristic Bernoulli pinbed gives GCN-01:

\[
\pi\text{ is base-16 normal}
\quad\Longleftrightarrow\quad
E(\nu^U_{B,\ell})\longrightarrow0
\]

for each fixed \(\ell\ge1\), where

\[
E(\nu)=\|B_2*\nu\|_{L^2(\mathbb T)}^2
=\sum_{h\ne0}\frac{|\widehat\nu(h)|^2}{4\pi^4h^4}.
\]

This is a complete target-equivalent observer, not a proof of its limiting
condition for π. It retains every nonzero Fourier mode with a summable weight.
By contrast, JTLC-03 constructs a singular invariant digit law supported on
\(\{0,8\}\) for which every odd Fourier mode, and hence every fixed-lag
correlation at every odd mode, vanishes while
\(\operatorname{Re}\widehat\mu(2)>9/10\). That is a precise negative control
against promoting a first-mode lag instrument to a normality oracle.

### 3.2 Source completion is uniformly controllable without imposing decay

The positive decreasing BBP tail satisfies
\(0<T_n<1/(64n^2)\) for \(n\ge1\). GCN-02 derives, for all integers
\(B,\ell\ge1\),

\[
\left|\sqrt{E(\nu^Y_{B,\ell})}
-\sqrt{E(\nu^U_{B,\ell})}\right|
<\frac1{64\sqrt3\,B^2}.
\]

The bound is uniform even for moving lags. It transports a response; it does
not require that every moving-lag response vanish. Normal radix orbits can
have moving lags with correlations approaching one. A failed stronger
moving-lag maximum condition is therefore not a refutation of normality.

### 3.3 Legal gauges and source identity answer different questions

For \(s=j/15\), the same-forcing seed change obeys

\[
U_n(s)=U_n(0)+16^ns,\qquad 16^ns=s\pmod1.
\]

All lag records and the normality truth value survive this constant orbit
translation. The literal identity \(U_0=0\) does not survive a nonzero
representative change. Thus a complete normality instrument need not identify
the original representative; authenticating that representative requires its
separate source pin.

Arbitrary sample-dependent rephasing is a different operation. It can map a
constant sequence to an evenly spaced finite grid without preserving the
declared dynamics. It is not justified by calling it a gauge. An admissible
frame change requires a defined connection, lawful transition transport and
proof that the particular target descends.

The Yang–Mills comparison should preserve this correction: gauge-invariant
observables need not recover every gauge representative. They do need to
separate the target-relevant classes and retain the correct source state.

## 4. A concrete source-bound GNS adapter

This is a classical interface theorem, proposed here as a precise reproduction
contract. It is not presently an identification between BBP arithmetic and
Yang–Mills dynamics.

Let \(A,B\) be unital \(*\)-algebras with positive normalized states
\(\omega_A,\omega_B\). Let \(\Phi:A\to B\) be a unital
\(*\)-homomorphism satisfying

\[
\omega_A=\omega_B\circ\Phi.
\]

The map on GNS classes

\[
V[a]_A=[\Phi(a)]_B
\]

is well defined and isometric, because

\[
\|V[a]_A\|^2
=\omega_B(\Phi(a)^*\Phi(a))
=\omega_A(a^*a)
=\|[a]_A\|^2.
\]

Its extension is unitary onto the closure of
\(\pi_B(\Phi(A))\Omega_B\). Surjectivity onto the full target Hilbert
space additionally requires that this cyclic subspace be dense. The algebra
actions intertwine on their canonical invariant dense domains. For general
\(*\)-algebras those actions may be unbounded; no bounded-operator assertion
is automatic.

To transfer dynamics, require an actual dynamical compatibility condition,
such as

\[
\Phi\circ\alpha_t=\beta_t\circ\Phi,
\]

and the hypotheses needed to implement the two dynamics on the reconstructed
spaces. To transfer a spectral statement, identify the relevant vacuum,
orthogonal complement, time parameter and generator domains. A bounded
semigroup intertwiner is often a cleaner statement to verify than informal
manipulations of unbounded generators.

**What must be reproduced:** source moments, multiplication, adjoint, unit,
null quotient, cyclic closure and the particular dynamics used by the theorem.
Matching a few correlators, matching finite spectra, or embedding both objects
in some Hilbert space is insufficient.

**Calibrated failure cases:** use a changed source state, a map that does not
preserve the adjoint, a proper cyclic subspace, and a representation-compatible
map that fails to intertwine dynamics. Each should reject the corresponding
stronger transfer claim while preserving any weaker valid algebraic statement.

## 5. Arithmetic gap versus doubled dynamics: an exact counterexample

The existing arithmetic thermofield construction has

\[
H_0|n\rangle=\log n\,|n\rangle,
\qquad
\Delta|i,j\rangle=(j/i)^\beta|i,j\rangle
\]

for \(\beta>1\). Its one-copy Hamiltonian has a unique lowest basis state
and first excited eigenvalue \(\log2\). Consider instead the natural
self-adjoint doubled diagonal operator

\[
L=H_0\otimes I-I\otimes H_0,
\qquad
L|i,j\rangle=\log(i/j)|i,j\rangle,
\]

on its maximal square-summability domain. It satisfies
\(\Delta=e^{-\beta L}\) on the basis. Now

\[
L|n+1,n\rangle=\log(1+1/n)|n+1,n\rangle,
\qquad 0<\log(1+1/n)\longrightarrow0,
\]

while \(L|n,n\rangle=0\) for every \(n\). Thus \(L\) has arbitrarily
small positive eigenvalues and an infinite-dimensional zero eigenspace. It
also has negative spectrum by swapping the two indices.

This is an elementary operator counterexample, not a numerical observation.
The one-copy gap and the positive Gibbs/GNS construction do not transfer to a
positive-energy, unique-vacuum, gapped physical time generator. The doubled
operator is not being proposed as the Yang–Mills Hamiltonian; its purpose is
to expose the missing dynamical identification in that proposed inference.

**Provenance:** the one-copy and modular formulas are in A1–A5 of the pinned
[arithmetic thermofield dossier](https://github.com/femboy2112/SUCC/blob/db9fb4b84672050efa79b13377f1e73364598a14/research/2026-10-22/ARITHMETIC_ER_EPR_FOUNDATIONS.md).
The displayed eigenvector calculation is the complete additional argument.
It requires no physical interpretation of arithmetic and proves nothing
against the external Yang–Mills existence construction.

## 6. Useful next dependency cuts

1. **Reconstruction adapter.** Instantiate the GNS contract on a declared
   finite observable-word algebra with an authenticated source state. Extend
   it to a continuum domain only after proving the relevant continuity,
   density and limit hypotheses. This makes a reproduced interface concrete.
2. **Finite nonabelian Wilson slice.** Use ordered edge transports and show
   that closed-loop holonomy transforms by basepoint conjugation, hence class
   functions are invariant. Keep a nonflat positive control. The finite group
   and exact SU(2) versions are useful implementation tests, not a substitute
   for a four-dimensional continuum construction.
3. **A genuinely applicable multiscale estimate.** Identify one specific
   estimate from the external construction and a source-derived arithmetic
   transfer operator satisfying its hypotheses. Test the estimate against the
   same-forcing coherent wrong seed before proposing an original-zero saving.
   Until that operator and those hypotheses are supplied, the resemblance to
   renormalization is a research analogy. The original source-selected signed
   estimate is still the missing arithmetic edge.

These opportunities are complementary. The first two can reproduce useful
mathematics now. The third is the route that could change an arithmetic proof
frontier, and its hypothesis debt must remain visible.

## 7. Reproduced finite baseline checks

The repository-mapping audit ran the following command in the isolated worktree
at Main XXV, with bytecode output disabled:

```sh
PYTHONDONTWRITEBYTECODE=1 python - <<'PY'
import unittest
patterns = [
    'test_weil_gns_gate.py',
    'test_holonomy_proof_transport.py',
    'test_arithmetic_tfd.py',
    'test_fourier_yoneda_pinbed.py',
    'test_bbp_minimal_path_gauge.py',
]
for pattern in patterns:
    suite = unittest.defaultTestLoader.discover('tests', pattern=pattern)
    result = unittest.TextTestRunner(verbosity=1).run(suite)
    print(pattern, 'tests=', result.testsRun,
          'failures=', len(result.failures), 'errors=', len(result.errors))
PY
```

| Existing suite | Tests observed | Failures | Errors |
|---|---:|---:|---:|
| `test_weil_gns_gate.py` | 5 | 0 | 0 |
| `test_holonomy_proof_transport.py` | 8 | 0 | 0 |
| `test_arithmetic_tfd.py` | 14 | 0 | 0 |
| `test_fourier_yoneda_pinbed.py` | 31 | 0 | 0 |
| `test_bbp_minimal_path_gauge.py` | 7 | 0 | 0 |
| **Total** | **65** | **0** | **0** |

The tool returned process exit code zero, and each suite separately reported
`OK`. The displayed runner reports individual failures but does not itself
aggregate them into a nonzero process exit status; the per-suite results,
rather than exit status alone, are the evidence for this receipt. A future
automation should explicitly aggregate `wasSuccessful()` for its exit code.

These checks exercise existing finite implementations. They do not certify
the infinite analytic claims, the sibling branches' full validation, the full
SUCC required gates, or any external Lean proof. The five suites are cheap
canonical controls to rerun when integrating this adapter. They are not five
independent mathematical witnesses: their source dependencies overlap.

## 8. Claim ledger

| Claim | Earned state | Boundary / next discriminator |
|---|---|---|
| Existing SUCC finite transport and positivity implementations pass the five listed suites | **OBSERVED: 65 tests** | Finite code scope only; full integration gates remain separately recorded. |
| A source-preserving unital star map induces the stated GNS isometry | **CLASSICAL / PAPER DERIVATION** | Dense range and dynamical compatibility are separate hypotheses. |
| The arithmetic doubled Liouvillian has no positive gap above zero and has many invariant vectors | **ELEMENTARY PAPER PROOF** | Counterexample to an automatic transfer, not a Yang–Mills conclusion. |
| Fixed-lag complete pinbed criterion characterizes normality | **INHERITED SIBLING PAPER RESULT** | Limit for π is open; sibling references remain pinned and unmerged. |
| Legal relative gauge can preserve normality while losing literal seed identity | **INHERITED EXACT ALGEBRA** | Target descent and source authentication must remain distinct. |
| Yang–Mills existence supplies BBP signed cancellation, RH positivity or a physical mass gap through present SUCC modules | **UNVERIFIED / NO BRIDGE ESTABLISHED** | Supply source-state and dynamics identification plus an applicable quantitative theorem. |
| Full Yang–Mills proof has been replayed through SUCC | **NOT CLAIMED** | Requires the actual external source, pinned toolchain, full checker evidence and theorem-specific adapter. |
