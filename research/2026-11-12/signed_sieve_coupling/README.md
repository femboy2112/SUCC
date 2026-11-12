# SUCC signed-sieve coupling — a carrier-first Goldbach lower operator

**2026-11-12. Research-only, additive continuation of draft PR #600.**  The strong/binary Goldbach conjecture is **OPEN**.  This package supplies exact operator identities, a new locally scoped criterion (stronger than Goldbach), adversarial controls, and a finite verification up to 500,000. It is **not** a universal proof, Lean proof, or claim of original priority for sieve/Liouville identities.

## The target

For `H=ell^2(N_{>=2})` and `Delta_+|N>=sum_{a+b=N,a,b>=2}|a,b>`, the original SUCC intertwining defect `D=(P⊗P)Delta_+-Delta_+ P` satisfies for even `N>=4`

`||D|N>||^2 = R(N) = (p*p)(N)`.

Here `P` is the prime projector and `p` its diagonal source. Goldbach asks for `R(N)>=1` for every even `N>=4`. Neither the operator identity nor Hilbert positivity proves it.

## What the new round established

For a prime-inclusive sieve cutoff `z`, let `q_z = p+c_z` where `c_z` marks composite integers without any prime divisor <=z. Define the *signed* source `s_z=p-c_z=2p-q_z`. Then

```
L_z(N) := (q_z*s_z)(N)
        = 2(p*q_z)(N)-(q_z*q_z)(N)
        = (p*p)(N)-(c_z*c_z)(N) <= R(N).
```

All convolutions are **ordered** additive convolutions of sequences supported on integers >=2. Source/endpoint boundary `2..N-2` is retained. The second expression requires just a count of `prime + rough` representations and a purely sieve-generated count of `rough + rough`; it does not directly count prime+prime pairs. It is also equivalent to a majority condition among the positions with *both* endpoints rough.

At **cube-root resolution** `z=floor(N^(1/3))`, all surviving composites at arguments <=N are semiprimes; therefore `s_z(k)=-lambda(k) q_z(k)` and

`L_z(N) = -(q_z*(lambda q_z))(N) = #prime+prime - #rough-semiprime+rough-semiprime`.

The exact tensor operator `K_z=(Q_z⊗S_z+S_z⊗Q_z)/2=P⊗P-C_z⊗C_z` is an increasing lower operator for `P⊗P`. It converges strongly but **not in operator norm** as z grows. The finite information resolution moves with N: a fixed cutoff is proven to fail on infinitely many even inputs, using prime density and the CRT.

**Global conjectural next inequality** (NOT established):

`for all sufficiently large even N, L_floor_cuberoot(N)(N)>0`.

This criterion is **strictly stronger than binary Goldbach**, so a failure of the criterion would not refute Goldbach. At the same time, any proof of eventual positivity plus finite checking below the threshold would settle Goldbach.

## Finite exact outcomes

- Pure Python proof-contract tests: **16 test families PASS** (independent trial-division calibration, Liouville selector, operator-order monotonicity, exact Haar expansion, counterfeit source, fixed-cutoff failure, small-prime boundary).
- Independent Python direct trial-divisor/roughness audit: **all 4,095 even targets 4..8,192** satisfy the stronger condition.
- Separate C++17 exact NTT scan with modulus **998244353**: **all 249,999 even targets 4..500,000**, zero nonpositive bounds. For this range all convolution coefficients are <998244353, so the modular result equals the integer count. Exact direct-count spot checks are embedded in the C++ scan.
- **Fresh vs earlier exploratory FFT:** all 100,000 even targets `300002..500000` passed, minimum `L=2057` at `N=300094`. The earlier numerical survey up to 300,000 must not be counted as an independent holdout.
- At the quartic cutoff `floor(N^(1/4))`, **eight** even targets through 500,000 fail to certify (e.g. `N=82862, L=-2`), illustrating a real resolution tradeoff despite positive actual Goldbach counts.

No claim is made of a new Goldbach verification record (the ordinary conjecture has been verified much farther in the literature). This is a computational check of the **stronger signed minorant**.

## Entry points

- [THEOREMS.md](THEOREMS.md): formal domain/operator/cube-root/majority/Scott/no-go/average results and proofs.
- [CLAIMS.md](CLAIMS.md): claim status, dependencies, countermodels, next verdict-changing probes.
- [PROBES.md](PROBES.md): analytic target, alternative decompositions, and falsification controls.
- [LITERATURE.md](LITERATURE.md): primary and independent work, priority/authority boundaries.
- [signed_sieve.py](signed_sieve.py): exact Python finite source.
- [test_signed_sieve.py](test_signed_sieve.py): elementary proof-contract tests.
- [independent_audit.py](independent_audit.py): independent exact finite test.
- [exact_scan.cpp](exact_scan.cpp): modular NTT exact integer convolution verifier.
- [scan_500k.json](scan_500k.json), [audit_8192.json](audit_8192.json): actual receipts.
- [VALIDATION.md](VALIDATION.md): command outcomes and explicitly unrun project gates.

## Reproduce (from this directory)

```sh
python -m unittest -q test_signed_sieve
python independent_audit.py
g++ -std=c++17 -O3 -Wall -Wextra -pedantic exact_scan.cpp -o /tmp/succ_signed_scan
/tmp/succ_signed_scan 100000
/tmp/succ_signed_scan 500000
```

Only code and documents under this **new research subtree** are changed. No BBP four-pole source, π seed, imported proof, provenance manifest, formal source, CI configuration, or main branch are modified. SUCC `AGENTS.md` and `docs/METHOD.md` control status and review authority.
