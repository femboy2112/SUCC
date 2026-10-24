# Source Genesis: exact-source Lean proof scope

**Local result: 41 new declarations kernel-checked, all 41 type/axiom exports
accepted, and four positive/mutant pairs passed.** The rejected mutants fail
semantically; no source changed during the successful run. Hosted CI is
reported separately by the integration receipt.

The new source is [BBPSourceGenesis.lean](../../formal/duck_pi/BBPSourceGenesis.lean)
under Lean **4.14.0**, mathlib
**4bbdccd9c5f862bf90ff12f0a9e2c8be032b9a84**. It imports the existing
`PiSource`, `BBPIntegral` and `BaileyCrandall` declarations from PR #232;
their source files and historical authority records are unchanged.

The serial checker is
[check_pi_source_genesis_lean.py](../../scripts/check_pi_source_genesis_lean.py).
Its final status, exact source hashes, theorem type expressions, dependency
revisions, command exits and paired mutation results are in
[the observation](pi_source_genesis_receipts/lean/kernel-observation.json).
This JSON is a reproducible observation, not an independently trusted kernel.

## The actual selected-orbit theorem

Write `Y_n` for the unreduced authentic BBP forced orbit, `T_n` for its
summable source tail, and `E_a(t)=exp(i a t)`. For **every** real `a` and
natural `J,L,d`, define

    P(a,J,L,d) = sum_(j<L) E_a((16^d-1)16^(J+j) pi),
    Q(a,J,L,d) = sum_(j<L) E_a(Y_(J+j+d+1)-Y_(J+j+1)).

The new declarations prove

    |P-Q| <= |a| [sum_(j<d) T_(J+1+j)
                        - sum_(j<d) T_(J+L+1+j)]
          <= |a|/[32(J+1)].

The first statement is `pi_lag_sum_transport`; the final uniform bound is
`pi_lag_sum_transport_uniform`. Setting `a=2*pi*h`, `J=0`, `L=N-d`
recovers the question's original complex correlation `C_d(N;pi)` for
integers `h` and `d<=N`. The transported sum uses the original signs of
the two-time phases. It is not a sum of absolute prime-path costs.

The proof closes these dependencies:

1. The imported, unconditionally proved BBP identity identifies the actual
   mathlib `Real.pi`, without an input axiom about pi or its digits.
2. `pi_lag_lift_identity` subtracts the two authenticated orbit equations.
   The correction is `T_(j+d+1)-T_(j+1)`; it is not
   `(16^d-1)T_(j+1)`.
3. `tail_succ_le` and `tail_add_le` prove monotonicity from the actual
   rational forcing and summable Green series.
4. `phase_lipschitz` proves the sharp `|a|` Lipschitz estimate by the
   complex derivative norm and the real mean-value inequality.
5. `lag_window_telescope` retains the cancellation of the tail differences,
   including overlapping windows.
6. The imported `tail_le_shifted` yields the formal majorant
   `T_(n+1) <= (1/32)(1/(n+1)-1/(n+2))`. Finite telescoping gives the
   uniform bound without estimating any unknown infinite sum numerically.

This is **source-specific transport control**, valid for the actual
pi-selected orbit and a particular exact rational recurrence. It does **not**
bound `P` or `Q` by `o(L)` and does **not** establish cancellation of even one
nonzero Fourier mode. No normality theorem is claimed. The sharper paper
constant derived from the positive beta kernel is intentionally not promoted
to Lean authority by this coarser formal theorem.

## Other declaration groups

| Group | Exact checked scope | Boundary |
|---|---|---|
| Signed moments | `m_0=0`, `m_1=15/64`, through `m_4=8995/32768` over the explicit signed residue vector | Poles are in the forcing-index variable |
| Kernel factorization | `g=(1-t)H`, positivity on `0<=t<1`, positive denominator on `[0,1]` | No integral interchange inferred from algebra alone |
| Kernel bounds | `1/4<h(t)<1` on the stated open/closed domains, `1-h(t)<=2(1-t)` | Integrated beta bounds and all-order Hankel positivity remain paper proofs |
| Reciprocal endpoint identities | `H(t)(4-4t+2t^3-t^4)=16-t^8` and the exact shift at `t=1+s` | Full coefficient/Pell and asymptotic hierarchy is a separate paper proof |
| Fixed-pole identification | Cauchy entries equal `1/(i+1-a_j)`, exact nonzero determinant, four readouts uniquely identify residues | No identification theorem for unknown pole locations |
| Initial state | `Y_n(s)+T_n=16^n(s+T_0)` and first fractional steps `2/15` versus `7/15` | The unforced `1/3` orbit is not the forced source |
| Weighted invariant | For every natural K, sum `(-1)^j binom(K,j)16^j=(-15)^K !=0` | No formal rational-function coboundary classification or normality implication |

The all-quantifier Lean statements are proofs, not finite Python tests. Some
are elementary classical identities; the source specializations and the
lag transport are new to this repository. Scholarly novelty is unverified.

## Reproduction and hostile controls

With the pinned dependencies present in `formal/duck_pi/.lake/packages`:

```sh
python scripts/check_pi_source_genesis_lean.py --output /tmp/pi-source-genesis-lean
```

The local run uses an independently located cache with the **same exact
manifest revisions**:

```sh
python scripts/check_pi_source_genesis_lean.py \
  --dependency-project /home/leah/SUCC-rf/formal/mathlib_bridge \
  --output /tmp/succ-pi-source-genesis-lean-final2
```

The checker rebuilds the three prerequisite project modules and the new
module into a fresh output directory, serially with one Lean worker and a
4 GiB Lean internal memory cap. It does not rebuild mathlib or alter the cache. It
exports every new theorem's actual kernel type and axiom dependencies;
only `propext`, `Classical.choice`, and `Quot.sound` are allowed.

Four calibrated positive/mutant pairs test the signed first moment, changed
initial state, exact kernel factorization, and invariant sign. The negative
claims must fail by a semantic type mismatch, with their positive controls
compiling. Missing imports, unknown identifiers and parse errors cannot
count as successful refutations.

The existing Duck/pi workflow has an additive checker step and a separately
named artifact. Existing proof authority is preserved. Local kernel success
and hosted CI success remain separate receipts.

The first checker attempt with a 2 GiB internal Lean ceiling aborted while
loading/elaborating the unchanged `BaileyCrandall` prerequisite. Its
[failure observation](pi_source_genesis_receipts/lean-resource-cap/kernel-observation.json)
and memory-exception log are retained. The subsequent configuration uses
the actual single-worker flag `-j 1` and a 4 GiB internal ceiling. A resource
abort is not a rejected mathematical theorem and is not a passing check.
