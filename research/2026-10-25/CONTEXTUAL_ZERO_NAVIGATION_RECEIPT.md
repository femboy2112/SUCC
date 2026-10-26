# Contextual SUCC zero / observer navigation: executable theorem and hostile controls

**Research date:** 2026-10-25. **Dependency:** CZR #290 (source-typed polynomial null relations); downstream architecture addition, not a replacement of historical finite causal records. **Target:** a *backbone interface* independent of π, RH, or any particular field's physical substrate.

## A. Research object

A declared finite source context $\mathcal F=(X,\mathcal L,\mathcal P,\mathcal U,\tau)$ has exact rational coordinates, global finite-carrier zero laws, probe maps to $\mathbb Q$, and total movement maps $X\to X$, all with resource costs and one source passport. An observer carries a sorted nonempty support $B\subseteq X$, budget, and immutable journal. Hidden actual source state is only supplied to a **synthetic model execution**; the planner cannot read it.

1. **Learn:** a realized probe return $y$ restricts $B$ to its full fiber. This is a sound update, since its producing world stays in the fiber. Requiring a declared probe and a positive cost prevents hypothetical measurements from being treated as observed data.
2. **Move:** a realized action transports every remaining possible world through one total transition. Thus the actual new world lies in the transported support. Every global finite source zero survives because the map's codomain stays in $X$. A local zero may stop being true; its past observation stays in the source journal.
3. **Prove:** a polynomial source/chart zero is checked either against all original model states or against the current belief. Those certifications are different. A chart map acts through explicit polynomial pullback, and its inverse is not inferred.
4. **Plan:** finite AND/OR dynamic programming minimizes worst-case paid cost. An independent policy checker verifies all possible probe branches, transitions, budget usage and terminal goal. The positive cost recurrence proves soundness/completeness for the finite declared menu by induction on remaining budget. A failed plan means *no guarantee under those probes, movements, source and budget*, not a metaphysical impossibility.

## B. The new coherence theorem

Let $R=\mathbb Q[x_1,\ldots,x_d]$ and $I(B)=\bigcap_{s\in B}\ker(\mathrm{ev}_s)$. For every actualized observation shrinking $B'\subseteq B$,

$$I(B)\subseteq I(B').$$

Proof: if $f(s)=0$ for every $s\in B$, it does so for all $s\in B'$. This holds identically for every finite source context, without a probability model. It does not say the values of an unobserved variable are physically collapsed by epistemic bookkeeping, nor that a *movement* shrinks the same set. A source-valid chart $\phi$ gives $\phi^*(I(\phi(B)))\subseteq I(B)$, with possible information loss for noninjective maps. Exact syntactic polynomial zero, source-universal zero and belief-relative zero are separately labelled.

## C. Independent plan oracle calibration

The model uses $X=\{0,1,2,3\}$, clockwise/anticlockwise one-cost actions, one-cost exact readout $x$, and an optional parity readout. From complete uncertainty and budget 3, the minmax policy begins with the exact readout and then moves at most twice to the target $\{0\}$. Each world $x\in X$ was simulated with independently checked source journals and goal results. With budget 2, no guaranteed policy exists. With only bijective moves or only parity observation, the observer cannot single out the target from $B=X$, even if given ten actions. It does **not** follow that the actual world cannot reach the target; the observer cannot *guarantee* it without distinguishing information.

An independently authored value-only minmax solver (not reusing the production proof-tree implementation) examined **all 28 total transition maps on three source states**, three singleton targets, and budgets 0..4: $27\times3\times5=405$ exact instances. Every minimal cost or declared lack of a plan agreed; a separate policy checker and every hidden-world execution agreed for every returned policy. This is finite exhaustive evidence, not a universal theorem solely from testing.

## D. Mutations and limitations

- Source field label mismatch rejected; laws not true for *all* declared states rejected, even if current belief happens to satisfy them.
- Undeclared or zero-cost probes, actions pointing outside their codomain, unaffordable actions, duplicate possible states, guessed model outcome and inconsistent chart dimensions rejected.
- An observation can make $x-2=0$ true on current support, but a subsequent movement to $x=3$ makes that local relation false now while retaining the exact earlier event in history.
- A polynomial identity on a finite carrier need not be an identity in the full polynomial ring. Global **within X** is not mathematically universal; this is explicitly surfaced.
- A chart can project $x\mapsto x^2$ and lose sign: source evidence about $x^2$ does not establish $x$ without further probes.
- A proposed policy does not consume resources or write a journal event; only simulated realization does. A forged policy with missing branches, wrong source, or fraudulent cost is rejected.
- A gauge-centered potential is invariant under uniform additive shifts but is **not** a physical quantum vacuum theorem.

## E. Outstanding verdict-changing probe

Integrate the same context interface with a *verified* original BBP source witness and two complementary observation charts (real-circle and odd-conductor residues). Demand an independently source-attested map on the actual signed carries, not a rational phase surrogate; construct and refute competing policies using source-specific future information. Track whether a new observation reduces the uncertainty relevant to the actual upper bound for selected Weyl sums (not merely the number of finite states in a synthetic example). No transport from polynomial ideals, simulator planning or untyped virtual field rhetoric to π normality/RH is licensed.

## F. Reproduction

Run `PYTHONPATH=. python -m unittest discover -s tests -p 'test_contextual_zero_navigation.py' -v` and `python scripts/contextual_zero_backbone_probe.py --verify`. Local Python 3.13.5: **14 new tests passed** and **14 inherited CZR tests passed** (28 total). The 405-case independent planner holdout is included in the 14 tests. Additional hosted CI and AGENTS.md validation must be checked separately; no GitHub hosted success is presumed. No original source files were changed. The QFT analogy is explanatory only.
