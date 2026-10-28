# Seinfeld SUCC: source-selected coherence groups, arithmetic path sums, and checkpoint memory

**2026-10-26 — additive research, source-typed continuation of draft PR #313.** Starts from the exact branch/energy and carry-spill results at `79344c62c39c96755b742700b3d4d22fa60d86da`. Original four-pole forcing and original zero state remain unchanged. This is an application of classical finite conditional expectation, finite stochastic lumpability, Fourier characters and relative-entropy disintegration. Not a novel physics path-integral theorem, no source-conditioned signed cancellation theorem and **π base-16 normality remains OPEN**.

## Steelman of the new intuition

Instead of treating the `16^N` possible inverse histories as fundamentally irreducible, group them into **coherence classes** preserving selected observables and their possible future transitions. On each class, sum the *complex phase amplitudes* before producing the working result. Retain a fixed global reference law, a changing working law and a well-ordered record of likelihood/carry/source updates. A realized path changes mathematical knowledge (conditioning); a model with genuine feedback can also change the transition law (reinforcement). These two interpretations are **not** identified.

This addresses the question in recent SUCC discussions: what information does uniform inverse averaging erase, and how can it be retained without promoting a fake mixing theorem? Physically, Feynman's path-integral program already sums/group contributions and uses stationary-phase constructions; this is a **source-typed arithmetic analogue**, not a claim of discovering a superior version of quantum mechanics.

## 1. Exact coherence-group path sum (finite, classical)

Let `Ω_N` be any finite path space, `μ` a strictly positive reference probability law, `ν` a declared working/selected law with `ν≪μ`, and `κ:Ω_N→G_N` a finite coarse graining. Set `L=dν/dμ` and let `F_h(ω)=exp(i S_h(ω))` be any modulus-one character/phase. Exact disintegration gives

$$
\boxed{\mathbb E_\nu F_h=\sum_{g\in G_N}\mu(\kappa^{-1}(g))\,\mathbb E_\mu[L F_h\mid\kappa=g]=\sum_g\nu(g)\,\mathbb E_\nu[F_h\mid g].}
$$

Define the source-labelled **class amplitude** `A(g;h)=E_μ[1_{κ=g}LF_h]`. Then `Z(h)=∑_g A(g;h)` is exact. There is no approximation and no generic cancellation. Replacing `A` by positive masses `ν(g)` discards the signed phase and is **not** an authorized pushforward for the signed observable. A quotient can preserve an observable's current value yet fail to transport the future dynamics.

The new `grouped_phase_amplitudes` implementation performs this pushforward
using an **exact 16-coordinate rational formal group-algebra vector** for each
class. At the h=8 parity character, explicit cyclotomic evaluation is exactly
`parity_evaluate_amplitude`, demonstrating a uniform field's opposite signed
class amplitudes (+1/2,-1/2) versus a single selected zero-digit class
amplitude (+1,0). **A nonzero formal group-algebra vector is not an evaluated
nonzero cyclotomic character**: reduction by the root-of-unity polynomial is
a separate typed operation, as enforced by native SUCC's `Cyclo16`.

The finite relative-entropy chain rule is

$$
\boxed{D(\nu\|\mu)=D(\kappa_*\nu\|\kappa_*\mu)+\mathbb E_{g\sim\kappa_*\nu}D\bigl(\nu(\cdot|g)\|\mu(\cdot|g)\bigr).}
$$

This quantifies *exactly* what information is retained by the groups versus hidden inside the groups. For uniform `μ` on 16^N paths, selected `ν=δ_{ω*}`, and grouping by the first `t` digits:

$$\boxed{N\log16=t\log16+(N-t)\log16.}$$

The group's reference mass is `16^{-t}` and its conditional reference fiber has `16^{N-t}` elements. Selection is **not** equivalent to averaging this latter fiber: the conditional posterior is a point mass. On the uniform path reference the chosen-history likelihood has second moment `16^N`. Grouping alone does not cancel this information cost; it records where it is held. Both log bases are computed as *exact integers* in the implementation, without numerical log claims.

## 2. Source-specific phase-sufficient groups

For one hexadecimal branch digit `j∈C_16` and character `χ_h(j)=exp(2πihj/16)`, the exact equivalence relation is

$$\boxed{j\sim_h k\iff h(j-k)\equiv0\pmod{16}\iff j\equiv k\pmod{d_h},\quad d_h=16/\gcd(16,h).}$$

The minimal group labels for frequencies `h=1,2,4,8,16` have respectively `16,8,4,2,1` classes. Every claim of observational equivalence must specify the **frequency family**: parity is sufficient for `h=8` but not for the quarter-turn `h=4`; `j=0` and `j=2` have the same parity and opposite `χ_4` phase. The code verifies minimality by exact integer congruences, not approximate complex roots.

**Important:** a phase-sufficient grouping is not automatically a **dynamically sufficient** grouping. A finite stochastic transition `K` induces an exact quotient on `κ` iff the probability of entering each target group depends only on the current group, not on the hidden state. This is classical *strong lumpability*: for all `x~x'` and all target classes `g'`,

$$\sum_{y:\kappa(y)=g'}K(x,y)=\sum_{y:\kappa(y)=g'}K(x',y).$$

The native exact rational `quotient_transition` either constructs the quotient or returns an explicit state/row counterexample. For a deterministic arithmetic successor, replace the row sums by `κ(Tx)=κ(Tx')`. If this fails, enlarging the checkpoint state (e.g. retained remainder, actual carry, Gaussian signed holonomy, time/source index) is required. An elegant quotient that erases such source state is not a source-authentic explanation.

## 3. Checkpoint Fourier energy (global / working / information gained)

Take a fixed reference measure `μ` and increasing memory sigma fields `F_0⊂F_1⊂⋯⊂F_N`. For a final square-integrable observable `F`, define its *reference-backpropagated* working evaluation `M_t=E_μ[F|F_t]`. By the standard conditional-expectation orthogonal projection theorem,

$$\boxed{E_\mu|M_t|^2-E_\mu|M_{t-1}|^2=E_\mu|M_t-M_{t-1}|^2\ge0.}$$

This is **increasing accessible Fourier energy on a fixed reference**. It does not say the Fourier energy of a dynamically changing physical/working probability law must increase or decrease. Nor does it give cancellation along a selected deterministic history.

Example: under iid uniform 16-digit reference let `F=(1/N)∑_{k=1}^Nχ_h(J_k)` for `16∤h`. Under the checkpoint that reveals the first `t` digits, `M_t=(1/N)∑_{k≤t}χ_h(J_k)` and

$$\boxed{E_\mu|M_t|^2=\frac{t}{N^2},\quad E_\mu|M_t-M_{t-1}|^2=\frac1{N^2}.}$$

Yet one selected history with all `J_k=0` has `M_t(ω*)=t/N` and final amplitude **one**, despite `E_μ F=0` and `E_μ|F|²=1/N`. The exact reference mean says nothing about that selected history without a theorem authenticating its typicality.

For *actual* empirical selected branch digit `J` and a coarse remainder-bin observation `B`, distinguish

$$E_{\rm global}(8)=|\mathbb E\chi_8(J)|^2,\qquad E_{\rm working,B}(8)=\mathbb E\left|\mathbb E[\chi_8(J)\mid B]\right|^2.$$

Then

$$\boxed{E_{\rm working,B}(8)-E_{\rm global}(8)=\operatorname{Var}(\mathbb E[\chi_8(J)\mid B])\ge0.}$$

Both are computed from the *same actual rational source history*, using `lambda_source_duality.branch_defect` when the authenticated adapter is invoked. As bins refine, positive conditional energy can go **up**, all the way to one (#313); this is measurement information, not progress toward digit mixing. A simple two-bin example gives global energy zero, working energy one—without any arithmetic normality result.

## 4. Realization as read, and realization as write: a finite no-go

There is no automatic physical collapse in a deterministic arithmetic orbit. Mathematical **conditioning** uses a posterior law; **reinforcement** changes the next transition kernel. To separate them, take a declared 16-color Pólya urn with each initial color count one and realized past counts `N_j(t)`:

$$p_{t+1}(j)=\frac{1+N_j(t)}{16+t}. $$

Relative to iid Haar digits, the exact path likelihood is

$$\boxed{L_N(J_1,\ldots,J_N)=\prod_{t=0}^{N-1}\frac{16(1+N_{J_{t+1}}(t))}{16+t},\qquad E_{\mathrm{Haar}}L_N=1.}$$

For a fixed nontrivial Fourier mode, the unconditional ensemble mean is zero at every time, but its realized time-average `A_N(h)=N^{-1}∑χ_h(J_k)` has

$$\boxed{\mathbb E_{\mathrm{P\acute olya}}|A_N(h)|^2=\frac{N+16}{17N}\longrightarrow\frac1{17}\neq0.}$$

Proof: under the exchangeable symmetric Pólya law, `Eχ(J_i)conj χ(J_j)=1/17` for `i≠j`; diagonal is one. This is a **hostile countermodel**: reference symmetry, correctly normalized likelihood martingale, every intermediate checkpoint and a true realized-path feedback law do not automatically force cancellation. It is **not** asserted to model the authentic BBP path or actual lightning. Physical high-voltage channels modify conductive geometry, but SUCC must type that physical analogy separately.

## 5. The exact remaining obligation for π

SUCC already has the genuine selected `U_0=0`, `U_{n+1}=16U_n+r(n+1)` and its signed carry/arrival-bin transport on PR #313:

$$\widetilde C_{N,M}(h)=\frac1N\sum_{n=1}^N\exp\left(\frac{2\pi i h(c_{n+1}+\tau_{\lfloor M\{U_{n+1}\}\rfloor})}{16}\right),\qquad \tau_b=\frac{b+1/2}{M}.$$

Its distance from the **authentic Weyl mean** is paid: `π|h|/(16M) + (π|h|/(8N))Σ_{n≤N}r(n+1)`. We need a **source-selected signed estimate** showing `\widetilde C_{N,M_N}(h)→0` at a preset growing resolution, or a new provably weaker sufficient bound. Grouping the terms into classes indexed by `(literal carry, future remainder bin, signed atom/prime clock)` preserves the sum exactly; it does *not* bound it.

**Candidate research move:** find a *source-derived*, **future-stable** quotient `κ_{N,t}` (conditional class of source histories) whose number of effective classes is controlled and for which one can prove **signed** cancellation either within each class or between classes. The quotient must distinguish the genuine zero seed from changed-seed coherent controls and all source-mutant moment/packet decoys. Preserve each group's complex amplitude and an explicit residual. A finite phase equivalence, positive energy, or conditional entropy alone is not enough. Test the signed four-step holonomy, conjugate Gaussian atoms, Oily primitive-graded character, and literal 2-adic carry **jointly** rather than relying on one coordinate.

## 6. Research authority, falsifiers and references

- **PAPER-PROVED / CLASSICAL:** finite path disintegration, KL chain rule, minimal phase quotient, strong lumpability, checkpoint isometry, symmetric Pólya second-moment formula.
- **EXACT FINITE:** executable tests, all congruences, exact Fraction/source-parity certificates. Local isolated tests are not the full SUCC native test suite; hosted CI must be checked separately.
- **HYPOTHESIS/OPEN:** a source-authenticated coherence quotient sufficiently strong to force *selected* Fourier cancellation. No all-time estimate `S_N(h)=o(N)` is established here; **π base-16 normality is OPEN.** No quantum collapse, physical measurement or proof of RH is asserted.
- **Controls:** original changed-seed `V_n=-T_n` coherent orbit; SS-08 positive rational counterfeit; PR #313 conditional-energy saturation `E(h)=1, Δ=15` at high resolution; Pólya symmetry-with-memory; opposite-phase/parity group aliasing; nonlumpable source-group transitions. A successful method must reject each for a declared source reason.
- Classical refs: [Stanford EE376A entropy chain rule](https://web.stanford.edu/class/ee376a/files/2017-18/lecture_20.pdf); [J. L. Doob, conditional expectation/martingales](https://link.springer.com/chapter/10.1007/978-1-4612-0877-8_12); [Klauder 1979, path integrals and stationary-phase approximations](https://doi.org/10.1103/PhysRevD.19.2349). These references do not prove any SUCC-specific asymptotic.

**Next falsification:** for an authentic finite prefix, exhibit a nontrivial phase-sufficient group quotient that is ALSO stable under source successor with carried remainder information; prove a nonvacuous signed bound beyond generic triangle/Cauchy, or exhibit an exact counterexample requiring a refined group memory coordinate. Continue on a draft PR, do not merge or revise archived originals without maintainer permission.
