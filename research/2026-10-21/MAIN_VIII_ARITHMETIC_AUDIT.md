# Main VIII arithmetic integration audit

Date: 2026-10-21. Reviewer: cloud arithmetic constructor, with a separate
reconstruction of the argument. This is a same-model mathematical review and
an exact computational cross-check, **not an external referee report**.

## Pinned scope and verdict

Incoming PR #212: `04dc97022d4b75e8d229128de50509c413d86b8b`.
Files reviewed on the unreviewed integration union
`c82f5e34145661d96e87612d0a8cc633759409b7`, not on main:

| File | SHA-256 |
|---|---|
| `research/2026-10-20/ABC_EFFECTIVE_MEAN.md` | `c7447c22aeaac0889d0b05a816fbbe3f402163481a7fc422d8a193ca5d883a62` |
| `observational_succ/abc_effective_mean.py` | `4dce1bdecae86e23a7895abfa32fdc9f60c7ae5bf064c5a59c5f5a24dbb5fa45` |
| `tests/test_abc_effective_mean.py` | `4528b73cbba643fe23362a4586509696df51b3829b91d4c457fc1cce6c8a162f` |

**Verdict:** the effective mean-value theorem and the genuine obstruction at
and above `t=1` survive this review. No mathematical integration blocker was
found in this family. Preserve **PROVED PAPER**, not a whole-theorem formal
status. Academic priority remains **UNVERIFIED**. The open interval between
the established upper bound `t<2/3` and the obstruction `t>=1` is unchanged.
This verdict covers these arithmetic statements, not the entire union.

## Independent reconstruction of the load-bearing steps

Write `H=abc/rad(abc)`, with positive ordered primitive `a+b=c<=X`, real
`X>=2`. For pairwise-coprime positive `d,e,f`, put `D=def` and
`M=floor(X/2)`.

1. **Uniform absolute counting.** In the raw count, slice `a=du`.
   The condition `f|(du+ev)` gives one residue class for `v` because
   `gcd(e,f)=1`. Its discrepancy from `(X-du)/(ef)` is at most one.
   With `n=floor(X/d)` and `theta=X/d-n`, direct summation gives
   `X^2/(2d)-sum_{u=1}^n(X-du)=d(n+theta^2)/2`, between zero and `X/2`.
   Thus the raw discrepancy is at most `X/d+X/(2ef)<=3X/2`, including
   `d>X` and fractional cutoffs. This is an absolute error, not a relative
   asymptotic for arbitrary moving moduli.

2. **Actual global primitivity.** Full Möbius inversion replaces each
   modulus by `d/gcd(d,k)`, etc., after dividing the source triple by `k`.
   Pairwise coprimality makes their product `D/gcd(D,k)`. The resulting
   main coefficient is
   `D^(-1) sum_{k>=1} mu(k)gcd(D,k)/k^2`
   `=1/(zeta(2)D) product_{p|D} p/(p+1)`.
   The normalized tail is at most `sum_{k>M}1/k^2<=1/M`; the row errors
   sum to `(3/2)X H_M`. This proves the displayed uniform discrepancy.
   Terms with `gcd(k,D)>1` cannot be omitted: at `(X,d,e,f)=(4,2,1,1)`
   that shortcut gives two points, whereas exactly one is primitive.

3. **Positive expansion and moment input.** Prime-power telescoping gives
   `g_t(p)=0` and
   `g_t(p^k)=p^{t(k-1)}-p^{t(k-2)}>=0` for `k>=2`.
   Every occupied product satisfies `D<=H^2`. Distinct reduced primitive
   slopes differ by a nonzero determinant divisible by `D`, hence
   `N_X<=1+X^2/D`. On `H<=X`, this absorbs the singleton and sums to
   `2E_3(t)X^2`. For the remaining points, the exact radical-pair Euler
   sum bounds the number with `H>y` by
   `3B_eta X^(2+2eta)y^(-2/3)`.
   Layer-cake integration from `y=X`, with
   `eta=(2/3-t)/2`, gives the stated quadratic bound for `t<2/3`.
   The integration cannot be used at its divergent endpoint.

4. **Product cutoff and limit order.** For `t<s<2/3`, a selected product
   `D>Y` forces `H>sqrt(Y)`. Positivity bounds its aggregate contribution
   by `K_s Y^(-(s-t)/2) X^2`. For `D<=Y`, the coefficient mass is at most
   `Y^alpha E(t,alpha)` provided `alpha>t` and `2alpha-t>1`.
   Apply the uniform count only to this finite sum. To bound the density
   tail, first fix a second finite cutoff, take `X` to infinity, and then
   increase that second cutoff. This proves the density tail without
   presupposing the full mean-value limit or interchanging uncontrolled
   infinite sums.

5. **Rate optimization.** Put `s=2/3-h`, `alpha=(1+t+h)/2`,
   `beta=(s-t)/2`, where `0<h<2/3-t`. Then
   `alpha+beta=5/6` and
   `r=beta/(alpha+beta)=(2-3t-3h)/5>0`.
   The choice `Y=(X/(1+log X))^(6/5)` is at least one for `X>=2`.
   Since `M>=X/4` and `H_M<=1+log X`, the error is bounded by the stated
   explicit constant times `((1+log X)/X)^r`. Absorbing the logarithm
   yields every power exponent `0<delta<(2-3t)/5`, **not the supremum**.
   The constants depend on the fixed parameters `t,h` (or `t,delta`),
   and are not uniform as the endpoint is approached.

## The `t>=1` obstruction is a theorem, not a failed method

At `t=1`, retain only the three single-slot divisor selections `2^k`,
`2<=k<=K`. Each has weight `2^(k-2)` and normalized fixed-divisor density
`(2/3)/(2 zeta(2) 2^k)`. Their total limiting contribution is therefore
`(K-1)/(4 zeta(2))`. For each fixed `K`, positivity gives this lower
bound for the liminf of `S_1(X)/X^2`; sending `K` to infinity proves
divergence without interchanging a moving cutoff and a limit.

The quantitative version also survives: sum the absolute errors to get
`3(2^(K-1)-1)((3/2)XH_M+X^2/(2M))`. Taking
`K=floor(alpha log_2 X)`, fixed `0<alpha<1`, makes this
`o(X^2 log X)`. Subsequently taking `alpha` to one gives
`liminf S_1(X)/(X^2 log X)>=1/(4 zeta(2) log 2)`.

For `t>1`, take `a=2^(floor(log_2 X)-1)` and positive odd `b<=X-a`.
For real `X>=8`, `X/4<a<=X/2`, there are at least `X/8` such `b`,
and `H>=a/2>X/8`. Thus `S_t(X)>=8^(-(t+1))X^(t+1)`.
No assertion about the unresolved `2/3<=t<1` range follows from this.

## Exact finite cross-checks on the pinned union

Python `3.12.14`, interpreter
`/workspace/scratch/0a4459d8f487/vii-venv/bin/python`:

| Command | Outcome |
|---|---|
| `python -m unittest discover -s tests -p test_abc_effective_mean.py -v` | 11 tests passed, 0.226 seconds |
| `python scripts/abc_effective_mean_probe.py` | 1,729 cases, zero failures; exact maximum raw error/budget `3289/4040`, finite-center error/budget `25/42` |
| `python scripts/main_vii_arithmetic_holdout.py --max-x 35 --max-divisor 9` | 8,398 Farey slope controls; 8,398 full Möbius controls; 17,784 raw lattice controls; 600 divisor-expansion controls; zero failures |

The last script imports no SUCC arithmetic module: its Farey recurrence,
direct lattice census and Möbius-derived coefficients provide computational
methods distinct from the production implementations. Its census SHA-256 is
`0468623867aa562fc05d4498d9b77759a66e134d79c573d3d30dfc08c4a0edeb`.
Re-running a pre-existing holdout is not a new external referee.

An initial `pytest` invocation could not run because pytest is absent from
this interpreter. The repository's unittest suite ran successfully instead.
No full suite or new Lean build was run in this lane. These finite checks
support implementation fidelity; the universal conclusions above rest on
the reconstructed paper argument.

## Integration and next obligation

The PR #214 cofactor identity `DU=abc<=X^3/4` is compatible with this proof.
The implication `D>X^2 => U<X/4` is one-way. It does not sum the high-divisor
incidences or remove multiplicity. The next unresolved aggregate obligation
is a source-faithful bound on the high-product divisor sector for some
`t>=2/3`, or a nontrivial explicitly restricted family in that range.
Simply renaming this sector as a cofactor sum is not an improvement.

No source archive, common claim registry, or mathematical implementation was
modified by this audit. Historical receipts remain historical. The combined
repository gates and final integration verdict belong to the coordinator.
