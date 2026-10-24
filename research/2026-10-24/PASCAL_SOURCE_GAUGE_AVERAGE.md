# PASC-10 — Source-ensemble Haar theorem and finite selector-grid obstruction

**2026-10-24 addendum to [PASCAL_CARRY_INTERFEROMETRY.md](PASCAL_CARRY_INTERFEROMETRY.md).** This is a separate, narrow classical covering-map theorem and exact finite arithmetic source-gauge control. It **does not establish π normality, the selected y0=0 signed estimate, or a new probability law on the real source**. It is source-faithful in its forcing, but **changes the initial selector and averages over that change**. This distinction is the central limitation.

## Statement 1: universal exact initial-selector Haar average (PROVED)

Let any fixed deterministic real forcing r(n) be given and define, for each initial x∈R/Z,

$$
y_0^{(x)}=x,\qquad y_{n+1}^{(x)}=16y_n^{(x)}+r(n+1)\pmod1.
$$

Thus y_n^(x)=16^n x+y_n^(0) mod1. Choose any finite distinct increasing integer indices W of length D, and 0<τ≤1/4. Define \(\delta,\delta^+,\eta,\kappa,E_\tau,Q_0,Z\) *exactly* as in PASC-01, with this particular x as the source selector.

For each fixed pair s≠t, the circular difference \(\delta_{s,t}^{(x)}\) is Haar-uniform as x ranges over Haar measure, because its x coefficient \(16^t-16^s\) is a nonzero integer and multiplication by such an integer preserves Haar measure.

Conditional on the successor-close event \(|\operatorname{cen}(16\delta+\eta)|\le\tau\), the sixteen inverse branches of the covering map \(T_{16}\) have **equal Haar mass** \(2\tau/16\). The integer centered carry label κ mod16 distinguishes them (including the wrap at the centered boundary). Hence, for every offdiagonal ordered pair,

$$
\mathbb E_x[1_{E_\tau}]=2\tau,\qquad
\mathbb E_x[1_{E_\tau}1_{\kappa=0\bmod16}]=\frac{2\tau}{16}.
$$

Each of D diagonal pairs contributes one to E and Z exactly. Therefore

$$
\boxed{\mathbb E_x Q_0=D+2\tau D(D-1),}
$$

$$
\boxed{\mathbb E_x Z=D+\frac{\tau}{8}D(D-1),}
$$

and

$$
\boxed{\mathbb E_x(16Z-Q_0)=15D.}
$$

For each nonempty Walsh mask A, offdiagonal uniform carry labels have mean zero, diagonals have Walsh character +1, giving \(\mathbb E_x M_A=D\) for all 15 masks. The four primitive Ramanujan shells therefore have Haar means \(D,2D,4D,8D\); their total is \(15D\).

This shows the \(O(D)\) signed-excess target holds **exactly in the full initial-selector ensemble**, for arbitrary deterministic forcing, with diagonal coefficient 15. It supplies a calibrated positive control and confirms that the diagonal allowance cannot simply be discarded.

**Selection obstruction:** the actual π source is the single point x=0. A Haar average over x cannot bound its value. This is not a proof of normality, not an actual-source time average, and not an independent Galois-embedding result. The theorem is too general to discriminate π from any other specially selected initial state.

## Statement 2: deterministic finite prime selector grid (PROVED, exact source)

Let q be an odd prime with \(\mathrm{ord}_q(16)>\max W-\min W\). For each j=0,…,q−1 substitute the initial selector \(x=j/q\), leaving *the complete original signed BBP forcing unchanged at all times*. If s≠t∈W, the integer \(16^t-16^s\) is invertible modulo q. Thus \(\delta_{s,t}^{(j/q)}\) traverses exactly one shifted uniform q-point circle grid as j varies.

Each of the sixteen inverse-branch events is a circular arc of length 2τ/16; relative to normalized grid counting its discrepancy from Haar measure is at most 2/q, with endpoint-inclusive counting. Summing the 16 branch discrepancies bounds the full event's error by 32/q, and central zero-branch error by 2/q, for each offdiagonal pair. Consequently, with \(D=|W|\),

$$
\boxed{
\left|
\frac1q\sum_{j=0}^{q-1}
\left(16Z(j/q)-Q_0(j/q)\right)-15D
\right|
\le\frac{64D(D-1)}q.
}
$$

The factor 64 is a safe, explicitly justified endpoint budget. Its size is *not* a fitted statistical confidence interval and can be sharpened only with a separate boundary audit. The order hypothesis is mandatory; if q divides any \(16^t-16^s\) the uniform-grid argument fails. A prime near 3 or 5 is not an admissible shortcut.

## Exact rational tests and adverse selected comparison

The new \`pascal_gauge_average.py\` constructs the exact forced orbits \(y_n^{(j/q)}\) from the zero-initial BBP source and integer modular powers, computes every ordered successor-close pair, and checks the finite-grid rational inequality. New \`test_pascal_gauge_average.py\`: **3 local test methods passed**, bringing the focused Pascal+dyadic total to **24**.

For the actual BBP forcing at indices W={6,7,8} (D=3), exact grid ensembles give:

| q | τ | q-grid mean signed \(16Z-Q_0\) | Haar mean | absolute error | proved bound |
|---:|---:|---:|---:|---:|---:|
| 41 | 1/4 | 1819/41 | 45 | 26/41 | 384/41 |
| 41 | 1/16 | 1909/41 | 45 | 64/41 | 384/41 |
| 97 | 1/4 | 4359/97 | 45 | 6/97 | 384/97 |
| 97 | 1/16 | 4385/97 | 45 | 20/97 | 384/97 |

These are exact Fractions, not floating approximations. The selected authentic \(p=41\) first-birth window at τ=1/16 has signed excess \(16(20)-40=280\), versus a hypothetical same-length Haar-selector mean \(15D=210\). Thus even a *small actual* window already refutes replacing the selected signed value by its ensemble mean. The source contract y0=0 must be preserved.

## Final scoped verdict

- **PASC-10a, disclosed:** for every deterministic forcing, Haar averaging over the initial selector makes offdiagonal 16 carry branches uniform, and the exact full signed mean is 15D.
- **PASC-10b, disclosed:** finite rational prime selector grid under the stated order hypothesis has a \(64D(D-1)/q\) worst-case discrepancy bound.
- **PASC-10c, observed exact finite:** the four displayed actual forcing finite grid results and hostile selected-vs-average mismatch.
- **UNVERIFIED:** any source-specific inequality of the form \(16Z(y_0=0)-Q_0(y_0=0)\le C D\) for the infinite prescribed prime windows; any universal transfer of the Haar result to the selected π source.

**Next lamp:** a source-specific **derandomization / point-selection mechanism** that distinguishes x0=0 from arbitrary ensemble exceptions, retains all later carries, and directly bounds the weighted source-corrected fifteen-mode jet. Pure initial-selector Haar averaging is contextually saturated for the target, not a proof of an impossibility for arithmetic source methods.
