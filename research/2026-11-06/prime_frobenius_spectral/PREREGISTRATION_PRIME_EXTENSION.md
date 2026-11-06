# Preregistration 2 — recovered n<p≤2n source-Frobenius interference

2026-11-06, strictly additive child of #531. The preceding first preregistration only certified the pole ranges 2n<p≤4n and 4n<p≤8n−7, p≡1 mod4. While attempting further source-selected signed residue estimates, analytic finite-field interference revealed a stronger band n<p≤2n.

**Already explored, NOT blind:** exact tests for n≤250 established that p in (n,2n] divides reduced U_n except p=19 when n=10..16. The derivation predicts the four-pole normalized pU_n coefficient, after factoring 16^(n-(p+1)/2), is one of five rational constants:
- for p≡1 mod4, 7/2, 33/10, 47/15 according to whether the k=5 odd BBP pole and k=3 4j−1 pole are in the realized source past;
- for p≡3 mod4, −19/6 or −65/21 according to whether the k=7 odd BBP pole is in the realized source past.
The p=19 zero in the first of these two last cases is a *real finite p-adic source-cancellation counterexample*, not a proof failure. Because p>n≥8, p²>8n and all odd pole multiplicities are k≤7, so the principal-part residue calculations are well typed. This is source-specific, no real e(h U_n) transport.

**Fresh, unfit holdouts:** n∈{389,401,433,463,509,557}. For every prime n<p≤2n, p=19 exception impossible. Compute literal-zero full unwrapped U_n with both polynomial A/D and signed four-pole Fraction sources; verify v_p(U_n)=−1 exactly and (pU_n modp)= (16^(n-(p+1)/2) times above coefficient) modp, with the correct k=5,3,7 threshold. Also retain original preregistered n∈{161,173,199,211,257,293,317,383} in the original interval (2n,8n−7] and verify its p-adic residues and collisions.

**Theorem hypothesis:** for all n≥8, all n<p≤2n except possibly (p=19 and n=10..16), v_p(U_n)=−1. Combining with the earlier bands and PNT/AP gives liminf log d_n/n≥5. Also prove log d_n≤(8+o(1))n using the D(j) factor resultants and lcm(1..8n), yielding Θ(n) source-specific readout depth. These are asymptotic consequences of **known unconditional PNT/AP**, not any assumption of RH.

**Hostile controls:** p=19,n=10..16 must fail exactly and p=19,n≥17 while p>n must pass. A rational real-decaying denominator-rich sequence y_n=1/P_n trivially has huge odd-prime denominators and is non-Haar, so prime mass alone cannot imply a real signed Fourier contraction. The finite-field Legendre character must NEVER be renamed a real Fourier phasor absent explicit common-basis transport.

No post-hoc removal of exceptions or source changes. PASS requires elementary full proof and all exact rational residue oracles. OPEN remains π normality and the missing real Poisson contraction.
