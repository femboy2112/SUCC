# Quotient the carrier; retain and calibrate the signal

**Pi base-16 normality: OPEN. RH: OPEN.** Additive continuation of draft #544,
parent `a974db527c19708006b9f6d7f0ca01d08d1e0524`. The proof baseline stays
`d32342d375f44ddf62221ad6aff2f534abdc0a03`; freshly fetched main is
`43a607818907120d4cdab73d240f5b4d7700b63f` (Main XXI). Its handoff and canonical
source conventions were read without rebasing or importing integration work.

The user's proposal survives in two precise forms. Learning the local phase
can remove a controlled nuisance error while retaining the full signed
signal. Separately, an authentic completion residual has an exact
Euler–Mascheroni phase after a specified logarithmic subtraction. Their
connection to selected covariance is a concrete remaining research question.

## Strongest source result: an exact gamma residual phase

Keep the original four poles and literal U0=0. Write
`X_n=16^(n-1)pi`, `T_n=X_n-U_n=sum_(j>=1)16^(-j)r(n+j)` and `e(t)=exp(2pi i t)`.
[GQ2–4](gamma/THEOREMS.md) prove

```
C = pi(7/9600-7sqrt(2)/1152) + 53log(2)/1440
    - 7sqrt(2)log(1+sqrt(2))/576,

0 < sum_(n<=N)[nT_n-1/(64n)] - C < 7/(512N),
lim N*(sum_(n<=N)[nT_n-1/(64n)]-C) = 7/512.
```

Thus `sum nT_n-(log N)/64 -> C+gamma/64`. More directly, the coherent product

```
e(h[C+(log N)/64]) * product_(n=1)^N [e(hU_n)e(-hX_n)]^n
    -> e(-h gamma/64)
```

has error less than `11pi|h|/(256N)` for every integer N>=1 and fixed h!=0.
This is a derived source identity, not a constant fitted to numerical data.
The proof uses the authentic tail integral and exact endpoint telescoping.
It extends the inspected earlier source finite parts; no worldwide novelty
or new classical special-function theorem is asserted.

The subtraction convention matters: replacing log N by log(lambda N) shifts
the finite part by `-log(lambda)/64`. The completed reference follows the
seed if applied to a general U_n(s), making this quotient seed-independent.
Keeping the original unwrapped zero reference instead makes its renormalized
weighted sum finite **iff s=0**. The phase-only statement has integer aliases.
This separates calibration from literal boundary authentication.

## Learning really can isolate the signed signal

For a finite authenticated epoch let `a=e(h[U]_p)`, `b=e(h(U-[U]_p))`,
`z=ab`, and let P average on a declared observation transcript's fibers.
The learned quotient is the orthogonal projection

```
Q = M_a P M_conjugate(a),       Qz = a Pb.
```

[QS1–6](quotient/THEOREMS.md) prove its variational optimality and the sharp
operator constant

```
||P-Q||op² = max_occupied_cell (1-|E[a|cell]|²).
```

For M equal local-phase cells, this is at most `min(1,pi²h²/M²)`. Hence
learning then correcting the phase approaches directly learning the signed
source signal, uniformly over every bounded complement. Moreover

```
W = E(Pa Pb) + E[(a-Pa)(b-Pb)],
|W-E(Pa Pb)| <= sqrt(V_a V_b) <= pi|h|/M,
V_a=E|a-Pa|²,  V_b=E|b-Pb|².
```

Here the digit cells resolve the **current** local phase. They agree with
successive actual local trajectory digits only while the clean prime clock
law holds. No future forced transcript is silently substituted across a pole
birth; the source probe groups actual current principal parts directly.

The retained signed mean is the object to investigate. Greater correlation
is not itself a failure: for the coherent complement it correctly reveals
signal 1. Nested transcript refinements supply the exact signed depth ledger
`Cov(a,b)=sum_d E[Delta a_d Delta b_d] + final residual`. All cross terms and
phase signs survive. These are finite observer results, not physical
nonlocality, ensemble typicality, or a new category incompatible with SUCC.

## Triangulation and falsifiers

The [fixed protocol](PROTOCOL.md) was committed before source execution.
300 outward-interval configurations cover five original epochs, h=1,3,
five depths, two cell origins, and original/synthetic/matched-seed families.
The finest partition makes a exactly measurable, so the discarded signed
residual is exactly zero for all families. The retained means distinguish
the source from coherent controls: at A=2203,h=1, the original |W| is about
0.03255 while the matched same-forcing control is near1. These are finite
observations, not an asymptotic saving. Exact local knowledge still leaves
substantial original complementary variance: about0.83208 in that case.

[QC3–4](hostile/THEOREMS.md) independently calibrate two different small
residuals. For uniform x and b=e(theta)conjugate(a),
`M² residual -> e(theta)pi²h²/3`. For b_M=e((M-h)x), the full mean is0 but
`M residual -> h`. These disprove a universal gamma coefficient or universal
quadratic residual rate for that particular observation error; they do not
disprove an unspecified original-source gamma connection.

## The exact remaining chain

```
original zero source
  -> [OPEN] signed conditional-product / depth-increment estimate
  -> original signed covariance decay
  -> full Weyl decay for every fixed h!=0 and all integer epochs A
  -> base-16 normality of pi.
```

The last two arrows retain the preceding round's audited Green transport
and all-epoch gluing. QS gives explicit error bounds for replacing covariance
by its learned counterpart. GQ supplies an exact source calibration. **No
theorem yet transports the gamma phase limit to a bound on that retained
signed counterpart.** The coherent wrong seed shares the completion-referenced
gamma limit but has Weyl means tending to1, so any such bridge must retain
zero-boundary information that the completed quotient alone removes.

The next discriminating theorem is a source-derived signed estimate for the
depth increments, possibly after an explicit gamma counterphase transport,
with a uniform error for every large A and fixed h. A proposed transport must
state its actual map and fail on coherent wrong-seed and alias controls.

See [claim/attempt ledger](CLAIM_LEDGER.md), [validation](VALIDATION.md),
[provenance](PROVENANCE.json) and the per-front proofs/oracles. New analysis
is paper-proved with independent algorithm checks and same-model cross-review;
no new Lean certificate or external scholarly review is claimed.

Reproduce all new checks and the three cheap required repository gates:

```sh
python research/2026-11-08/quotient_signal/validate.py --output /tmp/succ-quotient-replay
```

Use `--full` to additionally repeat the unchanged native suite. The default
explicitly compares its inputs against the pinned previously tested baseline.
