# BPGS — Boundary-complete geometry selection, source transport, and hidden mixed susceptibilities

**Research status (2026-10-22):** new-to-SUCC synthesis of classical Kron/Schur/Woodbury mathematics, exact new-to-project finite derivations, hostile rational regressions. **Not an academic novelty claim, an observation of reality, a physical model of lightning, or a fundamental geometry theorem.**

**Parent:** draft PR #239 `research/source-faithful-bidirectional-histories-2026-10-22@6b50a7828cb9350aa391a5469cde8454b8a0b95c`, stacked on #237 `391c304e768d073ae747459d279e14d5357092e5`, rooted at reviewed `main@b116841f12b41aaf7600da39bbb40577f25b6295`. Independent source research #238 `adf663f1523b28b51789859e0cc24169bfb5e7e5` supplies the p-adic first-/second-level and correlation nonidentification countermodels; **its assumptions are not imported into the physical resistor source**. Historical imports and root `main` are untouched.

## 0. Steelman: a simultaneous reconstruction-and-commutation program

The originating conjecture: geometry might be selected by **completing different mathematical models from partial source data and then requiring that every boundary/interface transfer commute with the actually observed source interactions**. A source-grounded physical observation should choose among the remaining mathematical models, not manufacture a chosen fit. This can be made rigorous for declared finite model families, not without an independently authenticated realization map.

We separate **(I) sufficiency** (a smaller observable/transfer state predicts an unlimited number of finite allowed continuations), **(II) identifiability** (specified measurements uniquely infer that state within a declared family), **(III) categorical naturality** (the same labeled intervention agrees under detailed and reduced representations), **(IV) physical source adequacy** (a measured physical process actually instantiates these labels and laws). I–III are the mathematical target; IV remains UNVERIFIED. In particular, a perfectly commuting synthetic diagram is insufficient for IV.

## 1. Precise finite source, operator, and ports

Take a finite undirected positive-conductance graph G with vertices V, a fixed nonempty electrode set B, and interior I. Each connected component reaches B, so the Dirichlet interior block `A=L_II` is invertible positive definite. Fix **m labeled, oriented candidate source ports** `b_e=delta_x-delta_y`; source labels, positions, and physical meaning must not be inferred from the resulting matrix alone. Negative/zero conductances are excluded.

Let `H=[Id_B; -A^{-1} L_IB]` be the harmonic extension of every boundary voltage. Define, with `P` the V×m matrix of source port incidence columns and `P_I` its interior restriction,

\[
\begin{aligned}
\Lambda&=L_{BB}-L_{BI}A^{-1}L_{IB},\\
W&=H^\top P\quad(B\times m),\\
R&=P_I^\top A^{-1}P_I\quad(m\times m).
\end{aligned}
\]

The source-dependent **port-response jet** is `J(G;P)=(Lambda,W,R)`. `Lambda` is the externally observed static DtN map; `W,R` are supplementary internal transfer data, generally **not available from boundary readouts alone**. `R` is positive semidefinite and `R_ee>=0`. Reversing one port orientation changes its W column and the corresponding R row/column by sign; Lambda stays invariant. This is a port **gauge**, not a new physical source.

## 2. BPGS-01 — finite exact boundary-port closure (CLASSICAL algebra, PROVED LOCAL instantiation)

For a fixed candidate port `e`, add its physical conductance `g>0` to G. Let `w_e=W[:,e]`, `r_e=R[e,e]`, `c=g/(1+g r_e)`. Then

\[
\boxed{\begin{aligned}
\Lambda' &=\Lambda+c\,w_e w_e^\top,\\
W'&=W-c\,w_eR_{e,:},\\
R'&=R-c\,R_{:,e}R_{e,:}.
\end{aligned}}
\]

**Paper derivation:** the grounded interior block becomes `A'=A+g b_{e,I} b_{e,I}^T`. Sherman–Morrison gives `A'^{-1}=A^{-1}-c A^{-1}b_{e,I} b_{e,I}^TA^{-1}`. Substitute into R to get its update. The new harmonic extension evaluated at any candidate `f` changes by `-c R_{ef}(w_e^T u_B)`; hence every W column updates as above. Completing the grounded Dirichlet energy (or expanding the new Schur complement) yields the Lambda update. No Gaussian-elimination oracle or material continuum assumption is hidden in this algebra.

**Consequence (all finite future words):** given only J and the *source-certified* sequence `(e_1,g_1),...,(e_k,g_k)` of fixed port additions, iterate the boxed rules to predict **every intermediate and terminal DtN matrix**, W and R. This is a finite sufficient state for arbitrary finite continuations from the declared port alphabet, without reconstructing the original interior graph. It is not claimed to be the minimal observable state or to uniquely encode G.

**Naturality law:** for the detailed graph update `T_e^g` and the above rational operator `U_e^g`,

\[
\boxed{J(T_e^g G;P)=U_e^g(J(G;P)).}
\]

This is an actual commuting square of specified maps, not endpoint resemblance. It composes for every lawful word. Independent positive increments commute as terminal `J` operations (even though intermediate `J`s differ), since they correspond to the same final Laplacian `L+sum g_e b_e b_e^T`. Therefore **fixed-increment endpoint holonomy is zero**. With field- or memory-dependent conductance changes, the interventions can cease to commute, as demonstrated by the existing history-DtN exact `1/4411` order defect. No categorical square is asserted between such *different physical histories* without including the changed material state.

**Classical multiport relation:** with diagonal positive `D=diag(g_e)` and all edges applied, `Lambda(D)=Lambda+W(D^{-1}+R)^{-1}W^T` (Woodbury); this is also a direct test of the sufficiency assertion. The sequential rational update is convenient because the source event record and order are preserved explicitly even when final states coincide.

## 3. BPGS-02 — precise backward reconstruction with an actual event log

Suppose a **known** source event `(e,g)` was applied, and the full post-event port jet `J'` is retained. Then `g R'_{ee}<1`, and setting

\[
 c_{\mathrm{back}}=\frac{-g}{1-g R'_{ee}}
\]

in the same three rank-one formulas applied to `J'` reconstructs `J` exactly. Reversing the **logged event order** therefore reconstructs all prior J states. Proof: `R'_{ee}=r_e/(1+g r_e)`, so `1-g R'_{ee}=1/(1+g r_e)>0`; substitution cancels the forward Woodbury update. This is an algebraic *inverse on the attainable source-labelled image*, not a permissible negative-conductance physical operation or evidence of backwards time causation.

Crucial hostility: changing a recorded `g` to a different value can give a mathematically well-typed but wrong predecessor. An observed `Lambda'` alone cannot select that event log (the hidden bridge example is explicit). Thus **backward SUCC-style reconstruction agrees with forward evolution only when the same source event history and sufficient port information are preserved**. Prime multiplicative FUCC and Bayesian reverse probabilities remain separate typed operations unless an independent source realization is supplied.

## 4. BPGS-03 — one independently calibrated intervention selects a unique parameter

Consider two boundary electrodes L,R and interior u,v with four unit arms L-u,u-R,L-v,v-R, and one unknown nonnegative `u-v` bridge conductance `g`. Every such G has *exactly the same* bare DtN matrix `[[1,-1],[-1,1]]`, so all baseline boundary voltages and currents fail to identify g. Insert a **known, independent** increment `a>0` on L-u and measure effective conductance C(a,g):

\[
\boxed{C(a,g)=\frac{(2a+4)g+3a+4}{(a+4)g+2a+4}.}
\]

Kirchhoff's interior equations, solved exactly under boundary drive L=0,R=1, give this formula. Differentiate:

\[
\frac{\partial C}{\partial g}=\frac{a^2}{((a+4)g+2a+4)^2}>0 \quad (a>0).
\]

Hence C(a,.) is strictly increasing on **the declared parameter family** `g>=0`. Its exact unique inverse is

\[
\boxed{g=\frac{3a+4-(2a+4)C}{(a+4)C-(2a+4)}.}
\]

At a=1, C(1,0)=7/6 and C(1,7)=49/41; the latter recovers **g=7**. At a=0 the response equals 1 for all g, so inversion is impossible. No arbitrary unknown graph, moisture profile, plasma kinetics or boundary contact resistance can be recovered from this single scalar datum without the model-family assumptions.

**Quantitative noise boundary:** for any `g1,g2>=0`,

\[
\boxed{C(a,g_2)-C(a,g_1)=\frac{a^2(g_2-g_1)}{D(a,g_1)D(a,g_2)}},
\quad D(a,g)=(a+4)g+2a+4.
\]

If `0<=g1,g2<=G`, this gives the rigorous Lipschitz bound

\[
|g_2-g_1|\le\frac{D(a,G)^2}{a^2}|C(a,g_2)-C(a,g_1)|.
\]

Uniform stability fails as the prior upper bound G tends to infinity: saturated large bridges are hard to distinguish with finite measurement precision.

## 5. BPGS-04 — two-strength boundary-only calibration of one visible port

Fix a boundary drive f and an otherwise unchanged/RESET initial network. For one declared port e, let `A=(w_e^T f)^2` and `r=R_ee`, with A>0. Two independent known contact strengths `g1!=g2>0` give measured energy gains

\[ d_j=\frac{g_j A}{1+g_j r}.\]

Set `y_j=g_j/d_j`, `m=(y_2-y_1)/(g_2-g_1)`, `b=y_1-m g_1`. Then exactly

\[\boxed{ A=1/b,\quad r=m/b.}\]

For the diamond's L-u contact, `A=1/4`. Before the hidden bridge, `r=1/2`; after an unobserved bridge `g=7`, **the same A remains** but `r=9/32`. Thus a boundary-current measurement at two strengths on independently reset copies can reconstruct the local Green response needed to discriminate them, provided the identical source port and baseline really are reproducible. This does **not** recover every cross-port `R_ij` or the full graph: the complete finite port jet generally needs more probes and source constraints. No high-voltage experiment is recommended or performed.

## 6. BPGS-05 — invisible first and second variations, nonzero third-order contact

Let h be a source port with `w_h=0` (invisible under *every* current boundary voltage) and f a candidate visible port with `w_f!=0`. Put `q=R_hf`, `r=R_ff`, `s=R_hh`. Insert hidden `h` strength z and visible `f` strength a. The hidden event leaves Lambda and w_f unchanged, but changes r to

\[r'=r-\frac{zq^2}{1+zs}.\]

The contact response difference between a network with and without that hidden event is the exact matrix

\[
\boxed{\Delta_h\Lambda(a,z)=\frac{a^2 z q^2}{(1+zs)(1+ar)(1+ar')}w_f w_f^T.}
\]

Thus the first possible mixed monomial is `a²z`; all variations involving one hidden event of total degree 1 or 2 vanish, but generically

\[
\boxed{\left.\frac{\partial^3\Lambda}{\partial z\partial a^2}\right|_{a=z=0}=2q^2 w_f w_f^T.}
\]

If q=0, this particular contact cannot distinguish the hidden bridge. This is a **source-relative, higher-order electrical susceptibility**, not a Cherenkov cone or a proof that physical time runs backward.

For the exact diamond: `q=-1/2`, `w_f^T(1,0)=1/2`, `r=1/2`, `s=1`, so

\[
C(a,g)-C(a,0)=\frac{a^2g}{(2a+4)((a+4)g+2a+4)}
=\frac{a^2g}{16}+\text{higher total degree}.
\]

The mixed derivative is **1/8**. Its appearance is *not* fitted after observing the simulated output; the coefficient is derived from the source Green Gram matrix before the intervention and checked by a second rational Kirchhoff implementation.

## 7. BPGS-06 — categorical descent criterion and largest future-safe quotient

Let X be a finite source state family, A a declared finite alphabet of **total** deterministic source actions `T_a`, and `O:X->Y` the present available observations. An action on the observed object exists (a well-defined `\bar T_a:O(X)->O(X)` with `O T_a=\bar T_a O`) **if and only if** the kernel relation of O is preserved by `T_a`. This is elementary factorization/descent and is not supplied by a visually commuting endpoint diagram.

The hidden diamond with g=0 and g=7 has identical baseline O=Lambda, but the same L-u contact produces 7/6 and 49/41. Therefore no deterministic action `\bar T_contact` exists on baseline Lambda **alone**. This is a *typed counterexample to naturality*, not merely an observation-limited distinction.

The right repair is the **future-safe equivalence**

\[
 x\equiv_\infty y\Longleftrightarrow \forall w\in A^*,\ O(T_w x)=O(T_w y).
\]

It is the largest right congruence refining O equality; standard finite Moore partition refinement constructs it in at most `|X|-1` strict refinement rounds. For a four-state before/after contact model, O initially aliases the two initial bridge states and a single action separates them; one refinement round produces four distinct classes. A separate two-state fully invisible swap remains one observable equivalence class forever: **no authorized probe splits it**. This shows contextual saturation of one toolkit, not ontological equality.

On this quotient the observed action genuinely commutes; that gives a *minimal source-equivalent observable dynamics* under the declared actions, **not the unique hidden microgeometry**. `J` is another, sufficient but not generally minimal, realization of the same general principle. A source-honest geometry theorem must distinguish 'source quotient uniquely recovered' from 'all internal edges physically recovered'.

## 8. Cross-model triangulation: why several complete objects are not automatically ONE reality

The exact source program now has three independently developed mathematical model families:

1. **Electrical:** fixed-port DtN/Kron model. One calibrated L-u contact identifies `g` within the symmetric diamond family.
2. **Arithmetic ring:** #238's `Z/4Z` and `F_2[t]/(t²)` have identical first-level p=2 fingerprints but distinct multiply-by-2 image sizes (2 vs 1) on four elements. Its higher-level calibrated source action is required to choose.
3. **Two-clock coupling:** #238's Haar-marginal diagonal-SUCC couplings are classified by `w(y-x)`; uniform-independent and phase-locked sources have identical one-copy marginals, but `P(X=Y)=1/4` versus 1 on four phases.

An exact 2×2×2 product candidate family has eight survivors after its three separate **calibration-only** reports. Three independently assigned holdouts (contact C=49/41, multiply-by-2 image count 2, coincidence probability 1) reduce this *product family* to `(g=7, Z/4, locked coupling)` in the exact synthetic test. **This does not establish a physical arrow from resistor edge histories to arithmetic prime clocks.** Arbitrarily pairing three unrelated models is an epistemically worthless 'unification'.

A genuine cross-model naturality claim needs a shared physical source S with independently identified maps to both model action categories, a label-preserving comparison of **ordered histories**, and measured cross-channel correlations or transfer laws not chosen from a diagram. Source priors/gauges/clock origins must be recorded. The decisive next probe is a *cross-observable* that could refute such an arrow—rather than a fourth independently fitted marginal statistic.

## 9. Exact adversarial validation matrix / scope

- `tests/test_boundary_port_geometry.py` checks every one-edge update against a second RCNetwork implementation; 24 complete 4-edge orderings and every intermediate frame; repeated edges; exact forward/backward reconstruction with logged events; port orientation gauge; 16 positive `(a,g)` inverse examples and invalid negative/zero/float controls; four-corner source descent and future-safe refinements; prime-ring and phase-coupling cross-object ablations.
- `scripts/boundary_port_geometry_probe.py --check` checks the current Git-blob identities for the implementation/tests and the frozen exact rational receipt, plus complete exact replay. No arbitrary source strings, numerical float signs, or zeta zeros serve as numerical oracles.
- Commuting frame squares are exact **because detailed source ports are retained**. Field-dependent conductivity, time retardation, material damage, growth statistics, unknown physical graph, and non-wired place/multiplication maps are outside the proof domain.
- No experiment, high voltage, Cherenkov spectrum, spacetime metric, p-adic physical field, gravity, RH or signed completed Weil positivity is established by these results.

### Existing background and priority restraint

Dörfler and Bullo, *Kron Reduction of Graphs With Applications to Electrical Networks*, IEEE TCAS I 60(1), 2013, doi:10.1109/TCSI.2012.2215780: https://ieeexplore.ieee.org/document/6316101/ . Borcea, Druskin, Guevara Vasquez and Mamonov, *Resistor network approaches to electrical impedance tomography*, 2011: https://arxiv.org/abs/1107.0343 . Their classical reduction and inverse-data context must be credited; **no academic priority is claimed for Sherman–Morrison updates, Woodbury closure, minimal deterministic automata, or the elementary finite examples**. The cross-model SUCC research question is an application agenda and remains empirically unverified.

### Next verdict-changing probe

Recover enough of `J=(Lambda,W,R)` from independent **actual** current/voltage records and independently calibrated interventions *without supplying the full interior graph to the estimator*. Use a fresh source geometry not fitted to the diamond and hold out an edge sequence to test prediction (including the cubic hidden-mode signal). In parallel require a source-authenticated cross-channel event that selects one arithmetic/geometric model without building that selection into the apparatus. A synthetic pass cannot satisfy either physical requirement.
