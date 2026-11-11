# Cursed categorical computation, round I

## Scope and source convention

This is a research archive of the first conversational exploration, not a verbatim transcript or a claim that the constructions below prove a digit-distribution theorem. It preserves the eight substantive routes, their exact domains, their useful jobs, and their failure modes. Round II supplies more explicit equivalences and a fresh standalone probe.

The authenticated forcing and seed are

$$
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},\qquad n\ge1,
\qquad U_0=0,\quad U_n=16U_{n-1}+r(n).
$$

Write $P_n=\sum_{j=1}^n16^{-j}r(j)$. Then $U_n=16^nP_n$ and

$$
\sum_{n\ge1}\frac{r(n)}{16^{n-1}}=\pi,
\qquad P_\infty=\frac\pi{16}.
$$

The factor of $16$ is deliberate. The inverse-beta fixed point below has value $\pi$ at clock zero; the $P_n$ normalization has limit $\pi/16$.

Status vocabulary: **PROVED** means the stated mathematical proposition has a proof here or in an identified source; **PROVED_CONDITIONAL** retains its hypotheses; **VERIFIED_FINITE** identifies a finite calculation; **REFUTED** has an explicit counterexample; **OPEN** names a missing implication. A cited repository theorem is not a new independent proof or a newly rerun repository test.

At the first inspection, live `main` was Main XXII, commit `43886e830cee5ff6d6b37719e18d809819673bd9`. The relevant later work was on draft research branches. Immutable references and external sources are collected in [SOURCES.md](SOURCES.md).

## I.0. The one-object CCC obstruction

**PROVED.** A category with exactly one object that is terminal has exactly one morphism. Therefore a literal one-object Cartesian closed category is trivial: a CCC has a terminal object, and in a one-object category that is the only object.

This does not prevent a nontrivial one-object monoid category, a C-monoid with additional operations, or a many-object category reconstructed from idempotents. It prevents replacing those distinct constructions by the phrase “one-object CCC.” A successful finite lambda reduction is not a proof of all C-monoid axioms or of a faithful arithmetic compiler.

**Job:** reject a type error before it becomes a research premise. **Next test:** any proposed one-object model must state which terminal-object requirement it does not impose, or accept triviality.

## I.1. Two averaging idempotents manufacture a two-dimensional oscillator

Let $P_2$ average the adjacent pairs $(0,1),(2,3),(4,5)$ in $\mathbb Q^6$, and let $P_3$ average the triples $(0,1,2),(3,4,5)$. Both are symmetric idempotent matrices. They represent the generators of the one-object monoid category

$$
\langle p,q\mid p^2=p,\ q^2=q\rangle.
$$

The subtraction in

$$
C=P_2P_3-P_3P_2
$$

takes place in a linear operator algebra, not in the bare monoid. Exact rational matrix multiplication gives

$$
C^\mathsf T=-C,\qquad \operatorname{rank}C=2,\qquad C^3=-\frac29C.
$$

Consequently the two nonzero complex eigenvalues are $\pm i\sqrt2/3$. The remaining four eigenvalues are zero. These statements are **PROVED** by the displayed finite matrices and exact reduction; the archive probe reproduces the identities.

The oscillator exists for these projections independently of the arithmetic source. The source-specific statement is separate. Put

$$
r^{(n)}=(r(n),r(n+1),\ldots,r(n+5))^\mathsf T,
\qquad \mathscr A_n=\langle r^{(n)},Cr^{(n+1)}\rangle.
$$

The earlier Omega–Haar dossier states and proves $\mathscr A_n>0$ for $n\ge1$ and

$$
\mathscr A_n\sim\frac{675}{128}n^{-9}.
$$

The fresh archive probe checks seven exact clocks and the Laurent coefficient by direct rational expansion. Its seven inequalities do not independently prove positivity at every clock; the universal positivity claim retains its repository proof provenance.

**Job:** a tiny exact compiler of two alternative averaging schedules into an oriented source observable. **Boundary:** source orientation is not a signed orbit-frequency estimate. **Hostile control:** replacing the source by a constant vector gives zero area while preserving every operator identity. **Next test:** derive, or falsify, an inequality that connects this oriented source packet to the actual carry-sensitive signed observable.

## I.2. A genuine CCC with two objects

Rodenburg and van der Linden's classical representation theorem constructs a Cartesian closed category with exactly two objects from a genuine C-monoid, recovering that monoid as the endomorphisms of one object. One object $T$ is terminal; the other $U$ supports the required universal product and exponential behavior. In the appropriate construction,

$$
U\times U\cong U,\qquad U^U\cong U.
$$

**PROVED_CONDITIONAL:** the input must satisfy the C-monoid axioms. The result does not say that every monoid, every finite combinator table, or SUCC's current clock action is a C-monoid.

**Job:** a compact possible semantic destination: higher-order structure can reside in arrows despite a tiny object inventory. **Boundary:** the theorem is classical; applying it to SUCC requires a separately authenticated compiler and the complete input axioms. **Next test:** audit the actual pairing, projections, evaluation, currying, and equations rather than inferring them from successful examples.

## I.3. Unary substitution can retain a many-object lambda theory

For a beta-lambda theory $L$, its unary terms $L_1$ form a monoid under substitution. Let $\mathbf B L_1$ be its one-object category. The UniMath formalization proves, for a target category $\mathcal D$ with the required colimits, an equivalence of functor categories

$$
[\operatorname{Lawvere}(L),\mathcal D]
\simeq
[\mathbf B L_1,\mathcal D].
$$

The formalization uses the category of retracts and the Karoubi envelope, with an explicit fully faithful embedding of the Lawvere category into the completion. This is **PROVED_CONDITIONAL** on those hypotheses and conventions.

It is an equivalence of the specified representation/functor categories. It is not an assertion that the one-object category itself is a CCC, nor an unconditional equivalence between the underlying many-object Lawvere category and the bare monoid category. Round II gives the concrete idempotent-to-family mechanism.

**Job:** isolate a small unary substitution kernel while retaining reconstructible higher-arity observations. **Boundary:** coding terms does not decide beta equality. Neither this theorem nor an imported formalization establishes SUCC's full source-to-lambda compiler. **Next test:** match the actual compiler's equality and observer contracts to the formal theorem's hypotheses.

## I.4. Two arrows and one relation expose the origin

In the bicyclic monoid

$$
\mathcal B=\langle s,t\mid ts=1\rangle,
$$

represent $s$ by the unilateral shift $S$ on the vector space with basis $(e_j)_{j\ge0}$, and $t$ by its backward partial inverse $T$:

$$
Se_j=e_{j+1},\quad Te_0=0,\quad Te_j=e_{j-1}\quad(j\ge1).
$$

Then

$$
TS=I,\qquad ST=I-P_0,\qquad P_0e_j=\mathbf1_{j=0}e_0.
$$

These identities are **PROVED** on every basis vector and hence on every finitely supported vector. They also hold in the standard Hilbert-space realization. The difference $I-ST$ belongs to the linearization, not the bare monoid.

The distinguished origin is a place to attach the typed requirement $U_0=0$. The origin projector does not, by itself, verify the seed's value or the four-pole source. A finite square shift matrix has an additional upper-boundary defect, so tests must not mistake that truncation for the infinite shift identity.

**Job:** distinguish a one-sided boundary from a reversible bilateral shift. **Hostile control:** on a bilateral shift $TS=ST=I$, so the origin projector disappears. **Next test:** retain the projector, source passport, and evaluator together. Round II shows that the same rank-one defect generates every finite rational matrix.

## I.5. The chaotic groupoid that identifies every forcing with zero forcing

For any two rational source sequences $r,q$, define their finite partial sums $P_n^r,P_n^q$ using the same radix convention. The clock-preserving map

$$
K_{r\to q}(n,u)
=\left(n,u+16^n(P_n^q-P_n^r)\right)
$$

satisfies

$$
K_{q\to v}K_{r\to q}=K_{r\to v},\qquad
K_{r\to r}=\operatorname{id},\qquad
K_{q\to r}=K_{r\to q}^{-1}.
$$

Give source sequences the role of objects and choose exactly this arrow between each ordered pair. This is an indiscrete (chaotic) groupoid. The formulas are **PROVED** by addition and subtraction of the partial sums.

In the source coordinate $z=16^{-n}u-P_n^r$, the indexed positive affine action is

$$
\mathcal A^r_{a,b}(n,u)
=\left(an+b,\,16^{an+b}\left(z+P^r_{an+b}\right)\right),
\quad a\ge1,\ b\ge0.
$$

The map $K$ preserves $z$ and therefore intertwines these actions. It also preserves the initial state at clock zero because every $P_0$ is zero. This makes the observer boundary especially sharp: preserving a seed and an abstract affine carrier does not identify the forcing.

For the authentic source $r(1)=47/15$, the zero-seed state has phase $2/15$ at clock one. Zero forcing has phase zero. The groupoid isomorphism identifies the undecorated carrier, but it does not preserve this phase observation.

**REFUTED:** abstract source-clock conjugacy implies equality of real-phase statistics. **Job:** a calibrated semantic false-positive control. **Next test:** all claimed equivalences used for arithmetic conclusions must state the additional source and observer structure they preserve.

## I.6. One idempotent randomizes a digit and still fails Haar

On $[0,1)$ let $T(x)=\{16x\}$ and $b_a(y)=(a+y)/16$ for $0\le a<16$. On probability measures set

$$
L\nu=\frac1{16}\sum_{a=0}^{15}(b_a)_*\nu,
\qquad Q=L T_*.
$$

Since $T_*L=I$, it follows that $Q^2=Q$. Thus $Q$ represents a one-generator idempotent monoid. Yet

$$
Q\delta_0=\frac1{16}\sum_{a=0}^{15}\delta_{a/16}
$$

is atomic and non-Haar, and is fixed by $Q$.

The first conversation gave Wasserstein distance $1/32$. Its metric must be specified: with the ordinary interval cost $|x-y|$,

$$
W_1(Q\delta_0,\lambda)=\frac1{32}.
$$

Integrating the CDF difference on the sixteen cells proves this value. With the geodesic metric on the unit circle, the optimal symmetric Voronoi cells instead give $1/64$. Both distances are positive; neither metric supports a Haar conclusion.

**REFUTED:** first-digit uniformization plus idempotence implies Haar measure. **Job:** separate local averaging from actual orbit statistics. **Next test:** preserve and estimate the signed defect of the source-selected orbit, rather than adding further idempotence checks.

## I.7. Four arrows see a coupling that perfect marginals conceal

The one-object group category $\mathbf B(\mathbb Z_2\times\mathbb Z_2)$ has four arrows. Its mixed character is

$$
\chi(x,y)=(-1)^{x+y}.
$$

Three two-bit laws all have fair marginals, while their mixed expectations are

| Joint law | $\mathbb E\chi$ |
|---|---:|
| Independent fair bits | $0$ |
| Locked bits, $X=Y$ | $+1$ |
| Twisted bits, $X=1-Y$ | $-1$ |

These are exact finite calculations. They refute inference from marginal fairness to independence. A specified zero mixed coefficient is also insufficient to establish independence: the later ratio-joining dossier supplies a nonproduct joining with a vanishing selected $h=8$ coefficient and an exactly shared second digit.

The stronger repository countermodels realize Haar marginals and nonproduct $2\!:\!3$ joinings along normal single orbits. Those statements retain the proofs and hypotheses in PR #593; they are not consequences of the four-element example alone.

**Job:** a minimal adversarial coupling diagnostic. **Next test:** identify the full family of mixed observables a claimed product-joining conclusion requires, and test null controls which conceal dependence from one selected mode.

## I.8. Self-application describes the BBP recursion; boundedness selects its value

Put $R(n)=r(n+1)$ for $n\ge0$ and

$$
F(g)(n)=R(n)+\frac{g(n+1)}{16}.
$$

In untyped lambda syntax,

$$
W_F=(\lambda z.F(zz))(\lambda z.F(zz))
\longrightarrow_\beta F(W_F).
$$

This one beta step expresses self-reference. It does not establish convergence, termination, or an analytic denotation on its own.

On $\ell^\infty(\mathbb N_0)$, $F$ is a $1/16$-contraction, so it has the unique bounded fixed point

$$
B(n)=\sum_{k\ge0}16^{-k}r(n+k+1),\qquad B(0)=\pi.
$$

The series converges uniformly because $R$ is bounded and the weights are summable. The uniqueness proof is immediate from the contraction estimate. Without boundedness, every sequence

$$
B(n)+C16^n
$$

is another fixed point, and conversely every difference between two fixed points has that form. Thus the analytic boundary condition is doing real work.

**PROVED:** the syntax step, the bounded fixed-point theorem, and the unbounded counterfeit family. **OPEN:** a source-preserving full lambda compiler and a signed statistical theorem for the selected orbit. **Job:** separate recursive syntax from analytic boundary selection. **Next test:** require the compiler to reject the growing homogeneous branch for the stated reason, not because a finite truncation happens to look benign.

## I.9. The statistical seam retained for the next round

For adjacent orbit blocks of equal length $M$, let $H^-,H^+$ be their signed CDF defects from the chosen reference law, and put $D^\pm=\int|H^\pm|$. Define

$$
\Omega_M=\int \min(|H^-|,|H^+|)\,
\mathbf1_{H^-H^+<0}.
$$

The pointwise absolute-value identity gives

$$
D_{2M}=\frac{D^-+D^+}{2}-\Omega_M.
$$

The Lambda–Haar compiler dossier already uses this exact cancellation identity. A sufficient source-derived lower bound on $\Omega_M$, with the required endpoint, late-block, and odd-length controls, would provide actual statistical leverage. None of the categorical identities above supplies that bound.

The live dependency remains: authenticated source and seed, a sound observer, and an arithmetic estimate for the signed defect. Wrong seeds, zero forcing, pole mutants, and nonproduct joining controls must remain distinguishable. Base-16 normality of $\pi$, the original-zero signed parity problem, and RH remain **OPEN**.
