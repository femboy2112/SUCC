# Liber Sextus — De Applicationibus

## 1. The application contract

The foundation does not authenticate an application merely by naming its carrier.
An application supplies a state space, lawful operations, a readout interpretation,
a selected initial condition when relevant, and the target to be preserved.
This book gives one exact arithmetic discrimination result and records the maps
to existing SUCC constructions. The authentic BBP forcing and original zero seed
are retained. **R0, π normality, Goldbach, completed-Weil positivity and RH remain
OPEN.** No new physical measurement or proof-assistant result is asserted here.

The following are interfaces to existing theorems, not renamed discoveries.

| SUCC object | Principia instantiation and preservation law | Additional premise / information lost |
|---|---|---|
| Contextual zero, CZB-02/04/08 | A nonempty source fiber $B$ is conditioned by an actual readout; $B'\subseteq B$ implies $I(B)\subseteq I(B')$. An action instead pushes $B$ through its transition. | Monotonicity concerns facts about a fixed source history. Current-state zeros need not survive movement; a planned probe is not an event. |
| Source-labelled succession and future-safe quotient | A representation $q$ carries each enabled action and its readout/cost exactly when those data are constant on its fibers. Induction then carries every legal word. | Source labels are model data. A correct label comparison is not empirical authentication. Partial-action enabledness must be retained. |
| Ancestral relations, PAP-03/04 | Endpoint exactness is equivalent to preservation of source-reachable report supports on observation fibers; this is weaker than word/cost preservation. | An existential quotient can splice witnesses from different roots. The existing three-state example already proves the failure. |
| Carrier-relative target descent | $P=\bar P\circ E$ exactly when $P$ is constant on the actual nonempty fibers of $E$. | Full source reconstruction is unnecessary; jointly executable access and external source adequacy remain separate. |
| Operational Yoneda, O211–O226 | Legal histories form the declared category. Full representables retain arrows; a restricted probe family is faithful precisely when it separates the relevant arrow pairs by lawful precomposition. | Endpoint forgetting, restricted context access, and source interpretation are distinct maps. An abstract precursor need not be physically resettable. |
| Scott evidence / completion | Consistent finite information is ordered by refinement; a supplied Scott-continuous map transports directed suprema. | A source observation not preserving those suprema has no such transport. The supremum is mathematical, not a last physical clock tick. |
| SUCC/FUCC | On arithmetic states, $S(n)=n+1$, $V_p(n)=pn$, hence $V_pS=S^pV_p$. This is an exact typed action relation. | Any compression must separately preserve the relation and the target. Projection can discard paths that a later operation returns. |
| Fourier/Haar observers | Linear Fourier readouts preserve signed sums; retaining every Fourier coefficient determines a circle probability law. Conditional digit Fourier inversion recovers the joint digit/future defect. | Marginalization discards the joining; positive energy discards some phase information; finite mode banks are incomplete. |
| BBP completion | The source-selected correction satisfies $U_n+T_n=16^n\pi/16$; its rational enclosures transport each fixed finite readout with a paid error. | Source-depth convergence does not imply temporal cancellation along the selected orbit. |

For the first four rows, [Book I](01_source_observer.md) and
[Book III](03_knowledge_proof.md) give the general proofs. The specializations
follow by substituting the indicated SUCC maps. The chronological action laws,
not the names of the modules, are the required hypotheses. Exact originating
paths and draft heads are recorded in the [provenance audit](../../research/2026-11-13/principia_observatoris/provenance_audit.md).

Two additional preservation checks can be stated directly. The contextual-zero
ideal implication follows because a polynomial vanishing on $B$ vanishes on
every subset. For SUCC/FUCC, both sides applied to $n$ equal $pn+p$.
These elementary proofs do not establish the missing arithmetic averages.

## 2. A sharp finite discrimination theorem for the authentic forcing

This section reuses the archived positive moment representation and classical
finite realization algebra. Its new-to-round assembly is a **sharp observation
budget with an exact compulsory residual** against bounded-dimensional stationary
linear rivals. It is not a new infinite-Hankel-rank theorem: that obstruction
already appears in [Source Genesis, G1/G2 and §5](../../research/2026-10-24/PI_SOURCE_GENESIS_GREEN.md)
and [Green/coefficient duality](../../research/2026-10-24/BBP_GREEN_RANK_COEFFICIENT_DUALITY.md).
No scholarly novelty is claimed.

For integers $n\ge1$, retain

\[
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2}.
\]

Fix an integer $N\ge1$. Put $m_k=r(N+k)$, $k\ge0$, and

\[
H_d(N)=(m_{i+j})_{0\le i,j\le d},\qquad H_{-1}:=(),\quad\det H_{-1}:=1.
\]

The model class consists of all scalar sequences

\[
\widetilde m_k=C A^k b,
\]

where $A$ is a fixed $t\times t$ complex matrix, $b\in\mathbb C^t$,
$C\in\mathbb C^{1\times t}$, and $t\le d$. The parameters may depend on
$N,d$, but not on $k$. No stability, positivity, minimality, or rationality
is assumed of a rival.

### PA-01. Strict source moment positivity — inherited theorem, explicit specialization

Every $H_d(N)$ is positive definite.

**Proof.** Monomial integration gives

\[
r(n)=\int_0^1 t^{8n-8}g(t)\,dt,\qquad
g(t)=4-2t^3-t^4-t^5=2(1-t^3)+(1-t^4)+(1-t^5).
\]

Thus $g(t)>0$ on $0<t<1$. Push the positive measure
$t^{8N-8}g(t)dt$ forward under $u=t^8$, and call it $\nu_N$.
It has positive density on $0<u<1$ and moments $m_k$. For any nonzero
$c\in\mathbb C^{d+1}$,

\[
c^*H_d c=\int_0^1\left|\sum_{j=0}^d c_j u^j\right|^2d\nu_N(u)>0,
\]

because a nonzero polynomial has finitely many zeros. This is an all-$d,N$
proof, not an extrapolation from finite determinants. ∎

### PA-02. Sharp $2d+1$-readout discrimination and compulsory residual — proved paper

For every $N\ge1,d\ge1$:

1. No rival of dimension at most $d$ agrees with all $2d+1$ values
   $m_0,\ldots,m_{2d}$.
2. There exists a rational $d$-dimensional stationary linear rival agreeing
   with all first $2d$ values $m_0,\ldots,m_{2d-1}$.
3. Every rival in this class agreeing with those first $2d$ values has the
   same next value. Its failure is exactly

\[
\boxed{m_{2d}-\widetilde m_{2d}
=\delta_{N,d}:=\frac{\det H_d(N)}{\det H_{d-1}(N)}>0.}
\tag{PA-2}
\]

Consequently the first assertion's consecutive-readout budget is sharp in this
model class. It does not assert that every other sampling policy needs that many
queries, or that source authentication must be done by sampling.

**Proof.** The rival's Hankel block factors as

\[
(\widetilde m_{i+j})_{0\le i,j\le d}
=\begin{pmatrix}C\\CA\\\vdots\\CA^d\end{pmatrix}
\begin{pmatrix}b&Ab&\cdots&A^db\end{pmatrix},
\]

so its rank is at most $d$, unlike $H_d$. This proves assertion 1.

Set $G=H_{d-1}$, $v=(m_d,\ldots,m_{2d-1})^T$, and $p=-G^{-1}v$.
These are exact rational data, and $G$ is invertible by PA-01. Define the
monic polynomial $P(u)=u^d+\sum_{j<d}p_j u^j$. The equations defining $p$
say exactly

\[
\sum_{j<d}p_jm_{k+j}+m_{k+d}=0\qquad(0\le k<d).
\tag{PA-3}
\]

Initialize $\widetilde m_0,\ldots,\widetilde m_{d-1}=m_0,\ldots,m_{d-1}$
and use the fixed recurrence

\[
\widetilde m_{k+d}=-\sum_{j<d}p_j\widetilde m_{k+j}.
\tag{PA-4}
\]

It has a rational companion-matrix realization of dimension $d$.
Induction using PA-3 proves agreement through $2d-1$. At $2d$,

\[
m_{2d}-\widetilde m_{2d}=m_{2d}-v^TG^{-1}v
=\det(H_d)/\det(G)>0,
\]

by block elimination and positive definiteness. This proves assertion 2 and
the residual for the constructed rival.

For any rival matching those same $2d$ values, its first $d\times d$
Hankel block equals $G$, forcing its dimension to be at least $d$, hence
exactly $d$. Cayley–Hamilton supplies a monic degree-$d$ recurrence.
Its first $d$ equations are PA-3; invertibility of $G$ fixes its coefficients
uniquely as $p$. The next value is therefore the one in PA-4, proving assertion
3. This remains valid for complex or non-diagonalizable rivals. ∎

The polynomial $P$ is the source measure's monic orthogonal polynomial.
Classical Gaussian quadrature also realizes the same matched prefix with
positive weights and $d$ real nodes inside $(0,1)$, but algebraic nodes
are unnecessary for the rational companion certificate above. This classical
neighbor is documented in [NIST DLMF §3.5(v)](https://dlmf.nist.gov/3.5#v);
the proof of PA-02 does not invoke a numerical quadrature routine.

**Small exact control.** At $N=d=1$,

\[
m_0=47/15,\quad m_1=106/819,\quad m_2=829/19635.
\]

The one-dimensional rival has $A=m_1/m_0=530/12831$, $b=m_0$, $C=1$.
It matches the first two values and misses the third by

\[
\delta_{1,1}=\frac{362310761}{9825530715}>0.
\]

Removing the dimension promise defeats every fixed readout budget: apply
the construction with arbitrarily large $d$. Removing exactness requires
a tolerance calculation, supplied next. Replacing the genuine measure by a
single atom destroys PA-01 for $d\ge1$ and permits a one-dimensional exact
model at all horizons; this is the positive control for the rival class.

### PA-03. A rational noise margin against all bounded-order rivals — proved paper

With the same hypotheses, every dimension-at-most-$d$ rival satisfies

\[
\boxed{\max_{0\le k\le2d}|m_k-\widetilde m_k|
\ge\gamma_{N,d}:=
\frac1{(d+1)\|H_d(N)^{-1}\|_\infty}>0.}
\tag{PA-5}
\]

Here the matrix norm is the maximum absolute row sum. Since $H_d$ is
rational, $\gamma_{N,d}$ is an exact positive rational number.

**Proof.** The rival Hankel block $\widetilde H$ has a nonzero kernel
vector $z$, normalized by $\|z\|_\infty=1$. Put
$\epsilon=\max_{k\le2d}|m_k-\widetilde m_k|$ and $E=H_d-\widetilde H$.
Then $z=H_d^{-1}Ez$ and $\|E\|_\infty\le(d+1)\epsilon$.
Taking norms proves PA-5. ∎

This bound is conservative; PA-02's last residual is exact only under the
preceding exact matches. If observed moments have certified error at most
$\eta$, while a rival fits those observations within $\varepsilon$, then
$\eta+\varepsilon<\gamma_{N,d}$ excludes that rival. A fitted floating rank
without an error bound cannot apply either theorem. No onset-independent
positive margin is possible as $N\to\infty$: the zero-output rival has
uniform error at most $r(N)\to0$. Observation count and resolution cost are
different resources.

### PA-05. Explicit source-dependent scale of the first compulsory error — proved paper

The preceding determinant ratio can be priced analytically, without evaluating
a growing determinant. The source-density sandwich used below is **inherited**:
[the Pascal real-kernel dossier §2](../../research/2026-10-24/PI_PASCAL_REAL_KERNEL.md)
already proves $15/8<g(t)/(1-t^8)<4$, and PJT-10 applies it to all positive
Pascal moments. Its executable antecedent is
[forcing_pascal_beta_bounds](../../observational_succ/pi_pascal_kernel.py),
originating at commit
[8f2e6f852efafb4a0c871418c97ed819b1217d7d](https://github.com/femboy2112/SUCC/commit/8f2e6f852efafb4a0c871418c97ed819b1217d7d).
The present application combines that same measure comparison with monic
minimization and a beta/Jacobi norm to price PA-02's compulsory residual;
neither the constants $15/64,1/2$ nor the measure sandwich is a new discovery.

For $N\ge1,d\ge1$, let $\alpha=N-7/8>0$ and define the
positive rational number

\[
h_d(\alpha)=
\frac{d!(d+1)!}
{(2d+\alpha+1)(d+\alpha)
\displaystyle\prod_{j=1}^d(d+\alpha+j)^2}.
\]

Then the error of every dimension-at-most-$d$ rival matching the first $2d$
authentic forcing values obeys the strict two-sided bound

\[
\boxed{\frac{15}{64}h_d(N-7/8)
<\delta_{N,d}<\frac12h_d(N-7/8).}
\tag{PA-6}
\]

In particular, for each fixed $d$, the first compulsory error has order
$N^{-2d-2}$ as $N\to\infty$: there are positive constants depending only on
$d$ bounding its ratio to that power above and below for all sufficiently large
$N$. This is a detection-precision statement about the forcing, not a
statistical statement about the phase orbit.

**Proof, inherited source comparison re-derived.** The measure in PA-01 has density

\[
\frac{d\nu_N}{du}
=\frac18 u^{\alpha-1}
\left[2(1-u^{3/8})+(1-u^{1/2})+(1-u^{5/8})\right].
\]

For $0<a<1$ and $0<u<1$, strict concavity gives
$u^a<1-a+au$, while $u^a>u$. Consequently

\[
a(1-u)<1-u^a<1-u.
\]

Adding the three contributions, with the first counted twice, gives

\[
\frac{15}{64}u^{\alpha-1}(1-u)
<\frac{d\nu_N}{du}
<\frac12u^{\alpha-1}(1-u).
\tag{PA-7}
\]

The coefficient $15/64$ uses the actual four-pole weights, since
$2(3/8)+1/2+5/8=15/8$.

**Proof, monic minimization.** For any positive measure with all finite Hankel
blocks positive, the degree-$d$ monic orthogonal polynomial minimizes
$\int |P|^2$ among monic degree-$d$ polynomials: subtract that polynomial from
any competitor, use orthogonality, and the extra squared norm is nonnegative.
Its minimum is the Schur complement $\det H_d/\det H_{d-1}$ by the coefficient
calculation in PA-02. Thus $\delta_{N,d}$ is this minimum for $\nu_N$.

It remains to compute the corresponding minimum for the beta weight
$w_\alpha(u)=u^{\alpha-1}(1-u)$. Define

\[
F_d(u)=u^{d+\alpha-1}(1-u)^{d+1},\qquad
R_d(u)=\frac{F_d^{(d)}(u)}{w_\alpha(u)}.
\]

The Leibniz expansion expresses $R_d$ as a sum of terms
proportional to $u^{d-j}(1-u)^j$, $0\le j\le d$, so it is a polynomial
of degree at most $d$. Expanding $(1-u)^{d+1}$ first shows its leading
coefficient is

\[
L_d=(-1)^d\prod_{j=1}^d(d+\alpha+j)\ne0.
\]

For every polynomial $q$ of degree below $d$, $d$ integrations by parts give
$\int_0^1 qR_dw_\alpha=0$. Every boundary term vanishes: near zero the
derivatives of $F_d$ of orders $0,\ldots,d-1$ are
$O(u^\alpha)$ or smaller, and near one they vanish at least quadratically.
The condition $\alpha>0$ is essential here. The remaining integrals are
absolutely convergent. Therefore $P_d=R_d/L_d$ is the monic orthogonal
polynomial for this weight.

Using the same integrations by parts, now with $q=P_d$, yields

\[
\begin{aligned}
\int_0^1P_d(u)^2w_\alpha(u)\,du
&=\frac{(-1)^d d!}{L_d}
  \int_0^1u^{d+\alpha-1}(1-u)^{d+1}\,du\\
&=\frac{d!(d+1)!}
{(d+\alpha)(2d+\alpha+1)
 \displaystyle\prod_{j=1}^d(d+\alpha+j)^2}
=h_d(\alpha).
\end{aligned}
\]

The beta integral in the second line is elementary: repeatedly integrating
the integer power $(1-u)^{d+1}$ gives
$(d+1)!/\prod_{j=0}^{d+1}(d+\alpha+j)$.
No asymptotic formula or numerical orthogonal-polynomial solver is used.

Apply the lower inequality PA-7 to the minimizing polynomial for $\nu_N$,
and the upper inequality to $P_d$. A nonzero polynomial is nonzero off
finitely many points, so both integral comparisons are strict. This proves
PA-6. Finally, the explicit denominator in $h_d(N-7/8)$ has degree $2d+2$
in $N$ and leading coefficient one. Hence
$N^{2d+2}h_d(N-7/8)\to d!(d+1)!$, proving the stated order. ∎

**Scope and controls.** The companion rival in PA-02 attains the specified
maximal exact prefix; inequality (PA-6) prices its ensuing failure. This is not a lower
bound on the error of every approximate fit at the final point alone:
an approximate fit can move errors into earlier points. PA-03 is the
appropriate all-rival uniform-error bound. For growing $d$, use PA-6's
full formula rather than a fixed-$d$ asymptotic. The independent
[scale probe](../../research/2026-11-13/principia_observatoris/arithmetic_scale_probe.py)
compares the closed beta expression with exact source LDL residuals and
rejects swapped-bound mutants; its
[receipt](../../research/2026-11-13/principia_observatoris/receipts/arithmetic_scale.json)
records finite implementation checks separately from this all-parameter proof.

### PA-06. The exact late-onset scale at fixed dimension — proved paper

For every fixed $d\ge1$ put $c=15/64$, $a_d=c\,d!(d+1)!$ and
$b_d=(d+1)2^d\binom d{\lfloor d/2\rfloor}$. For the authentic forcing,
as the integer onset $N\to\infty$,

\[
N^{2d+2}\delta_{N,d}\longrightarrow a_d,\qquad
N^{2d+2}\gamma_{N,d}\longrightarrow a_d/b_d.
\tag{PA-8}
\]

Let $e_{N,d}$ be the infimum, over the PA-02 stationary scalar-output
linear rivals of dimension at most $d$, of the largest absolute error in
the $2d+1$ consecutive forcing samples starting at $N$. Without identifying
an optimizing rival, PA-02/03 already imply

\[
0<a_d/b_d\le \liminf_{N\to\infty} N^{2d+2}e_{N,d}
\le \limsup_{N\to\infty} N^{2d+2}e_{N,d}\le a_d .
\tag{PA-9}
\]

Thus even when rivals may spread errors over the entire window, their minimum
uniform error has order $N^{-2d-2}$. The constants in PA-8 are limits for the
specified certificates; PA-9 gives bounds and does not assert that its
endpoints are attained.

**Proof.** In the centered coordinate $v=1-u$, put $p_k(N)=\int v^k\,d\nu_N$.
This is the existing Pascal moment $D_{N-1,k}$;
[PJT-10 §3](../../research/2026-10-24/PI_PASCAL_REAL_KERNEL.md) already gives
its fixed-$k$ endpoint asymptotic. Here is the argument in the present
variables. Write $d\nu_N=f(u)u^{\alpha-1}(1-u)\,du$, $\alpha=N-7/8$.
By PA-7, $f$ is bounded, and the one-sided derivative of each $u^a$ at
$1$ gives $f(1)=c$ by continuous extension. The beta probability measure
with density proportional to $u^{\alpha-1}(1-u)^{k+1}$ has
mean $1-u$ equal to $(k+2)/(\alpha+k+2)$; hence it concentrates at $u=1$.
Its average of $f$ tends to $c$. Since
$\mathrm B(\alpha,k+2)=(k+1)!/\prod_{j=0}^{k+1}(\alpha+j)$, we obtain
$N^{k+2}p_k(N)\to c(k+1)!$ for each fixed $k$.

Let $L_{ji}=(-1)^i\binom ji$ for $0\le i\le j\le d$ (zero otherwise),
and $D=\operatorname{diag}(1,N,\ldots,N^d)$. The matrix $LH_dL^T$ has
entries $p_{i+j}(N)$; $|\det L|=1$. Therefore

\[
G_d(N)=N^2DLH_d(N)L^TD\longrightarrow cF_d,\qquad
(F_d)_{ij}=(i+j+1)! .
\]

After factoring $(i+1)!$ from row $i$ of $F_d$, column $j$ evaluates
a monic polynomial of degree $j$ at $i=0,\ldots,d$. The Vandermonde
determinant gives $\det F_d=\prod_{j=0}^d j!(j+1)!>0$. In particular,
$F_d$ is invertible. Since $\det G_d=N^{(d+1)(d+2)}\det H_d$,
taking consecutive determinant ratios gives the first limit of PA-8.

For the second limit set $\ell_i=(-1)^i\binom di$. Inverting the scaling,
$H_d^{-1}=N^2L^TDG_d^{-1}DL$. After division by $N^{2d+2}$ all terms
except its two degree-$d$ factors vanish. The remaining coefficient is
$[(cF_d)^{-1}]_{dd}=\det(cF_{d-1})/\det(cF_d)=1/a_d$. Thus

\[
N^{-2d-2}H_d(N)^{-1}\longrightarrow\ell\ell^T/a_d.
\tag{PA-10}
\]

The absolute row-sum norm of $\ell\ell^T$ is
$2^d\binom d{\lfloor d/2\rfloor}$. PA-5 gives the second limit.
Finally $\gamma_{N,d}\le e_{N,d}\le\delta_{N,d}$: PA-03 excludes all
smaller uniform errors, and the PA-02 companion attains the upper bound
as its maximum error on this window. This proves PA-9. ∎

**Alternating direction.** Put $s_i=(-1)^i$ for $0\le i\le d$. Since
$s^T\ell=2^d$, PA-10 also gives the purely algebraic limit
\[
\frac{1}{(s^TH_d^{-1}s)\,\delta_{N,d}}\longrightarrow 4^{-d}.
\]
Identifying $1/(s^TH_d^{-1}s)$ with an attained minimax radius requires
a separate optimality and realization proof. The
[sharp rival radius dossier](../../research/2026-11-13/principia_observatoris/sharp_rival_radius.md)
proves that identification (PA-07), constructs a rational attaining rival,
and shows that it also has a realization by positive weights and distinct
stable modes in $(0,1)$. Consequently the exact minimum uniform error satisfies
\[
e_{N,d}\sim \frac{15\,d!(d+1)!}{64\,4^d}\,N^{-2d-2}
\qquad (N\to\infty,\ d\text{ fixed}).
\]
The fixed-dimension limit does not apply
uniformly as $d$ grows, manufacture arbitrary physical precision, or bound
any phase-orbit exponential sum.

## 3. Why this theorem does not linearize π normality

The all-order positive Hankel property implies no finite constant-coefficient
linear recurrence for the forcing on any tail. If the unwrapped $U_n$ obeyed
such a recurrence on a tail, so would $r(n)=U_n-16U_{n-1}$, since fixed
shift-polynomial operators commute. This contradicts PA-01. This assertion is
valid for every seed; it cannot select the original seed's statistics.

The completed **phase** is another object. Draft #607 proves, for each integer
$b\ge2,h\ne0$, that $e(hb^n x)$ has finite stationary linear realization
if and only if $x$ is rational. Its polynomial-root proof applies to the
authentic completed BBP phase by π's classical irrationality. The same draft
exhibits irrational infinite-rank phases whose shell Fourier mean tends to one.
Thus neither rank, exact source identification, nor a very large finite source
match supplies R0. See the pinned [HBC-01–06 dossier](https://github.com/femboy2112/SUCC/blob/18a32aa23e1861a67b9f8d904f625b41aac00c1a/research/2026-11-12/boundary_filter_complexity/HANKEL_THEOREMS.md).

The finite discrimination theorem of [Book IV §3](04_horizons_completion.md)
requires authenticated finite realization bounds. The BBP counterpoint is not
that finite computation is impossible: the original rational recurrence is
productive with an unbounded clock and integer registers. It is that **fixed
finite-dimensional stationary linear memory** is a much smaller class than
finite-description computable dynamics.

## 4. Coarse Fourier observations lose a genuine target distinction

**PA-04 — classical finite-bank countermodel.** Fix a finite set
$F\subset\mathbb Z\setminus\{0\}$. Choose an odd integer
$q>\max(\{1\}\cup\{|h|:h\in F\})$, let $\lambda$ be circle Haar measure,
and put $\nu_q=q^{-1}\sum_{j=0}^{q-1}\delta_{j/q}$.
Then both measures are invariant under multiplication by 16, they agree on
every Fourier mode in $F$, and they disagree on whether the law is Haar.

**Proof.** Multiplication by 16 permutes residues modulo odd $q$, proving
invariance. The finite geometric sum gives
$\widehat\nu_q(h)=1$ if $q\mid h$, and zero otherwise. Thus it vanishes on
$F$, as does $\widehat\lambda$, while $\widehat\nu_q(q)=1$.
The measures are different, and $\nu_q$ is atomic. ∎

This is a target-descent failure on an explicit invariant-measure source class.
It is not a counterfeit satisfying the original BBP zero-seed contract. All
Fourier modes remove the ambiguity by density of trigonometric polynomials;
finitely many modes do not. Likewise, averaging a digit/future joint law before
Fourier inversion can erase the signed conditional defect even if the leading
digit marginal is uniform. The existing recursive Haar and BF-03 interfaces
already retain that distinction.

The relevant “interventions” in an arithmetic application are declared source
transformations or alternative computations with proved transport laws. They
are not physical controls that change π's digits. A change of seed or forcing
is a hostile auxiliary model until its relation to the target source is proved.

## 5. The live signed frontier, with its quantifiers

For the authenticated source write $Y_n=U_n+T_n=16^n\pi/16$ and

\[
W_B(h)=\frac1B\sum_{n=B}^{2B-1}e(hY_n).
\]

The weakest open signed rung recorded by Main XXV is

\[
\exists\eta>0, B_0\quad\forall B\ge B_0:\quad
1-\operatorname{Re}W_B(1)\ge\eta.
\tag{R0, OPEN}
\]

Normality requires $W_B(h)\to0$ for **every fixed nonzero** integer $h$.
The original-zero all-epoch signed Basel formulation is equivalent, not an
independently established source estimate. All cited draft work below remains
outside the present branch except for the founding #618 ancestry.

| Pinned research | What it supplies | What remains unpaid |
|---|---|---|
| Main XXV frontier | Signed-rung hierarchy; exact source/zero anchor; completion and Haar interfaces | R0 and all stronger statistical rungs |
| #608 / #610 | Source currents; #610 RI-8E gives the attributed paper bound $\lvert S_N^U(h)\rvert\le N-[1-\cos(\pi/8)]\log_\beta N+O_{\beta,h}(1)$, for fixed $h\ne0$ and an allowed $\beta$ above a proved irrationality exponent | Its normalized saving tends to zero; it does not establish R0 |
| #609 | Common-root exact prefix certificates; commuting time/resolution count square; signed time-energy increment | Certified prefix growth is not discrepancy decay |
| #611 | Completed-to-rational signed lag transport; complete fixed-lag all-mode observer; absolute aggregate schedule theorem | No new all-shell source cancellation input |
| #612 | Fixed-lag characteristic pinbed equivalence and lag-uniform $O(B^{-2})$ norm transport | The equivalent pinbed limit is still OPEN for π |

The present round adds PA-02/03 as a source-faithful finite model discriminator
and PA-05/06 as estimates of the precision it costs at late onset. PA-07
settles the optimal threshold when all readouts can carry bounded error.
It derives **no improvement** to the signed Fourier-loss order, R0, or normality.
The useful new connection is a priced boundary: exact short-prefix imitation by
low-order linear models is possible, but fails at an explicit next readout with
an exact rational residual. This prevents an illicit finite-realization closure
argument while giving a constructive test of any claimed finite surrogate.

## 6. Claim ledger and next theorem

| ID | Scope / status | Proof and decisive control |
|---|---|---|
| PA-01 | Inherited source-specific moment positivity; CLASSICAL / PROVED PAPER | §2 integral proof; one-atom source loses strict higher-rank positivity |
| PA-02 | Sharp consecutive discrimination budget and compulsory rational residual; PROVED PAPER, new-to-round assembly | §2 full proof; rational companion matches the maximum prefix |
| PA-03 | Explicit rational tolerance margin; PROVED PAPER, elementary rank perturbation | Kernel-vector proof; zero source approximation shows no horizon-uniform margin |
| PA-04 | Finite Fourier bank cannot decide Haar even on invariant laws; CLASSICAL COUNTERMODEL | Odd-$q$ grid versus Haar |
| PA-05 | Explicit two-sided beta bounds for the compulsory forcing error; PROVED PAPER, source-specific elementary synthesis from the existing PJT-10 measure sandwich | Rodrigues proof; exact finite bound and swapped-bound controls; fixed-$d$ error order $N^{-2d-2}$ |
| PA-06 | Exact fixed-dimension late-onset constants for the exact-prefix residual and inverse-norm certificate; PROVED PAPER, finite Gram consequence of inherited PJT-10 endpoint asymptotic | Centered determinant ratio, scaled inverse matrix and norm limit; PA-9 alone supplies bounds, not minimax optimality |
| PA-07 | Exact minimax uniform forcing error, also attained among positive stable mixtures; PROVED PAPER, source-specific application of classical moment and regularity-radius algebra | [Full proof](../../research/2026-11-13/principia_observatoris/sharp_rival_radius.md); alternating optimal perturbation and a rational companion, independently replayed in the [sharp-radius receipt](../../research/2026-11-13/principia_observatoris/receipts/sharp_rival.json) |
| Statistical gain | R0 / signed normality estimate | OPEN; no estimate in this book |

The next theorem with genuinely arithmetic consequence is a source-selected
positive lower bound in R0 on every sufficiently large shell, or a demonstrably
weaker independently tractable premise that implies it. A general geometry,
rank, or quotient theorem must identify which exact source fact forces that
bound and why the coherent changed seed fails that fact. The Principia supplies
the typed reconstruction and falsification apparatus; it does not postulate the
missing signed inequality as a foundational axiom.
