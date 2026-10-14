# ZCR-A: Archimedean isometry source-map supplement

**Parent:** [ZCR](CLAIM_SUPPLEMENT_ZERO_CENTERED.md), [ZCR-F](CLAIM_SUPPLEMENT_ZERO_CENTERED_FUCC.md). **RH PROVED: no.** [Theorem and controls](../research/2026-10-13/ZERO_CENTERED_ARCH_DILATION.md).

| ID | Statement | Status |
|---|---|---|
| ZCR-A01 | Continuous dilation x->qx with zero extension induces integer-cell D_q f(k)=f(floor(k/q)) for k>=q, else 0. Distinct from address sampling T_q. | PROVED LOCAL |
| ZCR-A02 | D_q*D_q=I/q; U_q=sqrt(q)D_q is isometric but not onto. | PROVED LOCAL; surjective-unitary reading REFUTED |
| ZCR-A03 | L_s(U_q f)=q^(1/2-s)L_s(f); modulus 1 iff Re(s)=1/2; no zeta-zero conclusion follows. | CLASSICAL/PROVED LOCAL source realization; RH bridge UNVERIFIED |
| ZCR-A04 | Exact block telescopes and finite-sequence covariances; distinguish sampling from dilation with counterexample. | TESTED/PROVED LOCAL |

**Controls:** tests/test_zero_centered_arch_dilation.py; no zero reads. No global L² convergence, genuine gamma/poles, conductor or Weil positivity claimed.
