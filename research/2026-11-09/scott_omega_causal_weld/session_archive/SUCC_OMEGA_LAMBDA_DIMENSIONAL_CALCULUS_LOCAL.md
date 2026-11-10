# SUCC × generalized omega combinators × dimensional pin-bed calculus

**Local research memo — 2026-11-09/10**  
**Repository policy:** READ ONLY. No GitHub file, PR, branch, commit, issue, or `main` touched.  
**Starting context:** `SUCC_C_MONOID_CAUSAL_SHADOWS_LOCAL.md`; SUCC Main XXI at `43a607818907120d4cdab73d240f5b4d7700b63f`, plus PRs #541 (Fourier–Yoneda pinbed), #543 (driven pinbed), #565 (Haar split idempotent), #568 (Fourier–Gamma), #571 (oriented Haar successor), #574 (two-fiber contrast) — the PRs are NOT assumed merged.  
**Truth state:** A new exact omega growth observation plus standard currying and CRT theorems, locally checked. The desired C-monoid realization as a source-preserving SUCC model, and any source-selected π/RH estimate, remain UNVERIFIED/OPEN. No original priority asserted.

## 1. Exact omega-indexed beta growth: the real spark

For integer `k>=2`, define the **untyped** generalized self-application term

\[
\omega_k := \lambda x.\underbrace{x\,x\cdots x}_{k\text{ occurrences}},
\qquad \Omega_k:=\omega_k\,\omega_k,
\]

where application is **left-associative**. This is established notation for `ω₃ = λx.xxx` and `Ω₃=ω₃ω₃`, e.g. Barendregt, *The Lambda Calculus: Its Syntax and Semantics*, §4.1.8, and Freek Wiedijk's type-theory lecture notes.

Let `E_k(m)` be the left-associated application of `m>=2` copies of `ω_k`. Contract the leftmost `ω_k ω_k` redex (not an arbitrary redex). Direct capture-free substitution proves

\[
E_k(m)\xrightarrow{\beta,\,\mathrm{leftmost}}E_k(m+k-2),
\qquad E_k(2)\to E_k(k)\to E_k(2k-2)\to\cdots .\tag{Ω-growth}
\]

Derivation: the contracted application of two copies is replaced by `k` copies, leaving the other `m−2` copies untouched. Consequently:

| Term | Syntactic copy counts at successive leftmost contractions | Increment |
|---|---|---:|
| Ω₂ | 2,2,2,2,... | 0 |
| Ω₃ | 2,3,4,5,... | 1 |
| Ω₄ | 2,4,6,8,... | 2 |
| Ω₅ | 2,5,8,11,... | 3 |
| Ω_{d+2} | 2,2+d,2+2d,... | d |

**This exact k−2 grading is the proposed omega/SUCC bridge.** `Ω₃` carries a *metalevel* syntactic successor if the index is `number of ω₃ copies minus 2`. It is **not** itself the Church numeral successor (`SUCC = λn f z. f(n f z)`), and none of these Ω terms is normalizing. The chosen reduction strategy and explicit syntax-tree representation matter: a graph reducer with sharing may display a different materialized copy count. Conflating syntactic growth with mathematical/physical space or temporal causation would be a category error.

### Sharp negative theorem: raw Ω₄ is NOT two independent Ω₃ systems

With a budget of `N` expansion steps, a single `Ω₄` trajectory contains at most `N+1` positions along one line of counts `2+2t`. Two independently addressable `Ω₃` counters have states `(i,j)∈N²` and steps

\[
S_x(i,j)=(i+1,j),\qquad S_y(i,j)=(i,j+1),\qquad S_xS_y=S_yS_x.
\]

Their reachable states within total budget `N` number

\[
\#\{(i,j)\colon i+j\le N\}=\frac{(N+1)(N+2)}2.
\]

The two generated actions are independent; the single `Ω₄` action is just one step generator. An assignment that maps an `Ω₄` step to `(i,j)→(i+1,j+1)` reaches only the diagonal and fails the desired 2D coverage. An equivalence requires a **compiler with two labeled coordinate actions and their commuting-square certificate**, not merely a two-copy growth rate.

## 2. Exact positive theorem: a sheet IS a curried single higher-order program

Let `H` be any set (pin heights, observed phase vectors, source labels, or rational measurements) and `X`, `Y` be coordinate sets. A sheet is a map

\[P:X\times Y\to H.\]

The same data have the **canonical lossless curried representation**

\[\widehat P:X\to H^Y,\qquad \widehat P(x)(y)=P(x,y),\]

with inverse `P(x,y)=ev(\widehat P(x),y)`. In any CCC this is the natural isomorphism

\[\boxed{\operatorname{Hom}(X\times Y,H)\cong\operatorname{Hom}(X,H^Y).}\tag{Curry}\]

This is the rigorous core of *two indexed Ω₃-like successor directions ↔ one higher-order computational object*. It is not an identity between the literal untyped combinators `Ω₃⊗Ω₃` and `Ω₄`. It can be implemented by λ abstraction, Church numerals, and pairing:

```
ZERO := λf.λz.z
SUCC := λn.λf.λz.f(n f z)
PAIR := λa.λb.λp.p a b
FST  := λp.p (λa.λb.a)
SND  := λp.p (λa.λb.b)
Sx   := λp.PAIR (SUCC (FST p)) (SND p)
Sy   := λp.PAIR (FST p) (SUCC (SND p))
BED  := λx.λy.PIN x y
```

For **well-formed numeral pairs**, `FST(PAIR a b)=β a`, `SND(PAIR a b)=β b`, and both step orders yield the same canonical pair `(i+1,j+1)`. These terms show definability in untyped lambda calculus; they do **not** by themselves certify an extensional C-monoid or prove a physical realization.

For arbitrary dimension `d`, define `Pin_d(H):= H^{N^d}`. Then

\[
\boxed{\operatorname{Pin}_{d+1}(H)\cong(\operatorname{Pin}_d(H))^{\mathbb N}.}\tag{Layer}
\]

This is a **dimension-preserving change of computational presentation**, not a reduction in topological dimension. The dimensional index of the source is carried by the number of independently recoverable input directions.

### More categorical than currying alone

Let `P_d=(N^d,≤)` be the coordinatewise causal poset. The category of indexed histories and their commuting natural transformations obeys the functor-currying isomorphism

\[\operatorname{Fun}(A\times B,\mathcal E)\cong\operatorname{Fun}(A,\operatorname{Fun}(B,\mathcal E)).\]

The arrow direction on `P_d` encodes accessibility. A functor into a category `E` maps each causally licensed successor to an actual state transformation and must preserve every square/cube relation. This is an exact universal *observer language*; preserving the source-selected physical law is an extra constraint.

The presheaf category `Set^{P_d^op}` is a CCC and has small limits/colimits (for small `P_d`), so it can serve as a principled place to assemble observers, restrict finite pinbeds, and glue patches. This uses **more than** the original one-object C-monoid; a bare CCC does not promise all colimits or arbitrary topological gluing.

## 3. A particularly SUCC-like result: CRT gives a genuine one-clock 2D Fourier pinbed

Finite **periodic** pinbeds have coordinate groups `G=Z/mZ×Z/nZ`. A single clock can carry the entire 2D *translation group* iff `gcd(m,n)=1`:

\[\mathbb Z/(mn)\mathbb Z\cong\mathbb Z/m\mathbb Z\times\mathbb Z/n\mathbb Z,
\qquad t\mapsto(t\bmod m,t\bmod n).\tag{CRT}
\]

This is group-level equivalence and is much stronger than merely pairing all states. For `m=3,n=4`, the clock `t (mod 12)` visits all 12 pins. The independent x/y moves are realizable as distinct powers of the same clock:

\[
S_x=T^4,\qquad S_y=T^9,
\]

since `4=1 (mod 3),4=0 (mod 4)` and `9=0 (mod 3),9=1 (mod 4)`. All product Fourier characters become ordinary 1D characters:

\[\boxed{e^{2\pi i(hi/3+kj/4)}\;\longleftrightarrow\;e^{2\pi i(4h+3k)t/12}.}\tag{Fourier-CRT}\]

The 12 indices `(h,k)` map bijectively to the 12 frequencies `4h+3k mod 12`: **no Fourier information is lost**. An exact formal-root coefficient probe checks all 12 modes against a nonuniform integer-height pinbed. This is a concrete bridge from source CRT/LCM geometry to Fourier–Yoneda observation.

**Hostile control:** for the ordinary hexagonal digit clock, take `G=Z/16×Z/16`. The synchronized one-clock path `t→(t,t)` visits **16 out of 256 pins**; x and y marginals are individually uniform, but the joint mode `(h,k)=(1,15)` equals **1** on the path and **0** on Haar. Thus individual coordinates looking Haar does not imply the joint sheet is Haar. Product cyclicity **fails** because `gcd(16,16)≠1`. One can still enumerate all 256 states using a non-homomorphic mixed-radix algorithm, but then the original independent local translations are *not* both induced by fixed powers of one step generator.

**General form:** `∏ Z/m_i ≅ Z/(∏m_i)` as translation groups iff the periods are pairwise coprime. For `N^d` or `Z^d` with `d>1`, a single *fixed translation generator* does not suffice; arbitrary countable coding alone cannot preserve the full product action.

## 4. Volume as Ω₅ or Ω₃ plus Ω₄; where the sphere fits

The structure behind the proposed `3 Ω₃` versus `1 Ω₃ + 1 Ω₄` is exactly **associativity/currying of product indices**, once an Ω₄-like device has been independently constructed as a two-index sheet:

\[
\mathbb N^3\cong\mathbb N\times(\mathbb N\times\mathbb N),\qquad
H^{\mathbb N^3}\cong (H^{\mathbb N^2})^{\mathbb N}.
\]

It is legitimate to name the compiled second type `Ω₄^SUCC`, but the equality must be **proved for the compiler**; it is not a property of the bare self-application term `ω₄`.

For a 3-ball with its origin omitted,

\[B_R^3\setminus\{0\}\cong(0,R)\times S^2,\quad(r,\hat n)\mapsto r\hat n.\tag{Polar}\]

This realizes precisely **radial one-dimensional SUCC × a two-dimensional angular sheet**. Importantly `\hat n∈S²` represents **two** local coordinates (e.g. polar and azimuthal angles). A single *scalar* θ plus r cannot encode the complete 3D volume as a continuous, locally invertible chart. If θ abbreviates a whole `S²`-valued `Ω₄` angular object, then the user's proposed split is sound.

A round sphere's **metric up to isometry** is determined by a *single scale* `R` (Gaussian curvature `K=1/R²`), but its points still have two independent local degrees of freedom. One scalar describes a **family of shapes**, not every position on a shape. More generally, constant positive curvature alone needs completeness/global topology assumptions to conclude it is the round sphere.

### Why "self-closing sheet" is mathematically promising

An octahedron is a closed triangulated 2D surface with `V−E+F = 6−12+8 = 2`. Each of six vertices has four equilateral faces, giving vertex angular defect

\[\delta_v=2\pi-4\pi/3=2\pi/3.\]

The discrete Gauss–Bonnet sum is

\[\boxed{\sum_{v}\delta_v=6(2\pi/3)=4\pi=2\pi\chi(S²).}\]

This is an exact example of closing a 2D sheet, without adding an extra intrinsic coordinate. It also gives a **global consistency condition** for pinbed curvature. A sphere has no single nonsingular global flat coordinate chart; chart transition/gluing data are genuinely load-bearing. For the Riemann sphere `CP¹`, the two standard complex affine charts glue on the overlap by `w=1/z`. Each complex coordinate carries **two real dimensions**. A separate exact rational-pair probe verifies the chart-transition involution `z→1/z→z` away from zero.

## 5. A higher-cell that stores something positions cannot: holonomy

Two coordinate successors can commute on positions while **phase transport** around their square fails to commute. For group-valued edge transports `U_x(i,j), U_y(i,j)`, compare:

\[U_y(i+1,j)U_x(i,j)\quad\text{and}\quad U_x(i,j+1)U_y(i,j).\]

In an abelian phase group, their ratio is the plaquette holonomy `H_{xy}`. A synthetic exact `16`th-root clock model sets

\[U_x(i,j)=e^{2\pi i j/16},\qquad U_y(i,j)=1.\]

The plaquette has constant nontrivial phase `e^{-2πi/16}`, even though the underlying x/y position successors commute. An exact integer-mod-16 test verifies the nontrivial phase on 64 plaquettes and invariance under a nonconstant vertex gauge transformation. This is **a declared toy connection, NOT a source-derived π or BBP phase**.

Here the higher cell is *not* just a pictorial cube: it carries a measured, orientation-dependent mismatch. This is a promising path for the source-faithful SUCC observer, but **no phase may be inferred from undecorated syntactic copy growth**. The connection/transport maps must be operationally sourced first.

## 6. Proposed formal SUCC calculus (a construction target, not an existing system)

Choose a carrier object `U` in a CCC or C-monoid-derived Karoubi envelope; represent sufficiently well-behaved numeral codes, pairing, and application in it. For each d:

1. **States:** `P_d=N^d` or a source-attested d-dimensional fiber; `0_d=(0,...,0)` is a marked seed.
2. **1-cells:** `s_i:p→p+e_i`, the independent lawful successors; include source/carry labels when present.
3. **2-cells:** declared interchange witness `χ_ij:s_i s_j⇒s_j s_i` only if both paths genuinely agree under the intended semantics, or a typed nonzero discrepancy instrument if they do not.
4. **3-cells:** compare distinct valid reordering witnesses on triple steps, imposing explicit cubical/braid coherence. Higher cells repeat with declared face and interchange laws; they are not automatically new physics.
5. **Observations:** a pinbed functor `P_d→E`, or a presheaf with probe family; Fourier characters are a *complete* finite probe basis when all retained; resource-bounded restrictions can alias.
6. **Geometry:** separate product/index dimension from metric, curvature, connectivity, boundary gluing and phase transport.
7. **Source realization:** a structure-preserving interpretation into actual SUCC carrier dynamics, with original rational BBP source, chronology, zero seed and old cofactor/carry intact where π applications are made.

The desired **compiler theorem**, to be established rather than asserted, is a source-respecting equivalence between (i) independently indexed `d`-axis successor histories and (ii) one explicitly typed higher-order λ term with all `d` steps, probes, signed history, and coherence available. For fixed product cells the currying equivalence is already proved in ordinary mathematics; the unresolved part is **faithful source realization and genuine semantics for the omega grading**.

## 7. The one discriminating experiment for SUCC

Build a `16×16` pinbed. Compare three execution languages:

- `A`: two independent labeled successor operators; full pair frequencies/probes.
- `B`: a bare `Ω₄` leftmost beta expansion; one count-only trajectory.
- `C`: one curried/indexed higher-order object with both labeled directions and explicit projections, or an encoded mixed-radix scheduler with original edge labels.

Pre-register: A and C should agree on every exact two-frequency test and every interchange/holonomy probe *if the compiler has correct laws*. B should fail (nontrivial conditional Fourier modes and independent horizontal/vertical steps absent). Try coprime `3×4` CRT torus as a **positive control**, and equal-period `16×16` diagonal torus as a **negative control**. Add nonflat gauge transports as a test requiring history-dependent rather than endpoint-only observation. This is the weakest useful discriminator for whether a claimed single higher-dimensional Ω unit really retains the sheet.

For authentic π, only after all these foundational tests should source-decorated squares be proposed and tested against #565 future-conditioned Haar, #571 signed currents, and #574 original-zero parity contrast. None of the structural identities entails cancellation for the selected π orbit.

## 8. Local exact receipts

`python /mnt/data/succ_omega_dimension_probe.py` yields:

```
OMEGA: verified beta-growth E_k(m) -> E_k(m+k-2) in 140 independent exact reductions
GRID: independent 2D SUCCs commute; growth-rank contrast in 680 states
CRT: 3x4 torus equals 12-state one-clock scan, 12 exact Fourier modes, local steps (4, 9)
CRT NEGATIVE: 16x16 diagonal leaves 240 pins unvisited, has invisible non-Haar Fourier mode (1,15)
CURRY: verified 340 exact pin readings in uncurried and curried descriptions
SPHERE: verified 4 exact stereographic transitions, octahedral Euler=2 and defect sum=4pi
HOLONOMY: verified 64 synthetic flux plaquettes + gauge invariance, NOT source-derived
SCOPE: no full C-monoid, topological dimension collapse, source-selected decay, or π-normality proof
```

Checks use exact AST beta substitution in the restricted closed-term family, fractions, integer modulo arithmetic, combinatorial counting and symbolic character exponents. No global λ beta confluence, no C-monoid model, no Lean formalization, no original BBP phase proof or complete SUCC test-suite run is claimed.

## 9. Claim ledger

| Claim | State | Scope and strongest counter |
|---|---|---|
| `E_k(m)→E_k(m+k-2)` | DISCLOSED | selected leftmost beta reduction; exact derivation and 140 AST replays |
| Ω₃ syntactic growth is one copy/step | DISCLOSED | does not identify Church SUCC, semantic N, or physical time |
| Raw Ω₄ is a full 2D pair of Ω₃ processes | REFUTED | one generator versus independent two, quadratic versus linear state growth |
| A 2D pinbed ≅ a curried 1D-indexed function-valued pinbed | DISCLOSED CLASSICAL | CCC exponential law; preserves both input axes |
| Finite coprime torus grid ≅ one cyclic clock plus translated axis operators | DISCLOSED CLASSICAL | CRT and complete Fourier character transport |
| Equal-period diagonal 16×16 scan is Haar | REFUTED | 240 unvisited sites and exact `(1,15)` Fourier mode=1 |
| `N³` can be represented as `N×N²` | DISCLOSED CLASSICAL | product associativity/currying, not Ω₅ term equality |
| Volume minus origin ≅ radial line × S² | DISCLOSED CLASSICAL | radial+2-dimensional direction; no scalar angle shortcut |
| Round S² is one-parameter family up to scale | DISCLOSED conditional | requires round/constant-curvature global assumptions, not point coordinates |
| Plaquette phase can be nontrivial on commuting position grid | OBSERVED exact toy | declared gauge transport; independent of authentic SUCC source |
| C-monoid implementation realizes higher Omega hierarchy as actual carrier actions | UNVERIFIED | requires model and faithful compiler |
| Higher cell phase implies original-zero signed BBP cancellation | UNVERIFIED | needs source-derived transport and all-epoch estimate |
| π base-16 normality; RH | OPEN | not changed by this research |

## Primary/background sources

- H. Barendregt, *The Lambda Calculus: Its Syntax and Semantics*, §4.1.8 (ω₃/Ω₃): https://pages.jh.edu/rrynasi1/FoundationsOFMath/Literature/LambdaCalculus/Barendregt1984TheLambdaCalculus.ItsSyntax%2BSemantics.RevisedEdition.pdf
- Stanford Encyclopedia of Philosophy, *The Lambda Calculus*: https://plato.stanford.edu/entries/lambda-calculus/
- Pieter Hofstra and Philip Scott, *Aspects of Categorical Recursion Theory*, §4.5 (C-monoids and CCC): https://www.site.uottawa.ca/~phil/papers/LambekAV.pdf
- Cornell, Church numerals / successor: https://www.cs.cornell.edu/courses/cs312/2008sp/recitations/rec26.html
- Dartmouth, cyclic groups CRT equivalence iff coprime: https://math.dartmouth.edu/~trs/PreTeXtProjects/old/abstract-algebra-refresher-CLI/output/web/section-9.html
- Cambridge, presheaf categories are Cartesian closed, colimits and exponentials: https://www.cl.cam.ac.uk/teaching/1314/L108/l108ex7.pdf
- International Union of Crystallography, *The Euler characteristic as a basis for teaching topology concepts to crystallographers*: https://journals.iucr.org/j/issues/2022/01/00/gj5277/index.html
- Repo read-only lineage: https://github.com/femboy2112/SUCC/blob/main/docs/PI_NORMALITY_FRONTIER.md ; https://github.com/femboy2112/SUCC/pull/541 ; https://github.com/femboy2112/SUCC/pull/543 ; https://github.com/femboy2112/SUCC/pull/565 ; https://github.com/femboy2112/SUCC/pull/571 .
