# SUCC Research Dependency DAG

One canonical proof-dependency graph, from carrier mathematics through to the RH application. Every
arrow carries a status so the reader sees immediately **which arrows are closed and which remain
open**. This is the *conceptual* proof DAG; for the *git* PR-dependency DAG of the Academic Main
consolidation see
[ACADEMIC_PR_DEPENDENCY_GRAPH_2026-10-15.json](ACADEMIC_PR_DEPENDENCY_GRAPH_2026-10-15.json).

Arrow status legend:
`[C]` classical imported theorem · `[P]` proved within declared assumptions · `[X]` exact finite
model · `[I]` implementation only · `[U]` unverified construction · `[R]` refuted inference.

## The graph

```
                    CARRIER MATHEMATICS
  B(N) --group completion [C,X]--> Z --localize [C,X]--> Q --adjoin i / complete [C,X]--> Q(i),C
  {Z/nZ} --inverse limit + CRT [C,X]--> Ẑ ≅ ∏Z_p --localize [C,X]--> A_f --× R [C]--> A_Q
                                   |
                                   v
                    SOURCE-INDEXED OBSERVATION
  carrier --finite source chart [X]--> observer interface
         --proof-access classify [P]--> {Simple | IdealHard | Fucked | Unresolved}
         --compact gluing (FIP) [C, nonconstructive]--> global section
         --noncompact escape [P]--> empty limit (no-go)
         --phantom source-map [P]--> ∀N∃z, ¬∃z∀N (no-go)
                                   |
                                   v
                    REPRESENTATION / DUALITY
  Ẑ --Pontryagin [C]--> Q/Z ;  A_f/Ẑ ≅ Q/Z [C] ;  (A_Q/Q)^∨ ≅ Q [C], self-dual, Q^⊥=Q
  S(Q_p) --local self-dual Fourier [C,X]--> S(Q_p)
  S(A_f) --integer-scale rational-translate span [C,P] (CTW-02; REFUTES [R] noninteger-necessity)
                                   |
                                   v
                    ARITHMETIC / ANALYTIC TRANSPORT
  S(A) --adelic Poisson [C,P | conditional on real Poisson]--> Σf = Σf^
  canonical Gaussian⊗∏1_{Z_p} --idelic Mellin [C,P]--> Gamma_R(s)·ζ(s), Re(s)>1
       --classical continuation/poles/FE [C import]--> completed ξ
  log-derivative scalar --[R] recoverable from log-deriv (CTW-11); NOT universal impossibility
                                   |
                                   v
                    WEIL / RH APPLICATION
  completed ξ --signed completed Weil distribution [X]--> W_ζ(f)
       --high-subspace / short-window positivity [P, scoped]--> Q_ζ(f) > c‖f‖²  (codim / a≤1/12)
       --K-relative transport [P]--> D_r ⪰ κ Q_r K Q_r   (relative to K=V*V, NOT κI)
       --zero-shift Douglas range [P]--> 0 ⪯ R0 ⪯ (11/40)²/κ·I   (no D^{-1}/K^{-1} at λ=0)
   ======================  FIREWALL  ======================
       --low Schur sign S0=A−R0 ................................ [U] OPEN
       --"all high positive ⇒ full Weil positive" ............. [R] REFUTED generally
       --source→Weil-sign typed morphism (K_g ⪰ 0) ............ [U] missing; assuming it restates RH
       --all-a / prime-active global positivity ............... [U] RH-equivalent, OPEN
       ==> RH ................................................. OPEN. RH PROVED: NO.
```

## Closed vs open — the one-line summary

- **Closed `[C]/[P]/[X]`:** every arrow from carrier construction through Pontryagin duality,
  finite-adèle spanning, adelic Poisson, idelic Mellin and the completed ξ. These are classical
  theorems (or exact finite models of them); their truth does not depend on any sign.
- **Scoped-closed `[P]`:** high-subspace and short-window Weil positivity, K-relative transport, the
  zero-shift residual bound — each true on a restricted domain / metric, none global.
- **Open `[U]` / refuted shortcuts `[R]`:** the low Schur sign, the "high ⇒ full" shortcut, the
  source→Weil typed morphism, and all-a positivity. **This is exactly where RH sits, and it is
  OPEN.**

Cross-references: [CARRIER_ATLAS.md](CARRIER_ATLAS.md) · [OBSERVER_PROOF_ACCESS.md](OBSERVER_PROOF_ACCESS.md)
· [RESEARCH_FRONTIER_2026-10-15.md](RESEARCH_FRONTIER_2026-10-15.md) · [CLAIM_LEDGER.md](CLAIM_LEDGER.md).

## Proof Teeth branch supplement

The [new claim supplement](CLAIM_SUPPLEMENT_PROOF_TEETH.md) adds a proved
finite-Haar → Hilbert-direct-limit → L²(Zhat) → ell²(Q/Z) chain. Its completion
arrow requires density and uniformly bounded compatible maps. Factorial
projections converge strongly, while norm(I−Pn)=1 at every finite stage.

Finite observation → coimage decoder is exact when the target is constant on
observation fibers. Extending linear decoders after completion additionally
requires one uniform bound ||hx||≤C||Ox||. Finite-stage invertibility alone
fails for O=diag(1/n), h=I. The separate Lean branch proves affine two-point
and rational cyclic-retract instances; it does not formally prove the Hilbert
completion arrow.

For the genuine four-low signed source, parity now splits the low space into
two 2×2 blocks, and the K-relative residual is a derivative norm modulo the
four low polynomial moments. Eight exact whole-Gamma-tail certificates reject
the displayed zero/frozen trial sufficient inequalities. These add a failed
method edge, not an edge to negative source sign or to RH. The original
S0≥0 edge remains OPEN. All-stage positivity, source identification and form
domains remain explicit premises in the capsule dependency graph.

## Observer–Schur Round II

The [Round-II supplement](CLAIM_SUPPLEMENT_OBSERVER_SCHUR.md) supplies these
additional arrows, each with its required domain:

```text
Linear observation + Hermitian form
  --kernel lies in radical [P]--> exact energy decoder on the image
  --D≥0, actual sqrt(D) range [P]--> finite quadratic fiber envelope S0
  --A≥αI and source reflection [P]--> two parity contraction problems
  --certified genuine residual upper bound [U]--> original S0 sign [U]

Actual compact source G + strong orthogonal Legendre chain
  --signed derivative regularity [P]--> quantitative operator-norm compression
  --"norm compression controls zero inverse" [R]--> REFUTED
  --"ordinary Galerkin controls K-relative residual" [R]--> REFUTED generally
  --bounded residual map [P]--> polynomial graph density
  --target in residual-range closure + controlled approximation [U]--> sharp residual

Pinned finite Python model -> fixed Lean instance grammar [X]
  -> fresh exact-term kernel replay [formal, recorded separately]
  -> universal Python/source identification [U, not supplied by hashes]
```

The authentic degree-eight even response family is excluded for the stated
sufficient criterion by a rational interval matrix proof. This is a failed
method edge, not negative original-source sign. The clamped-biharmonic example
shows that even every trial can fail such a conservative method for a genuinely
positive synthetic form. Neither counterexample is substituted for Suzuki.

## Arithmetic Resonance

The [Arithmetic Resonance supplement](CLAIM_SUPPLEMENT_ARITHMETIC_RESONANCE.md)
adds the following source-sensitive arrows. Here P means paper proof under the
written hypotheses, X means exact finite/interval computation, U means open.

```text
Authentic g' + real Gamma tower + poles/contact/prime2
  --Carleman exterior bound + endpoint distribution exclusion [P]-->
       maximal distributional annihilator lies in logarithmic form domain
  --moment-preserving form core + inherited D>=kappa K [P]-->
       ker R_Q*=0, closure Ran R_Q=M
  --compactness of authentic g' response [P]-->
       dense nonclosed range, no bounded right inverse on all M
  --exact continuum residual minimization on nested high spans [P]-->
       C_N decreases to0; both Schur brackets converge in low operator norm
  --quantified approximation of the four targets [U]-->
       useful K-relative residual certificate [U]

Same source Gamma multiplier
  --moment-corrected high-frequency modulation [P]-->
       D<=C K impossible for every finite C

Source square-root range
  --spectral theorem [P]--> finite matrix inverse-response measure
  --stronger fractional range / effective weak-spectrum mass [U]-->
       computable positive-shift-to-zero gap [U]
  --finite nonnegative spectral moments alone [REFUTED]-->
       no general inverse-response cap

Frozen degree20 source response + full Gamma tail [X,P]--> improved S0 upper
Low derivative cell bounds + full derivative tail + kappa [X,P]--> improved S0 lower
Both bounds --> unresolved sign (not positivity)
```

The dense-range theorem removes a qualitative obstruction for this source. It
does not give attainable response, a convergent energy-Galerkin method, a rate,
or a positive Schur lower certificate. The inherited synthetic counterexamples
retain their original domains. Cross-radius norm continuity and exact low blocks
past prime3 and prime-square4 do not carry first-window coercivity to those radii.

## Collective Observer child branch (2026-10-16)

```
#139 source-lambda -> #140 consensus -> receipt repair + typed effects [P,X]
finite cyclic Haar -> commuting E_m -> linear pool / algebra join [C,P,X]
                                             -> primitive conductor sectors [C,P,X]
declared joint transitions + original/current beliefs -> bounded AND/OR policy [P,X]
  full quotient-compatible legality/cost/outcome laws -> adaptive no-go [P,X]
#141 normalized Dirac clocks + #142 analytic band proofs (pinned, not merged)
  -> common rational period [P,X] -> global tuple-decoder obstruction [P]
  -> finite strip + replicas + sample tails + directed evaluation [P,X]
#137 pinned original signed source + high coercivity + derivative tail [P imports]
  -> exact polynomial moment subtraction -> sharper response cap [P,X]
  -> improved S0 lower enclosure; inherited upper -> BOTH SIGNS OPEN [U]
YEAN #138 exact types + local kernel/axiom audit -> finite implications [kernel]
  -> runtime model identification / nondeterministic extraction .... OPEN [U]
```

The [dependency manifest](../research/2026-10-16/COLLECTIVE_OBSERVER_DEPENDENCIES.json)
pins source identity, coordinate metric and shared premises. Independent finite
methods share one original arithmetic source; they are not independent sources.
See [CO-01–17](CLAIM_SUPPLEMENT_COLLECTIVE_OBSERVER.md) for domains and falsifiers.
