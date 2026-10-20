# Prime-clock-to-hologram transport calculus: exact composition and naturality

**Date:** 2026-10-19.
**Branch:** `research/amv-moonshot-c-hologram-naturality-2026-10-19`, based on
`origin/main = 455600a2e013895c36238a3a97e0f470fd7ba197` (Academic Main V).
**Module:** `observational_succ/hologram_transport_calculus.py`.
**Tests:** `tests/test_hologram_transport_calculus.py` (20 tests, all green, exact).
**Depends on:** `observational_succ/factorial_borwein_hologram.py` (the embedding
`I_N`, sampler `R_N`, windows `J_N`, `source_clock_gate`), with the authentic
prime oracles reused from `observational_succ/rad_ris_transport.py`
(`is_prime`) and `observational_succ/prime_phase_clocks.py` (`prime`).
**Global firewall:** ABC OPEN, RH OPEN, true signed completed Weil/Suzuki S4
sign OPEN. Academic novelty UNVERIFIED. No archival/frozen source modified; no
YEAN touched; not pushed; no PR; not merged.

This note is Moonshot C of the AMV Thinker-Dome. It formalizes the informal
statement already recorded in §7 of
[FACTORIAL_BORWEIN_HOLOGRAPHIC_CLOCK.md](FACTORIAL_BORWEIN_HOLOGRAPHIC_CLOCK.md)
— "for different N, M, `I_M R I_N = I_M`" — into an exact transport calculus with
a proven composition / naturality law, carried residue-projector covariance, and
a clean nonrecoverability witness. The goal is a coherent calculus, not a
decorative diagram.

## 0. Objects and their declared domains

Fix the factorial Borwein data of
[factorial_borwein_hologram.py](../../observational_succ/factorial_borwein_hologram.py).
For each horizon `N` in `1..256`, `B_N = U_{1/2} * conv_{(p,k) in J_N} U_{1/(2 p^k)}`
is the compactly supported nonnegative kernel with `B_N(m) = 1_{m=0}` on `Z` and
`sum_m B_N(x-m) = 1` (FBH-01). The three maps:

| Map | Signature | Definition | Domain (declared) |
| --- | --- | --- | --- |
| `I_N` (`lift`) | `ell^2(Z) -> L^2(R)` | `(I_N c)(x) = sum_m c_m B_N(x-m)` | finitely supported `c` |
| `R_N` (`sample`) | `ran(I_N) -> ell^2(Z)` | `(R_N f)(m) = f(m)` | **`ran(I_N)` ONLY** |
| `T_{M<-N}` (`transport`) | `ran(I_N) -> ran(I_M)` | `T_{M<-N} = I_M R_N` | `ran(I_N)` |

A point of `ran(I_N)` is represented EXACTLY by the pair `(horizon=N, coeffs=c)`
(class `RangeFunction`): `I_N` is injective on finitely supported sequences
(FBH-02), so this naming is faithful and equality is structural over
`(N, c)`. The horizon label is load-bearing — it selects the off-lattice shape.

## 1. The source-commuting diagram (PROVED LOCAL, EXACT)

```
                 I_N                         R_N
   ell^2(Z) ----------> ran(I_N) ----------------------> ell^2(Z)
      |                    |                                |
   id |                    |  T_{M<-N} = I_M R_N         id |
      v                    v                                v
   ell^2(Z) ----------> ran(I_M) ----------------------> ell^2(Z)
                 I_M                         R_M

   R_N I_N = id_{ell^2}         (ONLY on ran(I_N))
   R_M T_{M<-N} I_N = id        (sources pass through unchanged)
   T_{L<-M} T_{M<-N} = T_{L<-N} (on ran(I_N))
```

The content is that the SAME arithmetic source coefficients ride through every
horizon while only the off-lattice analytic representation changes.

## 2. Exact domain theorem

**Theorem (range retraction).** For every `N` and every finitely supported
`c in ell^2(Z)`, `R_N I_N c = c`. *Proof:* `(I_N c)(m) = sum_j c_j B_N(m-j) =
c_m` since `B_N(integer) = delta` (FBH-01). The sampler computes exactly this
through the kernel and asserts recovery. ∎ Verified by `verify_range_retraction`
and `test_R_after_I_is_identity_on_range` over `N in {4,5,6,7,8,10,16}`.

**Theorem (composition / naturality).** On `ran(I_N)`,
`T_{L<-M} ∘ T_{M<-N} = T_{L<-N}`, and both equal `I_L ∘ R_N`. *Proof:*
`T_{L<-M} T_{M<-N} = (I_L R_M)(I_M R_N) = I_L (R_M I_M) R_N = I_L R_N = T_{L<-N}`,
using `R_M I_M = id` on `ran(I_M) ⊇ im T_{M<-N}`. ∎ The middle cancellation is
the ONLY place the identity could fail; the implementation routes it through the
genuine kernel sampler, so the test is a real check of `R_M I_M = id`, not a
tautology. Verified by `verify_composition_law` and
`test_composition_law_three_horizons`.

**Exact composition confirmation.** For the source
`c = {-3:2, -1:1/3, 0:1, 1:-7/4, 4:5/2, 7:9}` and `(L,M,N) = (10,6,4)`:

```
transport(10, 6, transport(6, 4, c)) == transport(10, 4, c)
  == RangeFunction(horizon=10,
       coeffs=((-3, 2), (-1, 1/3), (0, 1), (1, -7/4), (4, 5/2), (7, 9)))
```

i.e. both routes land on `I_10 c` with the source coefficients byte-identical.

**Domain firewall (load-bearing).** `R_N I_N = id` holds ONLY on `ran(I_N)`. The
sampler `R_N`:
* REFUSES an `AbstractL2` equivalence class — point evaluation is not a bounded
  functional on `L^2`, so integer sampling is undefined there
  (`test_point_evaluation_on_abstract_L2_is_refused`);
* REFUSES a `RangeFunction` of a different horizon, or a bare coefficient tuple
  — these are out of `ran(I_N)` (`test_sampling_outside_the_declared_range_is_refused`,
  `test_transport_through_mismatched_range_element_is_refused`).

It is NEVER globalized to bounded point sampling of arbitrary `L^2` classes.

## 3. Residue-projector covariance under n -> n+1 (PROVED LOCAL, EXACT)

Let `S` be the SUCC shift with the declared orientation `n -> n+1`
(`(S c)(m) = c(m-1)`; a source at site `s` moves to `s+1`) and let `P_{p,r}` be
the authentic residue projector onto class `r mod p` for a genuine prime `p`
(authenticated by both `rad_ris_transport.is_prime` and
`prime_phase_clocks.prime`; its selection agrees with
`factorial_borwein_hologram.source_clock_gate`, see
`residue_projector_matches_clock_gate`).

**Theorem (covariance).** `S P_{p,r} = P_{p,(r+1) mod p} S` on `ell^2(Z)`.
*Proof:* `(S P_{p,r} c)(m) = (P_{p,r} c)(m-1)`, nonzero iff `m-1 ≡ r`, i.e.
`m ≡ r+1 (mod p)`; `(P_{p,r+1} S c)(m)` is nonzero iff `m ≡ r+1`, with the same
value `c(m-1)`. ∎ The shift conjugates the residue-`r` projector into the
residue-`(r+1)` projector — the correct phase orientation.

**Theorem (naturality).** The lifted operators `I_N S R_N` and `I_N P_{p,r} R_N`
on `ran(I_N)` commute with transport:
`T_{M<-N} (I_N S R_N) = (I_M S R_M) T_{M<-N}` and the same with `S` replaced by
`P_{p,r}`. *Proof:* both sides equal `I_M S R_N` (resp. `I_M P_{p,r} R_N`) by two
applications of a retraction identity. ∎ Consequently the intertwining
`S P_{p,r} = P_{p,r+1} S` transports verbatim into `ran(I_M)`. Verified exactly
by `residue_projector_covariance` and `test_covariance_and_naturality_through_transport`
over `p in {3,5,7}` and all `r`.

**Orientation is load-bearing (negative control).** For `p >= 3` and a source
meeting class `r`, the wrong orientation `P_{p,r-1} S` disagrees with
`S P_{p,r}` (because `r+1 ≢ r-1 (mod p)`); `p = 2` is the degenerate case where
`r+1 ≡ r-1`. Recorded by `wrong_orientation_differs` and
`test_wrong_phase_orientation_is_load_bearing`.

## 4. Required nonrecoverability counterexample (PROVED LOCAL, EXACT)

**Two distinct continuous off-lattice functions with identical integer samples.**
Take the single arithmetic source `c = delta_0` and lift at two horizons:

```
f = I_4 (delta_0) = B_4,        g = I_6 (delta_0) = B_6.
```

Both are continuous (`N >= 4`) and in `L^2(R)`.

* **Identical integer samples:** `f(m) = g(m) = 1_{m=0}` for all `m in Z`
  (checked on `-3..3`; `R_4 f = R_6 g = delta_0`). Integer sampling alone CANNOT
  recover which function it was — it recovers the source coefficients, not the
  off-lattice label `N`.
* **Distinct as functions:** at the off-lattice point `3/10`,
  `B_4(3/10) = 1` (it lies inside the wider `N=4` plateau, radius `5/16`),
  while `B_6(3/10) = 30922061/31104000 < 1`. Exact, unequal.
* **Flat collision too:** at `1/10` BOTH equal `1` (inside both plateaus), so not
  even every off-lattice probe separates them — matching the dossier note that
  `1/10` collides `N=4` and `N=6`.

Produced and asserted by `nonrecoverability_witness`; checked in
`test_distinct_functions_identical_integer_samples` and re-derived by hand in
`test_witness_is_reconstructed_by_hand`.

## 5. Separation: arithmetic source vs. analytic representation

The calculus is honest about what each layer carries.

* **Arithmetic source information** = the integer samples = the coefficient
  vector `c`. This is EXACTLY what `R_N` recovers and what every `T_{M<-N}`
  preserves. Residue projectors, the SUCC shift, and the authentic `p`-clock
  gates all act on this layer and are invariant under transport (§3).
* **Additional analytic representation** = the off-lattice shape of `B_N`, i.e.
  the finite multiset of squared window half-widths `{(1/(2 p^k))^2}` for
  `(p,k) in J_N`. This is NOT in the samples; it is readable only from the
  Fourier log-sinc germ (FBH-04/05) and it is exactly what the nonrecoverability
  witness shows the sampler cannot see. Transport `T_{M<-N}` DISCARDS the horizon-`N`
  analytic representation and installs the horizon-`M` one, keeping the source.

The three "factorials" remain distinct interfaces, never one normalization:
arithmetic Legendre occupation `v_p(N!)` (window structure), Borwein
simplex-volume `1/m!` (uniform-sum CDF, parent PR #189), and Poisson jump-time
`1/k!` (SUCC clock series). Guarded by `test_three_factorials_stay_distinct`.

## 6. Status labels (per AGENTS.md)

| Claim | Status |
| --- | --- |
| `R_N I_N = id` on `ran(I_N)`, EXACT | **PROVED LOCAL + TESTED MODEL** |
| `T_{L<-M} T_{M<-N} = T_{L<-N}` on `ran(I_N)` | **PROVED LOCAL + TESTED MODEL** |
| residue-projector covariance `S P_{p,r} = P_{p,r+1} S` | **PROVED LOCAL + TESTED MODEL** |
| naturality of shift/projector through `T_{M<-N}` | **PROVED LOCAL + TESTED MODEL** |
| nonrecoverability witness `B_4 != B_6`, equal `Z`-samples | **PROVED LOCAL + TESTED MODEL** |
| point evaluation bounded on general `L^2` | **REFUSED (firewall), not claimed** |
| any RH / Weil / Suzuki-S4 consequence | **OPEN / not claimed** |
| academic novelty of the indexing | **UNVERIFIED** |

## 7. Open obligation

The transport calculus preserves the arithmetic source and transports authentic
residue/SUCC structure with correct orientation, but it establishes NO positive
signed Weil form: `B_N` is a nonnegative probability kernel with a coercive
translate Gram (FBH-05), which is a Hilbert-coercivity statement, **not** Weil
positivity (genuine Gamma, pole, conductor, prime-power source signs). The
remaining obligation — unchanged by this note — is to exhibit, if it exists, a
PROVED map from these source-authenticated transported projectors to the signed
completed Weil distribution and its `S4` sign, with fake-composite and matched
non-Euler controls and no nontrivial zero positions as construction inputs. Until
such a map is proved, the transport law is a faithful source-certificate
calculus and nothing more. RH PROVED: NO.

## 8. Reproduce

```sh
PYTHONPATH=. python3 -m unittest tests.test_hologram_transport_calculus -v
PYTHONPATH=. python3 -m observational_succ.hologram_transport_calculus   # demo
```
