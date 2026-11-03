# Operation Inertial Gyroscope — source-locked E consensus without gimbal lock

**2026-11-03 · DRAFT RESEARCH.** Additive child of [PR #480](https://github.com/femboy2112/SUCC/pull/480) at **a5ea2c51446feb1e48099f18730fc60fa2f45d8e**. Parallel #481 Gaussian restoration and #479 Hannibal are read-only provenance; **not merged**. Original four signed BBP poles, literal U₀=0, existing production, formal/Lean, historical contracts, source, workflows and main stay unchanged.

## A source-aligned mathematical spinning top

Use the established rational quaternion \`H\` carrier and the original BBP real phases. Each nonzero harmonic h has an exact positive 2×2 density matrix ρ_(N,h)=1/2[[1,conj(c_N(h))],[c_N(h),1]] with c_N(h)=N^-1 Σ_(n<N) e(hU_n). Its trace/purity \`2 tr(ρ²)-1=|c_N(h)|²\` does not depend on common SU(2) orientation. Properly transporting changing local E-observer frames by quaternion groupoid links makes the measured Bloch-mean squared norm agree with the same source invariant. No Euler angles or gimbal singularities are required.

The original-source sign of a lifted spinor *does* depend on unwrapped integer carry; a central -1 twist is invisible in SO(3) but detectable in SU(2). Therefore require source- and seed-labeled quaternion frames, ordered nonabelian loop products, source-matched overlapping receipts and explicit spinor parity when the double lift is part of the observation contract. A network has a common frame iff all its nonabelian cycle products close (in the selected SU(2) cover).

**The no-go is explicit.** A coherent physical signal seen through alternating quaternion camera frames can falsely average to zero unless transported back. A four-frame quaternion twirl makes **any** pure source vector look zero on average, including a coherent fixed-point control. The original BBP phase rotations remain in one abelian Spin(2) subgroup, even though E observers can rotate noncommutatively. Old E² Gamma gain (1+i)/2 is NOT a unit quaternion: its norm²=1/2. Frame agreement alone never proves real-circle signed cancellation or π normality.

The frame-invariant mesoscopic top energy \`G_(N,M)=Σ_(1≤h<M/2)(1−2h/M)|c_N(h)|²=(Q_(N,M)−1)/2\` is exactly the inherited SUCC #475/#476 Fejér/Weyl gate in another mathematically safe coordinate carrier. Its *actual* zero-seed all-horizon sublog estimate remains **OPEN**. The original source Gamma/Green tail transports purity to the completed π radix orbit with an explicit O_h(1/N) cost, not with a decay proof.

## Files

- [PROOFS.md](PROOFS.md): exact gyroscope, frame-groupoid, source carry, Fejér/Gamma transport, false-Haar controls and claim ledger
- [gyroscope.py](gyroscope.py): source-exact four poles, quaternion links, Bloch diagnostics, frame-free rational checks, connected relay consensus
- [tests/test_inertial_gyro.py](../../../tests/test_inertial_gyro.py): root-discoverable 32 focused source, quaternion, relay and hostile cases
- [PREREGISTRATION.md](PREREGISTRATION.md), [HOLDOUTS.json](HOLDOUTS.json), [probe.py](probe.py): finite original zero-seed N=96/192/384, h=1/2/16 checks and reproducible receipts
- [SOURCE_MAP.md](SOURCE_MAP.md), [VALIDATION.md](VALIDATION.md), [NEXT.md](NEXT.md): scope, known witnesses, exact validation and next discriminator

**No physical general-Lorentz gyro claim:** these are spatial Spin(3)/SO(3) observer orientations, not arbitrary relativistic inertial coordinates. Classical Weyl and quaternion conjugation identities are not claimed as academic inventions. New papers are draft-only; do not merge, release or rewrite historical theorem contracts without authorization.
