# Connes oriented scaling: a source-typed SUCC/FUCC-to-local-trace bridge

**Base:** research/direct-quotient-pontryagin-transfer-2026-10-17 @ c8ed4929cb4659de5dfbd8c8c11475e723ec2c2d. **Date:** 2026-10-18. **Status:** exact local arithmetic; explicitly imported classical local-field harmonic analysis. NOT a global Connes trace, not a Weil positivity proof, not RH. Preserve O1–O8 from research/2026-10-15/ONE_OBJECT_TATE_WEIL_SUZUKI_CONNES.md.

## 1. Two quotients, two actions: an exact obstruction (COT-01 and COT-02)

Connes' scaling dynamics act on X=A_Q/Q^× by C_Q=A_Q^×/Q^×. This is not the additive solenoid A_Q/Q that SUCC has already reconstructed. In particular the integer successor S(x)=x+1 does not descend to X: the diagonal rationals -1 and -1/2 lie in the same multiplicative orbit, while S(-1)=0 and S(-1/2)=1/2 do not. A zero adele cannot be scaled into a nonzero one. This is a concrete counterexample, not merely a missing implementation.

Similarly the diagonal rational multiplier p is a gauge transformation on X; it acts trivially. A one-place idèle with p at the p-adic component and 1 everywhere else has adelic norm 1/p and is NOT gauge equivalent to a diagonal rational. The source implements and checks this fact using the existing exact RationalChartIdele class and its quotient normalization. The role of the original V_p:n↦pn is to help construct arithmetic charts and prime data, NOT to be mistaken for the adelic action itself.

## 2. Rational nonunit local fixed-point formula (COT-03)

Let p be prime, u=a/b∈Q^×, u≠1, in lowest terms b>0. Normalize additive Haar dx by vol(Z_p)=1; v=v_p. Write x=bz and use the approximate delta δ_r(y)=p^r 1_{p^r Z_p}(y). The exact local fixed-point integral is

\[
\begin{aligned}
I_{p,r}(u)&=\int_{bZ_p}\delta_r((1-u)x)\,dx\\
 &=|b|_p\,\#\{z\pmod{p^r}:(a-b)z\equiv0\pmod{p^r}\}\\
 &=p^{-v_p(b)}p^{\min(v_p(a-b),r)}.
\end{aligned}
\]

For every r≥v_p(a-b), the result stabilizes to the classical local coefficient

\[
T_p(u)=|1-u|_p^{-1}=p^{v_p(a-b)-v_p(b)}.
\]

Proof: ker multiplication by a-b on Z/p^r has p^{min(v_p(a-b),r)} members; scaling x=bz multiplies the Haar mass by |b|_p. The algorithm separately reports finite count, chart volume and whether stabilization has occurred. It is NOT the incorrect finite permutation trace of a nonunit on Z/p^r. At u=1 the ordinary trace diverges and a canonical distributional principal value is indispensable.

For an authenticated source word built from S and genuine V_p, the affine endpoint map x↦ax+b has rational fixed point b/(1-a) for a>1. A local chart translated to this fixed point has the same derivative a, hence the same local factor T_p(a). The causal event history is retained; no global descent of S is claimed.

## 3. What orientation actually proves (COT-04 and COT-05)

On L²(Q_p,dx), the unitary (half-density) scaling is

\[
(U_u f)(x)=|u|_p^{-1/2}f(u^{-1}x).
\]

For u≠1, the formal fixed-point coefficient, extracted with the associated Jacobian, is

\[
C_p(u)=\frac{|u|_p^{1/2}}{|1-u|_p},\qquad
C_p(u)^2=p^{2v_p(a-b)-v_p(a)-v_p(b)}.
\]

The equality |1-u^{-1}|_p=|1-u|_p/|u|_p proves exactly

\[
C_p(u^{-1})=C_p(u)>0.
\]

The code tracks its rational SQUARE rather than guesses a floating square root. This reciprocal symmetry genuinely depends on half-density: T_3(3)=1 but T_3(1/3)=1/3.

A stronger negative control follows immediately from the product formula. For any rational u≠0,1, including the real place and every exceptional prime dividing ab(a-b),

\[
\prod_{v\le\infty}C_v(u)^2
=\frac{\prod_v|u|_v}{(\prod_v|1-u|_v)^2}=1.
\]

The same cancellation happens for the unweighted local T_v factors. Therefore multiplying pointwise positive local weights on DIAGONAL rational scalings yields a trivial global quantity, not the Connes trace or Weil form. This is why the actual idèle-class quotient, primitive orbits, test distributions, principal-value contact and signs cannot be discarded.

## 4. A genuine half-density match at every prime jet (COT-06)

For a genuine local prime-place scaling u=p^k, k≥1,

\[
T_p(p^k)=1,\qquad C_p(p^k)^2=p^{-k},
\qquad C_p(p^k)=p^{-k/2}.
\]

Thus the oriented local fixed-point scalar reproduces precisely the **half-density portion** of the signed Weil prime-power magnitude log(p)/p^{k/2}. Obtaining the factor log(p) requires a separately justified primitive orbit length; the overall signed distribution and Haar/contact normalization remain unresolved. A rational composite multiplier u=6 is a valid rational dilation but p=6 is NOT a local prime place, and the implementation forbids it.

## 5. Hostile falsifier: orientation does not force positive type (COT-07)

At p=3 and u=4, the off-identity half-density scalar is C_3(4)=3 and remains 3 after inversion. If an arbitrary (NOT Connes-canonical) identity-contact c=1 is supplied to a two-point kernel, the corresponding matrix is

\[
G=\begin{pmatrix}1&3\\3&1\end{pmatrix},
\qquad \operatorname{spec}(G)=\{4,-2\}.
\]

The negative eigenvalue persists after orientation reversal. This **is not a negative witness against zeta**: c=1 was chosen as a mutation control. It decisively refutes the general inference "positive pointwise off-identity coefficients + choice of orientation => positive-semidefinite kernel." Once a Hermitian quadratic form is fixed, an invertible orientation/basis transport also preserves its inertia (Sylvester's law).

A Hilbert norm square is automatically nonnegative; the missing theorem is that its quadratic form equals the ORIGINAL source-derived completed Weil distribution for every admissible test. Importing positivity by defining an auxiliary norm is circular without that equality.

## 6. Exactly what remains missing (COT-08, UNVERIFIED)

Connes' primary article *Trace formula in noncommutative geometry and the zeros of the Riemann zeta function*, arXiv:math/9811068, §V Theorem 3, gives a regularized operator-cutoff trace with the local |1-u|_v denominator and an explicit Fourier-normalized principal value at u=1. Neither off-identity fixed point counts nor a finite cyclic representation fix the contact term. Our module does NOT construct these spectral/physical cutoffs, a trace-class limit, or their full all-place matching to the completed Weil distribution.

Connes–Consani, *Weil positivity and Trace formula: the archimedean place*, arXiv:2006.13771, Theorem 1, supplies a positive Sonin-projection trace in a **restricted Archimedean support** and Fourier/Mellin vanishing regime. It is serious precedent for the orientation/compression idea, not a global RH proof.

**Next discriminating gates:** (i) select a source-typed compact-open test on Q_p^× supported away from 1 and prove its trace pairing equals the normalized local Connes h(u^-1)/|1-u|_p pairing; (ii) cross-check Fourier-normalized identity contact against the repo's authentic finite-Gamma signed W_J contact on C_c²; (iii) derive the p^k primitive orbit mass/log p and the genuinely signed all-place trace, with p=2, chi_-3 conductor, fake6, phase and Gamma/pole controls; (iv) only after source-identifying the same distribution attempt noncircular all-test Weil positivity.

**Reproduction:** python -m unittest discover -s tests -p 'test_connes_oriented_scaling.py' -v. Ten local tests passed in an isolated context using strict interface adapters for the two imported upstream classes; integrated repository execution and GitHub CI must be checked independently. Negative controls include counterfeit prime 6, insufficient depth, u=1 contact singularity, reversal of unweighted terms, SUCC no-descent, separate idèle classes, and deliberately indefinite contact.

**Claims:** COT-01–07 exact/local classical/derived with explicit proofs; COT-08 UNVERIFIED. The local field and product-formula mathematics is classical; original project contribution is the source-typed interface, finite probes and obstruction inventory. RH PROVED: NO.
