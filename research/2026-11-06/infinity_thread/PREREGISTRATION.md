# PREREGISTRATION — Operation INFINITY THREAD / MESOSCOPIC GATE

2026-11-06. Strict additive child of SUCC PR #530 at SHA 9b53501e37f6bb9ab5bd6f63cadf4cbfc1607749. Original four-pole source, literal U0=0, source contracts and archived proofs immutable. All new proofs are **conditional**: they do not establish π normality.

## Analytic hypotheses (derived prior to measurements, not blind)

For unit complex observations f_n(h)=exp(2πih U_n) set W_N(h)=N^-1 Σ_(n<N) f_n(h). For A>=16 choose Q=2^floor(log₂(A)/2), m0=ceil(A/Q), m1=floor(2A/Q), L=m1−m0+1, and R_(Q,m)(h)=Q^-1 Σ_(j<Q)|m^-1 Σ_(t<m)f_(j+tQ)|². Define E_A(h)=L^-1Σ_(m0≤m≤m1)R_(Q,m)(h). Candidate universal finite gluing inequality (to be proved analytically):
    sup_(A≤N≤2A)|W_N(h)| <= 18Q/A + (64 E_A(h)/3)^(1/3).
Define P_A(t)=Σ_(h!=0)t^|h| E_A(h) with 0<t<1. P_(2^k)(t)→0 implies all-fixed-h Weyl→0 and π base16 normality for the original zero-seeded source. A proposed sufficient **infinite transfer** is P_(2^(k+1))≤rho P_(2^k)+epsilon_k for all large k, 0<rho<1, epsilon_k→0. This transfer is **OPEN**. The finite gluing proof alone is not a π advance.

## Preregistered calibration and new finite holdouts

Already-seen exploration, NOT blind: finite shell energies for original h=1 and 1/2-weighted h=1..12 at A=128,256,512,1024; original π shell potentials were approximately .0897,.0788,.0359,.0454 (not monotone!), shadows ≈2, periodic 1/17 ≈2. No numerical parameter search to set a decay law is allowed.

**New holdouts** A=2048 and A=4096, each with Q=2^floor(log₂ A/2), h=1,2,3, and truncated Poisson potential t=1/2, |h|≤12. Exact original four-pole **rational zero-seeded states** to n<2A, four-pole identity checks, unmodified. Comparator 1: non-original 2-adic isometric rational shadow H(n)=n/(2n−1)^4, predicted mean energy >0.99 for h=1..3. Comparator 2: coherent rational β=1/17 ×16 orbit, even Q, predicted shell R=1 for each mode with 17∤h; this is not the original source/seed. For original, record all data with no fit or monotonicity prediction. Distinct floating sums are numerical diagnostics **only**, not certificates for infinite decay.

Verify finite gluing inequality with original, shadow, periodic, and a fixed-seed synthetic complex-unit sequence (positive/negative controls). Verify algebraic character kernel and partial phase-tail bound exactly where possible. A finite test cannot validate ∀A, ∀h or source-selected asymptotics. If budget prevents full exact rational holdout, label blocked not passed.
