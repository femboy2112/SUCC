# Preregistered first-moment Gamma / harmonic / silver test — 2026-11-06

**Exploratory derivation already done before this preregistration; this is NOT a blind discovery.** For authentic BBP r(n), the local symbolic decomposition predicts a=15/64 and a finite source constant B=(27+31sqrt2)pi/128+(39/32)log2+(31sqrt2/64)log(1+sqrt2), with

    sum_(n=1)^N n*r(n) = a*H_N + B - E_N,  0<E_N<241/(288N) for N>=2.

Hence subtracting a log N instead yields the same B plus (15/64) Euler–Mascheroni γ in the limit, precisely distinguishing the universal harmonic/gamma counterterm from the original-pole silver-ratio finite residue. This has not established any phase or signed Weyl bound.

Frozen new finite checks: exact original source rational prefix evaluations at N=128,512,1024; compare to high-precision B using the provable tail interval, not floated proof. Verify *independent* SymPy digamma expression, rational partial fraction coefficient sum and rational positivity of n*r(n)-a/n; alternatively do exact polynomial proof. Both B and a must not be tuned after measurements. Negative control: H-shadow source has a different first-moment constant; equality of the universal 2-adic isometry must not imply the same B. Preserve failures, uncertainties and source provenance.

Certification verdict may rely only on theorem algebra and rational inequalities; numerics are finite corroboration. π normality and signed R decay remain OPEN.
