# PR #576 audit: reproducible defects, repairs and surviving claims

Tracking issue: [#578](https://github.com/femboy2112/SUCC/issues/578).

Audited head: `afabc458323ef2e3a20ce2bae77239c4190819c5` (11 commits above the
Main XXII integration). The supplied November 9 audit was a lead; this round
reproduced the defects against that exact checkout. The original 46 selected
tests passed, including the defective assertions. New hostile regressions
exercise the mistakes directly. The original commits and session archive are
preserved; notices in the active dossiers point here.

| Finding | Correct verdict and repair | Evidence |
|---|---|---|
| Capture under a lambda binder | The original reducer changes `lambda z.((lambda x.lambda y.x) z)` into the wrong term. Implement standard shift/substitute/unshift; use one global reduction budget. | [Semantic audit](SEMANTIC_AUDIT.md), independent named-variable oracle |
| SUCC/FUCC conflated with time powers | Actual arithmetic actions satisfy `V_p S=S^p V_p`; commuting powers of the BBP step do not verify that relation. Separate Church-natural actions from indexed rational BBP time advance. | Semantic audit and negative commuting-law test |
| Invented omega addresses | A left-associated `E_k(m)`, m>=2, has exactly one beta-redex at `('f',)*(m-2)`. Retain the copy-growth law; repair the address interpreter. | Generic AST enumeration and addressed contraction |
| Cofinality accepted from finite prefixes | Return UNKNOWN for arbitrary prefixes. A declared monotone affine generator has a proof-backed threshold witness. | Constant-prefix and alternating-axis counterexamples |
| Scott product topology assertion | Use the direct directed-supremum argument; do not assume equality of the two product topologies. | Semantic audit, section 5 |
| Lag bound called asymptotically sharp | The old inequality survives, but its sharpness assertion is false. The source limit is 15/64 and the product limit 225/4096. | Exact source envelope and independent full symbolic polynomial expansion |
| F-9 universal irrationality-measure requirement | Withdraw necessity. Known seed differences are exactly `16^n s`; finite digit certification terminates by nested enclosures and irrationality. | Exact seed counterexample, adaptive certificate, B07 |
| F-11 uniform Fourier truncation | Pointwise symmetric summation at a fixed finite irrational orbit survives. L2 does not bound atomic empirical evaluation, and the coefficient sequence is not l1. Replace the claimed uniform tail by a boundary-aware Fejer certificate. | B02 irrational near-jump counterexample; rational interval readout |
| C-monoid verification scope | Historical C1-C9 names are finite sample identities, including a previously hardcoded True. They are not a verified complete axiom presentation or faithful source embedding. | Corrected evaluator and explicit UNVERIFIED status |
| Signed covariance exactness and table | Nondyadic means were floats; P reported E[b] rather than E[ab]; tail-coupling documentation named a different quantity. Repair exact Fraction arithmetic and declare the actual coupling. | SIGNED_COVARIANCE_AUDIT.md and hostile nondyadic tables |
| Parity index in the maintained frontier | PPP/TFH uses s_n=(-1)^floor(Y_n), while f(Y_n)=s_(n+1). The same-epoch difference is (s_(2A)-s_A)/A, at most 2/A. | PPP-02 original convention and corrected NEXT.md/frontier |
| Lean authority | The three files contain concrete arithmetic checks. `ParityFourierSupport.lean` checks residues/counts, not Fourier integration. `Lag1Autocorrelation.lean` checks leading arithmetic and a positive integer, not the full polynomial identity. | Direct inspection of the declarations; no new Lean compilation claimed |

## Exact correction to the source constant

Set p=8n-7. Rearranging the unchanged four signed poles gives

```math
r(n)=\frac6{p(p+3)}+\frac4{p(p+4)}+\frac5{p(p+5)}.
```

Therefore for every integer n>=1,

```math
\frac{15}{p(p+5)}<r(n)<\frac{15}{p(p+3)},\qquad
\lim_{n\to\infty}n^2r(n)=\frac{15}{64}.
```

Multiply these positive envelopes at n and n+k. Because n+k>=n, both scaled
envelopes approach the same constant uniformly for every integer k>=1:

```math
\sup_{k\ge1}\left|n^2(n+k)^2r(n)r(n+k)-\frac{225}{4096}\right|
\longrightarrow0.
```

This is a direct rational squeeze. The old constant 225/16 is larger by a
factor of 256. Its finite upper inequality is not refuted. The new envelope
has the correct leading constant; it is still a bound on the forcing
product, not on a signed orbit correlation. No academic priority claim is
made for this elementary consequence of the already known decomposition.

## Surviving source construction

The finite identity `U_n+T_n^(L)=16^n P_L`, literal zero seed, exact four
poles, and directed source enclosures survive this audit. The new Cayley
observer reuses the tighter canonical tail bound already present in
`duck_bbp`, and pays the observer/source clock coupling explicitly.

The strongest corrected status for the computational semantics is finite
operational evidence plus the stated elementary proofs. A genuine nontrivial
C-monoid with a faithful indexed BBP compiler remains UNVERIFIED. Original
zero-seed parity balance, full hexadecimal normality, and RH remain OPEN.

The subsequent [affine source action](AFFINE_SOURCE_ACTION.md) does close a
specific intermediate gap: it gives a faithful action on `N0 × Q` whose
successor is the actual BBP step and whose declared clock dilation obeys the
affine relation. It retains the source cocycle and every seed fiber. It is a
representation on indexed rational states, not the still-missing embedding
inside a genuine C-monoid.
