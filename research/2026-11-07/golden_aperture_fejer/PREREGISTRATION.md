# Preregistered research — golden aperture / spatial Fejér triangle

Date 2026-11-07. Exact base: SUCC PR #538 head eda162b5610d4a9d66bb3c3acbcdc728cbc0eccd. Sister PR #539 is READ ONLY (fixed circular window, golden aperture). Main, original four signed BBP poles and literal U0=0 are frozen. Research only, no π normality claim.

## Exact mathematical predictions written before new numerical runs

G1. Let a=(sqrt5-1)/2, b=1-a=a^2=(3-sqrt5)/2. For *any* probability measure mu on T=R/Z, define E_a as L²-Haar discrepancy after convolution with a uniform centered arc of *fractional length a*. Then
  E_a(mu)=(b/a)^2 E_b(mu)=a² E_b(mu)
by complementing arcs and translating by one-half.
For an empirical epoch mu_A=A^-1 sum_{n=A}^{2A-1} delta_{x_n} (x_n rational BBP phases),
  E_a(mu_A)= (1/(b A²)) sum_{n,m}(b-||x_n-x_m||)_+ - b
           = (1/(b A²)) integral_0^b [B_A(t)-2A² t] dt.
Both are **exact Q(sqrt5) identities** for rational x_n, with a finite nonnegative L² value.

G2. Because a is irrational, every nonzero Fourier multiplier sinc(pi h a) is nonzero. Therefore E_a(mu_A)->0 iff all fixed-h Weyl sums->0; for original BBP source plus tail, this is precisely π base16 normality (premise not proved).

G3. For genuine original BBP source and zero seed, T_n < 1/[15(n+1)^2]. The golden normalized arc has a²=b> T_n for n>=1. The exact *square root energy* transport over [A,2A) must satisfy
 |sqrt(E_a(mu^pi_A))-sqrt(E_a(mu^U_A))|
 <= sqrt(2/15)/(a A) (H_{2A}-H_A) <= sqrt(2/15) log2/(a A).
This is O(1/A) as a *fixed* aperture, compared to the parent critical Fejér O(A^-1/2) at H=A; not a real Weyl cancellation bound.

G4. If B_A(t) <= A+K A² t for ALL 0<=t<=b (a stronger range than #538 ET4, which starts at 1/(A+1)), then
 E_a(mu_A) <= 1/A + (K-2)b/2.
Thus K=3 finite observations cannot yield convergence of this fixed aperture; asymptotic K=2+o(1) would be sufficient. More generally the *one integrated excess* tending 0 is exactly equivalent to normality, not an unproved saving.

G5. Finite critical source Fejér boundedness from #538 plus ×16 frequency-ray rigidity implies explicit logarithmic recovery for the golden E_a. State exact constants, separate their origin, do not assert unconditional C critical upper bound.

## Frozen tests before new source values

- Exact Fraction original four-pole source, U0=0. New golden aperture computed by exact rational comparisons to b and rational outward sqrt(5) enclosure at epochs A=79,157,281,389 (no golden aperture values measured before this preregistration). Check E_a>=0 and E_a equals both pair and integrated-excess forms. Report E_a rigorously enclosed, not floating as a proof.
- Independent check on uniform rational grids and constant-phase ghosts, plus golden Pisot-power locked ghost (not an original BBP source). For constant ghost E_a=a exact, for a uniform q-grid expect E_a->0.
- Compare rigorous source/π aperture transport bound with certified rational tail enclosures and independent high precision only as diagnostic; do not infer a value of actual π normality.
- Exhaustive small-circle synthetic grids to test golden complementary arc and spatial triangle, including source-independent odd rational b alternatives.
- Preserve any failed probes. If fixed b formula fails, record refutation before changing definitions. Do not tune a, samples or K to results. Commit only on a strict additive research branch and open draft PR.
