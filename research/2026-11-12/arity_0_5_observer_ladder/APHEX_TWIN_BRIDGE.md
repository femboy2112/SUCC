# “Aphex Twin was right”? A typed, falsifiable reading of the Windowlicker equation

**Status:** SOURCE-VERIFIED title approximate; SYMBOL SEMANTICS **UNVERIFIED**; a typed **analogous** update is CLASSICAL algebra; no attribution of a previously unknown theorem or historical intent.

The 1999 *Windowlicker* B-side commonly called “Formula” or “Equation” carries a printed title transcribed approximately as

`Δ M_i^(-1) = -α Σ_(n=1)^N D_i[n] ( Σ_(j∈C(i)) F_(ji)[n−1] + F_(ext,i)[n−1] )`.

**Uncertainty retained:** Some transcriptions print `F_(ext,i)[n^(-1)]` instead of `[n−1]`; the cover's stylization and multiple reproductions do not authenticate this index choice. `M_i^(-1)` could denote a reciprocal rather than a matrix inverse; `Δ`, `α`, `D`, `F` and the units are not defined in the title. In particular there is **no visible Fourier transform operator in the printed equation**. No source establishes that James intended the variable identification below.

Grounded references: MusicBrainz release metadata and sleeve annotation: https://musicbrainz.org/release/bc081a27-34aa-4a0c-b6ec-9df4d0fd3a0d . Formula reproduced (with the index ambiguity) in https://mathoverflow.net/questions/56489/where-does-aphex-twins-windowlicker-equation-come-from . Carnegie Mellon's audio-education example: https://www.cs.cmu.edu/~15322/book/ch10/09.html . MusicBrainz notes the image-to-audio/spectrogram face; *that* is where the verified time-frequency connection occurs. Do not assert it is encoded by the equation itself.

## Falsifiable semantics (chosen here, not an identification)

- `i` labels a typed output channel, `j∈C(i)` selected inbound channels.
- `F_(ji)[n−1]` is a delayed interaction from channel j to i, `F_(ext,i)[n−1]` external source forcing.
- `D_i[n]` is the time-n response/envelope. `α` has dimension `[M_i^-1]/([D_i][F])`, not a magically dimensionless constant.
- Sum of the forces is well-typed only if external and incoming force terms agree in dimension and target fiber. All terms of the temporal sum require a common unit. This is implemented in the exact rational `LaggedForces` and `aphex_style_update` adapter.

The formal update can be rewritten as a source-labelled causal accumulation

`Δm_i[n] = -α D_i[n] · ( Σ_(j∈C(i)) F_(ji)[n−1] + F_(ext,i)[n−1] )`, then `ΔM_i^-1=Σ_n Δm_i[n]`.

Here time lag, typed units, graph in-neighbors and external forcing match the **shape** of the new channel-observer machinery. That is a legitimate useful interpretation, not an empirical claim about the track's design.

## The decisive limitation — and a repair

If `F_(ji)` is computed **only** from scalar and pairwise channel information, then a 3-way parity defect is invisible. Two 3-bit sources have identical one- and two-body moments but `E[X1 X2 X3]=+1` vs `−1`; exact Walsh inversion reconstructs each from its full interaction coefficient table. A higher-arity generalization must add e.g.

`Σ_(S⊆C(i); |S|≥3) T_(S→i)[n−1] (⊗_(j∈S) X_j[n−1])`.

Such terms are typed multilinear couplings in the SUCC research adapter; the update is a **proposed extension**, not the printed Aphex Twin title. In full dynamical systems, nonlinear pairwise terms using joint histories may simulate such an effect, so the countermodel applies specifically to the pairwise-marginal observational language.

**Hostile controls:** wrong force-unit fails; wrong alpha unit fails; sign and lag are explicit; even/odd parity pairwise alias demonstrates loss; unique higher-arity channel distinguishes. The music itself supplies no independently authenticated physical-force law, no proof of a Fourier identity, no π-normality evidence, and no RH argument. The coincidence is mathematically productive **because we can state exactly how it could be false**.
