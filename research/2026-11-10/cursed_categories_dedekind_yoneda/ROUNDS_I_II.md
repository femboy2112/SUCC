# Cursed Categories, Rounds I–II: archived mechanisms and exact boundaries

This is a clean reconstruction of the two exploratory conversation rounds, **not** a retroactive claim that every sketched mechanism was new or proved. Each mechanism is tagged as **CLASSICAL**, **PAPER DERIVED**, **FINITE TEST**, or **UNVERIFIED**. The mathematics below is kept separate from the BBP original-zero signed-decay question.

## I. The smallest categories that refuse to behave

**(C-1) One object cannot by itself be a nontrivial CCC — CLASSICAL.** If the sole object `*` is terminal, `Hom(*,*)` contains only `id`. A one-object **C-monoid** is extra algebraic structure; it is not literally a one-object CCC. For a *genuine* C-monoid, the Lambek–Scott Karoubi construction yields a CCC; Rodenburg and van der Linden (1989) even built one with exactly two objects and endomorphism monoid the original C-monoid. SUCC's bounded beta/de Bruijn sample checker is **not** a full C-monoid certification: see #579 semantic errata and Main XXIII `scott_omega_causal_weld/THEOREMS.md`.

**(C-2) Two idempotents make an oscillator — PAPER DERIVED in SUCC #582.** On six coordinates take `P2` averaging adjacent pairs `(0,1),(2,3),(4,5)` and `P3` averaging triples `(0,1,2),(3,4,5)`. Both square to themselves. The commutator `C=P2P3-P3P2` is skew-adjoint, rank two, satisfies `C^3=-(2/9)C` and has nonzero eigenvalues `+/- i sqrt(2)/3`. This is a representation of a quotient of the free idempotent-generated monoid, **not** an assertion that the free monoid has that finite spectrum. On the authentic moment source `R(n)`, SUCC proves an oriented adjacent-window area `A_n=<r^n,C r^(n+1)> >0`, `A_n ~ 675/(128 n^9)`. Source sign does **not** imply signed digit balance.

**(C-3) One parity sign builds a Möbius section — PAPER DERIVED in #582.** The radix-16 inverse branches are `s_k(t)=(t+k)/16` for `k=0..15`. Their 16-point Fourier filter bank has parity component `H8 f(t+1)=-H8 f(t)`; a continuous real section is antiperiodic. This is the Möbius line bundle associated with the chosen inverse-branch parity character, **not** a nonorientable physical circle or Berry phase. Signed odd-eight Fourier modes on the actual completed π orbit remain OPEN.

**(C-4) Bicyclic monoid detects a boundary — CLASSICAL.** The monoid with `t s=1` acts on `l2(N0)` by the unilateral shift `s` and its adjoint `t=s*`. Then `t s=I`, `s t=I-|0><0|`: the rank-one boundary projector lives in the **linear operator algebra**, not in the bare monoid. It marks the clock-zero state; it does *not* authenticate its numeric seed without a source-state label.

**(C-5) Two generators can hide a signed covariance — CLASSICAL.** The four-element group `Z2 x Z2` has mixed character `(-1)^(x+y)`. Independent, perfectly locked, and perfectly antialigned fair-bit couplings have identical marginals, while the mixed expectation is `0,+1,-1`. SUCC #593 constructs much stronger 2:3 Haar joinings, including nonproduct normal orbits and a nonproduct exactly-zero mixed `h=8` control. Finite character data cannot substitute for a full joining theorem.

**(C-6) One Haar projector is a convincing liar — PAPER DERIVED in #591.** The leading-digit randomization `Q` satisfies `Q^2=Q`, yet `Q delta_0` is uniform on the 16 rational points `a/16`, and `W1(Q delta_0,Lebesgue)=1/32>0`. Idempotence is not Haar equidistribution; actual zero-selected signed overlap is missing.

**(C-7) Arbitrary sources form a chaotic groupoid under gauge change — PAPER DERIVED in #579.** For rational sources `r,q`, put `P_n^r=sum_(j=1)^n 16^-j r(j)` and `K_(r->q)(n,u)=(n,u+16^n(P_n^q-P_n^r))`. Then `K_(q->v) K_(r->q)=K_(r->v)` and it intertwines their clock-preserving affine recurrences. These arrows need not preserve the real observer. Thus the *undecorated source dynamics* of authentic BBP and zero forcing are equivalent, but their observed phase laws are not. An observer-decorated groupoid does **not** identify them by default.

**(C-8) Source-dependent reverse-beta fixed point — PAPER DERIVED in #579/#584.** `F(g)(n)=R(n)+g(n+1)/16` and `W_F=(lambda z.F(zz))(lambda z.F(zz))` yield `W_F ->beta F(W_F)` by one step. The unique bounded sequence solution is the authentic BBP sum; without boundedness `B(n)+C 16^n` also solves the equation. Beta reduction gives an executable tree *shape*, not its infinite value or a normality theorem.

## II. Arrows become numbers; numbers become categories

**(C-9) The arithmetic hydra — CLASSICAL.** `B(N_>0, x)` is a one-object multiplicative category. Its action on positive integers yields, by category of elements/Grothendieck construction, the divisibility poset `D` with `m->n` iff `m|n`, morphism labeled `n/m`. **The two categories are not equivalent.** The slice `D/n` consists of divisors of `n` and is isomorphic to the product of finite prime-power chains `prod_(p|n)[v_p(n)]`. The inclusion `D/m -> D/n` for `m|n` has right adjoint `d|->gcd(d,m)`. These maps connect the categories *inside numbers* by coherent restriction functors.

**(C-10) Arithmetic Mobius inversion from incidence — CLASSICAL.** For the locally finite divisor poset, `zeta(a,b)=1` if `a|b`, and its convolution inverse is `mu_D(a,b)=mu(b/a)`. On `D/n` the incidence matrices factor into tensor products over prime-power chains, and the inverse is the product of prime-local first-difference operators. This is exact prime-coordinate algebra, not a real-phase cancellation bound.

**(C-11) Yoneda arithmetic pinbed — CLASSICAL.** `y(n)=Hom_D(-,n)` records which rational/natural divisor probes reach `n`. `Nat(y(m),y(n))~=Hom_D(m,n)`; `D` is equivalent to the full subcategory of representables in `[D^op,Set]`. A finite restriction of the pinbed need not be fully faithful.

**(C-12) Finite spans linearize to matrices — CLASSICAL.** A span `X<-S->Y` of finite sets yields nonnegative integer counts `A_(y,x)`. Pullback composition counts matching pairs and becomes matrix multiplication. Signed/complex operator coefficients require a separate group completion/scalar extension; none arise magically from counting.

**(C-13) Partitions, cumulants, Faà di Bruno — CLASSICAL.** The partition lattice's Möbius number is `(-1)^(n-1)(n-1)!`; moment-to-cumulant inversion and higher derivative composition are combinatorial manifestations. Possible SUCC use: mixed observer/carry correlations, not finite-fitted proof of asymptotic independence.

**(C-14) Finite sets carry factorial symmetries — CLASSICAL.** The groupoid of finite sets and bijections has automorphism group `S_n` at `n`; formal groupoid cardinality `sum_n 1/n! = e`. Quotienting computational traces by **verified** renaming symmetries can reduce duplicative proof paths. Never quotient source-distinct computations on aesthetic grounds.

**(C-15) CRT/profinite/adelic family — CLASSICAL.** `Zhat=lim_n Z/nZ ~=prod_p Z_p`, and `A_Q=R x restricted-product_p Q_p` add local rational/real transport. Prime-local data alone does not determine an Archimedean phase or original BBP real winding without an explicit source-attested comparison map. The product of additive characters on diagonally embedded rationals is classical, not a Weyl-sum estimate.

**(C-16) Traces as categories — PROPOSED.** A typed lambda state can be assigned a directed graph/category of finite reductions, source steps, and certificates; presheaves of traces can distinguish equality of output from equality of provenance. A full semantic-preservation/reflection theorem, confluence conditions, cost accounting, and source-locked carry transport are **UNVERIFIED**.

## Triage by actual SUCC utility

- **Already useful:** idempotent commutator/area (#582), inverse-branch parity packet (#582), faithful source gauge caution (#579), zero-anchor arithmetic compiler (#591), two-time joining controls (#593).
- **Cheap next implementation:** divisor-category Möbius, affine/Grothendieck arrows, presheaf cut queries, Farey/Stern-Brocot certificates, typed source-winding transporter.
- **Deep unsolved interfaces:** source-preserving equivalence between a lambda trace category and complete BBP cut observers; independently small *signed original-zero* overlap or odd-eight Weyl mean; completed prime/Gamma Weil compatibility.

## External classical provenance (not SUCC novelty)

- P. Rodenburg, F. van der Linden, *Manufacturing a cartesian closed category with exactly two objects out of a C-monoid*, Studia Logica 48 (1989), DOI 10.1007/BF00370825.
- Lambek and Scott, *Introduction to Higher Order Categorical Logic*, chapters on C-monoids and Karoubi envelopes.
- Basic classical sources: Yoneda lemma, Grothendieck category of elements, incidence algebras, Stern–Brocot/Farey theory, Dedekind–MacNeille completion.
- SUCC #579/#582/#584/#591/#593 are the primary sources for the *project-specific* claims here. The file claims no novel proof of normality or RH.
