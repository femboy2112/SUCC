# Circle/line geometry as a productive L/R observer

Translator bearing, 2026-11-11. Baseline inspected: `SUCC_worktree`, branch `aletheia/cursed-categories-dedekind-yoneda-2026-11-10`, commit `964768cd1fa5116f521625abfaaad8d8fab0f222`. This note makes no changes to that checkout. It applies the repository's steelman/crucible/verdict discipline to the new circle/line observer, after reading `AGENTS.md`, `docs/METHOD.md`, the round-III computation-graph note, and the pi frontier.

## 1. Strong conclusion and its exact scope

There is a finite program, using unbounded integer registers, which starts from the Euclidean unit circle and its arc-length functional, computes exact rational interval certificates, and emits an infinite Stern–Brocot L/R path converging to circumference/diameter. Every individual branch decision terminates. The key facts are a geometric integral identity, an explicitly contracting rational source, and irrationality of pi; none of the input is a list of pi digits or an oracle for comparing pi with rationals.

A useful additional structure survives the translation: each rational projective arrow has a rational **arc-length distortion cocycle**. Conic preservation alone discards that structure. The cocycle permits exact geometric checks on proposed transfers of measure or cancellation.

These are construction/proof statements, not claims of a novel theorem in the literature. They do not prove a temporal equidistribution estimate for the source-selected orbit. The repository's currently selected contrast `u_+(A)-u_-(A)` still needs an actual all-large-epochs bound, including its source, zero seed, clocks, signs, winding, and tail errors.

## 2. Keep two uses of the number line distinct

The coordinate `t` below parametrizes a geometric circle. The scalar `x` computed by the observer is the length ratio of that circle. These are different typed roles, even though both can be represented by real numbers. Mapping the computed scalar pi to the circle point `P(pi)` does not identify that point with one full turn or with the arc used to define pi.

Let the circle be `C = {(X,Y): X²+Y²=1}`, with the Euclidean metric inherited from the plane. Let the real line carry its usual order and arithmetic. Define

$$
P(t)=\left(\frac{1-t^2}{1+t^2},\frac{2t}{1+t^2}\right).
$$

This is stereographic parametrization. Direct differentiation gives

$$
\|P'(t)\|=\frac{2}{1+t^2}.
$$

The interval `0 ≤ t ≤ 1` traverses the first quadrant, from `(1,0)` to `(0,1)`. If `c` denotes circumference/diameter, then symmetry and diameter 2 give

$$
c=4\int_0^1\frac{dt}{1+t^2}.\tag{1}
$$

Thus the internal mathematical knowledge needed by the observer is explicit: a rational circle equation, a parametrization, the Euclidean arc-length rule, and exact rational arithmetic. We use the conventional name `pi` for the constant `c` identified by (1).

The metric matters. A projective conic by itself is not a circle with an arc-length functional. An ordinary Euclidean line is not globally isometric or homeomorphic to a circle. The correct projective correspondence includes the point at infinity; the correct metric correspondence equips the line chart with

$$
\frac{4\,dt^2}{(1+t^2)^2},
$$

rather than pretending that its ordinary Euclidean metric `dt²` is preserved.

## 3. An exponentially contracting source authenticated by that geometry

Equation (1), evenness, and the substitution `u = 2t - 1` imply

$$
\pi=2\int_0^1\frac{dt}{1-2t(1-t)}.
$$

On this interval, `0 ≤ 2t(1-t) ≤ 1/2`. The geometric series therefore converges uniformly; termwise integration is justified. To evaluate its coefficients, write `B(p,q)=integral_0^1 t^p(1-t)^q dt` for nonnegative integers. Integration by parts, taking the antiderivative of `t^p`, gives for `q≥1`

$$
B(p,q)=\frac{q}{p+1}B(p+1,q-1).
$$

The endpoint terms vanish. Iterating to `B(p+q,0)=1/(p+q+1)` gives `B(p,q)=p!q!/(p+q+1)!`. In particular,

$$
\int_0^1 t^n(1-t)^n\,dt=\frac{(n!)^2}{(2n+1)!}.
$$

Consequently

$$
\pi=\sum_{n=0}^{\infty}\frac{2^{n+1}(n!)^2}{(2n+1)!}.
\tag{2}
$$

This is a derivation from the retained geometry, not an inferred identity from numerical agreement.

Set

$$
\alpha_j=\frac{j}{2j+1},\qquad
Z_j(y)=2+\alpha_j y,
\qquad
Z_j=\begin{pmatrix}j&4j+2\\0&2j+1\end{pmatrix}.
$$

Composition convention: `MN` acts first by `N`, then by `M`. Write

$$
A_k=Z_1 Z_2\cdots Z_k,
\quad A_0=I,
\quad I_k=A_k([3,4]).
$$

Every `Z_j` maps `[3,4]` into itself, is increasing, and has slope `alpha_j < 1/2`. Thus the intervals are nested and

$$
|I_k|=W_k=\prod_{j=1}^{k}\frac{j}{2j+1}
=\frac{2^k(k!)^2}{(2k+1)!}<2^{-k}\quad(k\ge1).
\tag{3}
$$

Expanding the affine composition gives

$$
A_k(y)=2\sum_{n=0}^{k-1}W_n+W_k y.
$$

Its unique limiting value is exactly (2). More strongly, define the remaining tail after `k` factors by

$$
\tau_k=2\sum_{r=0}^{\infty}\prod_{j=k+1}^{k+r}\alpha_j,
$$

where the empty product is one. Then `pi=A_k(tau_k)`. Every factor lies in `[1/3,1/2)`. Comparing products with powers of `1/2` gives `tau_k<4`, since the first positive-length product is already strictly smaller. Comparing with powers of `1/3` gives `tau_k≥3`, and strictness follows from the product with `r=1` when `k≥1`, or the product with `r=2` when `k=0`. Thus

$$
3<\tau_k<4\quad\text{for every }k\ge0.
\tag{3a}
$$

Therefore geometric pi lies strictly between the endpoints of every `I_k`. The source is finite syntax: the integer counter `j` generates all its factors.

A directly implementable state is `A_k = [[q,r],[0,s]]`. Starting from `(q,r,s)=(1,0,1)`, consuming the factor with index `j` changes the registers simultaneously to

$$
q'=qj,\qquad r'=q(4j+2)+r(2j+1),\qquad s'=s(2j+1).
$$

The certified endpoints are `(3q+r)/s` and `(4q+r)/s`. No floating-point comparison appears.

### Literature connection

Gibbons' primary paper [G] develops safe streaming pi spigots using these affine factors, interval tests, right-side input consumption, and left-side digit production. It explicitly allows growing integer memory. Its later `piG2`/`piG3` optimization removes the safety test under Conjecture 1; that shortcut is not the certified algorithm used here. The direct geometric derivation and productivity argument in this note state the relevant justification explicitly.

## 4. Exact L/R convention: do not silently swap sides

Use the round-III endpoint convention

$$
E=\begin{pmatrix}a&c\\b&d\end{pmatrix},
\qquad \frac ab<\frac cd,
\qquad bc-ad=1.
$$

The determinant is **minus one**. Let

$$
L=\begin{pmatrix}1&1\\0&1\end{pmatrix},\qquad
R=\begin{pmatrix}1&0\\1&1\end{pmatrix}.
$$

The endpoint matrix updates on the **right**:

| Interval decision | Matrix update | New interval |
|---|---|---|
| `x < (a+c)/(b+d)` | `E <- EL` | `[a/b, (a+c)/(b+d)]` |
| `x > (a+c)/(b+d)` | `E <- ER` | `[(a+c)/(b+d), c/d]` |

In contrast, the direct projective actions of these matrices on a variable `y` are `L(y)=y+1` and `R(y)=y/(y+1)`. Match the observer's increasing endpoint chart by defining

$$
\phi_E(t)=\frac{a+ct}{b+dt},\qquad t>0,
\qquad B_E=\begin{pmatrix}c&a\\d&b\end{pmatrix}=ES,
\quad S=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
$$

The Möbius chart matrix is `B_E`, not `E`: its determinant is plus one. This chart sends zero to the lower endpoint, infinity to the upper endpoint, and one to the mediant. Let `t=phi_E^{-1}(x)`. Since `SLS=R` and `SRS=L`, the residual state obeys

$$
\begin{array}{c|c|c}
\text{condition}&\text{emitted branch}&\text{new residual}\\\hline
0<t<1&L&t/(1-t)=R^{-1}(t)\\
t>1&R&t-1=L^{-1}(t).
\end{array}
$$

For the initial bracket `[3,4]`, the chart matrix is `[[4,3],[1,1]]`, and its residual is `(x-3)/(4-x)`. One could instead use the decreasing chart represented by `E` itself, but its residual is the reciprocal of this one and its output rules are exchanged. The present note uses `phi_E` consistently. Run lengths recover continued-fraction coefficients, subject to the initial chart and the rational terminal convention. The scalar endpoint rules above eliminate ambiguity without relying on a slogan that an `L` always means the same direct projective action.

### Productive branch theorem

Initialize `E = [[3,4],[1,1]]`. To decide its next branch, let `m=(a+c)/(b+d)` and consume source factors until either `sup I_k < m` or `inf I_k > m`. Perform the corresponding update and repeat.

**Safety.** The source enclosures contain pi; a strict endpoint comparison is a rational certificate of the correct branch. Cross multiplication uses integers with positive denominators.

**Finite progress.** Every mediant is rational, whereas pi is irrational. Thus `delta=|pi-m|>0`. Equation (3) implies that eventually the whole enclosure lies on one side of `m`. This argument is reapplied after every finite output prefix. It proves that each requested finite prefix is produced in finite time, even though no fixed bound on total memory is assumed. Irrationality is an imported classical theorem; [B] includes a proof. It is not being inferred from the experiment.

**Recovery.** The output intervals are nested and contain pi. Their width is `1/(bd)`. Each branch replaces one positive denominator by `b+d`, so after `n` branches, `b+d≥n+2` and `bd≥b+d-1≥n+1`. Hence their widths are at most `1/(n+1)`, tending to zero. Their unique common point is pi.

This proves the finite-program/infinite-output request. General irrational computable inputs admit the same compiler; identification of this particular input as pi resides in the geometric source proof.

### A useful commuting square

When source enclosures lie strictly inside the endpoint bracket, set

$$
T=B_E^{-1}A_k.
$$

Consuming a source factor sends `T` to `TZ`. For an emitted endpoint-update branch `G`, put `bar G=SGS`; thus `bar L=R` and `bar R=L`. Since `B_{EG}=B_E bar G`, emitting the branch sends `T` to `(bar G)^{-1}T`. Associativity gives

$$
((\bar G)^{-1}T)Z=(\bar G)^{-1}(TZ).
\tag{4}
$$

This is exact coherence between input refinement and output representation change. The strict-interior qualification avoids poles of the residual chart at endpoint values. An implementation can instead remain in the direct cross-product formulation throughout.

For radix `b`, replace the output map by `x <- b(x-n)` with matrix `[[b,-bn],[0,1]]`, and emit `n` only when the transformed endpoint floors coincide. Contraction and irrationality again prove productivity. The finite source then supports L/R words, continued fractions, and base-b digits without changing which real it denotes.

## 5. A genuine circle/line arrow correspondence

Use projective homogeneous coordinates

$$
V([u:v])=[v^2-u^2:2uv:v^2+u^2].
$$

They satisfy `X²+Y²=Z²`. This is the rational projective-line/conic isomorphism. The finite chart has `t=u/v`, and the point at infinity maps to `[-1:0:1]`. Its affine inverse away from that point is `t=Y/(Z+X)`; the exceptional point is sent to infinity.

For `M=[[a,b],[c,d]]` in `GL_2(Q)`, define

$$
\widehat M=
\begin{pmatrix}
(a^2+d^2-b^2-c^2)/2&cd-ab&(c^2+d^2-a^2-b^2)/2\\
bd-ac&ad+bc&ac+bd\\
(b^2+d^2-a^2-c^2)/2&ab+cd&(a^2+b^2+c^2+d^2)/2
\end{pmatrix}.
\tag{5}
$$

This is the symmetric-square representation in conic coordinates. Direct algebra gives

$$
V(M[u:v])=\widehat M V([u:v]),\qquad
\widehat{MN}=\widehat M\widehat N,
$$

and, for `Q(X,Y,Z)=X²+Y²-Z²`,

$$
Q(\widehat M z)=(\det M)^2Q(z).
\tag{6}
$$

Scaling `M` scales `widehat M` by its square; projective actions are therefore well defined. In particular, the two signs of an `SL_2` matrix induce the same conic map. The correct projective action group is `PGL_2(Q)`; one must not claim faithfulness for distinct scalar representatives.

For the L/R generators,

$$
\widehat L=\frac12\begin{pmatrix}1&-2&-1\\2&2&2\\1&2&3\end{pmatrix},\qquad
\widehat R=\frac12\begin{pmatrix}1&2&1\\-2&2&2\\-1&2&3\end{pmatrix}.
$$

Thus the action groupoid of rational projective points and rational projective maps is isomorphic to the corresponding conic action groupoid through `V`; real points can likewise be used if the observer's targets are real. Objects and arrows are both transported, and composition is preserved. This is a concrete equivalence with real content, rather than an arbitrary numerical labelling of arrows.

The source matrices `Z_j` are not determinant-one matrices. Formulae (5)–(6) deliberately cover all invertible rational matrices so that the same functor also transports them.

## 6. The retained metric supplies a rational cocycle

Let `M(t)=(at+b)/(ct+d)` on a chart away from its pole. The pullback of circle arclength is

$$
M^*ds=\frac{2|\det M|\,|dt|}{(at+b)^2+(ct+d)^2}.
$$

Relative to `ds=2|dt|/(1+t²)`, the distortion is

$$
J_M(t)=\frac{|\det M|(1+t^2)}{(at+b)^2+(ct+d)^2}.
\tag{7}
$$

It is rational and positive on every real finite chart for invertible real `M`. For composition,

$$
J_{MN}(t)=J_M(N(t))J_N(t).
\tag{8}
$$

This follows from the derivative chain rule, with the same matrix-order convention as (4). The positive density extends across the projective point at infinity using its other chart.

Consequences:

- Arrow composition, interval refinement, and Euclidean-length transport coexist coherently.
- Mere conic preservation does not preserve Euclidean length. In the determinant-one case, `J_M` is identically one exactly when `M^T M=I`. The nontrivial positive L/R generators do not meet that condition.
- If a statistical argument silently drops `J_M`, it has changed the transported measure. A combinatorial branch count is not automatically a geometric arc-length average.

**Exact negative control.** In the parameter interval `[0,1]`, the first mediant is `1/2`; its circle point is `(3/5,4/5)`. This lies beyond the angular bisector `X=Y` of the first quadrant. Therefore the two circle arcs separated by that rational mediant have unequal Euclidean lengths. Assigning them equal geometric mass because the letters are L and R is already refuted at the first split, without a decimal approximation to pi.

The distortion is a candidate instrument for testing future cancellation claims, not a cancellation theorem by itself.

## 7. Categorical probes and variance

For a real target `x`, rational comparisons can be retained as a presheaf

$$
D_x:\mathbb Q^{op}\to\mathrm{Set},\qquad
D_x(q)=\begin{cases}\{*\}&q<x,\\\varnothing&q\ge x.\end{cases}
$$

Here rationals are ordered by their usual `≤` arrows. Restriction goes from a larger rational test to a smaller one. Upper comparisons give the covariant functor `U_x(q)={*}` exactly when `x<q`. Source refinement supplies finite witnesses for the successful rational tests; for irrational `x`, exactly one of the strict lower/upper tests eventually succeeds for every rational `q`.

Alternatively, on the category of rational open intervals with inclusion arrows, `F_x(I)={*}` exactly when `x∈I` is **covariant**. Its category of successful tests is cofiltered: intersect two successful rational intervals to obtain a successful object mapping into both. The direction must not be silently reversed when discussing Yoneda-style reconstruction.

These probe families identify the target while exposing its rational computational witnesses. They do not make every real computable. The finite source is additional structure: only countably many finite programs exist, while the full family of real cuts is uncountable.

## 8. Finite program is not bounded-state emitter

An autonomous deterministic machine with only finitely many complete states has an eventually periodic output stream. In a Stern–Brocot L/R representation, an eventual single-letter tail gives a rational endpoint. A periodic block containing both letters gives a nontrivial positive integer Möbius matrix `W=[[a,b],[c,d]]`; its fixed residual solves

$$
c\eta^2+(d-a)\eta-b=0.
$$

A finite rational prefix is another rational Möbius transformation, so the resulting real has algebraic degree at most two. Thus no autonomous bounded-state emitter can produce pi's L/R path. This conclusion uses the classical transcendence theorem for pi, not merely irrationality; [B] gives a self-contained proof of that imported theorem.

The construction above has finitely many rules and finitely many integer registers, with registers allowed to grow. That is precisely how the apparent conflict is resolved. Neither an infinite input tape nor an external clock should be smuggled in and then called finite state.

## 9. Discriminator and the live research boundary

The best immediate discriminator is to retain both the source certificate and the metric cocycle, then ask any proposed orbit statistic to survive the exact first-split negative control and a change of arithmetic output representation. If a claim depends only on the abstract L/R graph, it will also apply to computable nonnormal controls and cannot establish pi-specific radix cancellation.

More detailed source/shape information can be useful without being normality. For example, a quantitative separation estimate `|pi-p/q| ≥ C q^(-mu)` would turn (3) into an explicit source-precision budget `k > mu log_2(q) - log_2(C)` for deciding a threshold `p/q`. This is a conditional arithmetic statement; no such estimate is proved here. It illustrates a genuine bridge from Diophantine information to runtime rather than conflating runtime with digit frequencies.

The three clocks remain distinct: source-factor index, mediant-output index, and radix-digit index. Productivity alone gives no uniform bound sufficient to transfer a signed temporal average between them. That clock/observable estimate, for the actual selected source and seed, is where a future proof must add information.

### Claim ledger

| Claim | State | Boundary |
|---|---|---|
| Circle geometry implies the rational source identity (2) | Disclosed | Elementary calculus, Euclidean arc-length definition |
| Every L/R output step terminates and the path recovers pi | Disclosed | Exact arithmetic and imported irrationality theorem |
| Projective line/conic arrow correspondence and coherence | Disclosed | Rational maps; includes infinity; scalar matrices identified |
| Arc distortion cocycle (7)–(8) | Disclosed | Euclidean metric retained |
| Fair L/R branch counting equals Euclidean arc measure | Refuted | Exact first-mediant counterexample |
| The construction is an autonomous finite-state generator | Refuted | Classical transcendence used for the L/R argument |
| These structures yield the repository's selected contrast decay | UNVERIFIED | No all-large-epochs cancellation estimate obtained |
| Symbolic polynomial identities (5)–(6) pass implementation check | Observed | SymPy 1.14.0 run described below; not an independent mathematical proof |

## 10. Actual validation and source provenance

A local one-shot SymPy 1.14.0 computation expanded, for generic symbols, all entries of:

1. `lift(M)*V(u,v) - V(a*u+b*v,c*u+d*v)`;
2. `lift(M*N) - lift(M)*lift(N)`;
3. `lift(M).T * diag(1,1,-1) * lift(M) - det(M)**2 * diag(1,1,-1)`.

Every expanded entry was zero. It also printed the two generator lifts displayed above. The process exited zero. A second SymPy 1.14.0 check verified `B_{EG}=B_E(SGS)` for both branches and simplified `phi_{EL}(t/(1-t))-phi_E(t)` and `phi_{ER}(t-1)-phi_E(t)` to zero. It also exited zero. These checks verify formula transcription symbolically; the underlying justification is the quadratic embedding and ordinary matrix composition. No remote write, checkout change, or full repository gate was performed by this translator bearing.

[G] Jeremy Gibbons, *Unbounded Spigot Algorithms for the Digits of Pi*, author-hosted primary manuscript, published in *American Mathematical Monthly* 113(4), 2006, pp. 318–328; retrieved author PDF reports corrections September 2024. Sections 5–6 contain the safe algorithm and the explicitly conjectural shortcut. https://www.cs.ox.ac.uk/jeremy.gibbons/publications/spigot.pdf

[B] David H. Bailey, *An elementary, self-contained proof that pi is transcendental*, author-hosted mathematical proof, July 24, 2026. Used only for the imported irrationality/transcendence theorem and not as evidence for normality. https://www.davidhbailey.com/dhbpapers/dhb-pi-trans.pdf

Related primary geometric literature checked: Heather Abramson et al., *Continued fractions and lines across the Stern–Brocot diagram*, arXiv:2308.04654, subsequently *Involve* 18 (2025), 373–385. Its theorem about varying one continued-fraction entry gives pairs of Euclidean lines in the diagram; it is not being conflated with the metric unit-circle construction here. https://arxiv.org/abs/2308.04654

Official FLINT continued-fraction documentation was also inspected, but its current page announces partially LLM-generated material under revision; no theorem in this note depends on that page. The conic, metric, matrix-convention, and productivity arguments above are given explicitly so that their validity does not rest on a source's authority.

## 11. Review of the root synthesis

The translator bearing subsequently read the root's staging `README.md` and `PRECISION_TRANSFER.md`, and compared their source/tail conventions with the pinned frontier and round-III computation-graph proof. The reviewed file hashes were:

| File | SHA-256 |
|---|---|
| `README.md` | `23ee5e8701b310e52f61b556435a1d3a9fbca4ee929198b3ae13fc8c69066668` |
| `PRECISION_TRANSFER.md` | `b950f621a4b28a2d9401437d4e7c5e934b5ee155fd45639d100b01d2091fcbc7` |

No mathematical error was found in the inspected claims. The specific checks were:

- The metric ratio is invariant under a nonzero rational scalar representative of `M`. Its limit at infinity is `abs(det M)/(a²+c²)`, a positive rational number because an invertible matrix has nonzero first column. Continuity of the circle action extends the cocycle identity across poles and infinity. Thus `(t, M) -> J_M(t)` really defines the stated functor to the one-object multiplicative group of positive rationals. It is not faithful: identity and `diag(-1,1)` give distinct endomorphisms of the point zero, both with metric ratio one.
- A rational scalar multiple of an L/R word has square determinant in `Q`; `det(Z_1)=3` rules out the stated projective identification.
- The increasing endpoint chart and the swapped residual generators agree with section 4 above. Ordinary circle angles in radians are not the radix character's arguments in turns; `exp(i 16^(n-1) pi)` is minus one at `n=1` and one thereafter.
- The Fourier geometric sum is `(16^(2A-1)-16^(A-1))/15`. Combining midpoint error below `2^(-k-1)` with `2pi<8` yields the claimed `|h|/(60 A 2^s)` at `k=8A+s`, for nonzero `h`.
- The imported zero-seed completion and strict tail bound yield the additional `8|h|/((8A+1)(8A+2))`. The different-seed formula and its zero-completion control preserve the original clock.

This was a mathematical prose review by a same-model collaborator, not an independent formal proof check. No formal checker or new numerical experiment was run for these synthesis statements. The listed hashes identify the reviewed versions; this receipt does not cover unreviewed later edits. The comparison theorem pays approximation error and does not prove cancellation, as the synthesis explicitly states.
