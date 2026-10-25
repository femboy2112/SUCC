# Source paths, infinite observers, and the exact pi-normality obligation

**Date:** 2026-10-24.
**Working branch:** research/pi-path-selection-interference-2026-10-24.
**Current parent:** draft #272 at 6e8fa8b77886b13f1f533ed8083fd88c849d14b3.
**Initial research/test parent:** 8f2e6f852efafb4a0c871418c97ed819b1217d7d.
The intervening parent update changes nine proof/navigation/receipt files and
no Python source or tests. The [update record](PI_PATH_PARENT_UPDATE.json)
preserves this distinction. Main remains e648df3e4fca73ab6b942232b5ca4b310e9cac08.

## 1. Outcome

The proposed mechanism now has an exact mathematical realization: sum
source-derived phases over finite histories, cancel every incompatible
history, and retain the history with the authenticated origin. We proved
the projector, its boundary dependence, its source/carry transport and its
finite marginals, and built exact instruments with independent controls.

The central clarification is equally concrete: **the source has already
been identified.** The fixed BBP recurrence and initial zero select its
entire rational history; nested rational tail enclosures select pi/16.
What remains unproved is a frequency estimate along that selected history.
“Source-specific selection remains essential” should not obscure this
difference between identifying a source and bounding its statistics.

This round obtains a uniform theorem for the order of selection and
occupation limits, an exact infinite-amplitude obstruction, and a
quantitative preservation bridge for observer-history averages. It does
not prove either remaining source estimate or pi normality.

The main results are [SPS-01--25](../../docs/CLAIM_SUPPLEMENT_SOURCE_PATH_SELECTION.md).
Proof dossiers:

- [Exact interference and the authenticated carrier](PI_PATH_PROJECTOR.md).
- [Selection depth, occupation limits and infinite signed extension](PI_PATH_SELECTION_LIMITS.md).
- [Quantitative history preservation and the full conditional closure](PI_HISTORY_PRESERVATION.md).
- [Positive histories, entropy and operator obstructions](PI_HISTORY_OPERATOR_BOUNDARY.md).
- [All-time local-clock agreement and compensating correlations](PI_FINITE_PRIME_CORRELATION.md).
- [Validation and authority](PI_PATH_SELECTION_VALIDATION.md).

## 2. Live updates inspected

| Draft | Pinned head | Earned advance | Remaining statistical obligation |
|---|---|---|---|
| [268](https://github.com/femboy2112/SUCC/pull/268) | 06f6b03eed2521c6bd5c02db618cb421ac6b5a51 | Signed twisted-pair transport; exact but unstable odd-source identification; coprime-gain coercivity; inverse-branch first-saving contract | Agreement alone does not bound temporal signed correlations |
| [269](https://github.com/femboy2112/SUCC/pull/269) | b445b0d9c604f45548a45b5db4f31428f73b35a2 | Four-gate tomography, signed cyclotomic shells and prime-base transfer | Residue/ensemble identities do not give selected real carry frequencies |
| [270](https://github.com/femboy2112/SUCC/pull/270) | 3acd547ff122368d5694efdab029b3156a292d8a | Authentic 2-adic isometry and one-sixteenth residue refinement; exact inverse-cover carries; positive-dimension plus second-symmetry closure | Real all-scale collision saving and same-law tripling |
| [271](https://github.com/femboy2112/SUCC/pull/271) | 4eafc6151e9a494f2aea8ec79ca6cf5608152c80 | Full four-bit Walsh contrast and source-corrected Fourier/Taylor jet | The selected jet itself remains unbounded; small remainder is not small main term |
| [272](https://github.com/femboy2112/SUCC/pull/272) | 6e8fa8b77886b13f1f533ed8083fd88c849d14b3 | Full authentic Pascal valuation profile, optimal Mahler degree, positive kernels, carry-aware all-base filters, minimal recurrences, source-prime heights; late prescribed-constant and forcing-phase addenda | Exact source arithmetic still needs a real-frequency estimate |

This branch inherits #272 and its #270/#268 ancestors. The #269/#271
sibling path was read at the stated heads, not merged. Draft status,
paper authority, exact finite checks and formal-kernel authority remain
separate.

### The newest negative control is stronger than rational clustering

The late [prescribed-constant addendum](PI_PASCAL_PRESCRIBED_CONSTANT.md)
constructs a changed forcing with any prescribed positive real constant.
It retains rational source and forcing values at integer times, the full
dyadic profile, arbitrary fixed relative dyadic precision, positivity,
complete monotonicity and quadratic decay. It can also match source values
at every integer time to any fixed precision at any fixed finite set of primes.

Choose the transcendental constant \(\sum_{j\ge2}16^{-j!}\). Its orbit
has limiting circle law \(\delta_0\), and almost all pairs remain in the
central carry branch at the relevant polynomial radii. Thus adding
transcendence or finitely many prime congruences does not make those generic
properties sufficient for half retention.

The changed forcing is not the exact BBP four-pole rational function.
Its real density corrections and tail moments may be irrational even
though its integer source/forcing values are rational. It does not supply
full odd-prime analytic interpolation or equality at every prime. Those
scope distinctions are essential: this is a theorem about the insufficiency
of a proposed hypothesis class, not a counterexample to normality of pi.

### A direct answer about correlations of the unshared information

The new [SPS-25 corollary](PI_FINITE_PRIME_CORRELATION.md) extracts a
stronger observer consequence of that parent theorem. Let \(\pi_p\) be
the primary projection of the rational torsion group \(\mathbb Q/\mathbb Z\)
onto its \(p\)-power torsion. For rational lifts \(x,z\),

$$
\pi_p([x])=\pi_p([z])
\quad\Longleftrightarrow\quad x-z\in\mathbb Z_{(p)}.
$$

The parent's finite-prime congruences therefore preserve the **entire
primary source and forcing phases at every time**, not only a finite
prefix. Fix any finite prime set \(S\), use the constructed clustering
source \(H_n\), and define

$$
u_n=\sum_{p\in S}\pi_p([U_n]),\qquad v_n=[H_n]-u_n.
$$

The observed clocks are exactly the authentic clocks, and \(v_n\) has no
primary component in \(S\). Nevertheless, for every fixed integer \(h\),

$$
\frac1N\sum_{n<N}e(hu_n)e(hv_n)\to1,\qquad
\frac1N\sum_{n<N}|e(hv_n)-e(-hu_n)|^2\to0.
$$

Here \(e(t)=\exp(2\pi it)\). The identities follow from the full constructed
orbit's limiting law \(\delta_0\). Thus disjoint information can have
asymptotically perfect compensating phase correlation while every declared
finite local observer agrees forever.

This does not assign that behavior to the authentic BBP complement.
It shows exactly which inference needs the full source formula. Agreement
for every prime at a fixed time would identify the complete rational circle
phase; it still would not supply a time-frequency estimate. The quantifier
here is “for each fixed finite observer family, there exists a changed
source,” not one changed source invisible to all primes simultaneously.

### What the carry jet has already paid

The latest source-preserving phase removal retains the exact selected pair
mask and removes only the small forcing difference from the fifteen-mode
phase, at total error less than \(1485/28\). At the terminal radius
\(\tau\asymp p^{-2/5}\), its quadratic Taylor remainder is \(o(p)\).
This is real deterministic progress on an error budget.

The selected conditional Fourier sum is still the main term. The near-return
mask supplies additional Fourier frequencies, so fifteen outer characters
do not mean bounded total bandwidth. Removing forcing from that
discontinuous mask would itself require a new boundary-count theorem.

## 3. The source is already pinned down

Keep exactly

$$
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},
\qquad U_0=0,\quad U_n=16U_{n-1}+r(n),\quad y_n=\{U_n\}.
$$

The BBP identity and positive tail give, with \(\alpha=\pi/16\),

$$
16^K\alpha=U_K+T_K,\qquad
0<T_K<\frac1{(8K+1)(8K+2)}.
$$

The rational intervals

$$
I_K=\left[16^{-K}U_K,\
16^{-K}\left(U_K+\frac1{(8K+1)(8K+2)}\right)\right]
$$

are strictly nested and have intersection \(\{\alpha\}\). No new axiom
of geometry is needed for this selection; ordinary completeness and the
proved source identity suffice.

The earlier two-observer language must retain these types. A zero
differential can certify agreement after specified observer transport.
It does not remove a complementary source term before that transport has
been authenticated, and it does not determine correlations between different
times. The new projector makes the same boundary visible: inserting a finite
observable leaves the initial selector's Fourier transform explicitly.

The authentic rational denominator carriers also correct a potential
path-space error. Refining denominator \(D\) to \(D'\) preserves the point
by \(x\mapsto(D'/D)x\), not by residue reduction. The integer carry lift
must be retained separately from circle phases.

## 4. The precise success of the interference idea

For a cyclic carrier, candidate history \(x_0,\ldots,x_N\), initial source
\(s\), and recurrence defects \(d_0=x_0-s\),
\(d_j=x_j-bx_{j-1}-a_j\), the exact sum

$$
\Pi_s(x)=q^{-(N+1)}
\sum_{\lambda_0,\ldots,\lambda_N\bmod q}
\exp\!\left(\frac{2\pi i}{q}\sum_j\lambda_jd_j(x)\right)
$$

is one on the unique source history and zero on every other history.
This realizes cancellation using source constraints. Summing terminal
coordinates gives coherent finite marginals.

For observable frequencies \(h_j\), backward dual propagation gives

$$
\sum_x\mu_\sigma(x)e_q\!\left(\sum_jh_jx_j\right)
=e_q(C)\widehat\sigma\!\left(\sum_jb^jh_j\right).
$$

The delta-selected endpoint has modulus one; the corresponding uniform
ensemble can have zero character average. This is the exact remaining
boundary term, rather than an interpretive objection to interference.

There is also a genuine infinite-limit distinction. Raw joint amplitudes
have total mass one and variation \(q^{N+1}\). They do not extend to an
ordinary finite complex measure on infinite joint histories. Summing the
dual variables first gives positive Dirac prefix laws that do extend to
the selected infinite path. Other oscillatory or operator formulations
need their own convergence theorem; this result does not prohibit them.

## 5. The selection-depth theorem

Let \(\nu_{x,K}\) be the uniform law on the depth-\(K\) base-\(b\) cylinder
containing \(x\), and average its first \(N\) iterates. For \(m=\min(K,N)\),

$$
W_1\!\left(
\frac1N\sum_{n<N}(T_b^n)_*\nu_{x,K},
\frac mN\rho_m(x)+\left(1-\frac mN\right)\lambda
\right)
\le\frac{b^m-1}{2N(b-1)b^K}.
$$

This holds for every source, including a constant source, and for every
fixed affine forcing. The first \(K\) iterates retain the selected prefix;
after that, the cylinder uncertainty becomes exactly Haar.

For the genuine BBP intervals \(I_K\), put

$$
H_K=K+\left\lceil\log_{16}((8K+1)(8K+2))\right\rceil,
\qquad m=\min(H_K,N).
$$

The same selected-prefix/Haar mixture has a uniform error

$$
\boxed{\quad W_1(\text{averaged enclosure},\text{mixture})\le\frac2{3N}.\quad}
$$

Thus sublinear selection depth makes the ensemble Haar regardless of the
unknown source law. At depth comparable to the observation horizon, the
actual selected law remains in the answer with positive weight. This gives
a concrete uniformity requirement for any proposed infinite-observer proof.

## 6. The exact theorem still needed for normality

For the true source window \(\mu_p\), there are two useful targets.

**First, real anti-concentration.** Obtain a fixed positive exponent in
\(Q_\mu(\rho)\le C\rho^s\) for every weak limit and all sufficiently small
fixed radii. The inherited central-carry retention bound with factor
\(\theta<1\) at all prescribed scales, or on a prefix-uniform positive
proportion of scales, is one sufficient arithmetic formulation.
At \(\theta=1/2\), it yields \(s=1/4\). A terminal-scale estimate is not
enough for this route.

**Second, preservation of this same law under another independent gain.**
One may try to prove asymptotic tripling invariance directly, or use

$$
A_J\mu=\frac1J\sum_{j<J}(T_3^j)_*\mu,\quad
\epsilon=W_1(A_J\mu,\mu),\quad
\beta=W_1((T_3)_*\mu,\mu).
$$

The new finite theorem is

$$
\boxed{\quad
\beta\le4\epsilon+\frac{W_1((T_3^J)_*\mu,\mu)}J
\le4\epsilon+\frac1{2J}.
\quad}
$$

An independently proved \(\epsilon_p\to0\) with \(J_p\to\infty\) pays
the symmetry obligation. Existence of some sufficiently slow such schedule
is equivalent to \(\beta_p\to0\), so that existential formulation alone
does not weaken the missing theorem.

With both real premises, classical Rudolph--Johnson rigidity forces every
limit to be Haar. The inherited tail and good-prime coverage then give
every prefix frequency, hence base-16 and binary normality.
The [full proof](PI_HISTORY_PRESERVATION.md) includes the fixed-scale
Portmanteau step, the nonergodic residual, the actual source indices and the
window-to-prefix interpolation. All sufficiently large good primes are
required; an arbitrary sparse subsequence is insufficient.

### Why more observers alone do not provide preservation

Host's classical theorem shows that positive-entropy radix laws can become
Haar after tripling-history averaging even when the original law is singular.
The fair base-16 digits-0/1 law is a concrete example. The averaging can
produce the desired ensemble while changing the law being investigated.

Positive fixed history mixtures also have an exact operator classification:
stationarity is invariance under \(3^d\), where \(d\) is the gcd of supported
positive history lengths. For \(d=1\), this is tripling. For \(d>1\), it is
weaker but still adequate for the independent-gain rigidity route.
Signed mixtures can fake stationarity even with a positive output measure.

Nor can unique source be upgraded to compact unique ergodicity of a full
circle extension: its distinct fixed-point fibers already support distinct
invariant measures. A selected normal orbit would be generic for one law
inside a system that has others.

## 7. Exact measurements and what they establish

The [transport receipt](PI_HISTORY_TRANSPORT_RECEIPT.json) retains all nine
preregistered combinations. The compact table below uses lower endpoints
of exact decimal enclosures of width \(10^{-8}\).

| p | Source samples | beta | epsilon at J2 | epsilon at J4 | epsilon at J8 |
|---:|---:|---:|---:|---:|---:|
| 137 | 51 | 0.08481398 | 0.04240699 | 0.04442570 | 0.04464150 |
| 281 | 105 | 0.01999126 | 0.00999563 | 0.01146029 | 0.00903975 |
| 521 | 195 | 0.02471385 | 0.01235692 | 0.01482365 | 0.01199697 |

At \(J=2\), \(\epsilon=\beta/2\) exactly. The defects are not monotone.
These finite observations do not establish or refute asymptotic preservation.
The exact optimal circle transport has matching primal and periodic
Lipschitz dual witnesses, checked against independently enumerated assignments.
All 351 source states are independently authenticated by the original
four-pole formula; no pi digits are supplied to the constructor.

Other receipts include 90,280 small candidate histories plus a separate
14,641-case holdout; 240 cylinder combinations; 65 independent Machin
containment checks; and post-discovery raw-amplitude and fast-history
controls. Distinct enumeration counts are not conflated.

## 8. Which axioms or known theorems would settle it?

No foundational independence result has been proved, and no new set-theoretic
axiom is presently indicated. Source identification already uses familiar
finite algebra, completeness and the BBP identity. Infinite positive laws,
finite complex-measure extension and entropy rigidity have standard
mathematical frameworks. The outstanding work is an arithmetic theorem
about this source.

A named broad conjectural principle is Bailey--Crandall's Hypothesis A:
certain rational-function-forced radix recurrences starting at zero have
only the rational/finite-attractor alternative or an equidistributed orbit.
Their paper explicitly derives binary normality of pi under that hypothesis.
Assuming it would import the unresolved statistical content; it is not a
new proof obtained from source uniqueness.

Lagarias explains why the general vanishing-forcing shadow mechanism alone
cannot suffice: it applies to representations of every real number,
including nonnormal ones. The fixed rational arithmetic must contribute
something beyond that mechanism.

Primary sources used:

- Bailey and Crandall, [On the Random Character of Fundamental Constant Expansions](https://www.davidhbailey.com/dhbpapers/bcrandom.pdf), Hypothesis A and Theorem 1.1.
- Lagarias, [On the Normality of Arithmetical Constants](https://arxiv.org/pdf/math/0101055), introduction and source/orbit transport.
- Hochman, [A short proof of Host's equidistribution theorem](https://arxiv.org/html/2103.08938v2), Theorem 1.1.
- Bourgain--Lindenstrauss--Michel--Venkatesh, [Some effective results for times a times b](https://math.stanford.edu/~akshay/research/blmv.pdf), Theorem 1.3.
- Delon--Rabin--Gousseau, [Transportation Distances on the Circle and Applications](https://arxiv.org/pdf/0906.5499), equation (10).

## 9. Next proof target and dominance boundary

The lowest useful new result would be a nontrivial selected real carry saving
on a prefix-uniform positive density of scales, while keeping the literal
four-pole source and its exact pair mask. That would pay real collision
dimension. An independent source-law preservation estimate would then
activate the weaker two-gain route.

Alternatively, a sufficiently strong selected collision/Fourier estimate can
close the inherited one-base route directly. The projector is useful only
if it supplies such an estimate after normalization and with the authentic
selector retained.

Stop claiming progress toward that estimate when a derivation merely
changes the averaging law, discards the selector, exchanges unproved
limits, removes the discontinuous mask, or repeats an equivalent condition.
The present round closes finite construction and limit-control questions.
The actual arithmetic cancellation remains the next theorem.
