# Seinfeld SUCC, inverse averaging, and realized fields

**Result:** an exact retained-information construction, a source-authenticated
Fourier revelation theorem, finite discriminators for dynamic field feedback,
and a normalized-posterior interpretation of the earlier golden–Gamma source.
The arithmetic cancellation estimate remains **OPEN**. This round proves no new
selected Weyl saving, no normality theorem, and no physical identification of BBP.

**User-facing date:** 2026-10-26, America/New_York; execution continues into
2026-10-27 UTC. **Live research base:** PR [#313](https://github.com/femboy2112/SUCC/pull/313),
`79344c62c39c96755b742700b3d4d22fa60d86da`, descending through #312/#310/#309/#306.
Main remains `6dd80730c3575d91f746546a25da5aedbd2e2737`. Sibling #311 was inspected
at `a34c4484059e667202b97d5ab4102560987b1406`, not merged. The
[research contract](SEINFELD_REALIZATION_CONTRACT.md) records the questions,
rival hypotheses and falsification criteria before this synthesis.

## 1. The connection that survives

The author's proposal has a precise finite realization:

> Information removed by averaging can be retained as a labelled element of the
> averaging map's kernel. Selection pairs with that retained information. A
> subsequent material update can change the next path law, provided its update
> rule is specified.

The word **labelled** is essential. A zero after evaluation does not mean that
the labelled relation is absent. This is the existing Seinfeld distinction,
now applied directly to probability pushforward and its inverse problem.

Let $\pi:X\to Y$ be a finite surjection, and let $p_x$ be a rational probability
law. Define

$$
m_y=\sum_{\pi(x)=y}p_x,\qquad
u_x=\frac{m_{\pi(x)}}{|\pi^{-1}(\pi(x))|},\qquad z_x=p_x-u_x.
$$

Then

$$
\pi_*z=0,\qquad p=u+z,\qquad
\mathbb E_p f=\sum_y m_y\operatorname{avg}_{\pi^{-1}(y)}f+\sum_xz_xf_x.
$$

The residual $z$ vanishes against every coarse observable $f=g\circ\pi$.
It can have a nonzero pairing with an observable that distinguishes paths
within a fibre. Keeping $m$ and $z$ reconstructs the full law; keeping only
$m$ cannot generally do so. The law still does not specify which atom occurred.

For example, three atoms of a fibre can have weights $(1/4,1/8,1/8)$ and total
mass $1/2$. The uniform lift gives $(1/6,1/6,1/6)$. The indicator of the first
atom has expectation $1/6+1/12=1/4$: its missing $1/12$ is the pairing with
the retained zero-sum residual. All computations are exact.

Categorically, the useful completed object is the split sequence

$$
0\longrightarrow\ker\pi_*\longrightarrow\mathbb Q^X
\mathop{\longrightarrow}^{\pi_*}\mathbb Q^Y\longrightarrow0,
$$

with the specified uniform section and the positivity constraint $u+z\ge0$.
The signed residual supplies an honest role for positive and negative
directions without assigning negative probabilities. A zero object by itself
does not record which labelled path produced its zero evaluation. That path
data must live in the retained carrier.

This general linear-algebra/disintegration structure is classical and partly
present in `shadow_source_inference.py`. The new work makes its connection to
`seinfeld_succ.ZeroWitness`, rational branch Fourier data and the original BBP
source explicit. Full proofs and recovery limits are in
[the null-residual dossier](SEINFELD_NULL_RESIDUAL_AND_FOURIER_CODEC.md).

## 2. The latest branch changes what must be retained

PR #313 proves a quantitative carry/arrival replacement budget for the original
four-pole source. At prescribed subquadratic resolution the representation error
vanishes; it also proves that exact tail conditioning makes the actual branch
law a Dirac mass, with conditional mode energy one and total defect fifteen.
This latter obstruction occurs on the authentic prefix itself.

Consequently finer conditioning cannot be treated as a mechanism that makes
those positive energies small. What must survive is the **signed coupling of
source label, branch and remainder**. Marginals and energies do not determine it.

For a rational row of sixteen branch weights, the total mass and four exact
field values suffice for lossless reconstruction:

| Modes represented | Exact field | Rational coordinates |
|---|---|---:|
| Odd modes, represented by $F_1$ | $\mathbb Q(\zeta_{16})$ | 8 |
| Twice-odd modes, represented by $F_2$ | $\mathbb Q(\zeta_8)$ | 4 |
| Four-times-odd modes, represented by $F_4$ | $\mathbb Q(i)$ | 2 |
| Mode 8, represented by $F_8$ | $\mathbb Q$ | 1 |

Here $F_h=\sum_{j=0}^{15}p_j\zeta_{16}^{hj}$. These are four **field elements**
containing fifteen rational coordinates, not four rational numbers. Galois
conjugation supplies the other modes; successive antipodal splits reconstruct
the row. For fixed mass this is optimal among rational linear recoveries of
arbitrary rows. Removing any stratum has a pair of strictly positive probability
laws that agree on all remaining strata and differ on the omitted one.

All sixteen deterministic selectors have the same stratum energies
$(8,4,2,1)$. Their signed primitive phases are all different. Energy therefore
cannot recover the selector even in this smallest complete branch space.

There is an authentic source-level coupling control. The first two positive-time
branch/remainder records are

$$
(j_1,t_1)=(2,2/15),\qquad(j_2,t_2)=(4,836/4095).
$$

Swap the two digits while retaining the two source labels and remainders.
Both marginals, and every aggregate branch Fourier mode, remain unchanged.
The actual $h=1$ character mean changes by

$$
\frac{\zeta_{16}^{2}-\zeta_{16}^{4}}2
\left(e(t_1/16)-e(t_2/16)\right)\ne0,
\qquad e(s)=\exp(2\pi i s).
$$

The changed predecessors still map individually to the tagged successors on
the circle, but have even reduced denominators. The native odd-source passport
rejects them as the original selected history. This is a source-labelled
counterexample, not a newly admissible BBP orbit.

## 3. Selection restores phase through a signed information identity

On one finite filtered probability space, let $P$ be a reference path law,
$Q\ll P$ the selected law, and $F$ the terminal observable. With a trivial
initial sigma-field, put

$$
R_t=\mathbb E_P[dQ/dP\mid\mathcal F_t],\qquad
M_t=\mathbb E_P[F\mid\mathcal F_t].
$$

The exact identity is

$$
\boxed{\mathbb E_QF-\mathbb E_PF
=\sum_t\mathbb E_P[(R_t-R_{t-1})(M_t-M_{t-1})].}
$$

Thus the selected difference is the signed pairing between changes in selection
likelihood and changes in visible information. Positive quadratic energies are
not replacements for that pairing. A four-path rational example has covariance
increments $+1,-1$, positive observable energy at both steps, and total selected
difference zero. Reflecting the observable reverses the two signed terms while
preserving their energies.

This is a classical conditional-expectation identity, specialized here to the
source inverse tree. It makes the proposed information location explicit;
it does not estimate its temporal cancellation automatically.

### Exact single-revelation theorem

Fix radix $b\ge2$, depth $d$, a tail $a$, and integer frequency $h$. Give
$J\in\{0,\ldots,b^d-1\}$ the uniform **declared** reference law, with

$$X_J=(a+J)/b^d\pmod1,\qquad\mathcal F_t=\sigma(J\bmod b^t).$$

The character projection is exactly

$$
M_t=\mathbf1_{b^{d-t}\mid h}\,
e\!\left(\frac{h(a+(J\bmod b^t))}{b^d}\right).
$$

When $b^d\nmid h$, let $v_b(h)=\max\{q:b^q\mid h\}$. The character is
zero before $t_*=d-v_b(h)$ and equals its terminal character $F(J)$ afterward;
on the selected cylinder this is the selected value $F(J_*)$.
It has **one nonzero observable innovation**, not a fixed fractional loss at
every level. For $b=2$ and depth $4k$, the revelation is $4k-v_2(h)$ when
that number is positive. Frequencies divisible by the whole conductor are
constant on the fibre and have no innovation.

A selected word has density $R_t=b^t$ on its prefix cylinder and zero elsewhere.
Its second moment is $b^t$, its chi-square cost $b^t-1$, and its relative
entropy $t\log b$. All the selected character is recovered by the covariance
at $t_*$. These costs are identical for every word, including periodic ones.

`authentic_inverse_window` attaches this construction to arbitrary finite
windows of the original zero-seed four-pole recurrence. The forcing is stripped
exactly; the odd denominator selects the unique admissible inverse. Binary and
hexadecimal versions agree on the selected phase. Literal reduced-state branch
digits can differ from raw or normalized fibre coordinates; the proof and oracle
retain those conventions rather than identifying their digit strings.

### The continuous approximation obstruction is quantitative

For the inherited odd-torsion inverse $S$ and $16\nmid h$,

$$
\inf_{f\in C(\mathbb T)}\sup_{t\in D_{\rm odd}}
|e(hS(t))-f(t)|=1.
$$

Indeed all sixteen branch labels occur arbitrarily near each tail. Averaging
the squared distances to their rotated roots of unity gives
$\|e(hS)-f\|_\infty\ge\sqrt{1+\|f\|_\infty^2}$, so zero is the unique optimal
continuous approximant. Explicit nearby rational tails give a finite Lipschitz
lower bound. The exception $h=16k$ is exact: the character is $e(kt)$ and
continuous. This is a uniform all-carrier obstruction, not an orbit-specific
lower bound or a prohibition of averaged/source-dependent transport.

Proofs, the oracle and the precise finite/infinite boundaries are in
[the selection and revelation dossier](SELECTION_LIKELIHOOD_AND_REVELATION.md).

## 4. Realization and the lightning connection

An observed past event has conditional probability one. Its effect on future
predictions depends on the joint law and any declared material update. The
repository's existing history-dependent Dirichlet-to-Neumann construction
already models field recomputation and hidden material memory. This round
adds a common finite comparison that makes rival explanations disagree.

Take two arms of three unit-resistance edges. A realized prefix becomes
conducting. The remaining arm resistances after a first left event are $2,3$;
their currents are $1/2,1/3$. Choose the next edge proportionally to current.

| Declared law | Next left after observing/realizing L | Probability of LL |
|---|---:|---:|
| Known independent fair choices | $1/2$ | $1/4$ |
| Linear count reinforcement, initial weights $(1,1)$ | $2/3$ | $1/3$ |
| Field solved again after growth | $3/5$ | $3/10$ |

The field model assigns $P(LLR)=3/40$ and $P(LRL)=1/10$ even though both paths
end at the same geometry $(2,1)$. Their odds are $3/4$. A terminal Doob tilt
of the fair law preserves equal-endpoint odds, so it cannot reproduce these
path weights merely by reweighting terminal counts. The final field in this toy
depends only on the final geometry; it does not retain the full order as material
memory. The inherited DtN example separately addresses hidden material memory.

The normalization itself has a particularly direct form. For remaining lengths
$a,b$, use the potential $H=a!b!$ and the fair kernel $K$. Then

$$
D=\frac{KH}{H}=\frac12\left(\frac1a+\frac1b\right),\qquad
K^H(x,y)=\frac{K(x,y)H(y)}{(KH)(x)}.
$$

This gives the field choice $b/(a+b)$, and along a path

$$
\log\frac{P_{\rm field}(\omega)}{P_{\rm fair}(\omega)}
=\log H(s_T)-\log H(s_0)-\sum_{t<T}\log D(s_t).
$$

The accumulated normalization terms depend on the route. They explain the
different weights of paths with the same endpoint. If the potential is harmonic,
the extra factors disappear and ordinary endpoint Doob reweighting is recovered
(event conditioning when the terminal weight is the corresponding indicator).
This is a precise multiplication-to-log connection within the declared model.

There is a necessary identifiability control. Linear Pólya reinforcement has
exactly the same probability for every finite word as a fixed unknown bias
drawn once from a Beta law and subsequently learned by Bayes. Therefore a
reinforcement-shaped predictive curve alone does not establish a physical
change. Interventions require a specified causal model.

The field analogy has a classical primary reference in
[Losev–Smirnov, *How Long Are the Arms in DBM?*](https://arxiv.org/pdf/2307.14931):
dielectric-breakdown growth uses harmonic measure of the current cluster.
The finite theorem and physical scope are developed in
[the realized-field dossier](REALIZED_PATHS_AND_FIELD_FEEDBACK.md), with the
existing repository predecessors and Doob reference explicitly attributed.

## 5. Two controls that prevent artificial cancellation

**A mixing field does not automatically randomize the arithmetic factor.**
If an enlarged process projects almost surely to the exact original update
$U_{n+1}=16U_n+r(n+1)$ and retains $U_0=0$, its arithmetic projection is the
same deterministic history. Conditional on the current selected state,
auxiliary mixing leaves every successor character unchanged. Allowing mass
$\epsilon$ to leave that selected successor gives the sharp one-step bound
for the auxiliary projected next state $V'$ conditional on the current state:

$$|\mathbb E_{\rm aux}[e(hV')\mid Y_n]|\ge\max(0,1-2\epsilon).$$

Complete conditional cancellation needs leakage at least $1/2$. This says
nothing against cancellation across different deterministic source times.
Randomizing the initial seed is a different law; Haar seed averaging would
cancel nonzero-frequency characters for every forcing, including counterfeit sources.

**Local phase losses do not automatically multiply.** Let $X_0=1$ and take
independent signs $X_n$ with $P(X_n=1)=3/4$. For $Z_n=X_{n-1}X_n$,

$$
|\mathbb E[Z_n\mid\mathcal F_{n-1}]|=1/2,\qquad
\mathbb E\prod_{t=1}^nZ_t=\mathbb E X_n=1/2.
$$

The phase product telescopes. The twisted matrix is an idempotent with
eigenvalue one even though the underlying chain mixes in one step. The exact
recursion retains the feedback covariance omitted by a product of local means.
A genuine finite operator contraction can instead be certified by uniformly
positive probability paths from every start that reconverge with separated
accumulated phases, or by one such pair and finite irreducibility. The
[revelation dossier](SELECTION_LIKELIHOOD_AND_REVELATION.md) gives the quantified
criterion and its coboundary obstruction. It remains a theorem about a declared
kernel until an arithmetic observable transport has been proved.

## 6. The positive golden–Gamma connection: posterior and exact log coordinate

The earlier [common-source bridge](OILY_MACARONI_SOURCE_BRIDGE.md) and
[atomic substrate](FOUR_POLE_ATOMIC_SUBSTRATE.md) already provide the finite
polynomial, Gamma/Mellin, golden fixed-point and binary construction interfaces.
The [third-shadow continuation](OILY_TOTIENT_THIRD_SHADOW.md) retains their
normalization and source restrictions. Those contributions are used unchanged.
The new connection is that the **same finite beta family** arises from the
path-inference model used to distinguish reinforcement from learning.

### A selected finite prefix produces the previous common source

Declare a static latent bias $\Theta\sim\operatorname{Uniform}(0,1)$ and letters
that are independent conditional on it, with $P(R\mid\Theta)=1-\Theta$.
After the finite event $A_m=R^{m-1}$,

$$P(A_m)=1/m,\qquad \Theta\mid A_m\sim\operatorname{Beta}(1,m).$$

For $X_m=m\Theta$, the posterior density is exactly

$$p_m(x)=(1-x/m)^{m-1},\qquad0<x<m.$$

This is the earlier finite common source, recovered from a selected path and
its retained latent law. Its known observables give

$$P(X_m>1)=(1-1/m)^m\to e^{-1},\qquad
\mathbb E\log X_m=\log m-H_m\to-\gamma,$$

while its Laplace transform tends to $L(s)=1/(1+s)$, whose positive fixed
point is $\lambda=\varphi^{-1}$. The density and limits are inherited;
the explicit posterior/path interpretation is the added link.

### The logarithmic coordinate is even cleaner

Under each finite posterior, set $Z_m=-m\log(1-\Theta)$. Then
$P(Z_m>z)=e^{-z}$ for every $z\ge0$: **$Z_m$ is exactly exponential with
mean one at every finite $m$**, and

$$X_m=m(1-e^{-Z_m/m}).$$

An additional $R$ reweights by $e^{-Z_m/m}$ and rescales by
$c=(m+1)/m$. Its normalized update satisfies

$$\mathbb E_{\rm new}f(Z_{m+1})
=c\,\mathbb E_{\operatorname{Exp}(1)}[e^{-Z/m}f(cZ)]
=\mathbb E_{\operatorname{Exp}(1)}f(Z).$$

The exponential law is a fixed law of this tilt-and-rescale update. Its Laplace
transform and logarithmic moment are $1/(1+s)$ and $-\gamma$. The golden
fixed point and Euler's constant are therefore different exact functionals of
the same normalized conditional law. The declared prior selects shape one;
normalization invariance by itself does not make this the unique fixed law.

### The shrinking error is a positive log-linearization defect

Let $\delta=\lambda-\gamma$ and use the inherited Euler remainder
$\epsilon_m=H_m-\log m-\gamma$. The coupling gives

$$
\boxed{\epsilon_m=\mathbb E[\log Z_m-\log X_m]
=\delta-[\lambda+\mathbb E\log X_m]>0.}
$$

The **previously proved source-specific** Green-tail comparison now connects
this posterior log defect to the actual arithmetic error:

$$
\frac1{(8m+7/2)^2}<T_m<\frac{\epsilon_m^2}{16},\qquad
\left(\frac m{m+7/16}\right)^2<\frac{16T_m}{\epsilon_m^2}<1.
$$

Thus $T_m\sim\epsilon_m^2/16$. This is an inherited quantitative BBP theorem
with a new probabilistic interpretation of its error variable. It remains
distinct from cancellation of the expanding selected phases.

The [posterior dossier](POSTERIOR_GOLDEN_GAMMA_CONNECTION.md) proves these
path and hazard identities and records discriminating controls. Conditional
independence matters: reusing one latent coin for all trials preserves each
one-step conditional marginal but destroys the beta family for $m>2$.
A changed prior or scale changes the fixed-coordinate functionals. Full event
selection costs $\log m$ in relative entropy, while the latent posterior
marginal retains $\log m-1+1/m$; the exact difference is $1-1/m$.

This is finite conditioning with a continuous latent law, not a finite-state
exact output of an irrational constant or a sample-path limit of one fixed
$\Theta$. The infinite all-$R$ event has probability zero. A cumulative-hazard
coordinate can produce an exponential law for any continuous posterior, so
that form alone does not authenticate BBP. The explicit coordinate, finite
distortion and original-source error comparison are the pinned connection.

The same centering cancels from the error for any real constant in place of
$\lambda$, and a common phase offset leaves Fourier moduli unchanged. To make
the oily-macaroni offset necessary for an arithmetic cancellation estimate
still requires a source-dependent relative weight/phase identity that survives
the existing normalization controls. No BBP path sampler is identified here.

## 7. Authority, implementation, and the remaining proof cut

| Claim | Authority and limit |
|---|---|
| Coarse law plus labelled kernel residual reconstructs the joint law | PAPER-PROVED finite linear algebra; exact native implementation |
| Four dyadic field packets give an optimal rational-linear branch codec | PAPER-PROVED; exact rational and cyclotomic controls |
| Selection difference is a signed innovation pairing | CLASSICAL identity; source-specific finite interface |
| Inverse character has one explicit revelation level | PAPER-PROVED for every finite radix/depth; original-source wrapper and independent oracle |
| Odd selector has sharp continuous minimax error one | PAPER-PROVED on the entire odd carrier; no selected-orbit lower bound |
| Geometry changes path probabilities and equal-endpoint odds | PAPER-PROVED for the declared toy; no physical or arithmetic identification |
| Selected prefix recovers the beta family; exact log coordinate is exponential and its log defect is $\epsilon_m$ | PAPER-PROVED posterior interpretation; golden/Gamma limits and BBP tail comparison inherited |
| Deterministic factor/leakage and adaptive product counterexample | PAPER-PROVED; exact hostile controls |
| New selected $o(N)$ estimate, π normality, RH | OPEN; none proved |

The implementation adds `seinfeld_disintegration.py`, `path_likelihood.py`,
`path_field_feedback.py`, their three focused test modules, a source-hashed
[exact replay probe](../../scripts/seinfeld_realization_probe.py), and a
[standalone oracle](seinfeld_revelation_oracle.py) with no production imports.
All original source and archival bytes remain unchanged. There is no new Lean
formalization or claim of external peer review. The three delegated bearings
used the same model family; the independent algebra, source mutations and
standard-library enumeration provide different verification routes.

See [the validation record](SEINFELD_REALIZATION_VALIDATION.md) for actual test
counts, provenance and replay outcomes. Its full-suite status is recorded only
after the process completes. The
[next research handoff](../../handoffs/SEINFELD_REALIZATION_NEXT_PI_2026-10-26.md)
states the source transport and phase-correlation obligations precisely.

The remaining cut is to prove cancellation of the **authentic signed terms
across source times**, preserving their selector/remainder association and
paying the existing carry/bin transport errors. Writing those terms as a
likelihood covariance is an exact reformulation. It becomes a new arithmetic
estimate only when an independent source argument bounds the signed sum.

## 8. Publication-time connection to the latest coherence-group draft

Draft #314 appeared while this round was being published. Its formal
$\mathbb Q[C_{16}]$ class amplitudes are losslessly represented by our mass
and four-field codec. Its strong-lumpability requirement adds the precise
criterion for a grouping to preserve the next class as well as today's phase.
The [publication addendum](SEINFELD_COHERENCE_POSTERIOR_BRIDGE.md) pins the
inspected sibling commit and supplies the compatibility proof.

It also produces a sharper exact discriminator. In #314's symmetric
sixteen-color Pólya model, either avoiding color zero for $r$ steps or selecting
the literal word $1^r$ gives the same marginal
$\Theta_0\sim\operatorname{Beta}(1,15+r)$. Thus both selections retain the exact
exponential log coordinate, golden fixed point, Gamma log mean and shrinking
$\epsilon_{15+r}$ described above. Their joint laws retain different information:
the latent character's second moment tends to $1/15$ in the avoidance family
and to $1$ in the literal-word family. These moments also govern the future
empirical character averages through the exact diagonal/off-diagonal identity.

This proves that the shared constants marginal and its shrinking defect alone
cannot force Fourier cancellation in the declared model. The information in
the remaining color proportions matters. The addendum gives full paper proofs
and an independent rational replay; no sibling code or production/test change
is included, and no authentic BBP sampling identification is inferred.
