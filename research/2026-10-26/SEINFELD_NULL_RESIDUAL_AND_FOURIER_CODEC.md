# Seinfeld null residuals and the rational Fourier codec

**Research conclusion, 2026-10-26.** A finite average can be inverted after
retaining its source-labelled, signed null residual. The residual's evaluated
zero, its Fourier energies, and its separate marginals do not contain the same
information. For rational laws on sixteen branches, four exact cyclotomic
channels retain the residual's fifteen rational coordinates. An explicit
control built from the first two authentic BBP inverse fibres preserves both
marginals and every aggregate branch Fourier coefficient while changing the
actual tail-weighted character.

These are finite reconstruction and obstruction results. They provide no
selected Weyl saving or proof of $\pi$ normality. See the
[research contract](SEINFELD_REALIZATION_CONTRACT.md),
[round synthesis](SEINFELD_INVERSE_AVERAGING_AND_REALIZATION.md), and
[exact replay instrument](../../scripts/seinfeld_realization_probe.py).

## 1. Lineage, source and authority

The baseline is PR #313,
`79344c62c39c96755b742700b3d4d22fa60d86da`, on branch
`research/seinfeld-path-disintegration-2026-10-26`. The original source remains

$$
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},
\qquad n\ge1,
$$

$$
U_0=0,\qquad U_n=16U_{n-1}+r(n).
$$

All four signs, the zero seed, source indices, exact unwrapped states and
literal carries remain authoritative. The native source and its authenticator
are imported unchanged. No $\pi$ digits or assumed occupation law are
construction inputs.

The mathematical lineage is explicit:

- [Seinfeld SS-01–06](../2026-10-25/SEINFELD_SUCC_NOTHING_THEOREMS.md)
  distinguishes formal source-labelled null witnesses from their evaluations
  and proves odd-torsion inverse uniqueness and discontinuity.
- [Shadow source inference](../../observational_succ/shadow_source_inference.py)
  already implements the rational row-space/annihilator recovery criterion
  and exact same-observation/different-target countermodels.
- [Lambda source duality](../../observational_succ/lambda_source_duality.py)
  supplies the evaluated field $\mathbb Q(\zeta_{16})$, branch Fourier
  characters, source witnesses and original-history authentication.
- The [selected branch operator dossier](SELECTED_BRANCH_OPERATOR.md)
  and [native operator](../../observational_succ/selected_branch_operator.py)
  already establish the unique odd lift and the maximal energy of fully
  conditioned deterministic selection.

Finite linear splitting, cyclotomic Fourier inversion and odd inverse
uniqueness are **classical/inherited structure**. The contribution here is
their explicit source-labelled residual/Fourier interface and its combined
counterreceipts. The proofs below have paper authority; the accompanying
code gives exact finite witnesses. No Lean kernel authority, physical
realization claim or independent scholarly-priority claim is made. Internal
parallel derivations and audits are not external peer review. The
[import provenance](../../provenance/IMPORT_MANIFEST.json) and preserved
archival source files are unchanged.

## 2. The split sequence: what an average omits

### 2.1 Domains and the two distinct maps

Let $X$ and $Y$ be finite sets with $X\ne\varnothing$, and let
$\pi:X\to Y$ be a declared map. Write $Y_0=\pi(X)$ and
$X_y=\pi^{-1}(y)$ for $y\in Y_0$. The atoms of $X$ retain their source
labels even when distinct atoms have the same image under $\pi$.

Work first with signed rational measures, identified with $\mathbb Q^X$.
Their **pushforward** is the sum map

$$
P:\mathbb Q^X\longrightarrow\mathbb Q^{Y_0},
\qquad (Pp)_y=\sum_{x\in X_y}p_x.
$$

Choose the **uniform reference lift**

$$
S:\mathbb Q^{Y_0}\longrightarrow\mathbb Q^X,
\qquad (Sm)_x=\frac{m_{\pi(x)}}{|X_{\pi(x)}|}.
$$

On observables $f\in\mathbb Q^X$, the corresponding reference average is

$$
(Af)_y=\frac1{|X_y|}\sum_{x\in X_y}f_x.
$$

Pushforward of a measure sums masses; averaging an observable divides by
fibre size. These maps should not be silently identified. Uniform lifting
is a declared reference section, not an inference that the original
conditional law was uniform.

### 2.2 Split exact sequence and projections

**Proposition 1 — finite splitting.** For every such finite map,

$$
0\longrightarrow\ker P\longrightarrow\mathbb Q^X
\xrightarrow{P}\mathbb Q^{Y_0}\longrightarrow0
$$

is split exact, with $PS=I$. Consequently

$$
\Pi=SP,\qquad \mathcal N=I-SP
$$

are complementary projections, and

$$
\Pi^2=\Pi,\qquad \mathcal N^2=\mathcal N,
\qquad \operatorname{im}\mathcal N=\ker P.
$$

For every $p\in\mathbb Q^X$, put $m=Pp$ and $z=\mathcal Np$. Then

$$
\boxed{p=Sm+z,\qquad Pz=0.}
$$

**Proof.** For each $y$, summing the $|X_y|$ entries of $Sm$ returns
$m_y$, proving $PS=I$. The projection identities follow by multiplication.
Also $P(I-SP)=0$, while $(I-SP)z=z$ whenever $Pz=0$. This proves the
range statement and the decomposition. The decomposition is unique because
$m=Pp$ and $z=p-SPp$. $\square$

The implementation permits a codomain containing points outside $Y_0$.
Their marginal mass must be zero, and no division by an empty fibre occurs.

For probability laws, require $p_x\ge0$ and $\sum_xp_x=1$. Conversely,
a nonnegative mass-one $m$ and a fibre-null $z$ define a probability law
precisely when $Sm+z$ is nonnegative. The residual itself is a signed
measure and is not a second probability law. Where $m_y>0$, the actual
conditional probabilities are $p_x/m_y$; the reference values
$1/|X_y|$ coincide with them only when the residual vanishes on that fibre.

### 2.3 The Seinfeld zero retains its evaluation map

Using the ordinary measure-observable pairing,

$$
\boxed{\langle p,f\rangle
=\langle m,Af\rangle+\langle z,f\rangle.}
$$

The final term is exactly the information omitted by replacing $p$ with
its uniform lift. Regard $z=\sum_xz_x[x]$ as a vector in the free rational
space on the labelled atoms. For every $g\in\mathbb Q^{Y_0}$,

$$
\langle z,g\circ\pi\rangle
=\sum_y g_y\sum_{x\in X_y}z_x=0.
$$

Thus $z$ is a formal null witness for every observable pulled back through
$\pi$. It need not be the zero formal vector, and it need not vanish
against an observable that varies within a fibre. Keeping only its
evaluated zero discards its coefficients and labels again.

## 3. Exactly how much linear information is necessary

**Proposition 2 — dimension and observable recovery.** The following
statements hold over $\mathbb Q$:

$$
\dim\ker P=|X|-|Y_0|.
$$

Recovering every rational law from its pushforward and additional rational
linear measurements requires at least this many independent measurements.
The bound applies in particular on every fixed strictly positive marginal
whose full fibres remain available. For a single rational observable $f$,
its expectation is determined by the pushforward for every probability law
if and only if $f$ is constant on each fibre.

**Proof.** Choose an anchor $x_y\in X_y$ in each nonempty fibre. The
vectors $[x]-[x_y]$, for $x\in X_y\setminus\{x_y\}$, form a basis
of its zero-sum subspace. Summing their counts proves the dimension.

Suppose $L:\mathbb Q^X\to\mathbb Q^k$ has $k<\dim\ker P$.
There is a nonzero rational $v\in\ker P\cap\ker L$. At any strictly
positive rational law $p_0$, choose a sufficiently small positive rational
$\varepsilon$ so that $p_0\pm\varepsilon v$ remain strictly positive.
They have the same mass, pushforward and $L$-data, but are distinct laws.
Their positivity follows, for example, by taking
$\varepsilon<\min_{v_x\ne0}p_{0,x}/|v_x|$.

If $f=g\circ\pi$, its expectation is $\langle Pp,g\rangle$.
Conversely, if $f_x\ne f_{x'}$ for two atoms in the same fibre, the
Dirac laws $\delta_x$ and $\delta_{x'}$ have identical pushforward
and different expectations. $\square$

There are two relevant qualifications. First, the dimension lower bound
concerns **rational linear measurements**, not arbitrary set-theoretic
encodings. Second, if a fixed probability marginal has zero mass on some
fibres, those fibres contribute no feasible probability variation. The
dimension of that fixed-marginal probability family is

$$
\sum_{y:m_y>0}(|X_y|-1).
$$

The module's `null_dimension` records the full algebraic kernel dimension,
independently of these positivity-boundary restrictions.

Full reconstruction is stronger than recovering one specified observable.
For that observable, retaining the scalar $\langle z,f\rangle$ suffices.
For a family of target observables, the necessary linear information is its
rank restricted to $\ker P$. This is the inherited annihilator criterion
implemented by [shadow source inference](../../observational_succ/shadow_source_inference.py).

## 4. Exact rational Fourier reconstruction on sixteen branches

### 4.1 Four Galois strata

Let $p=(p_0,\ldots,p_{15})\in\mathbb Q^{16}$ be any signed rational
row, and define

$$
\zeta=e^{2\pi i/16},\qquad
F_h=\sum_{j=0}^{15}p_j\zeta^{hj},\qquad m=F_0.
$$

The four representatives $F_1,F_2,F_4,F_8$ belong respectively to
$\mathbb Q(\zeta_{16})$, $\mathbb Q(\zeta_8)$,
$\mathbb Q(i)$ and $\mathbb Q$. Their rational dimensions are
$8,4,2,1$. In the existing basis $1,\zeta,\ldots,\zeta^7$:

| Channel | Potentially nonzero coordinate positions | Rational dimension |
| --- | --- | ---: |
| $F_1$ | $0,1,2,3,4,5,6,7$ | 8 |
| $F_2$ | $0,2,4,6$ | 4 |
| $F_4$ | $0,4$ | 2 |
| $F_8$ | $0$ | 1 |

These basis dimensions follow from the classical cyclotomic polynomials
$X^{d/2}+1$ for $d=2,4,8,16$. For $d\ge4$, substitution $X\mapsto X+1$
makes the polynomial Eisenstein at two; $d=2$ is linear. Thus the
displayed coordinates are unique rational coordinates, not merely formal
coefficients with an unverified complex evaluation.

For a nonzero frequency modulo sixteen, write $h=2^v r$ with $r$ odd
and $0\le v\le3$. Rationality of the weights gives

$$
F_h=\sigma_r(F_{2^v}),\qquad \sigma_r(\zeta)=\zeta^r.
$$

So every Fourier frequency is supplied by one of these four tagged Galois
strata. The rationality hypothesis matters: this argument is not an
assertion about arbitrary irrational coefficient rows.

### 4.2 An explicit antipodal inverse

**Proposition 3 — lossless rational codec.** The map

$$
p\longmapsto(m,F_1,F_2,F_4,F_8)
$$

is a rational linear isomorphism

$$
\mathbb Q^{16}\cong
\mathbb Q\oplus\mathbb Q(\zeta_{16})\oplus
\mathbb Q(\zeta_8)\oplus\mathbb Q(i)\oplus\mathbb Q.
$$

Here the summands are separately tagged vector-space coordinates. This is
not a claim that the nested subfields inside $\mathbb C$ have zero
intersection.

**Proof and inverse.** For $d=1,2,4,8,16$, define the folded masses

$$
P_d(j)=\sum_{\ell=0}^{16/d-1}p_{j+\ell d},\qquad 0\le j<d.
$$

For $d\ge2$, the coefficients of $F_{16/d}$ in its power basis are

$$
D_d(j)=P_d(j)-P_d(j+d/2),\qquad 0\le j<d/2,
$$

because opposite powers differ by a minus sign. Also
$P_{d/2}(j)=P_d(j)+P_d(j+d/2)$. Starting from $P_1(0)=m$, therefore,

$$
\boxed{
P_d(j)=\frac{P_{d/2}(j)+D_d(j)}2,\qquad
P_d(j+d/2)=\frac{P_{d/2}(j)-D_d(j)}2.
}
$$

Apply these formulas for $d=2,4,8,16$. They recover $P_{16}=p$ from
arbitrary rational channel coordinates, proving both injectivity and
surjectivity. The dimensions are $1+8+4+2+1=16$. $\square$

When the total mass is known, fifteen rational coordinates remain. For a
probability row this equals the dimension of the zero-sum residual from
uniform measure. These are **four exact field elements containing fifteen
rational coordinates**. No stable decoding of those coordinates from
approximate complex values is asserted.

### 4.3 A strictly positive control for each omitted stratum

Fix $h\in\{1,2,4,8\}$ and put $b=8/h$. Define

$$
v_j=
\begin{cases}
1,&j\equiv0\pmod{2b},\\
-1,&j\equiv b\pmod{2b},\\
0,&\text{otherwise}.
\end{cases}
\qquad
p_j^{\pm}=\frac1{16}\pm\frac{v_j}{32}.
$$

Both $p^+$ and $p^-$ are strictly positive mass-one rational laws.
Their Fourier difference is controlled exactly by

$$
\sum_jv_j\zeta^{gj}
=\left(1-e^{2\pi i g/(2h)}\right)
\sum_{t=0}^{h-1}e^{2\pi i gt/h}
=
\begin{cases}
2h,&h\mid g\text{ and }g/h\text{ is odd},\\
0,&\text{otherwise}.
\end{cases}
$$

Among the four representatives, only channel $h$ changes. Its change is
$h/8\ne0$. Thus dropping any one stratum loses genuine probability
information, even for laws strictly inside the simplex. Taking additional
frequencies from the other three Galois strata cannot repair that omission.

## 5. Why the energies cannot replace the signed channels

For $z_j=p_j-m/16$, finite Fourier orthogonality gives

$$
\sum_{h=1}^{15}|F_h|^2
=16\sum_jp_j^2-m^2
=16\sum_jz_j^2.
$$

For a representative $b\in\{1,2,4,8\}$, its stratum energy is

$$
\mathcal E_b
=\sum_{\substack{1\le h<16\\v_2(h)=v_2(b)}}|F_h|^2
=\operatorname{Tr}_{\mathbb Q(\zeta_{16/b})/\mathbb Q}
\left(F_b\overline{F_b}\right).
$$

Each trace sum is rational and nonnegative. However, for every deterministic
selector $p=\delta_j$,

$$
(\mathcal E_1,\mathcal E_2,\mathcal E_4,\mathcal E_8)=(8,4,2,1),
\qquad F_1=\zeta^j.
$$

All sixteen selectors have identical energy data, while their first signed
channel distinguishes them. Even knowing every individual $|F_h|^2$ does
not determine the selector.

For a joint probability table $p_{s,j}$, let $m_s=\sum_jp_{s,j}$ and
let $F_s(h)$ denote the Fourier transform of the unnormalized row. The
conditional chi-squared defect is

$$
\sum_{s:m_s>0}\frac1{m_s}\sum_{h=1}^{15}|F_s(h)|^2.
$$

When each positive row is a deterministic selector, this equals
$15\sum_sm_s=15$. That maximal fully conditioned energy is inherited
from the [selected branch work](SELECTED_BRANCH_SYNTHESIS.md); no
contraction is claimed here.

## 6. The full joint law and its source-dependent pairing

Let $S$ be a finite set of retained source labels and let $p_{s,j}$ be a
rational probability law on $S\times\mathbb Z/16$. Keeping the mass and
Fourier packet **for each source label** reconstructs the complete joint law.
Keeping only the source marginal and the aggregate branch law generally
does not.

A small exact receipt puts mass $1/2$ on $(\alpha,0),(\beta,8)$, versus
mass $1/2$ on $(\alpha,8),(\beta,0)$. Both source marginals, both branch
marginals and all aggregate branch Fourier coefficients agree. The signed
source weights $a_\alpha=1$, $a_\beta=-1$ nevertheless give

$$
\sum_s a_sF_s(1)=1\quad\text{and}\quad -1.
$$

The discrepancy lies entirely in the source/branch coupling.

### 6.1 The actual character also retains the tail phase

Attach a canonical rational tail $t_s\in[0,1)$ to each source label,
and let

$$
X(s,j)=\frac{j+t_s}{16},\qquad e(x)=e^{2\pi i x}.
$$

For every integer $h$,

$$
\boxed{\mathbb E_p e(hX)=\sum_s e(ht_s/16)F_s(h).}
$$

This is a direct factorization of each summand. The source-dependent tail
phase cannot be dropped or replaced by an unlabelled aggregate branch
coefficient. It generally lies outside $\mathbb Q(\zeta_{16})$.

The implemented `labelled_character_pairing` permits exact rational source
weights and returns an exact branch-character pairing. Its documentation
explicitly distinguishes that observable from the real BBP Weyl sum. The
displayed identity is a symbolic complex identity; this dossier does not
pretend that a formal rational-circle expression is already a numerical
evaluation or that every tail phase belongs to the sixteenth cyclotomic
field.

### 6.2 An authentic two-row coupling counterexample

For the original source define, for $n\ge1$,

$$
x_n=\{U_n\},\qquad j_n=\lfloor16x_n\rfloor,
\qquad t_n=\{16x_n\}.
$$

The first two source rows are exactly

| Source index $n$ | $x_n$ | $j_n$ | $t_n$ |
| --- | --- | ---: | --- |
| 1 | $2/15$ | 2 | $2/15$ |
| 2 | $1076/4095$ | 4 | $836/4095$ |

These values follow from $U_1=47/15$ and
$U_2=16U_1+106/819$, with all quantities obtained from the original
four-pole formula. The source labels also retain their original forcings
$r(2),r(3)$ and successor states.

On these two tagged sixteen-point fibres, define $P$ by mass $1/2$ at
$(1,2)$ and $(2,4)$. Define $Q$ by mass $1/2$ at $(1,4)$ and $(2,2)$.
Thus $P$ samples the two authentic predecessors uniformly, while $Q$
explicitly swaps their branch choices.

The source/target marginal is unchanged, as is the complete aggregate
branch law. Therefore every aggregate branch Fourier coefficient is also
unchanged. Yet the actual frequency-one character satisfies

$$
\mathbb E_P e(X)-\mathbb E_Q e(X)
=\frac{\zeta^2-\zeta^4}{2}
\left[e(t_1/16)-e(t_2/16)\right]\ne0.
$$

Indeed $\zeta^2\ne\zeta^4$ and

$$
t_2-t_1=\frac{58}{819},\qquad
\frac{t_2-t_1}{16}=\frac{29}{6552}\notin\mathbb Z.
$$

This proves nonvanishing symbolically. No approximate cyclotomic or
transcendental evaluation is used.

The swapped predecessors are

$$
x'_1=\frac{4+t_1}{16}=\frac{31}{120},\qquad
x'_2=\frac{2+t_2}{16}=\frac{4513}{32760}.
$$

They still satisfy their respective tagged one-step circle transitions,

$$
\{16x'_n+r(n+1)\}=x_{n+1},\qquad n=1,2,
$$

because changing $j_n$ changes $16x'_n$ by an integer. Both swapped
predecessors have even denominators and fail the authentic odd-support
condition. They do not form one coherent authenticated history either:
the first row's successor remains $x_2$, rather than the altered $x'_2$.

This is an explicitly changed-selection law on authentic tagged inverse
fibres. It is a counterexample to recovery from separate marginals, not a
second zero-seeded source trajectory or a counterexample to normality.

## 7. Odd support and minimal deterministic character tags

### 7.1 The support restriction selects a unique joint law

The original source has odd reduced denominators. For an exact canonical
tail $t=a/q\in[0,1)$ with $q$ odd, its sixteen inverse branches are

$$
x_j=\frac{j+t}{16}=\frac{qj+a}{16q},\qquad 0\le j<16.
$$

The denominator of $x_j$ becomes odd precisely when the numerator cancels
the entire factor sixteen. Hence

$$
qj+a\equiv0\pmod{16},\qquad
\boxed{j_*(t)\equiv-aq^{-1}\pmod{16}.}
$$

Since $q$ is invertible modulo sixteen, exactly one branch qualifies.
This is the inherited odd-torsion inverse theorem, expressed in branch
coordinates.

For any finite family of such tagged tails and any prescribed source
marginal $m_s$, a joint law supported only on odd-denominator predecessors
is therefore uniquely

$$
p_{s,j}=m_s\,\mathbf1_{j=j_*(t_s)}.
$$

Its residual and nontrivial branch coefficients are consequently

$$
z_{s,j}=m_s\left(\mathbf1_{j=j_*(t_s)}-\frac1{16}\right),
\qquad F_s(h)=m_s\zeta^{h j_*(t_s)}.
$$

Thus exact tail data plus this support condition restore a unique lift.
They do not invert averaging on unrestricted probability laws. Nor does
support uniqueness imply any balancing of the selected characters across
different source times.

### 7.2 A minimal tag for one deterministic character

For any integer $h$, put

$$
d=\frac{16}{\gcd(16,h)}.
$$

This includes $h=0$, for which $d=1$. For any branch labels $j,k$,

$$
\zeta^{hj}=\zeta^{hk}
\quad\Longleftrightarrow\quad
16\mid h(j-k)
\quad\Longleftrightarrow\quad j\equiv k\pmod d.
$$

Hence a deterministic mode has exactly $d$ distinguishable selector
classes, and $j\bmod d$ is a necessary and sufficient tag over all
possible selectors. This is a finite tag-cardinality statement, distinct
from the rational-linear dimension of arbitrary probability laws. It
asserts neither that all tags occur in an authentic finite prefix nor
that a fixed odd tail admits more than its one selected branch.

The tag can be computed as $-aq^{-1}\bmod d$. If a common conductor
$Q=cq$ with $c$ odd is used instead, the numerator becomes $A=ca$ and

$$
-AQ^{-1}\equiv-(ca)(cq)^{-1}\equiv-aq^{-1}\pmod d.
$$

Thus odd conductor enlargement leaves the selected character unchanged.
Keeping only the numerator is insufficient: $t=1/3$ and $t=1/5$ both
have numerator one, but select digits five and three, respectively.
Replacing exact tail information by real proximity also fails by the
inherited SS-06 discontinuity theorem.

## 8. Native implementation and finite verification

The [module](../../observational_succ/seinfeld_disintegration.py) exposes:

| Interface | Exact responsibility |
| --- | --- |
| `disintegrate_law`, `FiberDisintegration` | Pushforward, uniform lift, retained null residual and observable reconstruction |
| `marginal_obstruction` | Two probability laws witnessing failure of recovery from the marginal |
| `DyadicFourier` | Four tagged field channels, fifteen rational coordinates, antipodal inversion and signed characters |
| `branch_law`, `branch_channels` | Complete joint branch law with its source labels retained |
| `labelled_character_pairing` | Exact rational source-weighted branch-character pairing |
| `odd_selector_tag` | Character class under the inherited unique odd inverse |
| `authentic_branch_law` | Full original-history authentication and native source-labelled inverse rows |

The implementation reuses native `FiniteMap`, `ZeroWitness`, `Cyclo16`,
`BranchWitness`, `exact_odd_inverse` and original-history verification.
The authentic row labels include source index, forcing, current and
successor, literal carry and conductor. Generic source strings are
provenance metadata; assigning such a string does not authenticate an
arbitrary law. The authentic constructor performs the additional check.
Its finite probability measure samples source times uniformly as a declared
observation convention; it is not a stochastic generation claim about
the deterministic orbit.

The constructor's focused verification was:

```text
python -m unittest tests.test_seinfeld_disintegration -v
Ran 16 tests in 0.762s
OK
```

The [tests](../../tests/test_seinfeld_disintegration.py) cover unequal
fibres and empty codomain points, exact probability aliases, independent
polynomial Fourier evaluation, rational rank, all four positive omission
controls, energy/phase aliases, grouped original forcing through 47 states,
conductor enlargement, source-row swapping, changed seeds and illegal
even-denominator inputs. These are exact finite observations supporting
the stated interface; they are not an infinite statistical proof.

A separate read-only cross-audit checked the likelihood and field-feedback
modules, including an independent exact cyclotomic check of conditional
projections for composite radices. Its scope was those finite identities
and source conventions. This dossier does not claim completion of the
round's full repository suite; the synthesis and replay receipt carry the
round-level validation status.

## 9. Verdict and remaining dependency

**Verdict: rigorous finite reconstruction and exact obstruction.** The
Seinfeld formal null component can retain information erased by averaging
when its atom labels and signed coefficients survive. Its evaluated zero,
Fourier magnitudes and separate marginals do not retain that information.
The authentic odd-support restriction selects a unique lift, and the
codec specifies how to retain its observable content exactly.

The next dependency is a separate source-derived bound on the retained
signed pairing, including its tail phase. No such smallness estimate is
proved here. Reconstruction, support uniqueness and exact conditional
information remain compatible with concentrated or nonnormal laws.
The selected arithmetic cancellation obligation identified in the
[previous synthesis](SELECTED_BRANCH_SYNTHESIS.md) therefore remains open.
