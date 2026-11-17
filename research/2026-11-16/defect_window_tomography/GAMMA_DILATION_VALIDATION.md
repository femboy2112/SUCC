# Gamma-dilation bridge — reproducible validation scope

**Date:** 2026-11-16. **Research head:** tracked through draft PR #657; see its changed-files view for the latest commit. This receipt describes **executed checks**, independent of the algebraic paper proofs in [the manuscript](GAMMA_DILATION_ANALYTIC_SEED.md). It does not upgrade the original BBP/π normality frontier.

## Executed exact symbolic controls

Environment: Python 3.13.5, SymPy 1.14.0, mpmath 1.3.0, assistant's Python execution kernel. The five SymPy expressions below **all simplified exactly to zero**; these expressions match source-independent equations GDB6–GDB14 with formal real \(y,k\) and a separately carried nonzero endpoint symbol \(z\).

~~~python
import sympy as s
y,k,z = s.symbols("y k z",real=True,nonzero=True)
L=1-2*s.pi*s.I*y
Lp=1-2*s.pi*s.I*(y+k)
M=z/L
Mp=z/Lp
dL=Lp-L
dM=Mp-M
checks={
 "boundary_zero": s.simplify(L*M-z),
 "mixed_compensation": s.simplify(L*dM+M*dL+dL*dM),
 "finite_gamma_gap": s.simplify(dM/z-2*s.pi*s.I*k/(L*Lp)),
 "jet_formula": s.simplify((1-z/M)-2*s.pi*s.I*y),
 "forward_Gamma2_integral": s.simplify(
    (s.exp(1)/2)*(s.exp(-L)/L+s.exp(-L)/L**2)
    - s.exp(2*s.pi*s.I*y)*(L**-1+L**-2)/2),
}
assert set(checks.values()) == {s.Integer(0)}
~~~

Executed output:

~~~text
boundary_zero: 0
mixed_compensation: 0
finite_gamma_gap: 0
jet_formula: 0
forward_Gamma2_integral: 0
~~~

**Independence:** SymPy's symbolic rewriting and Gamma integral evaluation are different routes within one classical derivation; they are not external, blind mathematical refereeing.

## Executed nontrivial complex-parameter incomplete-Gamma check

With 40 mpmath digits, the direct quadrature

~~~python
import mpmath as m
m.mp.dps=40
a=shape+1j*omega
lam=1-2j*m.pi*x
direct=m.quad(lambda u:u**(a-1)*m.exp(-lam*u),
              [1,4,12,40,m.inf])/m.gammainc(shape,1,m.inf)
reference=(m.gammainc(a,lam,m.inf)*lam**(-a)/
           m.gammainc(shape,1,m.inf))
difference=abs(direct-reference)
~~~

was executed at these **declared finite** parameter choices:

| \(\sigma\) | \(\omega\) | \(y\) | Observed \(\lvert\mathrm{direct}-\mathrm{reference}\rvert\) |
|---:|---:|---:|---:|
| 1 | 0 | 0.125 | printed 0 at 40-digit working precision |
| 2 | 0 | -0.125 | \(1.15687725073\times10^{-41}\) |
| 2 | 0.7 | 0.125 | printed 0 at 40-digit working precision |

This is a numerical diagnostic, not an interval-certified proof. The identities are justified independently by the Laplace integral and analytic continuation in the right half-plane.

## Executed forward-time Simpson calibration

A separate standard-library direct \(t\)-integral in the conditional Gamma(shape 1 or 2) forward clock used even Simpson \(N=8192\), \(0\le t\le\log_{16}44\), and compared to the explicit formulas.

| Shape | \(y\) | Absolute difference |
|---:|---:|---:|
| 1 | 0.125 | \(2.7880541330005276\times10^{-15}\) |
| 2 | 0.125 | \(3.675728001207349\times10^{-15}\) |
| 2 | -0.125 | \(3.675728001207349\times10^{-15}\) |

The positive mass beyond \(u=44\) is exponentially tiny, but these values are numerical checks, **not** sound interval certificates.

For the fixed original positive \(x=\pi/16\), the ratio of the existing GM9 absolute-error ceiling \(7/(4n)\) to the moving-frequency Gamma(2) reference magnitude \(|1-2\pi i16^nx|^{-2}\) was independently evaluated as:

~~~text
n=1     6.836136372e2
n=2     8.727942057e4
n=5     5.857164045e11
n=10    3.220009986e23
~~~

These reinforce the *proved order comparison*: the known error ceiling is insufficient to certify a relative phase at that moving frequency. They do **not** measure the actual Green calibration error, which might be smaller.

## Committed finite test suite and what has **not** been claimed

The test module [tests/test_gamma_dilation_seed.py](../../../tests/test_gamma_dilation_seed.py) has focused symbolic-rational models (Gaussian-rational pairs) and declared-tolerance Simpson/complex controls. The endpoint continuation below adds explicit mpmath precision to two comparisons. Run it via:

~~~sh
python -m unittest discover -s tests -p 'test_gamma_dilation_seed.py' -v
~~~

**Not executed from this session:** that actual GitHub-hosted Python file as a complete unittest module, the full root unittest suite, the three other AGENTS.md gates, Main XXIV/XXV/XXVI research gates, Lean proof compilation, and an external source-specific experiment. GitHub-hosted CI may be running separately; its status must be checked against the exact final PR head before making any pass claim. No imaginary CI outcome is recorded here.

## Endpoint continuation: actual module replay and precision repairs

The later endpoint-coercivity round executed the committed module under
Python 3.12.14 and mpmath 1.3.0. Its first replay found two numerical failures:

- Reassociating binary floating-point products at large magnitude broke an
  absolute eleven-decimal-place check of logarithmic transport.
- At large clocks, binary floating point rounded `1+q^2` to `q^2`, erasing
  the strict inequality `1/(1+q^2)<1/q^2`.

The repair retains the exact rational transport checks and evaluates the
two numerical comparisons inside `mp.workdps(70)`. The first comparison now
requires an absolute difference below `1e-60`; the second retains its original
strict inequality. Neither repair changes a source law or weakens a theorem.
The repaired focused module ran **13 tests, all passing**. The initial failed
full-suite logs are retained in
[the first complete attempt](endpoint_checks/first_full_suite_attempt/full_suite_shard_4.txt).
See [the endpoint validation record](ENDPOINT_COERCIVITY_VALIDATION.md) for
the subsequent complete repository replay and other gates.

The earlier “not executed” paragraph describes the original Gamma session;
this dated continuation supplies the actual later replay. It does not
retroactively claim that the earlier session executed those checks.

## Verdict and next probe

- **Disclosed classical identities:** Gamma/Laplace integral, upper-incomplete-Gamma specialization, moving-frequency chain rule, exact endpoint/mixed compensation, and inverse-conditioning formulas under stated domains.
- **Corroborated at implementation level:** five independently simplified symbolic identities and scoped complex quadratures; no physical/arithmetical independent-witness claim.
- **UNVERIFIED:** whether native zero-seeded BBP observations provide a stable, independently accessible Gamma analytic seed predicting source-selected future signed defects.
- **OPEN:** R0, π-normality, RH, completed Weil positivity.

A verdict-changing experiment must calibrate the new continuum/forward scale instrument on authenticated source histories, establish a high-frequency source-relative error budget, preserve the original \(U_0=0\) and winding, and split a predeclared new-window prediction from the coherent wrong-seed/locked and finite-shadow controls.
