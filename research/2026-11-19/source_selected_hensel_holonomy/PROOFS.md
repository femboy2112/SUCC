# 15 Angry Blind Fibonaccis — source-selected Hensel frames and causal order Jacobians

**Date:** 2026-11-19. **Research-only**; stacked on SUCC Jacobian objective gluing PR #669 at `5a71c7e33f0445236fd4f69da872ca5c71d1530d`. Exact original four signed BBP poles and literal `U_0=0` remain unchanged. These are new-to-this-research synthesis and derivations from existing SUCC / classical arithmetic, not global novelty claims. **R0, base-16 π-normality, and all-mode signed Weyl cancellation remain OPEN.**

## Source, types, and the relevant predecessor

For positive integers n, retain

\[
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},\quad
U_0=0,\quad U_{n+1}=16U_n+r(n+1),\quad U_n+T_n=16^n\pi/16.
\]

The signed Mellin impulse polynomial is `Q(t)=4-2t^3-t^4-t^5=(1-t)H(t)`, with `H(t)=4+4t+4t²+2t³+t⁴`. The authentic `r(n)` is **not** replaced by any Fibonacci forcing.

Declare the *auxiliary representation* `A=[[1,1],[1,0]]`, `M=A^{-1}=[[0,1],[1,-1]]`, and `T=Sym^4(A²)` acting on quartic monomials. This is the construction from SUCC #667, not an already established factor map from BBP's real orbit. SUCC #666 proved `H(M)=8I+M`, `det H(M)=55`; #668 established fixed-eigenvalue `T`/16 coincidences at 11 and 29 and the nonlift of eigenvalue exactly 16 from 11 to 121. #669 created the source+seed Jacobian, forward prime-rank repair, objective agreement and conditional Weyl gates. This note strengthens the **connection** among these statements and adds a chronological source-order calculation.

All `p`-adic descriptions below operate on exact rational or integer algebra and finite-field/power rings. They are **not** automatically real Fourier phases.

## SHH-01 — The ORIGINAL BBP filter picks the radix-matching 11-adic eigenline (EXACT)

The matrix source filter is

\[
H(M)=\begin{pmatrix}8&1\\1&7\end{pmatrix},\quad \det H(M)=55.
\]

Modulo 11, its kernel is the line spanned by `(1,3)^T`; its image is the line spanned by `v=(8,1)^T`. The Fibonacci transfer `A` acts as `4` on the kernel and `8` on the image:

\[
A(1,3)^T=4(1,3)^T,\qquad Av=8v\pmod{11}.
\]

Let `w(a,b)=(a⁴,a³b,a²b²,ab³,b⁴)^T`. Since `T=Sym^4(A²)`, on the surviving image line

\[
Tw(v)=8^8 w(v)=16w(v)\pmod{11},\qquad w(v)=(4,6,9,8,1)^T.
\]

The previously recorded left eigenrow `ell_11=(4,2,10,10,1)` obeys `ell_11 T=16 ell_11 mod 11` and `ell_11·w(v)=1 mod 11`. This identifies a **dual-normalized, source-selected** finite-field eigenchannel, rather than merely two matching determinant factors.

**Hostile differentiation:** the same homogeneous `T` has a 16-eigenchannel modulo 29, but `det H(M)=55` is a unit modulo 29, so `H(M)` selects no one-dimensional image there. The source mutation `H_*(t)=H(t)+t⁴` has `det H_*(M)=116`, a unit modulo 11, destroying the source-filter rank-one selection while leaving the auxiliary Fibonacci transfer unchanged. Neither mod-29 coincidence nor generic geometric golden structure supplies this source selection.

**Boundary:** this theorem uses `H` evaluated on a *declared* Fibonacci matrix. There is no authenticated map from its eigenchannel to the selected Archimedean phase `e(U_n)`; it is not a π-normality estimate.

## SHH-02 — The 11-adic no-lift is repaired by a moving eigenvalue, not by changing the carrier (EXACT)

The matrix has characteristic polynomial

\[
\chi_T(X)=(X-1)(X^2-7X+1)(X^2-47X+1).
\]

Over `F_11`, the source-selected line's eigenvalue is `16 ≡ 5`. The quadratic `f(X)=X²-47X+1` has `f(16)=-495=-45·11`, `f'(16)=-15`, an 11-adic unit. Hensel's lemma therefore gives a **unique root** `lambda_11 ∈ Z_11` congruent to 16 modulo 11, with

\[
\boxed{\lambda_{11}\equiv104\pmod{121}.}
\]

The underlying Fibonacci eigenvalue `a_s` is the unique root of `a²-a-1=0` with `a_s≡8 mod 11`; it lifts to `a_s≡85 mod 121`, and `a_s⁸≡104 mod 121`. The complementary root `a_k≡4 mod 11` lifts to `37 mod 121`. Because their difference is a unit, the spectral projector onto `a_s` exists over `Z_11`. The source filter eigenvalues on these two lines are `8+a_s^{-1} ≡92 mod121` (unit) and `8+a_k^{-1} ≡44 mod121` (valuation one). Hence the original filter identifies the surviving 11-adic channel at **all** prime-power resolutions through a spectral projector, even though its literal rank-one image only exists modulo 11.

Similarly, at p=29 the factor `X²-7X+1` has a simple root `16 mod 29` with unique lift `lambda_29≡683 mod841`. But no corresponding source-filter rank drop occurs.

For either p, choose a p-adic eigenrow `ell_p T=lambda_p ell_p`, and a *moving observer frame*

\[
\rho_p=16/\lambda_p\in\mathbb Z_p^\times,\quad
 g_n=\rho_p^n,\quad a_n=g_n\ell_p T^nv.
\]

Then `a_(n+1)=16 a_n` identically. This is **exact frame compensation**, not changed Fibonacci dynamics, and not an authenticated real-phase semiconjugacy.

At the first new precision,

\[
\rho_{11}\equiv56=1+55\pmod{121},\qquad
\rho_{29}\equiv117=1+116\pmod{841}.
\]

Thus `rho_11^n≡1+55n mod121`, `rho_29^n≡1+116n mod841`. The frame is invisible at the first p-adic digit, visible at the second, and returns every p forward clocks at that second resolution. Moreover, by elementary binomial lifting (odd p), `v_p(rho_p^{p^k}-1)=k+1`, so precision can reveal further unrecorded rotational memory. This **does not contradict** #668's fixed-scalar no-lift: the coefficient is now `lambda_p`, not 16.

## SHH-03 — A rotating frame can manufacture false Weyl cancellation (EXACT HOSTILE)

A crucial control: choose the *separately declared* complex additive readout of the 11-adic frame, `eta_n=e((g_n-1)/121)`, with `e(t)=exp(2πit)`. As `g_n≡1+55n mod121`,

\[
\eta_n=e(5n/11),\quad \sum_{n=0}^{10}\eta_n=0.
\]

For a **perfectly locked real orbit** `z_n=1`, the masked mean `B^{-1}Σ z_n eta_n` tends to zero even though the correct Weyl mean is identically one. The same holds for the original four-pole forcing with hostile seed `s=-π/16`: then `U_n(s)=-T_n→0`, so `e(hU_n(s))→1` for each fixed h, but multiplying by eta_n gives a mean tending to zero.

This is an exact refutation of the inference **"moving-frame cancellation implies actual phase mixing"**. The p-adic readout-to-complex phase is a declared observer map, not a source necessity. The correct objective observer must transport all local data into a common real Fourier basis (remove eta) before testing Weyl.

## SHH-04 — Noncommuting **chronological source** maps create a source-order Jacobian (EXACT)

Define the affine input transformation `S_a(z)=16z+a`. For consecutive *actual BBP inputs* `a=r(n)`, `b=r(n+1)`, reversing their order changes the resulting state by

\[
\boxed{(S_b\circ S_a)(z)-(S_a\circ S_b)(z)=15[r(n)-r(n+1)]=:D_n.}
\]

Equivalently, in the affine representation `M_a=[[16,a],[0,1]]`, the **matrix product difference**, not the group commutator, is `M_b M_a-M_a M_b=[[0,D_n],[0,0]]`.

The source-positive representation

\[
r(n)=\frac{6}{a(a+3)}+\frac4{a(a+4)}+\frac5{a(a+5)},\qquad a=8n-7,
\]

proves `r(n)>r(n+1)>0`, with strictly decreasing positive finite differences. The source order defect obeys

\[
\boxed{D_n>0,\qquad D_n=\frac{225}{32n^3}+O(n^{-4}).}
\]

The Jacobian with respect to the **four original pole amplitudes** is the explicit row

\[
\boxed{\frac{\partial D_n}{\partial c_j}
=\frac{120}{(8n-\beta_j)(8n+8-\beta_j)},\quad\beta=(7,4,3,2).}
\]

This is an order-sensitive *source* Jacobian. The homogeneous state derivative alone, `DS_a=16`, cannot see it. Both orderings are declared counterfactual computations; the authentic chronological BBP source always uses its original ordering.

**Delayed real-circle visibility:** `D_7<1/32`, and complete monotonicity makes `D_n` decrease thereafter. For every `n>=7` define `d_n` as the least nonnegative integer with `16^{d_n}D_n>=1/32`. Minimality and radix 16 give

\[
\boxed{1/32\le16^{d_n}D_n<1/2,\qquad d_n=3\log_{16}n+O(1).}
\]

If the two source orderings have identical later forcing, their states at all later times remain separated in the REAL circle by at least `1/32` at clock `n+1+d_n`, with chord distance at least `2 sin(π/32)`. A nominally tiny chronological ordering defect becomes macroscopically observable at a *logarithmic* delay. No reverse-time operation occurs.

The theorem is not a Weyl estimate: the defect compares the authentic source to a **different (swapped) source**, and the original same-forcing wrong-seed counterexample has identical `D_n` yet is real-phase locked.

## SHH-05 — The genuine BBP p² pole and the order Jacobian share an exact arithmetic pulse (EXACT)

For every prime `p>=7`, put `n_p=(p²−1)/8`. Then `n_p` is an integer and `r(n_p+1)` has the original BBP pole `4/p²`. All other forcing denominators at `n_p` and `n_p+1` are p-adic units (their offsets from p² are `−8,−5,−4,−3` and `+3,+4,+5`, none divisible by p>=7). Therefore

\[
\boxed{v_p(D_{n_p})=-2,\qquad p^2D_{n_p}\equiv-60\pmod p.}
\]

In contrast, as `p→∞` through odd primes,

\[
\boxed{p^6D_{n_p}\longrightarrow3600}\quad\text{in the real metric}.
\]

The same authentic BBP source-order event is **p-adically large** (`|D|_p=p²`) and **really tiny** (`D~3600/p⁶`). For sufficiently large p its delayed phase re-entry clock obeys `d_(n_p)=6 log_16 p+O(1)`. This is a certified arithmetic-to-real *counterfactual observation* bridge, not an all-shell signed real correlation.

At p=11, this event lies immediately before BBP clock `16` (n_p=15), precisely the prime at which SHH-01 selects the source-filtered Fibonacci eigenchannel. At p=29, the analogous event exists but the source-filter rank selection does not. This 11-versus-29 contrast is useful for a hostile source/observer test but does not prove a causal relationship between the filter and the chronological phase beyond the shared original source label.


## SHH-06 — One matched-leading-jet mutation breaks BOTH source signatures (EXACT HOSTILE)

The first source-mutation control above `H+t⁴` changes the leading source coefficient. A stronger single mutation preserves the source's mass zero and its first jet `Q'(1)=-15`, hence the leading `15/(64n²)` forcing asymptotic, while changing both the Hensel source-filter selection and prime-square commutator signature. Set

\[
\boxed{Q_*(t)=Q(t)+(1-t)^2,\qquad H_*(t)=H(t)+(1-t).}
\]

Its forcing is strictly positive and decreasing, with

\[
r_*(n)=r(n)+\frac{2}{(8n-7)(8n-6)(8n-5)}
=r(n)+O(n^{-3}).
\]

The auxiliary Fibonacci source filter becomes **exactly scalar**:

\[
\boxed{H_*(A^{-1})=(8I+M)+(I-M)=9I,\quad\det=81.}
\]

Thus the rank-one 11-adic image selected by the original BBP `H` is absent. At the original pole-square clocks the coefficient of `1/p²` has changed from 4 to 5, so for every prime p>=7,

\[
\boxed{p^2D^*_{(p^2-1)/8}\equiv-75\pmod p}
\]

versus **-60 modulo p** for the real BBP source. The source mutation keeps the same initial seed 0, `Q(1)`, `Q'(1)` and leading asymptotic, but it is **not the original four-pole source** (it adds source-lag terms). Its normality status is not assumed. This is a genuine independent discriminator rather than a positivity or first-jet argument.

## SHH-07 — Global agreement and the precise missing Weyl theorem


Let `a_(p,n)=e(h pr_p(U_n))`, where `pr_p(U_n)` is the canonical p-primary fractional part of the **rational** original state, and let `b_(p,n)=e(h(U_n-pr_p(U_n)))`. Then `e(hU_n)=a_(p,n)b_(p,n)` exactly. Zero averaging of a selected local p-wave does **not** establish zero averaging of this product. A locked same-forcing seed demonstrates the missing source/phase coupling.

A candidate next step is to condition the signed two-channel phase correlations on original-source 11-adic eigenline/resolution classes, retain full CRT real cofactor and all integer carries, and test whether the authentic zero-seeded source *precludes inverse tracking* at all late shell scales. All frame twists must be explicitly undone before forming the original Weyl mean. In a source-authenticated growing shift-bank `S_B`, prove `Q^U_(B,h)(S_B)→0` for each fixed h (with `|S_B|→∞`, `max S_B=o(B)`) or an all-shell positive lower bound on `H_(B;1,1)` (R0 only). These are still **OPEN**, and neither follows from SHH-01 through SHH-06.

### Verdict discipline

| ID | Claim | Status | Strongest hostile control |
| --- | --- | --- | --- |
| SHH-01 | Original BBP filter selects the 11-adic radix-matching Fibonacci line | Exact in declared module | p=29 match lacks filter selection; `H+t⁴` mutation breaks it |
| SHH-02 | Moving 11/29-adic eigenvalues and compensated frame repair | Exact by Hensel and binomial lifting | Fixed multiplier 16 still fails at p² |
| SHH-03 | Raw moving-frame phase cancellation can be completely fake | Refuted shortcut via locked control | `z_n≡1` and same-forcing `s=-π/16` |
| SHH-04 | Authentic ordered-source affine commutator and delayed phase separation | Exact counterfactual | Wrong seed leaves commutator unchanged |
| SHH-05 | Prime-square source-order valuation / real-scale contrast | Exact all primes p>=7 | p=29 has same pulse but no source spectral rank drop |
| SHH-06 | Matched source-zero/jet mutant breaks both the 11-adic selected line and p² pulse residue | Exact separating control | Q+(1−t)² retains leading n^-2 forcing |
| TARGET | Actual original-zero BBP source forbids all-shell inverse cofactor tracking | **OPEN** | Need a signed source-selected inequality and a fresh hostile holdout |

**No backward-time physics, quantum-speedup evidence, independent model witness, base-16 π-normality or RH proof is claimed.**
