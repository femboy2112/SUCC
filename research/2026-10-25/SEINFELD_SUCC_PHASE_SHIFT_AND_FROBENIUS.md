# Seinfeld SUCC II: Phase shifts, vanishing presentations, Frobenius thickenings, and arithmetic coherence

**Research-only · 2026-10-25.** Direct continuation of draft PR #294, `research/seinfeld-succ-null-provenance-2026-10-25@82f4617e31e06b84fdbe52b4b217b92dcd4732dd`. Parent `main@1e3a453e` contains Coherent Main X (π Gearbox). The author's proposed example is the chain `1=0+1=(1-1)+1=(2-1)^2=…`. **Actual scope:** classical exact algebra plus new-to-project, explicitly chosen phase interfaces, source-specific signed readouts, finite probes, and counterexamples. Neither π-normality, RH, physical phase, universal novelty, nor a new Lean theorem is claimed.

## 0. The proper object

A chain of rewrites can involve distinct **presentations** of the same number. Arithmetic equality is not a quantum operation or a U(1) phase assignment. The weakest faithful mathematical construction therefore has three separate types:

- a scalar evaluation identifying the numerical value (`0`, `1`, and so on);
- a labelled path of formal rewrites whose history is *not* thrown away by scalar evaluation;
- a **declared** observable, deformation or U(1)-valued 1-cochain on rewrite/source paths.

A change in the third type must not be presented as a forced fact about the first. A phase only becomes potentially non-removable after specifying which changes of gauge are allowed and what source measurement fixes the comparison. In all examples below phases are retained as exact rational *turns* `t ∈ Q/Z`, interpreted only when requested as `exp(2πi t)`. No floating complex computation is used as evidence.

## 1. Unit rewrites as a finite inverse-fiber tower (SPH-01)

Let the intermediate *symbol* `u` stand for the unit presentation `2−1`. In ordinary integers the source constraint is `u=1`. It implies all later equations `u^(2^k)=1`, but the reverse implication does not hold.

On the complex unit circle the equation `u^(2^k)=1` has exactly `2^k` distinct solutions

\[
 u_j=\exp(2\pi i j/2^k),\qquad j=0,1,\ldots,2^k-1.
\]

This is a concrete backwards fiber with exponential growth under information loss, not a claim that the original equality admits extra solutions. Retaining `u=2−1=1` leaves exactly the selected `j=0` point. Algebraically the ideal inclusion is

\[
 (u^{2^{k+1}}-1)\subset (u^{2^k}-1)\subset (u-1)
\]

in `Z[u]`. The later equation is weaker, with a larger solution set in characteristic zero. **Source selection is a separate constraint.**

## 2. A scalar-zero relation can have a nonzero first-order jet (SPH-02)

Use `R=Q[u]`, `I=(u−1)`. The congruence modulo `I²` is

\[
 \boxed{u^m-1\equiv m(u-1)\pmod{(u-1)^2}.}
\]

It follows directly by writing `u=1+ε` and expanding the binomial. Thus `u−1` and `u²−1` both evaluate to zero at `u=1`, yet their first-order conormal classes differ by a factor of two. More generally `I/I²` remembers the first derivative of a vanishing constraint, and higher powers `I^j/I^(j+1)` record higher jets. A phase deformation `u=e^{iθ}` gives the exact off-shell values `u^m=e^{imθ}` and first-order slope `m`. **If `2` and `1` retain their literal fixed integer values, there is no deformation and no new phase**; the declared free symbol `u` is essential.

## 3. Frobenius: coalescing roots, retained nilpotents (SPH-03)

Over `F₂`, the characteristic-two Frobenius identity gives

\[
 u^{2^k}-1=(u-1)^{2^k}.
\]

The group scheme of `2^k`th roots of unity has coordinate ring

\[
 \boxed{\mathcal O(\mu_{2^k}/F_2)
   =F_2[u]/(u^{2^k}-1)
   \cong F_2[ε]/(ε^{2^k}),\quad ε=u-1.}
\]

It has **one** geometric point over an algebraic closure of `F₂`, but dimension/rank `2^k` over `F₂`. The element `ε` is nonzero and satisfies `ε^(2^k)=0`, while `ε^(2^k−1)≠0`. The loss of distinct complex roots is not the loss of the nonreduced scheme structure. This is an established group-scheme fact, not a physical superposition or an independently proved classification theorem.

Primary context: [Stacks Project, roots-of-unity group scheme](https://github.com/stacks/stacks-project/blob/master/groupoids.tex), [Stacks Project, Frobenii §33.36](https://stacks.math.columbia.edu/tag/0CC6), and established descriptions of Cartier duality for constant cyclic group schemes and `μ_n`. The latter may inform a future clock-character comparison, but no categorical equivalence to BBP carriers is claimed here.

## 4. Relative phase on the SUCC/FUCC affine zero (SPH-04)

For the positive-integer basis, genuine prime `p`, and `ω_p=exp(2πi/p)`, define a *chosen* twist

\[
 S|n\rangle=|n+1\rangle,\qquad
 \widetilde V_p|n\rangle=\omega_p^n|pn\rangle.
\]

Then the two equal-endpoint paths differ by a definite phase:

\[
 \boxed{\widetilde V_pS=\omega_p S^p\widetilde V_p.}
\]

At `p=2` this is an anticommutation-looking sign `−1`; at `p=3` a primitive cube-root. The classical untwisted equality `V_pS=S^pV_p` still holds in its own type. The twist is not *derived* from the zero equation—it is an additional edge-observable. Exact phase checks require only rational residue turns `n/p`.

## 5. Independent prime phase labels need not glue (SPH-05)

If **each** genuine prime is independently assigned `χ_p(n)=n/p mod 1` on multiplication edges, the path phases around a prime-square do not generally agree. For primes `p,q` and start `n` the discrepancy, in rational turns, is

\[
 \boxed{D_{p,q}(n)
 =n\left(\frac{q-1}{p}-\frac{p-1}{q}\right)\pmod1.}
\]

The proof compares the paths `V_p V_q` (first multiply by `q`, then by `p`) and `V_q V_p`. At `(p,q,n)=(2,3,1)` the defect is `2/3` turns. Thus the independently chosen one-prime twists do **not** form a globally coherent commuting FUCC family. This is an exact negative control for any suggestion that arbitrary local phase shifts constitute a single universal Frobenius structure.

## 6. Flat all-prime cochains are source potentials (SPH-06)

A stronger complete classification is available using only unique prime factorization.

**Theorem (classical algebra, paper proof).** Suppose for every genuine prime `p` and positive integer `n` one supplies a rational-turn edge label `χ_p(n)`, and for every `p,q,n` it satisfies the complete prime-square coherence equation

\[
 \chi_p(n)+\chi_q(pn)
 \equiv\chi_q(n)+\chi_p(qn)\pmod1.
\]

Then there exists a potential `f:N_{≥1}→Q/Z`, unique up to the value `f(1)`, such that

\[
 \boxed{\chi_p(n)=f(pn)-f(n)\pmod1.}
\]

**Proof.** Set `f(1)=0`. For any `n`, choose a prime factorization `n=p_1⋯p_r` and define `f(n)` as the sum of phases along the corresponding multiplication path from 1. Two orderings of the same prime multiset differ by adjacent transpositions; each transposition replaces two legs of one declared prime square, which have equal phase. Therefore the definition is path-independent. Appending `p` gives the displayed edge equation. Any two such potentials have zero difference across every prime-multiplication edge and hence differ by a constant, since 1 reaches every positive integer by prime multiplication. The converse is immediate by telescoping. QED.

**Meaning:** full multiprime phase coherence forces the connection on the **multiplicative-only** source graph to be an exact potential. It is gauge-removable *there*. A genuinely non-flat or mixed-additive/multiplicative phase needs a separately specified observational reference, not just a zero equation. The module contains a finite all-edge solver; its success for a bounded horizon is only a finite check, while the above argument proves the universal theorem under its quantified hypotheses.

## 7. A single authenticated source supplies coherent FUCC phases (SPH-07)

Let `f(n)` be any circle-valued source readout. Define

\[
 V_a^f|n\rangle
 =e^{2\pi i(f(an)-f(n))}|an\rangle.
\]

Then **for every positive integer** `a,b` (with only actual primes designated primitive),

\[
 V_a^fV_b^f=V_b^fV_a^f=V_{ab}^f.
\]

The proof is the exact telescope through `f(bn)` or `f(an)`. This supplies the common potential required by SPH-06, without assuming independence of distinct primes. In particular `f(n)=U_n mod 1` for the original four-pole BBP source yields authentic source-aligned phases; a nonnormal counterfeit also yields an equally coherent family, so **flat FUCC phases do not imply normality**.

Hold the SUCC edge reference phase at zero. On the affine diamond, the *relative* phase is

\[
 \boxed{\Phi_p^f(n)
  =f(pn+p)-f(pn)-f(n+1)+f(n)\pmod1.}
\]

For the actual unwrapped BBP state, every term is an exact rational. This is a source-typed mixed difference, a candidate diagnostic. But if **both** SUCC and FUCC edges are labelled by the same total gradient `df`, every affine-loop phase telescopes to zero identically. The relative twist is therefore **reference-dependent**, not a gauge-invariant curvature of the fully gradient-labelled system. No mixing bound has been proved for authentic `Φ_p^U(n)`.

## 8. Selected-counterfeit obstruction survives the phase lift (SPH-08)

Keep SS-08's explicit nonnormal source:

\[
 T_n^*=\frac1{(8n+1)(8n+3)},\quad
 U_n^*=\frac{16^n}{3}-T_n^*,\quad U_0^*=0.
\]

Since `16^n≡1 (mod 3)`, its phase-valued `f*(n)=U_n* mod1` is the constant `1/3` minus `T_n*` at every positive index. Hence its mixed diamond phase is congruent to the exact small signed rational

\[
 \Phi_p^{*}(n)
 \equiv -\left[T_{pn+p}^*-T_{pn}^*-T_{n+1}^*+T_n^*\right]\pmod1,
\]

and for every prime `p` and `n≥1` it has the valid real representative bound

\[
 \boxed{|\Phi_p^{*}(n)|<\frac1{16n^2}.}
\]

Proof: `0<T_m*<1/(64m²)` for `m≥1`; apply the triangle inequality to four tails, and `p≥2`. Its total variation in `n` is summable, so for every fixed integer `h`, by `|e(x)−1|≤2π|x|` and `Σ_{n≥1}n^-2<2`,

\[
 \left|\frac1N\sum_{n=1}^Ne^{2\pi ih\Phi_p^{*}(n)}-1\right|
 \le\frac{\pi|h|}{4N}.
\]

The average therefore tends to **one**, not zero. This is a decisive hostile control against the implication "phase-twisted source coherence ⇒ mixing". The counterfeit changes the BBP forcing (it does not share the original four pole positions), so the result is not a counterexample to a fully authenticated π-specific theorem.

## 9. Next genuinely new arithmetic estimate (SPH-09, OPEN)

Test the authentic mixed phase

\[
 \Phi_p^U(n)=(U_{p(n+1)}-U_{pn})-(U_{n+1}-U_n)\pmod1
\]

against exact source-recurrence and independent Machin readouts, first for `p=2,3,5,7`, without moving to floating claims. An asymptotic sum bound

\[
 N^{-1}\sum_{n≤N}e^{2\pi ih\Phi_p^U(n)}=o(1)
\]

would be new source-selected information if proved; however **it has not been proved, and no implication to π normality has been established from it**. A separate argument must transport any signed mixed-phase saving to the original `S_N(h)` (Weyl), harmonic/cyclotomic criterion, or prescribed real-circle collision estimate `K_p(1)=p^{o(1)}`. A trivial change of representation, exact gradient, random-prime average, or successful finite sample does not pay that debt.

## Validation, provenance, and hostile controls

- Exact implementation `observational_succ/seinfeld_phase.py` (no floating phases, full domain gates).
- Independent finite rational tests `tests/test_seinfeld_phase.py` and deterministic replay `scripts/seinfeld_phase_probe.py` with frozen `research/2026-10-25/SEINFELD_SUCC_PHASE_RECEIPT.json`.
- Hostile controls include (i) loss of the original anchor `u=1`, (ii) naive cross-prime noncommutativity, (iii) reference-only relative holonomy compared with the fully flat gradient, (iv) nonnormal original SS-08 counterfeit, and (v) wrong/composite primitive labels.
- The classical sources above remain external and attributed. GitHub combined-tree CI and Lean authority are distinct from the isolated exact tests; no new Lean proof is claimed.

**Verdict:** the proposed phase shift has exact nontrivial mathematical interpretations—root inverse fibers, conormal jets, nonreduced Frobenius fibers, projectively twisted single-prime affine paths—and an equally exact **coherence obstruction**: independent local phases may not glue. When they do glue on the multiplicative graph, they are gradients. The authentic BBP distribution estimate remains the indispensable missing theorem.
