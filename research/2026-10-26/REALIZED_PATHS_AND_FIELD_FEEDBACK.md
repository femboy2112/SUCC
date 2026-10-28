# Realized paths, conditioning, and field feedback

**Research date:** 2026-10-27. **Baseline:** PR #313 at
`79344c62c39c96755b742700b3d4d22fa60d86da`.
**Status:** paper proofs and exact finite model certificates. This dossier supports
the [round synthesis](SEINFELD_INVERSE_AVERAGING_AND_REALIZATION.md).

The author's proposal has a precise classical realization: a selected path can
retain information that an endpoint or a path average loses, and an explicitly
declared material update can change the field governing later events. The
mathematical task is to distinguish three operations: conditioning a fixed law,
reinforcing transition weights, and changing the geometry before solving its
field again. They need not have the same predictions.

The results below give a common finite comparison, an exact discriminator between
endpoint conditioning and geometry feedback, and a limitation on transferring
auxiliary randomness to the original arithmetic source. They do **not** identify
BBP with a stochastic growth process. Selected Weyl cancellation, base-16 normality
of pi, and RH remain **OPEN**. No new scholarly priority or physical quantum
interpretation is asserted.

## 1. Provenance: what was already present

The [HISTORY-DTN dossier](../2026-10-22/HISTORY_DEPENDENT_DTN_SUCC_FUCC.md)
already develops finite Dirichlet networks, material memory, forward/backward
path laws, and the missing arithmetic-to-physical identification. In particular,
it proves the exact rank-one Dirichlet-to-Neumann update and gives two important
controls:

- A response-invisible interior edge changes the result of a later common
  intervention: the effective conductances become $7/6$ and $49/41$.
- A declared field-dependent constitutive update gives a terminal order defect
  $474/401-13/11=1/4411$. Fixed additive conductance increments, in contrast,
  have the same terminal network in either order.

Those facts and their scopes are inherited. The present two-arm model below
has a different discriminator: different **path likelihoods** can lead to the
same terminal geometry. It does not replace the inherited constitutive-memory
example or claim that its terminal field retains every event order.

The implementation reuses the existing interfaces:

| Inherited object | Repository implementation |
|---|---|
| Labelled complete path laws, forward/backward messages, Doob conditioning | [bidirectional_source_histories.py](../../observational_succ/bidirectional_source_histories.py) |
| Harmonic fields and growing Dirichlet networks | [growing_dtn_history.py](../../observational_succ/growing_dtn_history.py) |
| Exact passive network response and inverse controls | [dynamic_boundary_inverse.py](../../observational_succ/dynamic_boundary_inverse.py) |
| Endpoint versus source-history faithfulness | [field_history_lift.py](../../observational_succ/field_history_lift.py) |
| Original four-pole forcing, rational characters, zero-selected history | [succ_internal_matrix_walk.py](../../observational_succ/succ_internal_matrix_walk.py) and [lambda_source_duality.py](../../observational_succ/lambda_source_duality.py) |

There is no new generic path-probability or electrical-network engine here.

| Result | Authority and scope |
|---|---|
| Doob conditioning preserves same-endpoint path odds | CLASSICAL; finite proof below; inherited native implementation |
| The three declared models predict $1/2$, $2/3$, and $3/5$ after one left event | PROVED FINITE MODEL |
| Geometry gives a $3/4$ same-endpoint likelihood ratio | PROVED FINITE MODEL; an obstruction to endpoint-only reweighting of the fair law |
| Pólya reinforcement equals a static Beta mixture on every finite word | CLASSICAL; complete finite-word derivation below |
| A preserved deterministic factor cannot acquire auxiliary one-step attenuation | PROVED PAPER; native BBP finite certificates |
| Approximate preservation costs at most $2\epsilon$, sharply | PROVED PAPER; exact sharpness controls |
| The field update or its probabilities are derived from the BBP source | OPEN; no such map is supplied |

## 2. One finite graph, three different laws

### The declared geometry and its stopping rule

Let $L\ge2$ be an integer. Two disjoint arms, each consisting of $L$
unit-resistance edges, share a source vertex. The source has potential zero;
each remote endpoint has potential one. A realized prefix on an arm is declared
perfectly conducting and held at the source potential. This is an exact boundary
condition in a mathematical model, not a measured constitutive law.

Write $(l,r)$ for the numbers of realized edges on the two arms and put

$$
a=L-l,\qquad b=L-r.
$$

A live state requires $0\le l,r<L$. The process stops when either realized
prefix reaches a remote endpoint. No further field solve or growth transition
is asserted at that completed connection.

On an arm with realized prefix $l$, the potential at its original vertex
$k\in\{0,\ldots,L\}$ is

$$
\phi_l(k)=\frac{\max(0,k-l)}{L-l}.
$$

It satisfies the prescribed boundary values and the discrete harmonic equation
$2\phi_l(k)=\phi_l(k-1)+\phi_l(k+1)$ at every remaining interior vertex.
Uniqueness of the Dirichlet solution therefore identifies it with the network
field. The current through the first unrealized edge is $1/(L-l)$.

Consequently the two frontier currents are

$$
I_L=1/a,\qquad I_R=1/b.
$$

The declared field-growth rule selects a frontier edge in proportion to its
current, so

$$
\boxed{p_{\rm field}(L\mid l,r)
=\frac{1/a}{1/a+1/b}=\frac{b}{a+b}.}
$$

After selection, the corresponding prefix grows by one edge and the field is
recomputed. Every probability is rational.

### The comparison laws

The first reference is a **known independent fair law**. Observing a past letter
does not change the next-letter probability:

$$
p_{\rm fixed}(L\mid l,r)=\frac12.
$$

The second reference is linear branch-count reinforcement, with positive initial
weights $\alpha,\beta$:

$$
p_{\rm reinforce}(L\mid l,r)
=\frac{\alpha+l}{\alpha+\beta+l+r}.
$$

The probability of any ordered word is the product of its successive declared
conditional probabilities. The fixed and reinforced laws exist at every word
length. The field law has the stopping rule above. A common fixed horizon
$H\le L$ permits comparison of all words of length $H$, since no earlier step
can have completed an arm. A completed connection at the last step is allowed.

For $L=3$ and $\alpha=\beta=1$, the three laws begin with probability $1/2$
of a left event. After the first left event they disagree:

| Declared mechanism | Next left probability after $L$ | $P(LL)$ | $P(LR)$ |
|---|---:|---:|---:|
| Known fair law, observation only | $1/2$ | $1/4$ | $1/4$ |
| Linear branch reinforcement | $2/3$ | $1/3$ | $1/6$ |
| Recomputed harmonic-current growth | $3/5$ | $3/10$ | $1/5$ |

The last row follows from the remaining resistances $2$ and $3$. The first row
is a specific known-law comparison; it does not say that all conditioning leaves
predictions unchanged. A terminal constraint or an unknown parameter can change
conditional predictions.

### Relation to the physical analogy

The original [Niemeyer–Pietronero–Wiesmann paper](https://doi.org/10.1103/PhysRevLett.52.1033)
introduced a stochastic dielectric-breakdown model. An accessible primary
mathematical definition is Losev–Smirnov,
[*How long are the arms in DBM?*, §1.1](https://arxiv.org/pdf/2307.14931):
the next attachment law depends on the harmonic measure of the current cluster,
raised to the model parameter. The changing cluster therefore changes the next
law. The two-arm construction isolates that kind of feedback at exponent one;
its finite electrodes and stopped series arms are a separately declared model.

No claim about a physical material's parameters, a discharge experiment, or an
arithmetic field follows from this comparison. The field equation and the
material update must each be supplied and checked in the system being studied.

## 3. What endpoint conditioning can change

**Theorem 1 — same-endpoint odds invariant.** Fix a finite Markov path law $P$
with a fixed initial state $x_0$. Let $g\ge0$ be a terminal-state weight with
$h_0(x_0)>0$, where

$$
h_t(x)=\mathbb E_P[g(X_T)\mid X_t=x].
$$

On states with positive $h_t$, the Doob transition is

$$
P_t^h(x,y)=P_t(x,y)\frac{h_{t+1}(y)}{h_t(x)}.
$$

For every path of positive $P$ probability,

$$
\boxed{\frac{P^h(\omega)}{P(\omega)}
=\frac{g(X_T(\omega))}{h_0(x_0)}.}
$$

In particular, two paths with the same terminal state and positive reweighting
have unchanged odds.

**Proof.** The backward relation $h_t=P_th_{t+1}$ makes each transformed row
stochastic on its support. Multiplication along a path cancels every intermediate
$h_t$ factor, leaving the displayed endpoint ratio. If the terminal weight is
zero, the transformed path mass is zero. For two paths with the same terminal
state and positive weight, the surviving factor is identical. $\square$

For an event indicator $g=1_A$, this is ordinary conditioning on $X_T\in A$.
The finite implementation is inherited. For the classical transform, see
[Doob (1957), §2](https://www.numdam.org/item/10.24033/bsmf.1494.pdf).

The endpoint hypothesis is essential. Reweighting by an arbitrary function of
the entire path can represent any absolutely continuous path law. That broader
operation does not provide an endpoint-only explanation.

### An arbitrary normalized potential carries an additional path factor

A positive potential used to bias transitions need not satisfy the Doob backward
equation. For arbitrary strictly positive functions $v_0,\ldots,v_T$, define

$$
Q_t(x,y)=\frac{P_t(x,y)v_{t+1}(y)}{(P_tv_{t+1})(x)}.
$$

Every row is stochastic, but direct multiplication gives

$$
\boxed{\frac{Q(\omega)}{P(\omega)}
=\frac{v_T(X_T)}{v_0(x_0)}
\prod_{t=0}^{T-1}\frac{v_t(X_t)}{(P_tv_{t+1})(X_t)}.}
$$

The extra product is generally path dependent. It disappears when
$v_t=P_tv_{t+1}$; a path-independent factor can also be absorbed into the final
normalization. Thus a normalized potential can change same-endpoint odds,
but its intermediate normalization factors are part of the law that must be
retained. Identifying a general normalized potential with terminal conditioning
requires checking that this product does not vary within an endpoint fibre.

## 4. The geometry law has a nontrivial same-terminal ratio

**Theorem 2 — finite path discriminator.** In the three-edge model,

$$
P_{\rm field}(LLR)=\frac12\frac35\frac14=\frac3{40},
\qquad
P_{\rm field}(LRL)=\frac12\frac25\frac12=\frac1{10}.
$$

Both histories finish at $(l,r)=(2,1)$, with the same realized prefixes and the
same terminal field. Their likelihood ratio is

$$
\boxed{\frac{P_{\rm field}(LLR)}{P_{\rm field}(LRL)}=\frac34.}
$$

The fair law assigns each word probability $1/8$. The reinforced law with
initial weights $(1,1)$ assigns each probability $1/12$. By Theorem 1, the
geometry law cannot be obtained from the fair law merely by reweighting its
terminal count or terminal geometry. $\square$

Conditioning the field law itself on $(2,1)$ preserves the discrepancy.
The event probability is $11/40$, and the conditional probabilities of
$LLR,LRL,RLL$ are respectively

$$
\frac3{11},\qquad\frac4{11},\qquad\frac4{11}.
$$

These values are recovered by both time orientations of the existing labelled
path-law engine.

### The general adjacent-swap defect

For any live state with remaining lengths $a,b\ge2$, both orders of one left
and one right event are admissible. Their probabilities are

$$
P(LR\mid a,b)=\frac{b(a-1)}{(a+b)(a+b-1)},\qquad
P(RL\mid a,b)=\frac{a(b-1)}{(a+b)(a+b-1)}.
$$

Subtracting and dividing prove the exact formulas

$$
\boxed{P(LR\mid a,b)-P(RL\mid a,b)
=\frac{a-b}{(a+b)(a+b-1)},}
$$

$$
\boxed{\frac{P(LR\mid a,b)}{P(RL\mid a,b)}
=\frac{b(a-1)}{a(b-1)}.}
$$

After a first left event in the three-edge example, $a=2,b=3$, giving $3/4$.
This is a concrete probability observable on equal-endpoint routes, compatible
with the [Seinfeld distinction between endpoint coherence and labelled history](../2026-10-25/SEINFELD_SUCC_NOTHING_THEOREMS.md).

### An exact multiplicative potential becomes an additive log history

The field law also has a finite normalized-potential representation. Let $K$
be the fair next-letter kernel on live count states and set

$$
H(l,r)=(L-l)!\,(L-r)!=a!\,b!.
$$

Then $H(l+1,r)=H(l,r)/a$ and $H(l,r+1)=H(l,r)/b$. Consequently

$$
D(l,r):=\frac{(KH)(l,r)}{H(l,r)}
=\frac12\left(\frac1a+\frac1b\right),
$$

and normalized weighting by $H$ gives exactly

$$
\frac{K((l,r),(l+1,r))H(l+1,r)}{(KH)(l,r)}
=\frac{b}{a+b}=p_{\rm field}(L\mid l,r).
$$

For an admissible finite word with count states $s_0,\ldots,s_T$,
the normalized-potential identity therefore becomes

$$
\frac{P_{\rm field}(\omega)}{P_{\rm fixed}(\omega)}
=\frac{H(s_T)}{H(s_0)}\prod_{t=0}^{T-1}D(s_t)^{-1},
$$

$$
\boxed{\log\frac{P_{\rm field}(\omega)}{P_{\rm fixed}(\omega)}
=\log H(s_T)-\log H(s_0)-\sum_{t=0}^{T-1}\log D(s_t).}
$$

This supplies a concrete multiplicative-to-logarithmic normalization: the
endpoint potential and the accumulated normalizers are separate terms.
$H$ is generally not harmonic, so the accumulated term survives. For $LLR$
and $LRL$, the common endpoint and first two normalizers cancel in the ratio;
the remaining normalizers are $2/3$ and $1/2$, yielding $(1/2)/(2/3)=3/4$.
The factorials are a finite potential for this graph. They establish no
Euler–Mascheroni constant identity or source-authenticated BBP potential.

**What the field remembers.** In this toy, $(l,r)$ is sufficient for the next
transition. Equal terminal counts give equal future laws even when the past
path likelihoods differ. The current field therefore does not retain the full
order. A claim of terminal order memory requires an additional constitutive
state or update, such as the separately declared inherited HISTORY-DTN example.

## 5. Reinforcement and a static unknown field can be observationally identical

**Theorem 3 — complete finite-word equivalence.** Let $\alpha,\beta>0$.
For every ordered word $\omega$ containing $l$ left and $r$ right letters,
linear reinforcement has probability

$$
P_{\rm reinforce}(\omega)
=\frac{(\alpha)_l(\beta)_r}{(\alpha+\beta)_{l+r}},
$$

where $(x)_m=x(x+1)\cdots(x+m-1)$ and $(x)_0=1$. The same probability is
obtained by drawing one time-independent bias
$\Theta\sim\operatorname{Beta}(\alpha,\beta)$ and then drawing letters
independently conditional on $\Theta$.

**Proof.** In the reinforced process, the left numerator factors visit
$\alpha,\ldots,\alpha+l-1$ and the right factors visit
$\beta,\ldots,\beta+r-1$. The denominator factors visit the successive total
weights. Their product is the displayed expression, independently of the order.
For the static-bias model,

$$
\begin{aligned}
P_{\rm static}(\omega)
&=\int_0^1\theta^l(1-\theta)^r
\frac{\theta^{\alpha-1}(1-\theta)^{\beta-1}}
{B(\alpha,\beta)}\,d\theta\\
&=\frac{B(\alpha+l,\beta+r)}{B(\alpha,\beta)}
=\frac{(\alpha)_l(\beta)_r}{(\alpha+\beta)_{l+r}}.
\end{aligned}
$$

The beta-integral recurrence proves the last equality. This holds for every
finite ordered word, so all finite observational laws agree. $\square$

The paper identity holds for positive real parameters. The exact implementation
accepts integer or rational parameters and rejects floating-point replacements.

The posterior predictive probability in the static model is also
$(\alpha+l)/(\alpha+\beta+l+r)$. A changing prediction curve therefore does
not identify physical reinforcement. The ambiguity is classical; finite
edge-reinforced walks have a broader mixture-of-Markov-laws representation,
as stated in [Tournier (2009)](https://arxiv.org/html/0911.5255v1).

### What an intervention must specify

Observational equivalence does not identify counterfactual interventions.
Within these two declared models, suppose a left event has been recorded:

- Reset the reinforced model's physical weights to $(1,1)$ while retaining the
  observer's record. Its next left probability becomes $1/2$.
- Leave the static latent bias unchanged and retain the same record. Its
  posterior predictive probability remains $2/3$.

These are different declared interventions on different model variables. A
real identification would require evidence about which physical variable was
changed. Erasing an observation record, resetting a weight, and restoring a graph
boundary are not interchangeable operations. The comparison is a mathematical
intervention test, not an experimental construction protocol.

The geometry law's $3/4$ ratio also separates it from this count-exchangeable
Beta family. It does not rule out every possible static latent-variable model;
unrestricted latent descriptions can encode much more than one fixed branch bias.

## 6. A stochastic extension must preserve its arithmetic factor

**Theorem 4 — deterministic-factor identity.** Let $Y_t$ be an enlarged finite
state, including any retained history or field variables, and let $K_t$ be its
conditional transition kernel. Let $\pi_t(Y_t)=X_t$ be an arithmetic projection.
Suppose that, for every current state under consideration,

$$
\pi_{t+1}(Y_{t+1})=T_t(\pi_t(Y_t))
\quad\text{almost surely conditional on }Y_t.
$$

Then every observable $f$ on the projected successor satisfies

$$
\boxed{K_t(f\circ\pi_{t+1})(y)
=f(T_t(\pi_t(y))).}
$$

**Proof.** In

$$
\sum_{y'}K_t(y,y')f(\pi_{t+1}(y')),
$$

every positive-weight term has the same projected argument
$T_t(\pi_t(y))$. The row weights sum to one. $\square$

No independence, reversibility, or stationary field is required. If the proposed
dynamics depend on history, that history can be included in $Y_t$; the theorem
is conditional on the resulting current state.

For the unchanged arithmetic source,

$$
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},
\qquad U_0=0,\qquad U_{n+1}=16U_n+r(n+1),
$$

an auxiliary extension preserving this unwrapped successor has, for every
integer frequency $h$,

$$
\boxed{\mathbb E_{\rm aux}
[e(h\pi_{n+1}(Y_{n+1}))\mid Y_n]
=e(h[16U_n+r(n+1)]),\qquad e(t)=\exp(2\pi it).}
$$

Its conditional modulus is one. A field-only observable may average to zero
in the same row; that does not attenuate the character of the preserved
arithmetic successor.

**This is a conditional one-step statement.** It does not prohibit cancellation
across arithmetic times. A deterministic two-cycle with successive observable
values $+1,-1$ has unit conditional values and zero mean over every even horizon.
The selected BBP time-average problem remains open.

### The sharp approximate bound

Let $\epsilon$ be the conditional probability that the projected successor
differs from the prescribed value $Tx$. For every $|f|\le1$,

$$
\boxed{\left|\mathbb E f(\pi(Y'))-f(Tx)\right|\le2\epsilon.}
$$

The contribution of the correct outcomes vanishes in the difference; each
incorrect outcome contributes at most two. For a unit character this implies

$$
\boxed{\left|\mathbb E e(h\pi(Y'))\right|
\ge\max(0,1-2\epsilon).}
$$

Complete conditional cancellation consequently requires $\epsilon\ge1/2$.
The constants are sharp. With prescribed unwrapped successor zero and frequency
one, for $0\le\epsilon\le1/2$ place masses $1-\epsilon,\epsilon$ at
$0,1/2$; the mean is $1-2\epsilon$. For $1/2\le\epsilon\le1$, place masses
$1-\epsilon,1/2,\epsilon-1/2$ at $0,1/2,1$. The erroneous unwrapped-state
mass is $\epsilon$, and the character mean is zero. The last construction
explicitly uses different unwrapped states with the same character phase.

This measures an existing source substitution. A uniform law on sixteen distinct
real-circle inverse branches gives the selected predecessor mass $1/16$.
As a proposed row preserving that selected predecessor, its leakage is $15/16$.
Its root-of-unity cancellation is therefore a property of a different conditional
arithmetic law. A source-derived transport identity must account for this change;
the existence of the inverse ensemble does not supply that identity.

## 7. Reproduction and certification boundary

The new finite model and factor certificates are implemented in
[path_field_feedback.py](../../observational_succ/path_field_feedback.py), with
[focused tests](../../tests/test_path_field_feedback.py). The round's
[reproduction probe](../../scripts/seinfeld_realization_probe.py) integrates the
results with the source-labelled disintegration and selection-likelihood work.

The verification has independent checks rather than only matching two versions
of a recurrence:

- `source_path_law`, `dual_labelled_messages`, and
  `conditioned_bidirectional_path_law` evaluate the declared count graph with
  native retained labels and both time orientations.
- The arm potentials satisfy the discrete Dirichlet equations and are separately
  recomputed by `ConductiveState.potential`.
- The Pólya identity is checked by expanding integer-parameter Beta densities
  and exactly integrating the resulting polynomials.
- The BBP wrapper calls the native full-prefix authenticator. Holdouts at source
  indices $1,2,7,16,32,64$ and frequencies $1,8,17$ retain the zero anchor,
  original four signs, and unwrapped successor.
- Changed seeds, a changed source entry, altered projected successors, positive
  leakage, impossible conditioning, and continuation after breakthrough are
  retained rejection controls. Exact cyclotomic examples calibrate sharpness of
  the leakage bound; the two-cycle prevents a false inference about time averages.

The auxiliary transition rows in the BBP checks are declared inputs; passing
their factor test does not authenticate a stochastic feedback mechanism.
Source indices in that wrapper are the literal $r(n)$ indices, so index one is
$U_0\to U_1$.
The exhaustive count-graph factory additionally limits its horizon to twelve;
the paper formulas apply to arbitrary finite arm lengths with the stated
stopping restrictions.

The focused command is

```sh
python -m unittest discover -s tests -p 'test_path_field_feedback.py' -v
```

It completed locally with **19 passing tests**. This is finite computational
authority alongside the paper derivations. Full-suite results, exact-head
publication status, and the combined round receipt belong to the synthesis and
validation record; no full-suite count or infinite formalization is claimed here.

## 8. The remaining source-to-field obligation

The constructive part of the proposal survives: retain labelled histories,
specify a field state, state its update, and recompute the next law. The finite
comparison makes the resulting distinctions measurable. The surviving gap is
an explicit authenticated bridge to the original arithmetic process.

A candidate bridge must supply the field variables, their update, the selected
arithmetic projection, and the observable transport. Exact projection invokes
Theorem 4; approximate projection incurs the stated leakage cost. To advance the
arithmetic frontier, the remaining step must control a signed cross-time or
selected-path quantity using the full four-pole source and zero selector.

A changing predictive probability is consistent with both material modification
and learning about a static latent bias. Equal endpoints do not identify path
likelihoods. Auxiliary one-step mixing does not become selected time-average
cancellation without the intervening theorem. These are exact constraints on the
next construction, not a dismissal of the author's realized-path intuition.
