# SUCC quantum graphs to Yang–Mills: proposed bridge contract

Date: 2026-11-13. Parent: `3929e30930438881bebcb371646389d9e66bfbde`,
the first Yang–Mills research round. This is an additive continuation of PR #613.

## Object and intended result

The user asks whether the existing Haar-wavelet, successor/FUCC, computational
graph and quantum-shaped SUCC structures connect rigorously to the public
Yang–Mills construction. The faithful target is an explicit constructive
presentation of a declared quantum observable system, with maps preserving
states, inner products, observable products and any claimed dynamics.

The task does not assume that a finite graph solves the continuum limit, nor
that physically distinct alternatives are created by duplicating equivalent
lambda syntax. Keep the full state, including detail and history registers,
when declaring a transformation reversible.

## C1: successor/character representation

On the existing positive-integer carrier let `S e_m = e_(m+1)`, `S* e_1 = 0`.
Set `J=(S+S*)/2`. Proposed exact unitary map:

`W e_m = U_(m-1)(x)`, `x=Tr(g)/2`, `g in SU(2)`,

onto the **central** Haar `L2` space, with `W J W* = multiplication by x`.
The normalized Wilson vector is `exp(beta J/2)e_1 / sqrt(Z_beta)`.
Its polynomial expectations should equal the actual one-plaquette Wilson law.

- Initial status: classical representation/spectral facts; proof and source
  audit required in this round.
- Edge: intrinsic successor graph -> actual SU(2) Haar/Wilson state.
- Novelty tax: explicit source-specific assembly and finite error accounting;
  no priority claim for Chebyshev, Peter–Weyl, fusion or spectral theory.
- Cheapest falsifiers: replace the half-line with a bilateral/cyclic carrier;
  omit the vacuum boundary; claim compression preserves products; use `V_p`
  without transporting its one-based indexing.
- Fresh finite probe: independent Haar moment recurrence versus weighted graph
  return counts, every first truncation failure, exact polynomial Wilson states.
- Boundary: the central one-plaquette Hilbert space is not the continuum
  Wightman Hilbert space; J is a trace observable, not the physical Hamiltonian.

## C2: weighted graphs and finite quantum linear algebra

For a declared computable coefficient field, finite layered weighted graphs
should denote matrices by summing products of edge amplitudes. Composition,
tensor product and dagger should commute with denotation. Finite canonical
matrix graphs should supply a complete extensional presentation of the stated
matrix category; claims about a particular finite gate set need separate proof.

- Initial status: classical algebraic semantics; actual existing SUCC adapters
  and calibrated tests are needed.
- Edge: finite constructive syntax -> linear-algebra semantics, with exact
  interference, source state and measurement retained.
- Cheapest falsifiers: square before coherent summation; keep orthogonal path
  records while claiming interference; count beta-equivalent syntax twice;
  call a many-to-one deterministic map unitary.
- Boundary: no representation of every arbitrary complex coefficient by a
  finite exact program; no quantum speedup or physical implementation inferred.

## C3: Haar as a reversible observer coordinate system

For a declared measure mu and binary partition cell masses p,q>0, weighted
Haar analysis should preserve the exact Hilbert metric when both average and
detail are kept. For a Wilson law this constructs a basis of its own GNS
space; conjugated observables and transported state must remain attached.

- Initial status: classical weighted Haar/martingale algebra; exact adaptation
  to the specified source required.
- Edge: existing multiscale signed SUCC observations -> a source-preserving
  quantum representation, compatible with C1 and finite graph semantics.
- Cheapest falsifiers: discard detail, use unweighted Haar for unequal masses,
  retain transformed state but forget transformed observables, assume different
  interacting plaquettes are independent.
- Boundary: nested dense partitions can recover an L2 space, but do not prove
  the Yang–Mills ultraviolet limit, reflection positivity or a mass gap.

## Acceptance and stop conditions

Accept a connection only with its exact map, source, observable domain, proof
and adversarial control. Record the strongest surviving statement and any
unpaid interface. A calibrated finite implementation accompanies the proof;
finite agreement is not the universal proof. Root synthesis must independently
inspect the load-bearing equations and raw execution results. Parallel agents
share a model family and do not constitute blind external peer review.
