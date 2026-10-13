# E38 — Source-faithful arithmetic polarization: signed bridge and two obstructions

## 1. Original question

Can causally observed arithmetic coefficients supply an independently positive
polarization identified with the **completed** Weil pairing? The faithful
steelman permits nonlocal arithmetic/Archimedean coupling; it does not assert
that each prime impulse is positive. This first-generation investigation starts
at `5eb09e7cba36ec01b8f9d6834b78b5766fd93935`, on
`research/swm-e38-2026-10-13`. **RH PROVED: no.** No sibling conclusions,
nontrivial-zero locations, compiler, or full test suite were consulted.

## 2. Existing mathematical context

[Weil (1952)](https://denisevellachemla.eu/transc-Weil-1952.pdf) makes the explicit
formula distributional. [Suzuki (2023), §3.2, Proposition 3.1 and §3.5](https://londmathsoc.onlinelibrary.wiley.com/doi/full/10.1112/jlms.12785)
supplies the compact-smooth criterion and differentiation bridge below.
[Suzuki (2025), abstract](https://doi.org/10.4153/S0008414X25101739) constructs
the Weil Hilbert completion **under RH**; importing that positivity would be
circular. [Suzuki (2026 preprint), introduction, §3 and (8.3)](https://arxiv.org/html/2606.09096v1)
provides the completed source formula, localized operator interpretation, and
logarithmic form-domain warning. These are primary mathematical references,
not independent experimental votes.

The import origin is FuckingRH commit
`ba075348b7bcc66d938b3e0ca96c26e95bba340a`. Frozen dossiers inspected:
`OMEGA_SUCC_SECOND_ORDER_WEIL_REPORT.md`,
`GAMMA_ACTUALIZATION_INTERFEROMETER.md`,
`SUCC_GAMMA_PRIME_PATH_GERMS.md`, and
`DIRICHLET_LAMBERT_SOURCE_LIFT.md`. Exact-origin
`research/aletheia_2026-10-05/FUCC_MULTIPLICATIVE_OPERATOR.md` supplies the
isometries attacked in §9; Bernstein's source-compensation dossier and native
`carrier_hankel_bounds.py` are boundary context, not Weil-identification proofs.
`verify_provenance.py` verified all 72 manifest entries, exit 0.

## 3. Proposed SUCC objects

Let \(\mathcal D=C_c^\infty(\mathbb R)\), with its usual LF test-function
topology, \(\widetilde v(x)=\overline{v(-x)}\), and
\(\widehat v(z)=\int v(x)e^{izx}dx\). For \(F\in C_c^\infty(\mathbb R_+)\),
\(UF(u)=e^{u/2}F(e^u)\) is unitary from \(L^2(dx)\) to \(L^2(du)\):
\(\mathcal M F(1/2+iz)=\widehat{UF}(z)\). Multiplicative Haar measure is
\(dx/x\), convolution transports to additive convolution, and
\(F^\sharp(x)=x^{-1}\overline{F(1/x)}\) transports to \(\widetilde{UF}\).
These actual maps fix the half-density convention.

Normalized source \(a(1)=1\) gives \(b=\log_*a\) coefficientwise. Genuine zeta
has \(b(p^k)=1/k\), so \(c_{p^k}=b(p^k)\log(p^k)/\sqrt{p^k}=\log p/p^{k/2}\).
Conductor is 1, root number +1, Gamma factor
\(\pi^{-s/2}\Gamma(s/2)\), and completed poles are 0 and 1. Define, for
\(h\in\mathcal D\),

\[
\begin{aligned}
W_b(h)={}&\int h(x)(e^{x/2}+e^{-x/2})dx
-\sum_{n\ge2}\frac{b(n)\log n}{\sqrt n}[h(\log n)+h(-\log n)]\\
&-(\log4\pi+\gamma_E)h(0)
-\int_0^\infty\!\frac{[h(x)+h(-x)-2e^{-x/2}h(0)]e^{x/2}}{e^x-e^{-x}}dx.
\end{aligned}
\]

The sum is locally finite and the Gamma subtraction is retained. Only the
genuine tape yields zeta's authentic \(W\); mutations with this fixed completion
are diagnostics. Set \(Q_b(v,w)=W_b(v*\widetilde w)\).

## 4. Candidate theorem

**E38.1 — PROVED LOCAL, source injectivity.** For every two real tapes \(b,c\)
with the same declared completion, equality \(Q_b=Q_c\) on
\(\mathcal D\times\mathcal D\) implies \(b(n)=c(n)\) for every \(n\ge2\).
Consequently no polarization factoring only through \((|b(n)|)_n\) can equal
\(Q_b\) for every such tape. This is a restricted no-go, not a prohibition on
source-sensitive positive constructions.

**E38.2 — CLASSICAL signed bridge.** With \(g=-\Psi\) from the completed Suzuki
source and \(K(x,y)=g(x-y)-g(x)-g(-y)+g(0)\),
\(Q(v,w)=\langle S_a v',w'\rangle_{L^2}\) on
\(\mathcal D_a=C_c^\infty(-a,a)\), where \(S_a\) has kernel \(K\).
No sign is asserted for \(S_a\).

## 5. Proof attempt

For E38.1 use a real even smooth approximate identity \(\eta_\epsilon\).
Convolution \(v*\widetilde\eta_\epsilon\to v\) in \(\mathcal D\); equality of
pairings therefore gives equality of distributions. After canceling their
identical completion, isolate \(\log m\) with a bump avoiding every other
\(\pm\log n\). Its coefficient is
\(-(b(m)-c(m))\log m/\sqrt m\), hence vanishes.

For E38.2, distributional \(W=\Psi''=-g''\) and
\((v*\widetilde w)''=-v'*\widetilde{w'}\) give the displayed identity by
integration by parts. Terms depending on one variable vanish because
\(\int v'=\int w'=0\). Since \(K\) is continuous on the compact square,
\[
|Q(v,w)|\le2a\sup_{[-a,a]^2}|K|\,\|v'\|_2\|w'\|_2.
\]
Thus the common completion \(H_a=H_0^1(-a,a)\), norm
\(\|v\|_{H_a}^2=\|v\|_2^2+\|v'\|_2^2\), is sufficient. It is not asserted
to be the maximal closed Weil form domain or operator domain.

## 6. Crucible

Take \(b_\pm=b_\zeta\pm\delta_6\), and recover actual rational sources
\(a_\pm=\exp_*b_\pm\). Every diagonal event-feature Gram using squared
amplitudes is identical for these tapes, hence positive for both. Nevertheless,
with \(A=\log6\), nonnegative smooth \(\eta\) supported in \((-r,r)\),
\(0<r<A/4\), and \(v=\eta+\eta(\cdot-A)\),
\[
Q_{b_+}(v,v)-Q_{b_-}(v,v)
=-4\frac{\log6}{\sqrt6}\|\eta\|_2^2<0.
\]
This falsifies **identity from sign-blind covariance**, not positivity of the
genuine target. The probe reconstructs both logs through 16 and finds the same
positive Gram with LDL pivots 1,1,1. A rational log/square-root enclosure certifies
the negative normalized delta; Gamma and poles cancel exactly.

The obstruction does not depend on negative observed coefficients. Globally,
\(a_-(n)=\sum_{j=0}^{\min(v_2(n),v_3(n))}(-1)^j/j!\ge0\): alternating
partial sums are nonnegative, with the sole zero at truncation one. The finite
probe checks nonnegativity through its declared horizon, while this elementary
argument supplies the universal statement. Thus positivity of the raw source
also fails to repair sign-blind connected-feature identification.

Matched non-Euler control: take the primitive odd character modulo 5 with
\(\chi(2)=i\), \(\epsilon_\chi=\tau(\chi)/(i\sqrt5)=e^{2i\theta}\), and
\(D=(e^{-i\theta}L_\chi+e^{i\theta}L_{\bar\chi})/(2\cos\theta)\).
Both use \((5/\pi)^{(s+1)/2}\Gamma((s+1)/2)\), with no poles;
\(D\)'s root number is +1. This follows directly from the primitive-character
functional equation and Gauss sum, [DLMF 25.15.5–6](https://dlmf.nist.gov/25.15#i).
Its coefficients at 2,3,6 are \(t,-t,1\), \(t=\tan\theta\), giving
\(b_D(6)=1+t^2>0\), whereas \(b_\chi(6)=0\).
Exact isolation uses \(P(t)=t^8-16t^6+46t^4-16t^2+1\): opposite endpoint
signs and \(P'<0\) on \((1/4,1/3)\), hence
\(17/16<b_D(6)<10/9\). No completed DH sign or zero location is evaluated.

To check phase selection rather than fit it, evaluate
\(\tau(\chi)=-2\sin(\pi/5)+2i\sin(2\pi/5)\). Accordingly
\(\cos^2(2\theta)=(5+\sqrt5)/10\), and substituting
\(\cos(2\theta)=(1-t^2)/(1+t^2)\) gives \(P\). The isolated interval has
\(\cos^2(2\theta)>1/2\), selecting this root and excluding the conjugate
quadratic branch. A genuine simultaneous character conjugation is allowed and
must conjugate its epsilon factor; the single-coefficient mutant deliberately
fails multiplicativity. The control tests that failure, not an assertion that
every changed phase is illegitimate.

The probe also changes only \(\chi(2):i\mapsto-i\), producing \(b(6)=2\);
uses clock frequency \(\pi/\log2\) to distinguish log2 from 2log2 by phases
\(-1,+1\); and changes half-density at 4, doubling its log4 coefficient.
It separately doubles the genuine connected weight at prime 2 and recovers
that change by the independently implemented formal exponential/logarithm.
Dropping poles is separately falsified analytically by a nonzero even
nonnegative bump: its pole contribution is strictly positive.

## 7. Verdict

**FAILS / REFUTED:** universal identification through sign-squared source
features, and unitary identification of canonical prime isometries with real
translations (§9). **SURVIVES / CLASSICAL:** the signed differentiated bridge.
**SURVIVES / PROVED LOCAL:** E38.1 and the conditional transfer lemma below.
**TESTED MODEL:** bounded exact algebra and mutation receipts.
**BLOCKED:** an independently positive authentic arithmetic polarization; the
missing object is specified, not declared impossible. Scholarly novelty and
independent mechanization remain unverified.

## 8. Remaining obstruction

**E38.3 — conditional transfer, PROVED LOCAL.** For every \(a>0\), suppose
bounded source-constructed maps \(T_{a,N}:H_a\to\mathcal K_{a,N}\) into Hilbert
spaces satisfy, for all \(v,w\in\mathcal D_a\),
\[
|\langle T_{a,N}v,T_{a,N}w\rangle-Q(v,w)|
\le\varepsilon_{a,N}\|v\|_{H_a}\|w\|_{H_a},\qquad
\varepsilon_{a,N}\to0.
\]
Density extends the estimate to \(H_a\); taking \(N\to\infty\) on the
diagonal proves \(Q\ge0\), and exhausting \(a\) invokes Weil's criterion.
The hypotheses have not been supplied. Finite PSD, Hankel rank, or formal
coefficient stabilization supplies neither this identity nor this norm bound.
Square-rooting the target assumes its sign. **Next small lemma:** construct
one source-preserving \(T_{a,N}\) and prove the displayed estimate for one
fixed interval, including its Gamma/pole terms and the above mutants.

The order of quantifiers matters: each fixed interval needs an error tending
to zero for **every** test vector, rather than errors only on one finite
matrix. Uniformity in the interval radius is not claimed or needed for this
conditional smooth-core criterion. Continuity transfers the estimate within
one interval before exhaustion. The target remains the genuine completed
source, so finding a positive factorization of a substituted or truncated
form cannot discharge the hypothesis.

## 9. Cross-domain connection with actual maps

On \(\ell^2(\mathbb N_{>0})\), \(V_pe_n=e_{pn}\) is a proper isometry:
\(V_p^*e_1=0\). Log translations on \(L^2(\mathbb R)\) are surjective
unitaries. Therefore no onto unitary \(J\) satisfies \(JV_p=\tau_{\log p}J\).
Passing to \(\ell^2(\mathbb Q_+^\times)\) repairs surjectivity but not topology:
\(q_m=(m+1)/m\to1\), yet
\(\|V_{q_m}e_1-e_1\|^2=2\), unlike strongly continuous real translations.
No unitary identifies those representations either. Dilation, nonunitary
maps, or different source norms remain possible; their domain and adjoint must
be proved. A source-changing basis requires an actual test-space intertwiner
and completion-preserving form identity, not a renamed Gram matrix.

## 10. Deliverables

`exact_probe.py` is standard-library-only, horizon 16; `RECEIPT.json` records
commands, exits, hashes, source dependencies and controls. Algebraic receipts
support the stated finite scope; universal claims rest on the proofs above.
No numerical integral, CI result, physical-cognition theorem, archive rewrite,
license, default change, merge, or push is claimed. κ is direct source/proof
contact; φ separates covariance success from identity failure; σ retains
completion provenance; ρ receives no evidentiary weight. Principal and
independent crucible review remain the final acceptance gate.
