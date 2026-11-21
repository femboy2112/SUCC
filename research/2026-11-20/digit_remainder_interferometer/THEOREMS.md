# Reflected-digit / transmitted-remainder interferometer — exact radix seam and BBP source contract

**2026-11-20 · Research-only.** Additive continuation of SUCC's reflected-Haar seam PR #678, stacked on causal-origami #677, observer-headed GPS #676, constructive Fourier atoms #675. Original four-pole BBP source, literal zero seed, carry, historical data, and preexisting validation are unchanged. The mathematics below concerns a **declared geometric/representation instrument**, not an experimentally demonstrated photon scattering device or an established source-root factor map for hexadecimal digits. No π-normality or RH result.

## Steelman / user's corrected proposal

A coherent candidate propagates along a normalized semicircular interval. **The reflected branch reports the digit**; the **through-slit branch inherits the complementary remainder and becomes the beginning of the next recursive cycle**. The earlier `s -> L-s` involution wrongly identified the reflected branch *itself* with the next state; it is a period-two model and cannot encode the actual base-16 shift. We implement the corrected *joint* output, retain both branch labels and their causal order, and ask which parts are canonical arithmetic versus unverified BBP source-filter physics.

Let `L>0` be an arbitrary chosen arc-length unit, and let `s_n∈[0,L)` be the normalized current wave coordinate. Set `x_n=s_n/L`. The **path budget** is `E_n=16 s_n` (a declared geometrical length budget, **not** physical joules). The recorded/reflected path carries an integral multiple of `L`, while the continued path carries its remaining length.

## DRI-01 — Exact reversible digit / through-slit seam (PROVED; classical)

Set

\[
\boxed{d_{n+1}=\lfloor E_n/L\rfloor=\lfloor16x_n\rfloor,\qquad s_{n+1}=E_n-Ld_{n+1}=L\{16x_n\}.}
\]

Then `d_(n+1)∈{0,...,15}`, `s_(n+1)∈[0,L)`, and **the complete two-channel output reconstructs the input uniquely**:

\[
\boxed{16s_n=Ld_{n+1}+s_{n+1},\quad s_n=(Ld_{n+1}+s_{n+1})/16.}
\]

Equivalently `D_16:[0,1)→{0,...,15}×[0,1)` given by `x↦(floor(16x),{16x})` is a bijection with inverse `(d,r)↦(d+r)/16`. Its second component alone is the 16-to-one map `x↦{16x}`. This is a precisely typed case where discarding the digit destroys inverse access, while retaining reflected history makes the update reversible **as an information representation**. No physical energy accounting follows from this bijection.

The label is not independently defined by *the complementary arc alone*: the 16-valued integer winding/branch count must be retained. An unmarked two-path intensity is not enough to recover it.

## DRI-02 — Four binary stages, the 16-channel Walsh/Haar interface (PROVED; classical)

Iterate the binary digit/remainder operation four times: `u_0=x_n`, `b_j=floor(2u_(j−1))`, `u_j=2u_(j−1)−b_j` for `j=1,...,4`. Then

\[
\boxed{d_{n+1}=8b_1+4b_2+2b_3+b_4,\qquad x_{n+1}=u_4.}
\]

Each `b_j∈{0,1}` is one possible binary split record. For **four binary decisions**, the four bits carry the hexadecimal digit, while the final uncommitted residual becomes the next cycle's initial coordinate.

On the 16 digit labels, the Walsh–Hadamard matrix `W_(k,d)=(-1)^{popcount(k & d)}` satisfies `W^T W=16 I`. It is a unitary basis change after multiplication by `1/4`. This is the mathematically justified relation to a **binary Haar-like branch splitter**. A two-point Haar projector gives one binary channel label; four ordered binary decisions (or one calibrated 16-valued readout) are needed to encode an arbitrary hexadecimal digit. **The existing source-root character `(t/sqrt(2))^4=±1` from #678 gives only ONE such binary label; there is no currently authenticated map identifying it with one of the actual four digit bits.**

No literal physical claim that a single wave undergoes four noninvasive independent measurements is made: a coherent unitary routing followed by a digit register, or a measured branching device, needs distinct instrument semantics.

## DRI-03 — An exact unitary wave-coordinate routing (PROVED; classical Hilbert analysis)

Take `H=L²([0,1],dx)` and `K=⊕_(d=0)^15 L²([0,1],dr)`. Define

\[
\boxed{(Uf)_d(r)=\frac14 f\!\left(\frac{d+r}{16}\right).}
\]

For any `f∈H`, substitution `x=(d+r)/16` gives

\[
\sum_{d=0}^{15}\int_0^1|(Uf)_d(r)|^2dr
=\int_0^1|f(x)|^2dx.
\]

The explicit inverse for `g∈K` is `f(x)=4g_(floor(16x))({16x})` almost everywhere. Thus `U` is a **unitary** between Hilbert spaces. Composing it with the normalized Walsh matrix `W/4` on the 16 branch labels leaves the norm unchanged. Four binary `U_2` routings reproduce `U_16` up to the conventional binary-order permutation, because `(1/sqrt(2))^4=1/4`.

This is a legitimate **norm-conserving mathematical realization** of the user's split. It is not yet an actual source-selected physical scattering `S` with detector positions, phases and Hamiltonian. A waveform amplitude and its Born probability require an explicitly chosen normalized `f`; a deterministic source coordinate does not inherit a Gaussian or uniform distribution merely because `U` is unitary.

For uniform `f=1`, every branch has mass `1/16`. For `f=4*1_[3/16,4/16)`, only branch 3 has mass one. Hence the unitary split **does not force digit equidistribution or any π-normality statement**.

## DRI-04 — Contracting inverse branches and fixed points (PROVED; classical)

The digit-labelled inverse branches are `F_d(r)=(d+r)/16`, each with Lipschitz constant `1/16` and unique fixed point `r_d=d/15`. For any finite digit word `d_1...d_N`,

\[
\boxed{x_0=F_{d_1}\circ\cdots\circ F_{d_N}(x_N)
=\sum_{j=1}^N d_j16^{-j}+16^{-N}x_N.}
\]

A constant digit `d` corresponds to the rational fixed phase `d/15`. Arbitrarily long finite repeated-digit episodes correspond to long itineraries in an inverse-branch cylinder close to that fixed phase, but need not imply eventual periodicity. The *forward* radix map is expanding/discontinuous at digit thresholds; the *inverse branches* are contracting. This is a source-independent honest realization of an attracting branch geometry, **not** a theorem that the four BBP Mellin-filter zeros are digit-state attractors.

## DRI-05 — The authentic zero-seed BBP phase satisfies this exact seam (PROVED arithmetic; identity not normality)

Fix *only* the original signed poles

\[
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},\quad U_0=0,\quad U_n=16U_{n-1}+r(n).
\]

Let `x=Σ_(n>=1)16^(-n)r(n)=π/16` (classical BBP), `T_n=Σ_(k>=1)16^(-k)r(n+k)`, and `θ_n={U_n+T_n}={16^n x}`. Then

\[
\boxed{d_{n+1}=\lfloor16\theta_n\rfloor,\qquad \theta_{n+1}=16\theta_n-d_{n+1},\qquad
\theta_n=\frac{d_{n+1}+\theta_{n+1}}{16}.}
\]

The finite memory register `M_0=0`, `M_(n+1)=16M_n+d_(n+1)` obeys

\[
\boxed{x=16^{-n}(M_n+\theta_n).}
\]

This is an exact same-source *finite/acquired digit ↔ continuing analytic tail* interface. It recovers the standard hexadecimal expansion but does **not** establish its statistical distribution. Source-to-phase is authenticated via the zero seed and exact BBP tail; source filter root geometry has not been shown to realize the reflected digit port.

Using the original rational BBP partial sum `P_M=Σ_(j<=M)16^(-j)r(j)` and strict source-tail estimate `0<x−P_M<16^(-M)r(M+1)/15`, the interval `[P_M,P_M+16^(-M)r(M+1)/15]` certifies an `N`-digit prefix whenever floors of `16^N` times both endpoints agree. For `M=N=12` exact fractions certify **`3243F6A8885A`** as the first 12 hexadecimal digits of `π/16`. This is a known BBP evaluation, now reproduced as a source-anchored digit-splitting instrument; it is not independent confirmation of the classical BBP identity.

## DRI-06 — Constructive Fourier identity for reflected digit and through wave (PROVED; classical)

Define `e(t)=exp(2π i t)`. The **literal** joint split gives for any integer `h`

\[
\boxed{e(h\theta_n)
=e(hd_{n+1}/16)\;e(h\theta_{n+1}/16).}
\]

Iterating yields

\[
\boxed{e(hx)=\left[\prod_{j=1}^N e(hd_j16^{-j})\right]\,e(h\theta_N16^{-N}).}
\]

This is a constructive, chronologically labelled phase factorization of one *point*, not the temporal Weyl average `B^(-1)Σ e(hθ_n)` and not a theorem about the source-filter root projectors. The fractional frequencies `h/16` act on the **chosen real representatives**, not as unambiguously defined integer characters of an independently reduced circle state.

In particular, keeping the full reflected digit and through-port phase is lossless on the unit interval; discarding either can destroy information. This is mathematically the user's "origami paper folded back into the successor" interface.

## DRI-07 — Critical hostile controls (PROVED exact no-go)

1. **Plain fixed reflector:** If the only map is `s_(n+1)=L-s_n`, then `s_(n+2)=s_n`; a memoryless output based solely on s generates an at-most-two-periodic digit sequence. It cannot model the actual first three authentic hexadecimal digits `3,2,4` or generic digit sequences. **The expanding 16-fold arc budget and branch counter are load-bearing.**
2. **Two-root-class insufficiency:** The original root parity `w^4∈{±1}` separates the factors `t²+2` and `t²+2t+2`, but cannot by itself distinguish 16 hexadecimal digit values. Four independent binary stages or an independently calibrated 16-valued detector are needed to implement the abstract radix seam. No map from the original `H` root classes to the four stepwise bits is known.
3. **Original forcing, changed seed:** The same BBP forcing and `s=−π/16` has completed phase 0 at every step, hence every reflected digit is zero; the same forcing-spectrum/root-circle/5–11 ports do not select the original zero seed. The source anchor must be retained.
4. **Wrong register:** Retaining only the transmitted fractional phase erases the first digit. Indeed `x=(d+r)/16` for all 16 distinct d with the *same* residual r; no number of equivalent phase-only heads recovers d without memory or source access.
5. **Probability spoof:** Haar-unitary norm conservation and spatially uniform output under a uniform `f` hold also for nonnormal deterministic source points. Do not infer π-normality or independent prime statistics.
6. **Instrument spoof:** Calling the two complementary endpoint arcs "mirror round trips" is invalid without an actual path/recombination geometry, calibrated phase and scattering coefficients. The 16-channel split is a mathematically specified unitary, not a physical emission/detection experiment.

## DRI-08 — The four authentic source roots lie on hex routing boundaries in the natural left-arc chart (PROVED EXACT; chart-relative)

Choose the source-circle radius `R=√2`, upper semicircle endpoint at angle `π/2` as the origin, and the left-oriented arc coordinate `x=(θ−π/2)/π ∈[0,1]`. Then the original `H` roots have exactly the following coordinates:

| Root | Normalized left-arc coordinate x | 16x |
| --- | ---: | ---: |
| `+i√2` | `0` | `0` |
| `−1+i` | `1/4` | `4` |
| `−1−i` | `3/4` | `12` |
| `−i√2` | `1` | `16` |

**All four roots land on 16-fold routing-cell BOUNDARIES**, not interiors. At the two interior roots the abstract digit/remainder map gives `(d,r)=(4,0)` and `(12,0)` respectively; the lower endpoint `x=1` lies **outside** the half-open digit domain and must not be silently identified with `x=0` without an explicit endpoint gluing convention. The root positions are discontinuity points for the reflected-digit readout: arbitrarily small changes of the prepared arc coordinate across `1/4` or `3/4` change the selected digit. The transmitted residue is continuous only within a specified digit branch. This is an exact geometry/bookkeeping alignment but is **chart-relative and not a physical state-to-root map**. It suggests branch boundaries, orientation, reference offset and finite precision are load-bearing in any purported source-derived slit instrument. An arbitrary offset of the digit partition changes this alignment.

## DRI-09 — Open source-selected challenge (UNVERIFIED)

Construct from the original BBP zero-seeded source and its full signed pole/prime/cofactor/carry history a **calibrated forward-accessible factor map** from the actual phase observer's digit/residue state to the source's `H(t)` four-root circle and two parity projectors; or prove a precise no-go. The root algebra affords just one ± bit. The special root locations coincide with **digit-bin boundaries** under the natural left-arc chart (DRI-08), further raising a calibration/threshold requirement. A successful joining must supply the remaining four-stage digit extraction, transported source phases, and a signed all-late-shell estimate not already equivalent to the target. The source-root topology, 8-step stable filter, journal shifts and Hilbert unitary split alone are not estimates of real-phase digit statistics. R0 and base-16 π-normality are OPEN.

**Verdict:** DRI-01–06, DRI-08 and concrete negative controls are exact classical statements; explicit use of the immutable BBP source authenticates the source-selected trajectory and certified finite prefix. A physical one-slit/reflection mechanism, root-parity-to-digit bridge, new signed all-shell π phase bound, and physical energy conservation are **UNVERIFIED**.
