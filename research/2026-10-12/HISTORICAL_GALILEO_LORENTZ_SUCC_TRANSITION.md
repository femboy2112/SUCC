# A historical transition SUCC can reconstruct: Galilean covariance → Lorentzian geometry

**Checkpoint:** 2026-10-12. **Research status:** a retrospective, mathematically complete **1+1-dimensional vacuum-wave and transverse-Maxwell case study**, with exact rational source-shadow and proof-transform certificates. It is not a re-enactment of historical measurements, a formalization of all four Maxwell equations with sources, an experiment proving physical ontology, a claim of academic novelty, or an RH result.

**Source:** `observational_succ/galilean_lorentz_succ.py`, `relativistic_shadow_tower.py`, `maxwell_transverse_shadow.py`. Independent tests in `tests/test_galilean_lorentz_succ.py`, `test_relativistic_shadow_tower.py`, `test_maxwell_transverse_shadow.py`. Reproducible receipt: `scripts/historical_galilean_lorentz_probe.py` and JSON. Base is research branch PR #38, whose previous claims F1–F15 distinguish observational darkness, no global source, geometric holonomy and state-changing proof failures. The historical simulation uses the *environmental proof obligations*, not a story that one software experiment changed world physics.

## What actually happened historically—and what this simulation does not claim

Classical mechanics uses Galilean inertial changes of frame, for which time is absolute. Maxwellian electrodynamics introduces light propagation with a characteristic vacuum speed. The 1887 Michelson–Morley measurements imposed important empirical constraints on ether drift, and Lorentz, FitzGerald, Poincaré and Einstein contributed different conceptual/mathematical developments. Einstein's **1905** "On the Electrodynamics of Moving Bodies" appealed to the relativity of electromagnetic phenomena, including the magnet/conductor asymmetry, and postulated the same vacuum light speed in all inertial frames. It was not historically simply a symbolic wave-operator exercise.

This dossier **reconstructs the logical compatibility transition** under the explicit source assumptions: (i) fixed vacuum Maxwell wave law, (ii) same physical law in all inertial frames, (iii) two light directions, (iv) normalized clock measurements and (v) linear, orientation/time-preserving inertial transformations. An alternative coherent model of a *moving material medium* shows the wave-operator mismatch alone does NOT logically select special relativity from every imaginable theory.

Primary/historical witnesses:
- Einstein, *Zur Elektrodynamik bewegter Körper*, Annalen der Physik **17** (1905) 891–921, translated at https://sites.pitt.edu/~jdnorton/teaching/HPS_0410/chapters/origins_pathway/On-the_electrodynamics/index.html
- Michelson & Morley, *On the Relative Motion of the Earth and the Luminiferous Ether*, American Journal of Science **s3-34** (1887), 333–345: https://ajsonline.org/article/62505-on-the-relative-motion-of-the-earth-and-the-luminiferous-ether
- MIT STS.042, *Electrodynamics for Maxwell and Lorentz* https://ocw.mit.edu/courses/sts-042-einstein-oppenheimer-feynman-physics-in-the-20th-century-fall-2020/mitsts_042j_f20_lecnote_electrodynamics.pdf
- MIT 8.20, exact wave equation change-of-frame teaching control: https://stuff.mit.edu/afs/athena/course/8/8.20/www/sols/sol1.pdf

## Source contract: no observation-derived physical certainty is smuggled in

Fix 1+1 flat event carrier \(V=\mathbb Q^2\) as an exact rational model, coordinates \((t,x)\), natural units \(c=1\), and the symmetric principal symbol / Lorentz quadratic form
\[
\eta=\begin{pmatrix}1&0\\0&-1\end{pmatrix},\quad
\square=\partial_t^2-\partial_x^2.
\]
The rational source model is **declared**; source tags, owner names and source-versioned receipts do not authenticate experimental instruments. Its source-free transverse Maxwell subsystem is
\[
\partial_t E_y+\partial_x B_z=0,\qquad
\partial_t B_z+\partial_x E_y=0.\tag{0}
\]
This restricted physical subsystem is genuine mathematics contained in 3+1 Maxwell theory for \(E_y(t,x),B_z(t,x)\) with no charges or currents, while not claiming to prove the complete 3+1 theory. **All physical laws of the source are hypotheses of the model**, not deductions from finite observations.

## GL1 — The old field was correctly fitted to its original domain (CLASSICAL / PROVED LOCAL)

The unforced Newtonian equation \(d^2x/dt^2=0\) is form-invariant under
\[G_v:(t,x)\mapsto(t',x')=(t,x-vt).\]
Indeed, if \(x(t)=a+ut\), then \(x'(t')=a+(u-v)t'\), whose second derivative is still zero. This is a **positive** SUCC environmental-closure certificate. It prevents the false historical inference "Galilean mechanics was always inconsistent." Compatibility is indexed by the laws/probe class in question.

## GL2 — A new domain creates an exact noncommuting square (CLASSICAL / PROVED LOCAL)

Under \(G_v\), the chain rule gives
\[
\partial_t=\partial_{t'}-v\partial_{x'},\qquad
\partial_x=\partial_{x'},
\]
and hence
\[
\square=\partial_{t'}^2-2v\partial_{t'}\partial_{x'}+(v^2-1)\partial_{x'}^2.
\]
In matrix notation, a coordinate transformation \(y=Tx\) sends the principal symbol to \(T\eta T^T\). For \(G_v=\left(\smallmatrix1&0\\-v&1\end{smallmatrix}\right)\), the requested **same-form vacuum** square fails by
\[
\boxed{G_v\eta G_v^T-\eta=
\begin{pmatrix}0&-v\\-v&v^2\end{pmatrix}.}\tag{GL2}
\]
Therefore the operator itself is not form-invariant for **every** \(v\ne0\). This is a universal polynomial identity, not merely a numerical test.

A constructive scalar solution witness is \(f(t,x)=(t-x)^2\), which satisfies \(\square f=0\). In moving coordinates \(f'=((1-v)t'-x')^2\), and the same-form primed operator yields \(2[(1-v)^2-1]=2v(v-2)\). For rational \(v=3/5\) this is exactly \(-42/25\). This is the source-attested *mathematical* failure receipt.

**Falsifier:** every AFFINE wave \(f=a+bt+cx\) has zero second derivatives in every linear frame. Testing only those waves fails to see the obstruction. The probe class must be rich enough to excite second derivatives.

## GL3 — Stronger Maxwell no-go: changing field components alone cannot repair Galilean time (CLASSICAL / PROVED LOCAL)

Let \(F=(E_y,B_z)^T\), \(S=\left(\smallmatrix0&1\\1&0\end{smallmatrix}\right)\). The declared Maxwell subsystem is \((\partial_t+S\partial_x)F=0\). Under Galilean coordinate change the moving-frame flux is \(S-vI\), with characteristic eigenvalues \(1-v,-1-v\). Any invertible, pointwise zero-order change of field variables \(F'=RF\) changes the **principal** flux by similarity \(R(S-vI)R^{-1}\); its trace is \(-2v\), while the original flux \(S\) has trace zero. Therefore for \(v\ne0\), no such invertible mixing restores **the identical vacuum Maxwell principal system**. Derivatives of a variable \(R(t,x)\) only add lower-order terms and do not change this principal-symbol obstruction.

\[\boxed{v\ne0\ \Longrightarrow\ \forall R\in\mathrm{GL}_2:\ R(S-vI)R^{-1}\ne S.}\tag{GL3}\]

This is stronger than the scalar wave probe, although still specific to the declared source-free 1D transverse sector and field-redefinition class.

## GL4 — Two null shadows identify geometry up to scale; a clock completes it (CLASSICAL / PROVED LOCAL)

Do **not** give E the metric as an input. Let the unknown symmetric quadratic form be
\[Q(t,x)=a t^2+2btx+d x^2.\]
Three independent source-shadow measurements return
\[
Q(1,1)=0,\qquad Q(1,-1)=0,\qquad Q(1,0)=1.\tag{GL4a}
\]
The exact linear equations are \(a+2b+d=0\), \(a-2b+d=0\), and \(a=1\). Subtracting the first two gives \(b=0\), then \(d=-a=-1\). Thus
\[\boxed{Q(t,x)=t^2-x^2}\tag{GL4b}\]
**uniquely among symmetric 2x2 quadratic forms.** The rational source-shadow solver does not receive \(Q\) as an argument; A supplies the right-going ray, B the left-going ray, E a normalized clock. The order of arrivals is immaterial for unchanged-source receipts.

**Sharp negative:** the two null probes alone have rank two and leave \(Q=\lambda\eta\) for all scales \(\lambda\). A single null probe plus the unit clock also leaves a genuine rival, e.g. \(Q_1=t^2-x^2\) versus \(Q_2=t^2+2tx-3x^2\); both satisfy \(Q(1,1)=0\) and \(Q(1,0)=1\), but disagree about the opposite light ray. This exhibits an *unobservable geometric degree of freedom* prior to the missing probe.

**Source boundary:** the shadow values and the class "symmetric quadratic spacetime law" are assumed available. The theorem cannot authenticate actual light propagation or prove nature must have a quadratic metric from abstract rational outputs.

## GL5 — Minimal linear transformation repair (CLASSICAL / PROVED LOCAL)

Let \(T\) be an invertible, linear, future- and orientation-preserving map respecting each **oriented** null ray \(n_+=(1,1),n_-=(1,-1)\), and taking the moving observer's worldline \(x=vt\), \(|v|<1\), to its spatial origin \(x'=0\). Both null vectors are positive-eigenvalue eigenvectors of \(T\), giving
\[T=\begin{pmatrix}a&b\\b&a\end{pmatrix}.\]
The worldline condition implies \(b=-av\), hence
\[T=a\begin{pmatrix}1&-v\\-v&1\end{pmatrix},\quad a>0.\]
With **only light-cone/characteristic preservation** this is a one-parameter conformal ambiguity. The calibrated clock/interval law \(T^T\eta T=\eta\) adds \(a^2(1-v^2)=1\), hence the unique proper orthochronous boost
\[
\boxed{L_v=\gamma\begin{pmatrix}1&-v\\-v&1\end{pmatrix},\quad
\gamma=(1-v^2)^{-1/2}.}\tag{GL5}
\]
So the mathematical repair isn't a guessed "fancy coordinate change". It is **forced within the specified linear, oriented, clock-normalized class**. Without the clock, \(2L_v\) is a valid two-ray/worldline-preserving candidate but fails metric invariance by a factor four.

For rational tests we parametrize \(u=\tanh(\eta/2)\in\mathbb Q\cap(-1,1)\), giving \(v=2u/(1+u^2)\) and \(\gamma=(1+u^2)/(1-u^2)\). At \(u=1/3\), \(v=3/5,\gamma=5/4\):
\[L_{3/5}=\begin{pmatrix}5/4&-3/4\\-3/4&5/4\end{pmatrix}.\]

## GL6 — The repaired wave-solution square commutes for every C² field (CLASSICAL / PROVED LOCAL)

For any constant linear frame \(y=Tx\), define \((T_\ast f)(y)=f(T^{-1}y)\). The second derivative chain rule gives
\[
\square_y (T_\ast f)(y)=
\sum_{ab}[(T^{-1})\eta(T^{-1})^T]^{ab}(\partial_a\partial_b f)(T^{-1}y).
\]
When \(T=L_v\), \(T^{-1}\eta(T^{-1})^T=\eta\), so
\[
\boxed{\square_y\circ (L_v)_\ast=(L_v)_\ast\circ\square_x.}\tag{GL6}
\]
For Galilean \(G_v\) and nonzero \(v\), the operator square fails (GL2) and its failure has an explicit solution witness. Thus the canonical diagram *actually commutes for a whole solution space* after the repair. The code independently checks the principal symbol and an explicit quadratic witness.

This is the appropriate category-theoretic interpretation: spaces of smooth fields and their differential operators are the objects/arrows, with Lorentz pullback/pushforward providing a natural intertwiner. A merely commutative diagram on one observed constant function would be too weak.

## GL7 — The transverse Maxwell *field* representation commutes too (CLASSICAL / PROVED LOCAL)

Introduce \(f_+(x-t)=E+B\) and \(f_-(x+t)=E-B\). Each is transported along one null characteristic. Under the same Lorentz boost, transform both **coordinates** and **field components**:
\[
E'=\gamma(E-vB),\quad B'=\gamma(B-vE),\quad (t',x')=L_v(t,x).
\]
Let \(a=\gamma(1-v)>0\), \(b=\gamma(1+v)>0\) (with \(ab=1\)). The transformed characteristic functions become
\[
\boxed{f'_+(z)=a f_+(az),\qquad f'_-(z)=b f_-(bz).}\tag{GL7}
\]
Indeed \(x-t=a(x'-t')\), \(x+t=b(x'+t')\), \(E'+B'=a(E+B)\) and \(E'-B'=b(E-B)\). Every differentiable pair therefore remains a solution of both Maxwell transverse PDEs. The executable laboratory uses arbitrary exact rational polynomials for \(f_\pm\), including degree-three and degree-four cases, and independently computes coordinate pullback plus field mixing to verify the result. Composition of successive boosts is coherent.

## GL8 — All finite frame compositions preserve causality (CLASSICAL / PROVED LOCAL)

Every \(L_v\) obeys \(L_v^T\eta L_v=\eta\), has determinant 1, and maps future-directed timelike/null vectors to future-directed vectors. Therefore every finite product preserves Minkowski interval and the future causal cone. Simultaneity cuts may differ only on spacelike separation; actual source-event dependencies cannot be reversed. For 1+1 boosts, velocity composition is
\[v\oplus w=\frac{v+w}{1+vw},\]
so all positive- and negative-rapidity boosts form a group under composition. **In 2+1 / 3+1, non-collinear boosts need not commute**, as SUCC's existing CV3 Wigner-rotation research separately establishes. The new case study does not conflate the 1+1 commuting subgroup with the full Lorentz group.

**Independent time-orientation gate:** \(T^T\eta T=\eta\) does not by itself preserve the FUTURE causal cone. For instance \((t,x)\mapsto(-t,x)\) preserves the interval but reverses future-directed timelike vectors. We must verify proper orthochronous orientation separately. This is another example of source-law covariance not guaranteeing the specific operational meaning of a claim.

## GL9 — Both a Lorentz vacuum repair and a Galilean moving-medium repair are lawful under DIFFERENT source models (CLASSICAL / PROVED LOCAL)

One should not conclude from GL2 that the old coordinates cannot describe wave physics at all. Under a Galilean change of frame the **transported** operator remains lawful:
\[
\boxed{\square_{G_v}= (\partial_{t'}-v\partial_{x'})^2-\partial_{x'}^2.}\tag{GL9}
\]
It describes wave propagation against a background medium at a relative velocity; waves have primed velocities \(-1-v\) and \(1-v\). This is a coherent field-relative *preferred-medium* model. It does **not** make the unmodified same-form vacuum operator valid in every inertial frame. The Lorentz alternative has the same vacuum form in each inertial frame, in accordance with the additional relativity and light-speed principles.

**Critical SUCC falsifier:** the mere existence of a nonzero commuting-square residual does NOT mathematically imply that the Lorentz repair is physically uniquely true. The environmental source principles and observations determine which repair is actually appropriate. Historically, Maxwell/Lorentz/Einstein theories were not distinguished solely by reading one symbolic residual, and competing empirically equivalent ontological interpretations can survive accessible tests.

## GL10 — The old model has a quantitatively controlled ordinary-mechanics regime (CLASSICAL / PROVED LOCAL)

For \(v\) with rational \(\gamma\), the difference between Lorentz and Galilean time coordinates obeys
\[
|t'_L-t'_G|=|(\gamma-1)t-\gamma v x|
\le(\gamma-1)|t|+\gamma|v||x|.\tag{GL10}
\]
On bounded spacetime observations, the RHS tends to zero as \(v\to0\). Exact frame covariance remains false at every nonzero \(v\). High-frequency probes can amplify small coordinate errors, so there is no universal small-signal approximation without controlling probe regularity. Hence **"simple under the old observational regime"** and **"globally wrong for Maxwell-vacuum covariance"** can both be justified descriptions.

## GL11 — Observable spacetime geometry does NOT determine hidden ontology (PROVED CONDITIONAL COUNTERMODEL)

After the new repair, the operational light-propagation and clock results constrain a metric and frame group. They do not, by logic alone, certify the nonexistence of any undeclared hidden source parameter. Create two mathematical models with exactly the same observed light/clock laws but different unobservable `preferred-frame` tags. Both produce the same SUCC histories and satisfy every source-visible metric receipt, while an ontology predicate distinguishes them. No observer restricted to that interface can decide the tag. This does NOT say an ether exists or can never be experimentally distinguished by a larger probe class; it is a source-relative epistemic impossibility theorem.

## GL12 — Why this is a *real* complete historical-transition test for SUCC (and where it stops)

| SUCC layer | Old field / failure | Source-relative constructive repair |
|---|---|---|
| Environmental fit | Free-particle law closes in Galilean coordinates | Keep that valid approximation; don't call it universally wrong |
| Novel empirical forms | Two directions of light propagation | A pair of null characteristic constraints |
| Missing geometry | Galilean wave operator has cross term \(-2v\) | Time coordinate must mix with space for nonzero \(v\) |
| Incomplete shadow | Null cone alone leaves conformal scale | Add normalized proper-time / clock probe |
| Global carrier model | Symmetric quadratic geometry unconstructed | E solves exactly for its coefficients from three source receipts |
| Covariant proof transport | Old operator/model square fails; \(-42/25\) witness | Lorentz-covariant wave and Maxwell subsystem squares commute universally |
| Global frame composition | Proposed transformed facts might depend on path | Actual Lorentz group preserves causal order and interval |
| Environmental choice | A moving-medium Galilean law is also coherent | Add source model/relativity constraints; obstruction alone doesn't select ontology |
| Knowledge limit | Global geometric inference might tempt ontological overclaim | Two source models can share every existing observation but have different latent tags |

The historical conclusion **only** concerns the stated classical source-free sector and declared assumptions; it does not claim derivation of complete Maxwell electrodynamics with charges, GR curvature, quantum gravity, a physical measurement, the true physical interpretation of "ether", or a new historical discovery. The actual physics was built from experimental constraints and independently justified relativity postulates, not output solely by the algorithm. The SUCC implementation is a *mathematical proof/repair simulation*.

## Next SUCC challenges after this calibration

1. **Derive the admissible environment rather than hand-label it.** Inferring a quadratic principal symbol from given null rays and clock readings is conditional; a more general symbolic inverse-PDE test must discover source-family constraints and prove its own completeness.
2. **Extend to full 3+1 Maxwell tensor/source-current covariance**, with gauge freedom, constitutive relations and explicitly checked charge/current conservation; preserve non-collinear Lorentz/Wigner rotations from CV3.
3. **Independent empirical attestation and inference under noise.** Finite rational source receipts are mathematically exact, not historical measurements; develop confidence/interval certificates and physical instrument sourcing.
4. **Synthesis optimization / minimal repair discovery.** Given competing theories and constraints, find a minimal lawful field/geometry extension that discharges all certified residuals, without assuming the correct answer as an input or confusing source choice with proof of truth.
5. **Bridge to RH only by source-specific arithmetic.** The photon light cone is not an adelic Archimedean Gamma factor. This case proves SUCC can reconstruct a classical transition in its declared domain; it supplies no Weil positivity or RH implication.
6. **Independent machine-checking of universal statements.** Written chain-rule, linear-algebra and group proofs are universal, while Python's exact tests cover finite instances. Lean mechanization and historical/academic comparison are separate obligations.

**Novelty status:** GL1–GL11 are classical physics, linear algebra, representation theory, and observational inference. The new-to-project contribution is an integrated SUCC source/shadow/failed-diagram/repair/alternative-source/certificate pipeline with a proof and a counterproof at each stage. This is *not* a priority claim.
