# CC8 — Genuine source-selected signed moving-window collision budget

**Status: PROVED LOCAL algebraic transport identity; OPEN source-selected budget nonnegativity at every N and radius.** This is a refinement of CC4, not a proof of π base-16 normality.

## Setup (typed original source)

Use the exact original source x_n={U_n}, U0=0, U_(n+1)=16U_n+r(n+1). For a fixed c>0 and n with δ_n(c)=c/(n+1)≤1/2, define

    A_n(δ) = # ordered pairs (i,j), 0≤i,j<n, ||x_i−x_j||_T≤δ
    B_n(c) = # {0≤i<n : ||x_n−x_i||_T≤δ_(n+1)(c)}
    D_n(c) = # ordered pairs (i,j)<n : δ_(n+1)(c)<||x_i−x_j||_T≤δ_n(c).

Here D_n(c)≥0 counts OLD near-pairs exiting the shrinking observation radius; B_n(c) counts NEW near-pairs entering from the newly realized state. Set K>0 and signed budget/slack

    S_n^K(c)=K n² δ_n(c)−(A_n(δ_n(c))−n).

The desired near-pair upper bound at this c is exactly S_n^K(c)≥0. This definition explicitly *excludes* the forced n diagonal pairs from the excess-energy budget.

## Exact signed shell-balance identity, CC8-PROVED LOCAL

Since for each fixed δ, A_(n+1)(δ)=A_n(δ)+1+2B_n(δ), and A_n(δ_(n+1))=A_n(δ_n)−D_n, we obtain

    S_(n+1)^K(c)−S_n^K(c)
       = K c [ (n+1)²/(n+2)−n²/(n+1) ] +D_n(c)−2B_n(c)
       = K c [1−1/((n+1)(n+2))]+D_n(c)−2B_n(c).   (CC8)

**Proof:** Substitute the two exact counting identities and cancel n, n+1 diagonals. The rational simplification in the middle equals 1−1/[(n+1)(n+2)]. No probabilistic, spectral, prime, p-adic or asymptotic assumption. QED.

The original arithmetic forcing enters explicitly:

    B_n(c)=Σ_(m<n) 1[ ||(16^(n−m)−1)U_m + S_(n−m)(m)||≤c/(n+2) ],
    S_d(m)=Σ_(j=1)^d16^(d−j)r(m+j);

    D_n(c)=Σ_(i,j<n)1[c/(n+2)<||(16^|i−j|−1)U_min(i,j)+S_|i−j|(min(i,j))||≤c/(n+1)].

D_n is nonnegative, so it may compensate isolated B_n spikes. What must be proved for infinity is a long-horizon **signed sum** inequality that prevents S from becoming negative simultaneously for all c in the required range; the identity itself does not provide this inequality.

## Hostile original-source N=43,45,51,63 receipts — OBSERVED EXACT FINITE

At c=1, using the genuine rational original states from U0=0:

| n | new B_n(1) | shrinking-window refund D_n(1) | exact S_(n+1)−S_n |
|---|---:|---:|---:|
| 43 | 4 | 2 | −1981/660 |
| 45 | 6 | 0 | −19461/2162 |
| 51 | 5 | 4 | −8271/2756 |
| 63 | 5 | 0 | −29123/4160 |

These negative increments are NOT failures of the cumulative K=3 near-pair bound. They refute the shortcut that the source-selected collision slack must increase on every step. Every input is an exact Fraction; r(n) is original and seed literal zero.

## Genuine surviving target

For every sufficiently large n and each c in [1,(n+1)/2], show S_n^3(c)≥0, equivalently

    A_n(c/(n+1)) ≤ n+ 3n² c/(n+1),

or prove a bound with some fixed K. The ALL-radius finite audits for n=128,..,4096 are precisely finite checks of this target (with a 4/3 radius grid plus exact interpolation). The signed CC8 evolution creates an *operational scalar transport* on (n,c), showing where local neighbor-energy deficits must be offset by shell exit and prior slack. **It does not make the required cumulative sign control easier automatically and is not RH's Weil positivity.**

## Cross-place obstruction, CC8-NOGO

For any fixed k and arbitrarily large M, a rational q=2^k/(2^k M+1) has v₂(q)=k but 0<q<1/M. Thus knowing the exact 2-adic distance v₂(U_n−U_m)=v₂(n−m) alone gives NO lower bound on real circle separation, even with odd denominators. The authentic denominator magnitudes, carries and selected phase chronology must enter any CC8 proof. This is a **universal counterexample to a valuation-only lower bound**, NOT a counterexample to original SUCC π arithmetic.

## Claim boundary

- CC8 signed moving-shell identity: PROVED LOCAL (universal combinatorics, typed to real original source via lag recurrence).
- Exact negative local source increments: OBSERVED EXACT FINITE.
- Four-pole zero-seed all-n K3 signed budget: OPEN.
- Uniform Fejér critical energy and π normality: OPEN.
