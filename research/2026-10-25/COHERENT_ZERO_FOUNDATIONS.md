# Coherent zero relations: a source-typed foundation for balanced proofs

**SUCC research, 2026-10-25.** Baseline: Coherent Main X at 1e3a453e869992961bc2d7f3bb6f2f1ddab38854. This is a new-to-SUCC proof interface integrating classical polynomial ideal certificates and finite dynamical cohomology. No independent scholarly priority is asserted. Existing π Gearbox, source-faithful boundary, and original Weil provenance are unchanged. Draft VPB #289 is a separate positive-resolvent branch; this work does not assume it has been merged. **π normality and RH remain OPEN.**

## 1. Strongest faithful statement of the zero idea

The author's proposal is to start with 0=0 and simultaneously compose every valid zero relation, expressed in complementary mathematical bases. A rigorous realization is a **shared source of equations with transported certificates**, not an untyped assertion that every symbolic expression evaluating to zero can be freely substituted into every domain.

In a declared source model S, let A_i be a chart algebra and let ε_i be its intended semantic evaluation. Its zero relations form ker(ε_i) (an ideal when the evaluation is a ring homomorphism). To move a zero across charts, one needs a declared map whose semantic evaluation square actually commutes. One should retain *how* the expression becomes zero, not merely its final value 0. A string naming the source is a label, not a verified mathematical map or physical measurement.

Reflexivity 0=0 alone cannot distinguish the actual BBP source from a counterfeit or prove π normality. The latter is a quantitative statement about one authentic infinite orbit. Proof from multiple representations needs both **exact algebraic coherence** and **an independently proved asymptotic boundary bound**.

## 2. A complete cross-basis polynomial example from authentic BBP

The original source's four signed poles give the polynomial

\[
A(t)=4-2t^3-t^4-t^5.
\]

A different basis expresses the same kernel using

\[
B(t)=(t^2+2)(t^2+2t+2),\qquad A(t)=(1-t)B(t).
\]

Introduce formal chart variables P and Q; let the authenticated signed chart assert \(r_1=P-A(t)=0\) and the factored chart assert \(r_2=Q-B(t)=0\). The **proof certificate** is

\[
\boxed{P-(1-t)Q=r_1-(1-t)r_2.}
\]

It is a fully checkable polynomial ideal-membership witness after the two chart expressions have been mapped into one ambient ring \(\mathbb Q[t,P,Q]\). Both zeros contribute; they become structurally useful when the signed source and its positive factor chart are jointly constrained.

A separate ordered-real proof shows \(t^2+2>0\), \((t+1)^2+1>0\), and \(1-t\ge0\) on \([0,1]\). Therefore the BBP polynomial is strictly positive on \([0,1)\) and vanishes exactly at \(t=1\). **Ideal membership itself does not prove positivity**; the ordered-domain assumptions and factor proof are essential. This construction is an exact re-expression of the Main X authentic four-pole law, not a new theorem of digit normality.

The source-mutant \(4-2t^3-t^4-2t^5\) **fails** the old certificate, and the prototype rejects the claim. A false mixture of source labels is likewise rejected unless a legitimate common-source map is supplied.

**Consistency obstruction:** asserting both \(x=0\) and \(x-1=0\) over a nontrivial field yields the explicit unit certificate \(1=x-(x-1)\). This does not discover that every target is true; it demonstrates that the combined assumptions cannot have a common model. Thus, while all **valid** zeros coexist, incompatible purported zero relations cannot be accepted simultaneously.

## 3. The zero idea becomes finite dynamical cohomology

Let X be finite, let \(T:X\to X\) be a total deterministic map, and let \(f:X\to\mathbb Q\) be a source-labelled observable. Consider the coboundary equation

\[
\boxed{f=g-g\circ T.}
\]

**Theorem (finite coboundary criterion).** Such a g exists if and only if \(\sum_{x\in C}f(x)=0\) for every directed cycle C of T.

*Necessity:* summing the equation around any periodic orbit telescopes to zero. *Sufficiency:* choose a gauge value of g at a cycle root, solve successively around every cycle (the zero sum ensures closure), and then solve backwards along its trees. This is an exact finite-dimensional proof, not a heuristic or an infinite dynamical theorem.

The executable solver emits either a rational potential g, checked at every state, or an explicit nonzero cycle sum as an obstruction.

### An exact sharp optimal-error theorem

Allow an unresolved correction \(r\):

\[
f=g-g\circ T+r.
\]

For every cycle C, the coboundary sums to zero. Hence

\[
\|r\|_\infty\ge\max_C\left|\frac1{|C|}\sum_{x\in C}f(x)\right|.
\]

**This lower bound is sharp.** Put r equal to the cycle mean on each cycle, put r=0 on all noncycle vertices, and apply the exact coboundary criterion to f-r. Thus

\[
\boxed{
\inf_g\|f-(g-g\circ T)\|_\infty
=\max_C\left|\frac1{|C|}\sum_{x\in C}f(x)\right|.
}
\]

The source code constructs the minimizer and checks the lower/upper equality exactly in Fractions. A finite graph can be zoomed out to a potential plus a minimal residual whose **cycle means cannot be removed by a change of basis**. This is a concrete model of the user's point/graph/boundary intuition.

### A decisive limitation for base-16 π-normality

On the real circle, \(T(x)=16x\bmod1\) has the fixed point x=0. For any nonzero integer h, the character \(f_h(x)=e^{2\pi i h x}\) obeys \(f_h(0)=1\). At the fixed point, \((g-g\circ T)(0)=0\) for every globally defined g, so

\[
\boxed{\|f_h-(g-g\circ T)\|_\infty\ge1.}
\]

Therefore **no globally uniform o(1) approximate coboundary residual exists** for this Fourier character, irrespective of how g is parameterized. The digit-zero discrepancy \(1_{\mathrm{digit}=0}-1/16\) has the exact analogous lower bound \(15/16\). Finite rational-circle successor \(j\mapsto16j\bmod m\) reproduces that sharp \(15/16\) minimax residual, with the fixed point j=0 as the independently inspectable witness.

**This refutes the universal/source-blind version of the idea, not the π-specific version.** Periodic rational circle orbits do not establish the behavior of the actual selected π orbit.

## 4. How balanced zeros could still prove π normality

Main X fixes the genuine source \(U_0=0,\ U_{n+1}=16U_n+r(n+1)\), the signed four-pole forcing, and \(x_t=\{16^{t-1}\pi\}\). The π Frontier Contract requires

\[
S_N(h)=\sum_{t=1}^N e^{2\pi i h x_t}=o(N)\qquad \text{for each fixed } h\ne0.
\]

An operational target is a *source-authenticated*, N-dependent decomposition

\[
e^{2\pi i h x_t}=g_{h,N}(x_t)-g_{h,N}(x_{t+1})+r_{h,N}(x_t).
\]

It yields a **finite exact proof identity**

\[
\frac{|S_N(h)|}{N}
\le\frac{|g_{h,N}(x_1)-g_{h,N}(x_{N+1})|}{N}
+\frac1N\sum_{t=1}^N|r_{h,N}(x_t)|.
\]

If independent mathematical estimates using the **actual BBP signed source**, not a rational proxy, force both right-hand terms to zero, Weyl's criterion would establish base-16 normality. The fixed-point no-go proves that these residuals cannot instead converge to zero uniformly on the *whole* circle: they must be source-selected or measured in a suitable non-uniform but rigorously justified norm.

For any *finite* list f_0,...,f_{N-1}, the cumulative sum g_n=\(\sum_{j<n}f_j\) always gives f_n=g_{n+1}-g_n, yet f_n=1 makes \((g_N-g_0)/N=1\). Trivial cumulative telescoping therefore cannot be promoted to a normality theorem. The missing gear remains nontrivial **signed long-range cancellation** in an authentic source-selected Fourier/Walsh channel, precisely as recorded in Main X's π Frontier Contract.

## 5. Finite boundary correction arithmetic

The module also defines an explicitly finite rational certificate \(|L-R|\le\varepsilon\) with a source id and value chart. Same-source same-chart certificates compose by addition and transport under multiplication by scalar c with cap \(|c|\varepsilon\). A mismatch of source or real/p-adic chart fails. The triangle budget can be loose when signed errors cancel, as shown by the two complementary exact-rational tests.

No amount of testing a finite number of bounds proves that the missing boundary tends to zero. This remains an analytic theorem to be established, with legitimate limit domains and tail rates. Our code reports *exact finite algebra*, not an independently authenticated global proof calculus.

## 6. Status and falsifiers

| Claim | Claim status | Proof/negative control |
| --- | --- | --- |
| Multi-chart identities combine through ideal-membership witnesses | CLASSICAL / PAPER and exact finite tested | Original source premises must hold in one semantic model |
| BBP four signed poles can be balanced with a positive factor chart | CLASSICAL / PAPER and exact finite tested | Mutated -2t^5 coefficient invalidates original witness |
| Simultaneous incompatible zeros are sound | REFUTED | \(1=x-(x-1)\) under contradictory premises |
| Finite coboundary iff all cycle sums vanish | CLASSICAL / PAPER; exact rational tests | Signed cycle obstruction returned explicitly |
| Minimal uniform residual equals largest absolute cycle mean | PAPER PROVED; attained exact-rational tests | Restriction to finite deterministic source graph |
| Source-blind uniformly vanishing Fourier coboundary residual for base 16 | REFUTED | Fixed point x=0 forces \(\|r\|_\infty\ge1\) |
| Generic zero balancing establishes π normality | OPEN / UNVERIFIED | A new authenticated signed source-cancellation estimate is required |
| This establishes RH or signed Weil positivity | NOT CLAIMED | Positive polynomial factors are not completed signed Weil forms |

## 7. Reproduction and references

New code: observational_succ/coherent_zero_relations.py. Exact tests: tests/test_coherent_zero_relations.py. JSON replay: scripts/coherent_zero_relations_probe.py --verify. **14 exact local unit tests passed under Python 3.13.5, replay passed.** These are isolated tests, not a hosted whole-repository CI claim. No imported source or frozen provenance file was changed. Run all AGENTS.md mandatory validation on the actual commit before promoting the claims.

Relevant classical mathematics: polynomial ideal membership/syzygies (https://pmc.ncbi.nlm.nih.gov/articles/PMC6365845/), Wilf-Zeilberger certified telescoping (https://sites.math.rutgers.edu/~zeilberg/mamarim/mamarimhtml/multiwz.html), periodic-orbit cohomological obstructions/Livšic (https://annals.math.princeton.edu/2011/173-2/p11). These references are background; the finite residual minimax theorem above is proved directly.
