# Dirac-comb SUCC → Gamma: continuum transport and unavoidable aliases

**Source:** user's infinitesimal-Dirac-delta SUCC-sum/integral → continuum-time proposal.
**Branch:** research/dirac-comb-gamma-continuum-2026-10-16, from main 02fc9f46ad3b914d49df7a658e304d06ed8a6200.
**Status:** CLASSICAL mathematics with source-indexed reconstruction, PROVED PAPER derivations and exact arithmetic controls; independent finite numerical calibration. **RH PROVED: NO.**

## Object and provenance

A two-sided log-clock has translations S_h(u)=u+h on hZ, with rational h>0, and event measure

$$\mu_h=h\sum_{n\in\mathbb Z}\delta_{nh}.$$

The h is a necessary density normalization. This is a group-completed two-sided carrier, not a claim that a finite observer actualizes infinitely many events. It complements existing SUCC factorial/Gamma approximants and Tate/Poisson work; no imported source was modified. Mathematical operations are distinct from claims about physical time, Archimedean ontology or prime-source emergence.

The target is the **actual real-place Tate factor**

$$\Gamma_{\mathbb R}(s)=\pi^{-s/2}\Gamma(s/2),$$

including its pi normalization, half exponent and pole parity.

## DGC-1: a normalized Dirac-comb weak limit (CLASSICAL, proved)

For every compactly supported continuously differentiable f,

$$\langle\mu_h,f\rangle=h\sum_{n\in\mathbb Z}f(nh)
\longrightarrow\int_{\mathbb R}f(u)\,du$$

as h tends to zero through positive rational values. More quantitatively,

$$\left|h\sum_n f(nh)-\int_{\mathbb R}f(u)\,du\right|
\le h\int_{\mathbb R}|f'(u)|\,du.$$

The cellwise proof compares h f(nh) with the integral over [nh,(n+1)h]; their difference is at most h times the cell integral of |f'|. Summing yields the bound. Appropriate summability assumptions extend this to W^{1,1} representatives; it is not pointwise convergence of deltas.

**Exact rational control.** For f(u)=(1-u²)² on [-1,1], zero otherwise, integral=16/15 and total variation=2. Direct finite rational arithmetic gives, for h=1/q,

$$h\sum_n f(nh)=\frac{16}{15}-\frac{1}{15q^4}.$$

The exact O(h^4) error is a special polynomial quadrature identity, stronger than the generic O(h) bound; it is not a universal rate. Without the h prefactor the positive event sum diverges as h decreases. A one-sided clock is not an acceptable replacement for the entire real-line measure.

On smooth translation test functions, the finite-difference quotient (S_h-I)/h tends to the derivative in the stated topology; a full operator-generator claim must name its function space and generator domain.

## DGC-2: the completed real-place factor arises by weighting the clock

For Re(s)>0, define two **absolutely convergent** infinite sampled sums:

$$G_h(s)=h\sum_{n\in\mathbb Z}\exp(snh-e^{nh}),$$

$$R_h(s)=h\sum_{n\in\mathbb Z}\exp\left(\frac{snh}{2}-\pi e^{nh}\right).$$

Set x=e^u in Euler's integral. Then the weak sampling limit yields

$$G_h(s)\to\Gamma(s),\qquad
R_h(s)\to\pi^{-s/2}\Gamma(s/2)=\Gamma_{\mathbb R}(s).$$

For the general kernel f(u)=exp(zu-ae^u), a>0 and sigma=Re(z)>0, the DGC-1 derivative estimate yields the explicit analytic bound

$$\left|h\sum_n f(nh)-a^{-z}\Gamma(z)\right|
\le h\,a^{-\sigma}\bigl(|z|\Gamma(\sigma)+\Gamma(\sigma+1)\bigr).$$

Proof: |f'|≤(|z|+a exp(u))exp(sigma u-a exp(u)); each integral is an Euler Gamma integral. Gamma corresponds to (z,a)=(s,1), and Gamma_R to (s/2,pi).

For finite retained indices L≤n≤R, define u=(R+1)h and r=exp(sigma h-a(exp(h)-1)exp(u)). The omitted left tail has upper bound

$$\frac{h\exp(\sigma(L-1)h)}{1-\exp(-\sigma h)},$$

and, provided r<1, the right tail has upper bound

$$\frac{h\exp(\sigma u-ae^u)}{1-r}.$$

These bounds are theorems, but ordinary mpmath evaluations of the bounds are **not directed-rounding certificates**. RH-sign claims need independently certified enclosures.

## DGC-3: exact Poisson replicas and failure of all-height uniformity

Take the Fourier convention F(omega)=integral f(u)exp(-i omega u)du. Then the transform of exp(zu-a exp(u)) is a^{-z+i omega}Gamma(z-i omega). Poisson summation therefore gives exact periodizations, on Re(s)>0:

$$G_h(s)=\sum_{k\in\mathbb Z}\Gamma\left(s-\frac{2\pi i k}{h}\right),$$

$$R_h(s)=\sum_{k\in\mathbb Z}\Gamma_{\mathbb R}
\left(s-\frac{4\pi i k}{h}\right).$$

These follow from classical Poisson and Euler's integral, not from fitting zeta zeros. The replica sums are absolutely convergent on the stated half-plane by vertical Gamma decay.

For every fixed h, G_h has imaginary period 2pi/h and R_h has imaginary period 4pi/h. Their targets are not periodic. Indeed, for any fixed real sigma>0, set s_h=sigma+4pi i/h. Then

$$R_h(s_h)=R_h(\sigma)\to\Gamma_{\mathbb R}(\sigma)>0,$$

whereas Gamma_R(s_h) tends to zero by vertical decay. Therefore convergence cannot be uniform on the entire imaginary axis. A fixed source clock has spectral aliases: this is a **representation/observer defect**, not a nontrivial zeta zero.

## DGC-4: the continued sampled Gamma has an infinite pole lattice

Split R_h into nonnegative and negative n. The nonnegative-n sum is entire in s. For n<0, the absolutely legitimate expansion in Re(s)>0 gives

$$R_h(s)=h\sum_{n\ge0}\exp\left(\frac{snh}{2}-\pi e^{nh}\right)
+\sum_{m\ge0}\frac{(-\pi)^m}{m!}
\frac{h}{e^{h(s/2+m)}-1}.$$

The second expression is meromorphic on C; its sum is locally normally convergent away from the indicated poles. Every pole is simple, at

$$s_{m,k}=-2m+\frac{4\pi i k}{h},
\quad m\in\mathbb N_0,\ k\in\mathbb Z,$$

with residue

$$\mathop{\rm Res}_{s=s_{m,k}}R_h(s)=\frac{2(-\pi)^m}{m!}.$$

Proof: exactly one geometric denominator vanishes at each point, and its derivative with respect to s is h/2. For G_h the analogous poles are -m+2pi ik/h, with residues (-1)^m/m!.

The k=0 poles and residues equal those of genuine Gamma_R. The k≠0 aliases escape to imaginary infinity on each fixed compact subset when h tends to zero.

## DGC-5: naive sampled completion acquires uncancellable poles

For every m≥1 and k≠0,

$$\zeta(s_{m,k})\ne0.$$

Indeed s=-2m+it with nonzero t; by the classical functional equation,

$$\zeta(s)=2^s\pi^{s-1}\sin(\pi s/2)\Gamma(1-s)\zeta(1-s).$$

All factors on the right are nonzero: the sine has nonzero imaginary argument; Gamma has no zeros and is regular at 1-s; and Re(1-s)=1+2m>1, where the Euler product converges to a nonzero value. This uses no RH or nontrivial-zero location.

Consequently the **meromorphic continuation** of R_h(s)zeta(s) has spurious poles at every s_{m,k} with m≥1,k≠0. Its k=0 Gamma poles are canceled by the usual trivial zeta zeros; the extra aliases are not. Thus mere finite-step replacement of the real place by a sampled clock does **not** preserve the globally completed zeta meromorphy.

We deliberately do not use m=0 in this argument, which would require additional Re(s)=1 boundary analysis.

## Controls and acceptance gates

- Exact rational f-pairing confirms normalization and the 1/(15q^4) identity.
- Two computationally different finite analytic routes—direct e^{zu-ae^u} sampling and shifted Gamma Poisson replicas—agree at selected positive-real s.
- A separate numerical test approaches a pole via the negative-clock geometric series and recovers the predicted residue; this is a calibration, not the proof.
- Frequency-shift tests expose exact periodicity and failure of global uniform convergence.
- Source mutations: one-sided n≥0 loses the negative history; rate a≠pi or coefficient z≠s/2 changes the continuum target to a^{-z}Gamma(z). Mutants are labeled and cannot authenticate Tate's real place.
- Negative test: for m≥1 and k≠0, a finite sampled Gamma_R times genuine zeta has spurious completed poles.
- No fake composite at 6, Hecke-character parity or Euler-prime authenticity is claimed as tested here: the **prime source is not constructed at all**. These become mandatory if a future prime-to-Gamma or Weil-sign arrow is attempted.

## Reproduction and next lamp

Native new files:
- observational_succ/gamma_dirac_continuum.py
- tests/test_gamma_dirac_continuum.py
- scripts/gamma_dirac_continuum_probe.py

Run targeted checks:

    python -m unittest discover -s tests -p 'test_gamma_dirac_continuum.py' -v
    python scripts/gamma_dirac_continuum_probe.py --verify

A next discriminating probe would splice only this sampled Archimedean factor into the genuine source-completed Tate/Weil interface, compute the resulting pole/contact defect, and derive a **band-uniform de-aliasing error** with validated transcendental bounds and original prime-power provenance. That would strengthen a source-to-analytic interface, not supply positivity. The existing low Schur sign, all-window Weil positivity, and missing source-derived positive Hilbert identification remain open.

**Claim ledger:** DGC-1 through DGC-5 = PROVED PAPER with classical Euler/Poisson/functional-equation imports. Exact rational finite readout = PROVED EXACT; mpmath calibrations = OBSERVED on explicit samples; prime source derivation, physical interpretation, global Weil sign and RH = UNVERIFIED. No source-to-Weil-positive morphism has been constructed.

**Sources:** NIST DLMF §5.2 (https://dlmf.nist.gov/5.2), classical Poisson summation, Euler's Gamma integral, standard functional equation and nonvanishing of the Euler product for Re(s)>1. The manuscript's proofs spell out the relevant specializations. Imported/historical files unchanged.

**RH PROVED: NO.**
