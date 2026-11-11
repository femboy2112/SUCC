# Signed 3/2 fiber joining claim ledger — 2026-11-10

| ID | Scope / status | Formal receipt / falsifier |
|---|---|---|
| FJ-01 | DISCLOSED: two invariant `T²×T³` joinings with identical Haar marginals and mixed real `h=8` coefficient ≥+cos(π/16) or ≤−cos(π/16) | `PROOFS.md` §1, digit-block iid construction and first-two-digit bound; refutes marginal→joint Haar |
| FJ-02 | DISCLOSED: base-16 NORMAL α with nondecaying mixed h=8 fiber for every epoch; ± orientations | §2, injective `f(n)=floor(3n/2)` chain, finite dependency Var `O_k(N log N)`, square Borel–Cantelli; same-seed synthetic tests are NOT a proof of any single generated sample's normality |
| FJ-03 | DISCLOSED: periodic `α=1/9`, h not divisible by 3, `|T_A|≤2/L_A` despite nonnormal | §3, `K_ell mod9=6,3,0` and `1+ω+ω²=0`; test all residues |
| FJ-04 | DISCLOSED: irrational α avoids eventual uniform phase locking, limsup ≥1/1052929; not an average cancellation | §4, integer recurrence and unstable roots; irrational sparse radix16 digit counterexample shows subsequence T_A→1 |
| FJ-05 | DISCLOSED: sinc local ensemble identity and source resolution inequality | §5, integrate orthogonal integer characters over finite interval; narrow intervals retain coherent phases |
| FJ-06 | DISCLOSED exact rational finite enclosures, OBSERVED displayed decimal ticks: authentic `α=π` at A=263,521,1031, h=8 | §6, original four-pole BBP integer enclosure + separate rational Machin sine/cosine intervals; re-run tests; no asymptotic inference |
| FJ-07 | REFUTED: single ratio-fiber h=8 decay ⇔ full base-16 normality, or either implication | FJ-02 and FJ-03 countermodels in opposite directions |
| FJ-08 | OPEN / UNVERIFIED: original-zero T_A,8(π)→0, source-selected joining restriction, transfer to ordinary Weyl/Basel means, π normality, RH⇒π bridge | Need new authentic signed source theorem distinguishing independent and twisted Haar joinings, wrong seed, PPP-08, full Archimedean carry and prime-power data |

**Common provenance:** #588 ratio K-lemma; #585 Basel–Weyl; Main XXIII #584; source `r(n)` and `U_0=0` not rewritten. `PROOFS.md` contains quantifiers and explicit controls. Tests are finite, same-researcher evidence; no external referee/Lean certificate. All conclusions inherit the weaker unproved source premise when applied to π.
