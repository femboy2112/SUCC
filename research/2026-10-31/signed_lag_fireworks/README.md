# Signed lag fireworks: exact conductor counterexamples and a wider source bridge

**π base-16 normality remains OPEN.** This round proves no new unconditional
cancellation estimate for the actual zero-selected orbit. It supplies stronger
hostile examples, resolves the necessity of the lag gate, and improves the
original-source transport budget. These are paper proofs with exact finite
instruments, not Lean formalizations or claims of literature priority.

The child branch starts at verified PR #434 head
`030ee84b8b7f655fcf433375bfc0b347e0483c89`. All four original signed poles,
the literal selected boundary U0=0, imported mathematical modules and frozen
source/proof contracts are preserved. Changed seeds below are clearly marked
counterfactuals.

The strongest counterexample is the [dyadic shadow theorem](BOUNDARY.md): from
the actual rational U_M(0), exact floor rounding constructs an irrational
seed exponentially close to zero whose first M-term complex Weyl sum differs
by less than `22|h|/(105M²)`. Only `ceil(log_16(64M²))` more steps are needed
before its phases equal the coherent-tail phases at **every fixed harmonic**.
Its critical lag score tends to one even at h=1. This strengthens the previous
shadow with a denominator-dependent witness harmonic.

The [prime-conductor theorem](ARITHMETIC.md) determines the entire limiting
signed lag spectrum of a different same-forcing shadow family:

    q=3^a5^b, P=q/15, gcd(c,15)=1, s=c/q-pi/16:
    lim_N L_(N,floor(log_16 N))(h;s) = 1 if P divides h, otherwise 0.

These are single periodic completed orbits, can approach seed zero, and pass
any prescribed finite low-frequency band despite being nonnormal. For q=225,
the exact complete-period lag mean is e(k/15): every lag is supported, yet
discarding its phase changes the limiting score from zero to one. This
decisively rejects a magnitude-only conductor aggregation. It does not reject
a fully authenticated rational-state/zero-boundary transference theorem.

The [clipped source bridge](TRANSPORT.md) gives

    |C_(h,k)(N)-D_(h,k)(N)| <= sqrt(11|h|(16^k-1)/14),
    E* <= (8 B_h/9) 4^K/(K²N), B_h=ceil(sqrt(11|h|/14)).

Thus K=floor(log_4 N) has vanishing error O_h(K^-2), doubling the leading lag
depth. This estimate is seed-uniform and is **not selected cancellation**.
The [sharpness theorem](SHARPNESS.md) proves a matching leading-scale
obstruction: for the coherent seed and K~c log16N, 2<c<3, the reduced signed
score tends to 4/c-4/c² while the actual score tends to one. The gap is
(1-2/c)², exactly 1/25 at c=5/2. Thus merely widening a seed-uniform transport
bridge beyond the doubled leading clock cannot remove the selected problem.
The [two-scale Jensen proof](BOUNDARY.md) establishes that the signed gate is
necessary as well as sufficient for normality in the BBP family at either
clock. Merely weakening the clock does not remove the central arithmetic debt.

The [predeclared experiments](EXPERIMENTS.md) use an independent combined-source,
BBP-pi, interval angle-doubling instrument. The parent Machin/direct-Taylor
instrument is retained unchanged. Both are rigorous rational implementations
of the same source; they are not independent sources of asymptotic evidence.
All 23 cases completed; [RESULTS.md](RESULTS.md) records fresh positive as well
as negative scores and explicitly marks the over-deep finite bridge vacuous.

Read [CLAIMS.md](CLAIMS.md), [AUDIT.md](AUDIT.md), [VALIDATION.md](VALIDATION.md),
and [NEXT.md](NEXT.md) for the quantified claims, inherited metadata traps,
actual validation status, and remaining proof obligation. Exact raw arithmetic,
boundary and finite interval receipts accompany their executable generators.

Reproduce the focused research checks:

```sh
python -m unittest discover -s tests -p 'test_signed_lag_fireworks*.py' -v
python research/2026-10-31/signed_lag_fireworks/arithmetic.py
python research/2026-10-31/signed_lag_fireworks/run_boundary_receipt.py
python research/2026-10-31/signed_lag_fireworks/run_sharpness_receipt.py
python research/2026-10-31/signed_lag_fireworks/probe.py --output /tmp/fireworks-finite.json
```

The arithmetic and boundary JSON outputs are deterministic. The finite probe
also records elapsed durations, which naturally vary; its rational results
and source hashes are the reproducible content.
