# BBP one-digit → two-digit Haar: a source-exact spatial recursion and a real-time obstruction

**2026-11-09; research only.** Source: the original four signed BBP poles, literal U0=0. Parent: SUCC #562 at ff52b3d8cfe4a94c30716596bda4ce960d054f73. Original source/provenance, formal files, archives and main are unchanged.

**Status.** Spatial 2-adic Haar lift: PROVED PAPER (using inherited #527 zero/isometry). Real π one-digit Haar: OPEN. Real π two-digit Haar: OPEN. Full base-16 π normality: OPEN. No novel scholarly priority claimed for classical p-adic analysis, finite Fourier, or normality definitions.

## 1. Three incompatible meanings of BBP digits

(A) Spatial 2-adic precision digits: V(n) mod16 and floor((V(n) mod256)/16) of one **fixed 2-adic source state**. (B) Temporal 2-adic low-nibble pair: (V(n) mod16, V(n+1) mod16). (C) Actual **real hexadecimal digits** d_n,d_(n+1) of π. The last means an actual chronological normality question. A proof of Haar for (A) says nothing by itself about (B) or (C).

The source is

r(x)=4/(8x−7)−2/(8x−4)−1/(8x−3)−1/(8x−2)
     =(120x²−89x+16)/((2x−1)(4x−1)(8x−7)(8x−3)).

Every factor of the **combined denominator** is odd on Z₂. The bounded 2-adic source function

V(x)=Σ_(j≥0) 16^j r(x−j)

converges on Z₂ and obeys V(x+1)=16V(x)+r(x+1). The nontrivial exact V(0)=0 and V(n)=U_n(0) for n≥0 are inherited from SUCC #527, not inferred from a finite replay.

## 2. BSHL-01: closed original-source first spatial digit

For every nonnegative integer n,

    f(n)=V(n) mod16 = [2(n mod2)−n] mod16.

Proof: V(n)=16V(n−1)+r(n); thus V(n)≡r(n) (mod16) for n≥1, and V(0)=r(0)=0 (mod16). Original numerator P(n)≡8n²+7n, denominator D(n)≡8n²+2n+5 (mod16); D(n) is a unit. For n=2m, P(n)−(−n)D(n) is a multiple of 16 because it is 8m(m−1) mod16. For n=2m+1, P(n)−(2−n)D(n) similarly is 8m(m−1) mod16.

First residue cycle:

    (0,1,14,15,12,13,10,11,8,9,6,7,4,5,2,3).

It is a permutation (indeed f∘f=id). Hence the first **spatial 2-adic nibble** is exactly Haar over each complete 16-class clock. This is NOT simple normality of π's real hexadecimal digits.

## 3. BSHL-02: explicit ALL-k Haar-preserving recursive nibble formula

For every k≥1, a∈Z₂, t∈Z₂,

    V(a+16^k t) ≡ V(a)+16^k t r'(a)   (mod16^(k+1)).       (1)

Proof: for δ∈16^k Z₂ the source is 2-adic analytic and r(a+δ)−r(a)−δr'(a)∈δ²Z₂. The terms j≥1 of V(a+δ)−V(a) are in 16δZ₂ since the rational source is 1-Lipschitz. Both δ² and 16δ are contained in 16^(k+1)Z₂, proving (1) for every k, not merely a finite computation.

Crucially, the **original four poles** give

r'(a)=−32/(8a−7)²+1/(2a−1)²+8/(8a−3)²+2/(4a−1)²,

so

    s(a)=r'(a) mod16 = 10+(2a−1)^(-2) mod16
    = 11 when a mod4∈{0,1}; =3 when a mod4∈{2,3}.

Both 11 and 3 are units modulo16. Define the next spatial digit

z_(k+1)(a,t)=floor((V(a+16^k t) mod16^(k+1))/16^k).

Then

    z_(k+1)(a,t) = [ z_(k+1)(a,0)+s(a)t ] mod16.           (2)

For each old k-digit residue class a, as the NEW clock-refinement nibble t runs 0..15, the next spatial digit visits ALL 16 values exactly once. Induction establishes Haar preservation at **every spatial 16-adic resolution**.

**Requested 1→2 formula from the first digit.** Let d be the first spatial nibble, a=f(d), and

    b=(0,14,15,2,0,6,14,5,5,11,1,4,14,12,8,15),
    b_a=floor((V(a) mod256)/16).

Then the explicit source-recursive map is

    Lift₂(d,t) = (d, [b_(f(d))+s(f(d)) t] mod16).          (3)

The additional coordinate t is mathematically necessary: 16 possible first-digit values alone cannot encode all 256 two-digit pairs. For the **complete finite source-clock fiber** (d,t)∈Z16² with uniform counting measure, (3) is a bijection, hence its two-spatial-digit output is *exactly* Haar. No random BBP digit premise is needed.

## 4. BSHL-03: decisive counterexample from this very same source

The temporal first-nibble process has d_n^(2-adic)=f(n mod16). Its exact next-time map is

    g(d)=d+1 mod16 if d even,
         d−3 mod16 if d odd.

This is the 16-cycle g=f∘(+1)∘f^{-1}. Across one time period, each first digit occurs once, but **only 16 of the 256 adjacent pairs** occur. Thus, for the temporal pair law,

    E1=16Σ_a p1(a)²−1=0,
    E2=256Σ_(a,b)p2(a,b)²−1=15.

For k consecutive low-nibble *times*, only 16 k-words occur, and E_k=16^(k−1)−1. This proves that spatial Haar and temporal Haar are distinct even within the original BBP 2-adic source.

Further, for rational seed s=1/5 the original forcing gives U_n(s)=U_n(0)+16^n/5. This difference is zero mod256 in Z₂ once n≥2, while at the real place its fractional component stays **1/5** at every n. Source-spatial Haar cannot by itself select the real origin. The distinct p=2 *integral* residue also must not be mistaken for a nontrivial fractional additive character.

## 5. BSHL-04: exact real π two-digit readout, including ALL prime residues

The authentic completed orbit is x_n={U_n+T_n}={16^(n−1)π} for n≥1; T_n=Σ_(j≥1)16^-j r(n+j). Its actual consecutive real digits satisfy

    d_n=floor(16x_n);
    d_(n+1)=floor(16{16x_n});
    16d_n+d_(n+1)=floor(256x_n).                         (4)

The full additive CRT identity of #558/#562 gives, for all denominator prime powers,

    x_n={Σ_(p|den(U_n)) [U_n]_p + T_n}.                 (5)

Every inherited p-primary residue and the positive analytic Green tail is retained; it is NOT a single newly born prime. With the **literal real carry** κ_(n+1)=floor(16{U_n}+r(n+1)) and #562's complete all-prime winding ledger, the completed digit obeys

    d_n=(κ_(n+1)+δ_(n+1)) mod16,
    δ_(n+1)=floor({16{U_n}+r(n+1)}+T_(n+1))∈{0,1}.        (6)

The full 2-digit real word is therefore a two-time, all-prime and analytic-boundary observable. A rational-tail interval certifies a word only if both endpoints lie in the same 256-cell. Correctly distinguishing one time residue, one precision digit and one **real chronological digit** is the load-bearing interface.

## 6. BSHL-05: exactly 225 remaining two-digit Fourier modes

For N genuine chronological starting positions, p2(a,b)=N^-1 #((d_n,d_(n+1))=(a,b)), with row marginal r_a and column marginal c_b. The column marginal is just the one-digit frequency shifted one time step, so its ℓ¹ distance from the row marginal is ≤2/N. Define

    Erow=16Σ_a(r_a−1/16)²;   Ecol=16Σ_b(c_b−1/16)²;
    E2=256Σ_(a,b)(p2(a,b)−1/256)²;
    J_ab=p2(a,b)−r_a/16−c_b/16+1/256.

Elementary orthogonal projection and Fourier Parseval give, EXACTLY for every finite table,

    E2=Erow+Ecol+256Σ_(a,b)J_ab²
      =Erow+Ecol+Σ_(u,v=1)^15 |hat p2(u,v)|².           (7)

For cyclic finite windows (ONE artificial endpoint pair), Erow=Ecol=E1 and

    E2=2E1+E_mixed.                                     (8)

Hence even a PROVED one-digit Haar law would leave **225 mixed modes**. One-digit Haar plus vanishing of these 225 signed two-time Fourier coefficients implies two-digit Haar, but the required original-zero BBP arithmetic estimate is OPEN.

If a stationary circle measure has uniform one-digit marginals, P_ab=16p2(a,b) is doubly stochastic. Conversely, every *strictly positive* doubly stochastic P is a mixing, full-support stationary Markov digit model with uniform single-digit law and pair law P/16. Example P=(3/4)I+(1/4)J/16: all 256 transitions positive, E1=0, E2=135/16>0. Thus even one-digit Haar + topological full support + mixing do NOT imply two-digit Haar without a source-specific condition. A repeated 16-symbol cycle has E1=0, E2=15; order-2 de Bruijn digits have E1=E2=0 yet E3=15.

The exact **source-specific signed current to prove next** is

    C_(A,a,b) = (1/A)Σ_(n=A)^(2A−1) 1_(d_n=a)
                [1_(d_(n+1)=b)−1/16].                  (9)

If all C_(A,a,b)→0, and real one-digit Haar is independently proved, two-digit Haar follows. This is an equivalent reformulation until the original-zero four-pole source pays a nontrivial upper bound. General depth uses the same 16-child current at every word w.

## 7. BSHL-06: fresh finite original source certificate (not a limit)

The protocol was committed first at 2f163e155998bab2d89240a3a97ff715f63ea3a5. A 65,536-digit HEX prefix of the authentic zero-selected BBP source was then certified by TWO integer outward intervals (guards 24/32), with independent rational Machin/arctan validation of 128 digits. The 40,960-character earlier prefix matches #561's SHA256 when stored with newline. A separate rational Green-tail oracle checked 128 real 2-digit words.

SHA256 of the full 65,536-character stream with trailing newline:

    e42ee060201573db4a32a8c8e0a4ccac5a6cb061ae1ac8d71809234c58dfae53

Finite **cyclic** 65,536 sample: E1=16997/134217728≈0.000126638; E2=35323/8388608≈0.004210830; E_mixed=265587/67108864≈0.003957555.
Finite **linear** genuine 65,535 pairs: E2≈0.004205415; mixed≈0.003952721; all 256 words observed, pair counts range 213..302.

These are **finite** observations, not proof of real single-digit or pair normality. A separate complete local research bundle includes the exact stream, complete 16×16 tables, deterministic receipt, full source module and 22 focused passing tests. The GitHub branch contains an additive compact implementation and root-discoverable regression tests; their exact-head hosted CI is an independent gate.

## Next theorem and proof scope

Aim for an authenticated original-zero **signed 225-mode current** or a source-derived contraction of E_mixed, retaining both chronological real carries, the full #562 all-prime CRT residues, the 2-adic integral lift and the BBP future tail. The two-digit theorem would still leave k≥3 normality obligations. Must distinguish the mathematical coherent seed s*=−π/16, the dyadic shadows, the 16-cycle and the full-support Markov control. Do not claim base-16 normality or scholarly priority.

Prior internal source: #527/#528 (2-adic V and nonfactor), #557/#559/#561 (word Fourier and finite certified digits), #558/#562 (all-prime additive gluing and carry), #564 (source-twisted moving floors). Classical external background: Bailey–Crandall 2001, 2-adic Taylor, finite Fourier/Parseval, stationary Markov shift, Machin arctan.
