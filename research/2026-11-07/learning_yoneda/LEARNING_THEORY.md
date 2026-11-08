# Source-authenticated causal learning: precise realization and memory

Status: **classical theorems and proved finite-source specializations**. This
consolidates LY-1–LY-6; it is not an arithmetic typicality theorem. The category
implementation is an adapter to main, not a replacement category hierarchy.
Claim names below are local to this dossier, not new global registry entries.

## Objects, chronology and declared access

A complete mathematical source signature is
\(\Sigma=(X,S,\iota,\{F_t\},\{r_t\},b,\mathcal A,\mathcal Y,
\mathrm{enabled},\mathrm{cost},\mathrm{frame},\mathrm{origin})\).
Here X is the complete carrier space, S its declared initial-source family,
\(\iota:S\to X\) its initial embedding, F its chronological evolution,
and actions have both report maps and post-action transition maps. Source
formulas, initial boundary, unwrapped coordinates, carry conventions, clock,
probe domain, allowed interventions, reference transport and provenance all
belong to the contract. A digest checks byte identity, not empirical provenance.
An intervention that changes forcing belongs to a different signature or an
explicitly enlarged experiment; it cannot be called the original orbit.

For BBP, b=16, r is exactly the four-pole formula in the frozen main source,
\(U_0=0\), \(U_t=16U_{t-1}+r(t)\). The circle projection is
\(x_t=U_t-\lfloor U_t\rfloor\). The integer carry at t is
\(c_t=\lfloor16x_{t-1}+r(t)\rfloor\), with
\(\lfloor U_t\rfloor=16\lfloor U_{t-1}\rfloor+c_t\).
`learning.exact_history` retains all three coordinates. Alternative seed
families below use the same forcing but **different boundary contracts**.

A history is a legal sequence of original source, evolving full carrier,
actions, reports and frames. Its observable transcript omits privileged
simulator state. Prefix restriction preserves chronology. Given transcript w,
the belief consists of pairs (original source, current state) compatible with
w. On action a and report y,
\[
B\mapsto B_{a,y}=\{(s,F_a(x)):(s,x)\in B,
 a\text{ enabled at }x,\;O_a(x)=y\}.
\]
For a universally lawful policy, a must be enabled at every surviving x.
An empty fiber is model failure. It is not a proof of a target by vacuity.
Memory obeys \(m_{t+1}=D_t(m_t,a_t,y_t)\); actions may depend on memory and
declared public state. Targets are functions of the **original** source or
history, not automatically of the current physical state.

## Category and lawful composition

At a finite resource horizon use the existing
`operational_yoneda_descent.BeliefGame` and `ObservationPathCategory`.
Objects are (remaining budget, belief) within a fixed signature and target;
arrows are actual words of lawful action/report generators. Identity is the
empty word, composition concatenation. Histories with the same endpoint can
remain distinct arrows. Prefixes are factorizations of these arrows.
The finite API's size/depth caps are explicit implementation bounds, not
mathematical nonexistence claims. Arbitrary finite horizons use the same
mathematical free-path construction.

A source-preserving map consists of a map of source labels and full states
preserving initial embedding, target, enabledness, report labels, costs,
source formula and every transition square. Its source image must cover the
declared receiver candidate family. Phase-valued reports additionally require
the stated gauge transport. The existing `CertifiedSourceMorphism` checks
the finite state/output/target squares; external provenance and costs still
require their separate contract. Its `induced_observation_functor` maps each
generator, then concatenates, giving `yoneda.FiniteFunctor`. Identity maps and
composition obey the functor laws by generator preservation.

## LY-1 — history-relative realization

Let an internal model and an authenticated carrier have a source-covering map
of the preceding kind. Every finite lawful policy produces the same public
transcript and original-target value after transport. **Proof:** initial
states correspond. At each step the policy sees the same transcript, so
chooses the same action; enabledness, report and transition squares preserve
correspondence. Induction proves the assertion for every finite path.
This realizes the carrier **up to the declared observational equivalence**;
injective full-state reconstruction needs an additional separating property.
Behavioral bisimulation alone does not supply a missing source map.

For a probe subcategory J, restricted Yoneda detects arrows f,g:A→B iff
some j in J and u:j→A have fu≠gu. This is the exact definition of faithful
action on that hom-set. Including A and its identity suffices. Fullness or
object reconstruction is not inferred from arrow detection. The finite
adapter checks a real four-path example: `pin,pin`, `pin,wait`, `wait,pin`,
`wait,wait` can have one endpoint while retaining different histories.
This uses the established main Yoneda machinery and its prior theorem.

## LY-2 — three different minimal-memory problems

**Offline, fully known source:** if the encoder knows s and the decoder has
projected state p(s), the least number of memory symbols for target q is
\(\max_z|q(p^{-1}(z))|\). Necessity is pigeonhole inside one physical fiber;
sufficiency labels target values separately inside each fiber. This assumes
the encoder knows enough to choose those labels.

**Transcript encoder plus future state:** the encoder only knows w(s).
First require that (w,p) determine q. Join transcript values w,w' when
some compatible s,s' satisfy p(s)=p(s') but q(s)≠q(s'). The least number of
memory symbols is the chromatic number of this graph. Necessity follows
because equal encoded colors would confuse that pair; a proper coloring
defines a unique decoder on realized (color,p) pairs. A self-conflict makes
decoding impossible. This is **already main claim O65**, implemented by
`interobserver_channels.exact_minimum_channel`, a Witsenhausen-type classical
result. `crucible` provides an original-forcing embedding, not a new coding
theorem. A binary target can require three colors (the C5 example).

**Online transcript memory:** a small final alphabet does not imply a small
streaming working register. Let all words d of length N over an alphabet of
size b be admissible, with a prescribed final target q(d). At depth t define
\[
p\equiv_t p'\quad\Longleftrightarrow\quad
\forall v\in\{0,\ldots,b-1\}^{N-t},\quad q(pv)=q(p'v).
\]
Let W_t be the number of these residual target functions. Among deterministic
time-dependent online observers reading one symbol per step, the exact
minimum number of distinguishable memory states **at each t** is W_t.
The minimum peak fixed register size is
\(\lceil\log_2\max_t W_t\rceil\) bits, with time provided externally.

**Proof:** if two different residuals share memory, append a suffix on which
their targets differ. The same updates then produce the same final answer,
a contradiction. Conversely use the residual function as state. Equality
of residuals implies equality after appending any symbol, so this update is
well-defined. The final residual is the target answer. This proves both
optimality and attainability at every layer. It is the fixed-length version
of classical residual/Myhill–Nerode minimization; it does not assert the same
formula for a partial, adaptive or destructive observation language.

**Source specialization:** for the authentic forcing and declared seeds
\(s_k=k/16^N\), the calibrated pins of #542 read the hex digits of k and
all circle states coincide at time N. Hence the residual theorem applies
without substituting a different dynamics. Take M earlier hex data digits,
with a pin-only sequential menu and no access to future address digits or
the full unwrapped state, then
\(\ell=\lceil\log_{16}(4M)\rceil\) address digits (at least one).
The binary target asks for the addressed bit of the earlier data; wrap extra
addresses modulo 4M. At t=M, all \(16^M\) residuals differ: two data words
differ in some bit, and that bit has an admissible address. Thus even this
**single Boolean target** needs at least 4M working bits before the address,
although its final answer needs one bit. Storing the data attains the bound
at that cut. This sharp source-family application refines #542's final
ancestry-memory discussion; it is not a new information-theory theorem.

This is mathematical memory relative to a lossy projection. Complete
unwrapped arithmetic states can preserve information that the circle lost.

## LY-3 — toolkit-relative learning saturation

For a fixed finite deterministic carrier with complete known action menus
and observable enabledness (or the same enabled menu at every state),
start with the partition by currently available observable outputs and refine
by all action outputs and successor-block labels, including enabledness.
When one **global** refinement leaves the partition unchanged, it is an
output-compatible transition congruence. Induction on action words proves
that no finite admissible continuation distinguishes a surviving pair.
Conversely any split has a finite separating continuation, obtained by
backtracking the refinement. At most |X|−1 strict partition refinements are
possible; this is not a bound on waiting time in an unknown nonstationary
source. Target truth is checked for constancy on the resulting behavioral
classes; an unread target must not be inserted as an observable. For example,
two states with identical reports and transitions but opposite hidden target
values remain observationally inseparable forever. Starting refinement with
their target values would falsely manufacture a separating probe. Existing
main behavioral partitions and goal bisimulation address related but
differently typed tasks; the target-aware congruence is not by itself a
certificate that the target can be read. When enabledness is hidden, an
illegal action cannot be used as a discriminator; universally lawful policies
must instead be analyzed in the belief game with its actual report semantics.

Saturation of a single reached belief means every allowed continuation
preserves its target ambiguity; use the full belief game for destructive
actions, not just pairwise separability. Adding a new probe, source candidate,
precision tier or intervention changes the closure and may break saturation.
Finite data cannot establish completeness of an unknown physical toolkit.

## LY-4 — strict adaptive advantage, with identical resource accounting

Main already has a two-step adaptive proof policy that beats every fixed
two-step schedule; reuse that result. Here is a sharp threshold specialization.
At one declared measurement epoch consider M ordered, distinguishable phases
(for instance the finite seed grid at t=0), with the **only** probes
\(q_j(k)=1[k\ge j]\), j=1,…,M−1. Probes are nondestructive and no source
evolution occurs during this finite ideal query session. Each costs one.
An adaptive binary search identifies k in \(\lceil\log_2M\rceil\) probes.
Every fixed k-probe schedule has at most k+1 distinct output vectors because
its threshold boundaries cut the ordered list into at most k+1 intervals;
therefore fixed exact identification needs M−1 probes. Both bounds are sharp.
For M=16 this is 4 versus 15. It makes no claim for a richer fixed menu,
different time budget, destructive sensor, or actual physical acquisition.

## LY-5 — source-anchored coherent reconstruction

For \(z_n(h)=e(hU_n)\) and \(S_d(n)=U_{n+d}-16^dU_n\),
\(z_{n+d}(h)\overline{z_n(16^dh)}=e(hS_d(n))\) is seed-blind.
The open path K_(n,t)(h)=z_n(h)conj(z_t(h)) has seed charge
\(h(16^n-16^t)\); at t=0 and literal s=0 it is exactly z_n(h).
For finitely many integer tones the total charge is \(\sum_j h_j16^{t_j}\).
Zero charge erases the seed; nonzero charge retains a character of it.
These identities extend the declared common basis; the general charge
classification is inherited from #520, not counted again as an advance.

Under gauge \(z_n\mapsto e(\gamma_n)z_n\), open paths acquire
\(e(\gamma_n-\gamma_t)\); transport this factor before adding responses.
Use the positive-sign convention \(\hat\mu(h)=\int e(hx)d\mu(x)\).
For affine dynamics f(x)=bx+a, the proper pullback of a character is
\(e_h\circ f=e(ha)e_{bh}\). Thus the coherent observation map on laws
obeys \(\widehat{f_*\mu}(h)=e(ha)\hat\mu(bh)\).
The corresponding kernel transport is tensor-square pushforward and retains
all off-diagonal terms. Independent unknown frames destroy this comparison.

Law reconstruction (all moments), current-state reconstruction (point-law
special case), initial-seed reconstruction (inverse dynamics plus lift),
and full-history reconstruction (path plus interventions) are separate.
Even all circle moments at every time starting at N lose the 16^N ancestor
choices in #542; a retained earlier reading can distinguish them.
Finite-bandwidth limits are quantified independently in `spectral`.

## LY-6 — inverse limits and the exact quantifier firewall

Let S be compact Hausdorff and all transcript compatibility sets B_w be
closed. For one compatible infinite transcript, its nonempty nested finite
fibers have nonempty intersection. Equivalently a tower of nonempty compact
history spaces with continuous compatible bonding maps has a nonempty inverse
limit (the history spaces are compact Hausdorff). **Proof:** all finitely many coordinate/compatibility conditions can
be realized at their deepest level; apply compactness of the product. The
realizer belongs to S only if S itself is the authenticated source domain.

If the nested transcript maps are continuous and finite-discrete, a
continuous target q:S→Q has compact metric image, and q is constant on
every full-transcript fiber, then every epsilon admits a finite stage whose
fibers have q-diameter below epsilon. Prove this by compactness of the closed set of pairs with
target distance at least epsilon: each pair is separated at some stage,
and finitely many open separating sets cover it. Finite discrete continuous
targets consequently have an exact finite certificate. None of these
premises holds merely because an empirical prefix is long.

Counterexamples: S=positive integers with reports 1[s≤t] realizes every finite
all-zero prefix but no infinite all-zero transcript (lack of compactness).
In compact [0,1], nested compatibility sets (0,1/n) are nonempty with empty
intersection (lack of closedness). Cantor streams with coordinate probes
identify each stream in the limit, yet `stream is identically zero` is not
decidable from any finite prefix (discontinuous target). Eventually-zero
streams realize every finite binary word, while their projective completion
also contains non-eventually-zero streams (source-family inadequacy).
Finally `for every N there exists a finite-horizon model/certificate` never
implies a uniform all-epoch bound on one fixed model. The arithmetic front
gives a quantitative same-forcing instance of this last quantifier failure.

Closed individual fibers alone do not give the uniform target theorem:
take the compact set \(S=\{0,1\}\cup\{a_j=1/(j+3),
b_j=1-1/(j+3):j\ge1\}\) and q the inclusion into [0,1]. At stage n
pair a_j with b_j for j≥n and leave other classes singleton. These partitions
refine, every fiber is finite closed, and the full intersection separates all
points. Nevertheless every stage retains target diameter at least 1/2.
Its pair-equivalence relation is not closed: (a_j,b_j)→(0,1), which is
separated. This is the specific discontinuity that the finite continuous
transcript hypothesis excludes.

For the π gate one needs, for every fixed h≠0 and epsilon>0, a **single**
A0(h,epsilon) such that every A≥A0 has |c_A(h;0)|<epsilon. A model or
constant chosen separately after seeing A does not discharge this statement.
Use main `proof_contracts`; no formal-authority catalog is modified.

## Provenance and scope

Theorems on fibers, finite belief games, Yoneda, compactness and coding are
classical and/or inherited. Main O65, O392/O411–418, O595, O649/O651 and O662
already contain important parts. #542 supplies the BBP digit-pin and collapse
identity. External primary background: [Nerode, Linear Automaton
Transformations (1958)](https://doi.org/10.1090/S0002-9939-1958-0135681-9) and
[Witsenhausen (1976)](https://ieeexplore.ieee.org/document/1055607/).
The proofs above are supplied explicitly; no priority claim is made.
The new code checks source lifts, real functors, residual working-memory
optimality, and hostile controls. Neither finite learning nor compact
realization establishes zero-seed arithmetic mixing.
