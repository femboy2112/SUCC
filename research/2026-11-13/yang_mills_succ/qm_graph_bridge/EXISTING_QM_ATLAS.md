# Existing SUCC quantum structures: exact adapters and distinct meanings

**Date:** 2026-11-13. **Scope:** bounded read/proof continuation of the
Haar and graph bridges; no new implementation or test claims. Existing source
citations below are pinned to Main XXV
`db9fb4b84672050efa79b13377f1e73364598a14`; the continuation parent is
`3929e30930438881bebcb371646389d9e66bfbde`.

SUCC already contains several genuine mathematical QM representations. Their
useful connection is through exact state, observable and dynamics adapters.
Their shared Hilbert-space language does not identify their physical models.

## 1. What the repository actually represents

| Existing structure | Its mathematical object | Adapter and retained boundary |
|---|---|---|
| [Ω/Haar quantum bridge](https://github.com/femboy2112/SUCC/blob/db9fb4b84672050efa79b13377f1e73364598a14/research/2026-11-10/omega_bbp_operational_completion/quantum_bridge/README.md) | Finite unitary Haar transforms, Hermitian chronology operators, coherent registers and instruments | Full unitary conjugation preserves word expectations; omitted details require an explicit channel or projection |
| [Arithmetic thermofield foundations, A1–A7](https://github.com/femboy2112/SUCC/blob/db9fb4b84672050efa79b13377f1e73364598a14/research/2026-10-22/ARITHMETIC_ER_EPR_FOUNDATIONS.md) | Number-basis Hamiltonian, prime occupation factors, Gibbs purification and type-I modular representation | Exact prime-mode Fock identification below; its state and physical-time candidate remain separately specified |
| [Gaussian source proof, G2–G5](https://github.com/femboy2112/SUCC/blob/db9fb4b84672050efa79b13377f1e73364598a14/research/2026-10-14/SUCC_GAUSSIAN_GLOBAL_CONSTRAINTS.md) | An authentic completed-xi function in an even Bargmann–Fock reproducing-kernel Hilbert space | Exact occupation-coefficient interpretation; no Gaussian probability prior or field-theory dynamics follows |
| [Source Gaussian implementation](https://github.com/femboy2112/SUCC/blob/db9fb4b84672050efa79b13377f1e73364598a14/observational_succ/source_gaussian_fock.py) | Rational Euler-source intervals, Gaussian-kernel envelopes and conditional analytic tail/zero-count certificates | Finite analytic instruments, not a bosonic creation/annihilation simulator |
| [Arithmetic TFD implementation](https://github.com/femboy2112/SUCC/blob/db9fb4b84672050efa79b13377f1e73364598a14/observational_succ/arithmetic_tfd.py) | Exact Gaussian-rational amplitudes, reductions, mirror defects and cutoff leakage | Its `Gaussian` class means \(\mathbb Q(i)\), not a Gaussian quantum state |

## 2. Prime valuations give a literal bosonic Fock representation

Let \(\mathfrak h=\ell^2(\mathcal P)\), with one orthonormal mode
\(e_p\) per prime. The symmetric bosonic Fock space

\[
 \mathcal F_s(\mathfrak h)=\bigoplus_{k\ge0}\operatorname{Sym}^k\mathfrak h
\]

has normalized occupation basis indexed by finitely supported tuples
\((k_p)_{p\in\mathcal P}\) of nonnegative integers. Unique factorization
therefore makes

\[
 J|n\rangle=|(v_p(n))_p\rangle
\]

a unitary basis identification. This is the standard bosonic interpretation
of the vacuum incomplete tensor product already constructed in A4; it
requires no new arithmetic hypothesis.

If \(h e_p=(\log p)e_p\), then

\[
 JH_0J^{-1}=d\Gamma(h),\qquad
 d\Gamma(h)|(k_p)\rangle=\left(\sum_p k_p\log p\right)|(k_p)\rangle.
\]

The maximal diagonal domains agree because the eigenvalue is exactly
\(\log n\). The existing arithmetic partition function is consequently
the free bosonic prime-mode partition function:

\[
 \operatorname{Tr}e^{-\beta d\Gamma(h)}
 =\prod_p(1-p^{-\beta})^{-1}=\zeta(\beta),\qquad\beta>1.
\]

The prime multiplication operator is the **normalized** creator:

\[
 JV_pJ^{-1}=a_p^\dagger(N_p+1)^{-1/2}.
\]

Indeed the right side sends occupation \(k_p\) to \(k_p+1\) with
amplitude one, whereas the raw creator has amplitude \(\sqrt{k_p+1}\).
Confusing these operators changes their commutators and norms. Arithmetic
successor \(n\mapsto n+1\) becomes a nonlocal occupation transformation;
it is not a single bosonic creation operator.

## 3. Which Haar/graph maps lift by second quantization?

**QA-01 — CLASSICAL, proof reproduced.** For a unitary
\(U:\mathfrak h\to\mathfrak k\), define

\[
 \Gamma(U)=\bigoplus_{n\ge0}U^{\otimes_s n},\qquad U^{\otimes_s0}=1.
\]

Each tensor power is unitary, intertwines the permutation actions and thus restricts
unitarily to the symmetric sector. The orthogonal direct sum is unitary,
preserves the vacuum and particle number, and obeys
\(\Gamma(UV)=\Gamma(U)\Gamma(V)\) and
\(\Gamma(U)^*=\Gamma(U^*)\).
On finite-particle vectors, the definition of symmetric insertion gives

\[
 \Gamma(U)a^\dagger(f)\Gamma(U)^*=a^\dagger(Uf).
\]

The annihilation identity follows by adjoints on the corresponding domains.
Likewise \(\Gamma(U)d\Gamma(h)\Gamma(U)^*=d\Gamma(UhU^*)\), with
the generator domain transported. Consequently a source-weighted Haar
unitary, or a graph already proved to denote a one-particle unitary, has
this exact many-particle lift.

An arbitrary unitary on the **integer-state space** need not equal
\(\Gamma(U)\) under the prime occupation identification. For example,
\(\Gamma(U)\) preserves particle number and vacuum. One must declare
whether the original graph acts on one-particle modes or the full state
space. Calling the same Hilbert space a new one-particle space and applying
Fock again defines a different construction.

This lift transports an existing interaction if its Hamiltonian and
observables are also conjugated. A free Hamiltonian remains free under
this mode change. It does not acquire Yang–Mills interactions from a
different choice of basis.

## 4. The analytic Fock source is a different, useful interface

The xi dossier proves, from its theta source,

\[
 F(z)=\xi(\tfrac12+z)=\sum_{j\ge0}a_jz^{2j},\qquad
 \|F\|^2=\sum_{j\ge0}(2j)!|a_j|^2\le260/27.
\]

In the one-mode Bargmann basis \(z^n/\sqrt{n!}\), this is the vector
with amplitudes \(c_{2j}=\sqrt{(2j)!}\,a_j\), \(c_{2j+1}=0\).
The even Bargmann–Fock space has reproducing kernel \(\cosh(z\bar w)\).
This is a literal Hilbert-space
representation of an analytic arithmetic source. The word Gaussian refers
to the Hilbert weight/kernel; it does not assert Wick factorization or
that the vector is a Gaussian vacuum. Creation and annihilation do not
preserve the even subspace individually.

A Haar transform across Taylor coefficients is a unitary on that state
space when the factorial normalization is respected. It is not automatically
the second quantization of a one-mode unitary. Evaluation kernels and source
constraints must be transported too. The source proof's multiplication by
\(e^{-z^2/2}\) preserves the norm in its **transported RKHS**, not by
remaining an isometry in an unchanged Bargmann measure.

## 5. Finite CCR and dynamical boundaries

**QA-02 — exact cutoff obstruction.** Finite matrices cannot satisfy
\([a,a^\dagger]=I\), because the commutator has trace zero. On occupation
levels \(0,\ldots,N\), the standard truncated oscillator instead obeys

\[
 [a_N,a_N^\dagger]=I-(N+1)|N\rangle\langle N|.
\]

Below the top level, the diagonal difference is \((n+1)-n=1\); at
the top it is \(-N\). This is the retained boundary defect, not a
failure of finite-dimensional QM. Number-preserving \(\Gamma(U)\)
still restricts unitarily to a total-particle cutoff; truncated creation
operators must retain their boundary correction.

The existing TFD is a normalized purification only for \(\beta>1\).
Its type-I modular generator differs from physical one-copy time:
\(H_0\) has gap \(\log2\), whereas the doubled generator has
eigenvalues \(\log(i/j)\), arbitrarily small positive values and many
zero vectors ([crosswalk §5](../SUCC_CROSSWALK.md)). State reconstruction,
mode changes and positive kernels do not select which dynamics should be
identified with the Yang–Mills Hamiltonian.

**Verdict:** these adapters establish real quantum mathematical structure
already available in SUCC. An interacting Yang–Mills identification still
requires its source law, full field correlations, reflected reconstruction,
locality and time evolution. A Fock reference presentation may be useful;
the existing arithmetic Gaussian or free prime Gibbs model does not supply
those identifications. This atlas adds paper derivations only. No additional
tests were run while the parent validation gate was executing.
