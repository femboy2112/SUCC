# Cambrian F: closure, hidden memory, physics and proof authority

**Base:** `5eb09e7cba36ec01b8f9d6834b78b5766fd93935`. **Assignments actually executed:** 31--36, by one worker in an isolated worktree, rather than six claimed independent reasoners. **Domain:** declared mathematical carriers, exact rational controls, and paper proofs. **Status:** classical mathematics / PROVED LOCAL paper derivations / TESTED MODEL implementations. No empirical cognition, measured physical source, Navier--Stokes regularity result, RH proof, quantum speedup, or established priority claim.

## Independence, provenance and the load-bearing distinction

The worker's initial hypotheses were sent to the coordinator before receiving any other worker findings: autonomous quotient closure is fiber constancy; hidden linear elimination yields memory plus an initial-state forcing term; unrestricted hidden initial states and zero hidden initial states have different closure criteria. The first 28 exact tests ran before the coordinator supplied its stochastic joint-instrument criterion. That subsequent comparison is explicitly cross-pollination, not independent corroboration. All workers use the same model family.

Read inputs: `AGENTS.md`, foundations/method/architecture/roadmap, relevant ledger entries, source-driven dynamic-boundary and Galilean/Lorentz dossiers, and the uploaded campaign. Frozen import manifest records origin `femboy2112/FuckingRH`, commit `ba075348b7bcc66d938b3e0ca96c26e95bba340a`. The imported rational `quantum_records.py` is used without modification; its archive remains unchanged. Matrix arithmetic comes from the existing `dynamic_boundary_inverse.py`, whose RC laws and inverse-network ontology obstruction were inspected. No imported result is rewritten here.

The decisive common distinction is:

1. **failed quotient:** one present report hides states with different future behavior;
2. **law-level repair:** preserve an initial-state term, memory kernel, policy state or genuinely new probe, under a declared source law;
3. **physical source identity:** even an exact repaired boundary law can leave multiple physical interiors indistinguishable.

The arrows between these levels require proofs. Agreement of a simulator with its own construction cannot authenticate a physical origin.

## F0. Autonomous closure is exactly a descent obligation

Let $S,Y$ be sets, $q:S\twoheadrightarrow Y$, and $F_a:S\to S$ a total deterministic transition for each $a\in A$, with the same action availability on all source states. Then there is a unique family $\bar F_a:Y\to Y$ satisfying

$$
qF_a=\bar F_aq \quad\text{for every }a
$$

**iff**

$$
q(s)=q(t)\Longrightarrow q(F_a(s))=q(F_a(t))
\quad(\forall s,t\in S,\;\forall a\in A).
$$

**Proof:** necessity follows by applying $\bar F_a$ to equal images. For sufficiency define $\bar F_a(y)=q(F_a(s))$ for any preimage $s$; fiber constancy makes this well-defined. Surjectivity proves uniqueness. Induction gives equality on every finite action word. If admissibility varies by source state, equality of enabled menus on fibers is an additional requirement; no availability conclusion follows from output constancy alone.

For a finite-dimensional smooth ODE $\dot s=f(s,u)$, a linear surjection $P:S\to Y$, and unique local source/reduced solutions, the analogous autonomous law $\dot y=\bar f(y,u)$ exists exactly when

$$
Ps=Pt\Longrightarrow Pf(s,u)=Pf(t,u)\quad(\forall s,t,u).
$$

Sufficiency defines the reduced vector field as above, and projected trajectories satisfy it by the chain rule. A linear right inverse of $P$ gives smoothness of $\bar f$; necessity follows from derivatives at time zero for arbitrary initial states. This is a general vector-field theorem, not a claim that arbitrary PDE state spaces meet the finite-dimensional regularity hypotheses. The fluid obstruction below needs only smooth initial data and their instantaneous vector field.

**Quantifier boundary:** no test over finitely sampled states proves fiber constancy on an infinite density/state space. `finite_closure_obstruction` is exhaustive only over its explicitly supplied finite carrier table.

## F32. Exact hidden-state elimination and a sharp finite memory criterion

**Question:** for every rational block-linear source, all resolved initial states and all input sequences, when can eliminating hidden state preserve a memoryless law? **Positive hypothesis:** retaining the exact causal memory repairs elimination. **Rival:** the instantaneous resolved state alone always suffices after elimination. **Probe:** two hidden initial conditions with the same resolved state; independently replay a full block matrix against the eliminated recurrence, and mutate a relaxation rate on fresh inputs.

Let $x\in\mathbb R^r,z\in\mathbb R^h,u\in\mathbb R^m$, with $r,h,m\ge1$. Discrete dynamics are

$$
x_{n+1}=Ax_n+Bz_n+Eu_n,\qquad
z_{n+1}=Cx_n+Dz_n+Hu_n.
$$

### F32a. Elimination theorem (CLASSICAL / PROVED LOCAL)

For every finite $n\ge0$, every initial state and every input prefix,

$$
\boxed{x_{n+1}=Ax_n+Eu_n+BD^nz_0+
\sum_{j=0}^{n-1}BD^{n-1-j}(Cx_j+Hu_j).}
$$

**Proof:** induction on $n$ gives
$z_n=D^nz_0+\sum_{j<n}D^{n-1-j}(Cx_j+Hu_j)$; substitute into the source equation. The term $BD^nz_0$ is essential. Calling the convolution alone a complete reduced law when hidden initial state is unspecified is false.

For continuous finite-dimensional LTI dynamics with the same blocks, variation of constants gives the exact counterpart

$$
\boxed{\dot x(t)=Ax(t)+Eu(t)+Be^{Dt}z_0+
\int_0^t Be^{D(t-s)}\{Cx(s)+Hu(s)\}\,ds.}
$$

This is a linear special case of the classical Mori--Zwanzig memory formalism, not a new universal closure of nonlinear fluids. Every source evolution/history remains accounted for.

### F32b. Two different closure theorems (PROVED LOCAL)

**Unrestricted hidden initial domain:** an autonomous projected law over **every** $x_0,z_0,u$ exists iff $B=0$. Same $x,u$ and arbitrary $z,z'$ give a projected successor/derivative difference (B(z-z')), proving necessity by F0. Sufficiency is the source formula.

**Zero hidden initial domain:** with the explicit restriction $z_0=0$, the resolved recurrence $x_{n+1}=Ax_n+Eu_n$ is valid for **every** $x_0$ and **every** input sequence iff

$$
\boxed{BD^kC=0,\qquad BD^kH=0\qquad(0\le k<h).}
$$

**Sufficiency:** Cayley--Hamilton expresses $D^h$ as a linear combination of $I,D,\ldots,D^{h-1}$, so the stated identities imply them for every $k\ge0$. The memory sum vanishes.

**Necessity:** any memoryless law valid at $n=0$ for every $x_0,u_0$ must equal $Ax+Eu$. Set every input to zero. If $k$ is the first nonzero coefficient $BD^kC$, the memory discrepancy at $n=k+1$ is exactly $BD^kCx_0$, since all earlier coefficients vanish. Choose an $x_0$ on which that matrix is nonzero; contradiction. Thus all $C$-coefficients vanish. Now set $x_0=0$, use arbitrary $u_0$, and zero later inputs. The same first-coefficient argument proves every $BD^kH=0$. It is enough to test $k<h$ by Cayley--Hamilton.

For continuous kernels, $Be^{Dt}C\equiv0$ and $Be^{Dt}H\equiv0$ iff the same finite coefficient conditions hold: derivatives at zero give necessity and the exponential power series plus Cayley--Hamilton gives sufficiency. With arbitrary resolved initial states and smooth inputs, the first nonzero Taylor coefficient gives the analogous contradiction to the memoryless resolved law. This continuous statement is a paper proof; the executable implementation evaluates only discrete successors.

**Sharpness:** let $D$ be the $h\times h$ nilpotent upper shift, $B=e_1^T,C=e_h,H=0,A=E=0$. Then $BD^kC=0$ for $k<h-1$ and $BD^{h-1}C=1$. A test checking only $h-1$ coefficients would accept a false closure; the first nonzero effect occurs in $x_{h+1}$. Controls run at $h=1,2,3,4,7$.

**A separate initialization countermodel:** $C=H=0,B=1$ has zero convolution kernel and perfectly memoryless zero-initial behavior, yet arbitrary $z_0$ changes the next resolved state. A no-memory certificate must carry its initialization domain.

**Known dimension is a load-bearing source assumption.** If no finite upper bound on $h$ is supplied, no finite initial segment of zero kernel coefficients proves that all future coefficients vanish over the class of finite linear systems. For any measured length $M\ge1$, the nilpotent construction with $h=M+1$ agrees with the zero kernel at $k=0,\ldots,M-1$, then has $K_M=1$. Both are finite rational systems. Thus the finite certificate above comes from a structural dimension bound plus Cayley--Hamilton, not from a long all-clear record. This is an exact bridge to F35's single-hole query obstruction, with a different realization and a precise repair: a justified hidden-dimension bound.

### F32c. Memory realization is weaker than physical identity

For a scalar kernel $K_k=BD^kC$, the finite Hankel matrix $[K_{i+j}]$ factors as observability times reachability matrices, so its rank is a lower bound on any linear hidden realization of that kernel. This is a kernel-interface statement: it does not count actual physical vertices, nor does it assume the endogenous resolved $x$ is an independent laboratory input.

One hidden mode $B=C=1,D=1/2$ and two hidden modes
$B=(1/2,1/2),C=(1,1)^T,D=(1/2)I_2$
have $K_k=2^{-k}$ for every $k$. With shared $A,E$, $z_0=0$, they therefore have the same resolved trajectory for **all** initial $x_0$ and **all** finite or infinite input sequences, by the elimination theorem and induction. Their hidden dimensions differ. The second mode's antisymmetric component is invisible. An exact boundary record cannot choose the interior ontology within this interface; a newly admitted internal intervention/probe is needed.

Two distinct rates $D=\operatorname{diag}(1/2,1/3),B=(1,1),C=(1,1)^T$ instead give
$K_0=2,K_1=5/6,K_2=13/36$, with Hankel determinant $1/36>0$. This separates two **observable** memory dimensions from the one-rate rival. The existing RC star/twin-hub identity is the passive electrical realization of the same distinction; its positive conductance/storage conditions remain separate physical-law assumptions.

**Independent routes:** (i) algebraic induction, (ii) 32 frozen-seed rational block systems with an independently assembled unpartitioned block-power oracle, (iii) explicit sharp-delay and hidden-initial countermodels. Fresh 19-step rational input sequence tests the same-boundary/different-interior pair. A changed $D=3/5$ fails a fresh input against $D=1/2$. No floating sign or approximate trajectory is treated as a proof.

## F31. Quantum instruments are stronger than current outcome laws

**Typed question:** for every finite-dimensional density matrix, does equality of the current POVM imply equality of all future observation laws? **Positive hypothesis:** the full instrument, with outcome and posterior state, supports causal composition. **Rival:** matching current outcomes is sufficient. **Probe:** compare a Lüders Z instrument and a reset Z instrument, then measure Z again.

Let
$P_0=|0\rangle\langle0|,P_1=|1\rangle\langle1|$.
The Lüders Kraus operators are $P_0,P_1$; the reset instrument uses $P_0,|0\rangle\langle1|$. Both satisfy $\sum K_o^\dagger K_o=I$, and both POVMs are exactly $\{P_0,P_1\}$. Thus for **every** density matrix their first-outcome laws agree. For input $|1\rangle\langle1|$, the first reported outcome is 1 with probability one in both cases. The Lüders posterior is $|1\rangle\langle1|$; the reset posterior is $|0\rangle\langle0|$. A second Z measurement returns 1 versus 0 with probability one. The outcome-only semantic quotient fails causal closure.

For any positive trace-preserving map $\Phi$, trace distinguishability contracts on Hermitian differences: writing $X=X_+-X_-$, positivity and the triangle inequality imply
$\|\Phi(X)\|_1\le\operatorname{tr}\Phi(X_+)+\operatorname{tr}\Phi(X_-)=\|X\|_1$.
Every CPTP map meets these hypotheses. Finite classical readouts are the corresponding total-variation case. These are classical data-processing theorems, not mathematical truth probabilities.

**A dangerous rival killed:** a normalized **conditioned** branch need not obey unconditional trace contraction. The exact two-Kraus filter
$K_0=\operatorname{diag}(1,3/5),K_1=\operatorname{diag}(0,4/5)$
is complete. Condition outcome 0 for states $\rho=\operatorname{diag}(0,1)$ and $\sigma=\operatorname{diag}(1/10,9/10)$. Their original trace distance is $1/10$; conditioned distance is $25/106>1/10$. No contradiction: normalization is state-dependent and the conditioned map is not trace preserving. Outcome likelihoods must accompany conditional evidence.

The coordinator's independently frozen finite stochastic theorem later supplied a compatible interface: joint report-and-receipt rows must be constant on coarse source fibers to transport all-prior evidence and filtered posterior. Here the quantum state space is not finite. Applying its finite enumeration to all densities would be invalid; the all-density POVM equality above is an algebraic proof, and the future counterexample is exact. A genuine reduced quantum channel additionally needs positivity/complete positivity on the declared reduced state space, not merely an algebraic fiber map.

## F33. Null evidence reconstructs conformal geometry; constraints select modes

**Typed question:** for a nondegenerate real Lorentz form $g$ on $\mathbb R^{d+1}$, which metric information is determined by exact null directions? **Positive hypothesis:** null observations determine a conformal class in a declared coordinate basis. **Rival:** they identify absolute metric scale or unique physical ontology. **Probe:** finite rational null constraints against a positive scaled metric, then a timelike clock normalization.

Put $g(v,v)=-t^2+\sum_i x_i^2$. Suppose a symmetric form $h$ vanishes on the same null vectors. Evaluate $h$ on $(1,\pm e_i)$: subtraction gives $h_{0i}=0$, and addition gives $h_{ii}=-h_{00}$. For $i<j$, evaluate at $(1,(3/5)e_i+(4/5)e_j)$. Diagonal terms cancel, leaving $(24/25)h_{ij}=0$. Therefore $h=cg$. Nondegeneracy requires $c\ne0$; declared compatible timelike sign requires $c>0$. Conversely a positive scalar multiple has exactly the same null cone. These finitely many rational rays provide a sufficient algebraic constraint set, **given the coordinates and exact source-defined null status**. Missing or uncalibrated rays need not.

In 3+1 dimensions the symmetric form has 10 coordinates and these nine constraints have rank 9. Code checks the analogous rank in 1+1,2+1,3+1,5+1. A timelike squared-length observation at $v=(1,0,0,0)$ gives $-1$ versus $-4$ for $g$ and $4g$, exposing a scale if that clock normalization is independently available. Null rays alone cannot do it. On a manifold, converting observation sets to conformal coordinates requires global causality/access conditions; this dossier does not invent those conditions or prove a general boundary-rigidity theorem. The primary Lorentzian inverse-problem reference states such additional hypotheses explicitly.

**Maxwell type control:** for nonzero spatial covector $\xi$, let $C_\xi v=\xi\times v$. The real frequency symbol is
$S=\left(\begin{smallmatrix}0&c^2C_\xi\\-C_\xi&0\end{smallmatrix}\right)$, so
$S^2=c^2\operatorname{diag}(|\xi|^2I-\xi\xi^T,|\xi|^2I-\xi\xi^T)$.
The longitudinal pairs $(\xi,0),(0,\xi)$ are zero modes of this evolution symbol, but violate the Maxwell source constraints $\xi\cdot E=\xi\cdot B=0$. Transverse modes satisfy $S^2=c^2|\xi|^2I$. Treating the unconstrained six-component symbol as entirely physical creates spurious characteristic modes. The exact control uses $\xi=(2,3,6),c=2$, transverse multiplier 196. This is the constant-coefficient linear Maxwell model; no empirical medium or curved spacetime is reconstructed.

## F34. A genuine incompressible filtered-fluid closure obstruction

**Typed question:** on the periodic 2D torus, can a deterministic instantaneous closure depending only on low Fourier velocity $U=Pu$ reproduce the projected Navier--Stokes vector field for every smooth divergence-free initial state? **Positive hypothesis:** closure requires information sufficient for the nonlinear stress (or its history/hidden realization). **Rival:** discarded velocity modes have no relevant projected effect when $Pu=0$. **Probe:** high--high interactions whose difference is an admitted low mode, including the Leray projection so a pressure gradient cannot fake the obstruction.

Let $P$ be the spectral projection to $|k|\le1$; it commutes with time/spatial derivatives and the Fourier Leray projector $\Pi$. For smooth incompressible solutions,

$$
\partial_tU+\Pi\nabla\cdot(U\otimes U)=\nu\Delta U+\Pi Pf-\Pi\nabla\cdot\tau,
\qquad\tau=P(u\otimes u)-U\otimes U.
$$

This exact identity follows by applying $P$ to the source equation; no closure of $\tau$ has yet been supplied. For a general filter, idempotency/commutation must be checked instead of assumed. Even with a spectral projection, $P(w\otimes w)$ can be nonzero when $Pw=0$.

For every integer $N\ge2$, put

$$
w_N=(0,1)\cos(Nx)+(1,-N)\cos(Nx+y),\quad
k=(N,0),\;\ell=(N,1).
$$

Each amplitude is perpendicular to its mode, so $\nabla\cdot w_N=0$, and both modes lie outside the cutoff, so $Pw_N=0$. The cross-advection term at $q=\ell-k=(0,1)$ has sine coefficient

$$
-\tfrac12(a\cdot\ell)b+\tfrac12(b\cdot k)a=(-1/2,N).
$$

Leray projection at the vertical $q$ removes its second coordinate, leaving

$$
\boxed{\Pi P\nabla\cdot(w_N\otimes w_N)=(-1/2,0)\sin y\ne0.}
$$

Compare initial states $u=0$ and $u=w_N$ with identical force and viscosity. Both have $U=0$, but their resolved derivatives differ by $(1/2,0)\sin y$. Hence **no single instantaneous deterministic function of $U$** reproduces both source derivatives. This is a direct F0 fiber-constancy failure at smooth initial states, even after enforcing incompressibility and removing pressure. It refutes a universal exact closure on this interface, not approximate/statistical closures on a restricted source distribution.

The trigonometric derivation is independently checked using exact Fourier convolution with the derivative's imaginary unit tracked symbolically. Heldout $N=4,11,23$ were not used to select the formula; original controls also run $N=2,3,7,13,101$. The zero field is a negative/null control. No finite-dimensional universal fluid memory kernel is inferred; nonlinear hidden dynamics need their own source law and can require unbounded representation. Finite Galerkin systems satisfy finite ODE versions of F0 but do not automatically prove a continuum theorem. This establishes no 3D regularity or existence result.

## F35. Finite-query darkness, effective search and finitary proof are different

**Typed question:** for every deterministic algorithm accessing a Boolean sequence solely through point queries and stopping after finitely many answers, can it soundly certify $\forall n\,b(n)=1$ over the class of all computable Boolean sequences? **Positive hypothesis:** extra structural proof authority can certify universal claims, whereas finite black-box data alone cannot. **Rival:** a long all-clear transcript or ideal $\omega$ record authorizes the same finite proof.

**Finite-query theorem:** on the all-one sequence, let the stopping transcript query finite $Q\subset\mathbb N$. Choose $j\notin Q$, and define the computable rival $b_j(n)=0$ iff $n=j$, otherwise 1. Every observed answer is identical; induction on the adaptive policy gives exactly the same query and stopping transcript. Yet the universal statement differs. Therefore no such sound finite black-box certifier can accept the all-one sequence. The implementation constructs the single-hole rival after freezing the query transcript; it is not a source-generating oracle masquerading as a discovered source.

The obstruction is **interface information**, not a proof that any particular arithmetical sentence is undecidable/unprovable. An explicit source formula such as $b(n)=1$ for all $n$, or a finitely proved inequality $n^2\ge0$, changes the authority/interface and admits a structural proof. Providing a program's syntax supplies information unavailable in the point-query model; the uniform halting problem still has its separate computability theorem.

For an increasing family of first-order axiom sets $T_n$, any finite derivation from $\bigcup_nT_n$ uses finitely many axioms; choosing the maximum stage of their first appearances gives $\exists N:T_N\vdash\varphi$. The converse is immediate. No ideal union adds a new **finitary** proof if no finite stage already supports it. This elementary theorem depends on monotone theory extension; destructive source updates need epoch-tagged proof support instead.

For effectively enumerated axioms and a finitary effective deduction system, dovetailing finite axiom-enumeration stages and proof lengths semidecides derivability. It supplies no termination guarantee for an unprovable claim and no soundness beyond the chosen axioms. A consistency/reflection axiom changes logical authority; it is not another observed event. Gödel second-incompleteness conclusions need their arithmetic representability/derivability and consistency hypotheses. This campaign does not mechanize those hypotheses or infer RH/NS independence. The actual $\omega$-rule and physical infinite elapsed computation are not implemented.

**Probe:** a frozen adaptive 29-query all-one transcript and a 1024-element prefix both admit computable single-hole rivals. **Independent verification:** the adaptive-transcript induction and exact query set replay. A structural algebraic proof is an explicit positive control with stronger authority. Remaining access gap: no PA representability/reflection formalization is supplied by this assignment; it remains outside this implementation rather than falsely counted as checked.

## F36. A typed phenomenological/TLICA interface without empirical promotion

**Question:** in a declared finite attention-policy model, does the current belief representation determine all future source probes/model revisions? **Positive hypothesis:** include attention/policy state in a causally sufficient model. **Rival:** equal present belief entails equal future update. **Probe:** same belief, different protection state, identical lawful source and available sensor; release the policy latch and perform the next source probe.

Carrier state is $(b,r)\in\{0,1\}^2$, with belief $b$, declared protection latch $r$, and a fixed source bit $s$. A reveal probe is physically available throughout. The modeled `attend` action chooses a source-independent neutral report when $r=1$, preserving belief, and chooses reveal when $r=0$, assigning $b:=s$. The `release` intervention sets $r:=0$ and creates **no** observed source fact by itself. For $s=1$, states ((0,0),(0,1)\) have equal belief, but next beliefs are 1 and 0. The belief-only quotient fails F0; retaining the full finite policy state is an exact repair. The protected policy remains observationally blind on both source bits even though its source map is correct and reveal is available.

| User vocabulary | Declared mathematical object here | Separate obligation |
|---|---|---|
| $\kappa$, contact | Access to the declared source/instrument relation | Actual source authenticity is not established by a simulator |
| $\phi$, toolkit indistinguishability/pathway | Equivalence of source bits under the chosen neutral-only policy; reveal separates them | Equality relative to one policy is weaker than equality under every lawful probe |
| $\sigma$, source-map adequacy | Correct specified neutral/reveal outcome maps | A correct map can coexist with a policy that never uses the discriminating probe |
| $\rho$, commitment coupling | The explicitly chosen policy latch $r$ | It is a toy parameter, not measured human commitment or evidence for truth |
| $\mu$, probe availability | Reveal belongs to the lawful probe menu | Availability does not imply actual selection |
| $\mathrm{Cl}(Tools)$ | Closure of finite policy/action words | State-changing interventions require the enlarged state and source epoch |

No scalar truth score is formed. `release` and `reveal` are differently typed operations; intervention cannot be promoted to observation. This provides falsifiable consequences **within the toy model**: two same-belief policies give different next updates; release opens a source-revealing path; changing the sensor law can kill that prediction. It does not validate the user's phenomenological vocabulary empirically. Current external `TLICA.git` definitions were not independently retrieved in this assignment; alignment is limited to the supplied user vocabulary and SUCC state/interface discipline. Empirical/neuroscientific identification remains an explicit source/measurement gap.

## Reproduction and the next boundary

Files are confined to the `cambrian_f_*` code/test/script namespace plus this dossier and its result receipt. Shared ledger, README, CI, architecture, roadmap and archives are unchanged.

```sh
python -m unittest discover -s tests -p 'test_cambrian_f_*.py' -v
python scripts/cambrian_f_probe.py --check
python scripts/verify_provenance.py
```

The scoped test execution passed **28 tests**, including exact positive, negative, null and mutation controls. The complete baseline-plus-F Python suite passed **1,630 tests**; provenance and both mandated foundation/ordinal probes passed. Following a small input-iterable freeze and unused-import cleanup in the new module, the 28 scoped tests were rerun and passed; the coordinator should run the complete integrated head. None of these local results is a GitHub CI assertion. All universal results above are **paper proofs**, not newly Lean-checked statements. Finite tests verify implementations and expose countermodels; they do not upgrade sampled behavior to a theorem. Academic priority has not been surveyed exhaustively: the major closure, linear-memory, data-processing, metric-scale and proof-boundary mathematics is classical. The project contribution is a source/init/interface-explicit common closure discipline with cross-domain countermodels and executable repairs.

The highest-value next probe is to enrich the allowed intervention algebra and test whether a memory-equivalent pair remains equivalent after a **source-preserving, physically justified** intervention. This separates a behavioral law from true source identification more sharply than adding more passive boundary samples. A nonlinear closure claim should first pass the smooth high--high fluid obstruction and specify its source class, initialization distribution, hidden-state/history dependence and test-function domain.

## Fresh primary references and retrieval scope

Retrieved 2026-10-13; no source PDF is redistributed. These references establish classical context; the exact countermodels and proofs above are independently derived here.

- John Watrous, *The Theory of Quantum Information*, author-hosted chapters 2 (instrument definition and classical-record channel, pp. 112--113) and 3 (positive trace-preserving trace-norm contraction, Corollary 3.40): https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf ; https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf . Exact matching definitions/pages were retrieved, not merely a search snippet.
- Eric J. Parish and Karthik Duraisamy, *Non-Markovian closure models for large eddy simulations using the Mori--Zwanzig formalism*, Phys. Rev. Fluids 2, 014604 (2017): https://doi.org/10.1103/PhysRevFluids.2.014604 ; authors' preprint https://arxiv.org/abs/1611.03311 . The retrieved abstract explicitly describes finite-memory approximation, not a general exact instantaneous fluid closure.
- Eric J. Parish and Karthik Duraisamy, *A Dynamic Subgrid Scale Model for Large Eddy Simulations Based on the Mori--Zwanzig Formalism*: https://arxiv.org/abs/1611.02143 . Retrieved author preprint abstract; not used as proof of the exact toy triad.
- Yaroslav Kurylev, Matti Lassas and Gunther Uhlmann, *Inverse problems for Lorentzian manifolds and non-linear hyperbolic equations*: https://arxiv.org/abs/1405.3386 . The retrieved source identifies a conformal reconstruction under stated causality/observation assumptions; it does not authorize universal metric/ontology identification.
- Kurt Gödel, original 1931 paper: https://doi.org/10.1007/BF01700692 . Primary bibliographic source retrieved; no claim that this campaign rechecked the original metaarithmetic proof.
- A. M. Turing, original 1936 paper, university-hosted scan: https://www.astro.puc.cl/~rparra/tools/PAPERS/turing_1936.pdf . Scan opened; text extraction returned no text. Used for primary-source provenance of the classical computability boundary, not claimed as an executed proof checker.
