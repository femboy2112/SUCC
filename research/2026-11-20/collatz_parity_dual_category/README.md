# Operation Dual Categories — pi's hexadecimal journal as a 2-adic Collatz parity itinerary

**Research-only draft.** Continuation of SUCC #680 (digit/mirror/2/3/5 seam), with classical foundational citations and exact finite original-BBP checks. **Full pi normality, R0, integer Collatz, RH, and any physical-energy assertion remain OPEN.**

## The literal bridge

Let `C(a)=(3a+1)/2` for odd 2-adics and `a/2` for even ones. The classical Bernstein--Lagarias parity map `Q(a)=sum_j(C^j(a) mod2)2^j` is a 2-adic homeomorphism satisfying `Q C=S_2 Q`. Grouping bits into nibbles gives `Q C^4=S_16 Q`: **four chronological Collatz steps are literally one hexadecimal bookkeeping shift after a source-defined coordinate change**. Equivalently, the labelled action categories `Act({0,...,15}^N,shift)` and `Act(Z_2,C^4)` are isomorphic, via the parity map. This is categorical/dynamical equivalence, not Collatz termination and not an unproved BBP-to-Collatz factor map.

The *symbolic hexadecimal mirror* `d->15-d` maps to `V(Y)=-1-Y` in the 2-adic parity journal; transporting it back gives `Omega=Phi V Q`, the **known Monks--Yazinski nontrivial Collatz autoconjugacy**, with `Omega C=C Omega`. A raw state mirror is not this symmetry.

## Quarter root positions, with the source boundary explicit

The BBP Mellin filter `H=(t²+2)(t²+2t+2)` has oriented left-arc conjugate roots at `1/4` and `3/4` (#678/#679). The two odd Collatz classes `4k+1` and `4k+3` produce respectively two-step parity codes `01` and `11` (least significant first), which are *also* labels `1` and `3` on a quarter-grid. In fact `Q(a) mod4=a mod4` for every 2-adic a. The shared numerical chart is exact, but a root-position-to-Collatz-state morphism has NOT been authenticated: the actual BBP root coordinates also are 16-grid **thresholds** `4/16`,`12/16`, not parity input residues. The source root's coarse Haar port cannot distinguish these conjugates; retain the oriented head.

## The original BBP instance

Use unchanged source `r(n)=4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2)`, literal `U0=0`, and the analytic identity `x=pi/16`. Exact rational source-tail intervals certify `0.3243F6A8885A...` (12 digits). Treat these chronological digits as the low-to-high 2-adic Collatz parity nibbles. They uniquely determine, to 48 bits:

- `Y_pi = 0xA5888A6F3423 mod 2^48`, the *constructed parity address*.
- `alpha_pi = Phi(Y_pi) = 0x138D4B466283 mod 2^48`, the unique *2-adic Collatz state residue* generating that prefix.

The first 48 exact shortcut Collatz parities of this residue reproduce the 12 digit blocks, with two independent inversions (Bernstein formula and chronological backward branch reconstruction). It does **not** say `alpha_pi` is a positive integer, or that its infinite orbit solves Collatz, or that the chosen pi digit stream is Haar-generic.

The same-branch four-step affine slope `3^s/16` (s odd steps) satisfies `|A|_infty |A|_2 |A|_3=1`, an exact 2/3/real precision accounting identity, not thermodynamic energy.

## Reproduce

```bash
python -m unittest -v test_parity_dual.py
python independent_audit.py
python parity_dual.py
```

See [THEOREMS.md](THEOREMS.md) for nine scoped claims and proofs, [CLAIM_LEDGER.md](CLAIM_LEDGER.md) for hostile receipts, [NEXT.md](NEXT.md) for the missing source-specific arrow, [PROVENANCE.md](PROVENANCE.md) for primary source credits, and [VALIDATION.md](VALIDATION.md) for exact run results.
