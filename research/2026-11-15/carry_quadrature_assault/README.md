# Carry quadrature assault: exact excitation, unresolved signed density

**2026-11-15 · original BBP source · original zero seed**

This follow-up attacks the fourth-root gate named in the preceding SUCC
conversation. It proves a uniformly nonzero, temporally coupled source
response and a bounded reference that recovers the actual carry quadrature.
It also makes the quantized winding and the missing joint sign law explicit.
**The positive lower shell density, R0, and pi normality remain open.**

## What was obtained

For the authentic rational recurrence

\[
U_0=0,\qquad U_n=16U_{n-1}+r(n),\qquad
C_n=\lfloor U_n\rfloor,\quad y_n=U_n-C_n,
\]

where r is the original four-pole BBP forcing, define
m(n)=ceil(log_4 n), q_n=16^(m(n)), and s_n=n+m(n). The finite response

\[
R_n=U_{s_n}-q_nU_n
\]

obeys the all-index bound

\[
\boxed{1/128<R_n<1/4\qquad(n\ge4).}
\]

Hence the response Delta_(n,theta)=e(theta U_(s_n))-e(theta q_n U_n)
has squared magnitude greater than 4 sin^2(pi theta/128), for theta=1 or1/4.
Its summed intensity is bounded below by a fixed positive multiple of B on
**every** late B-shell. This is a proved source-excitation bound, distinct
from a signed-distribution bound.

The finite source reference J_(n,theta)=1-e(-theta R_n) gives

\[
\boxed{
\frac{\Delta_{n,1/4}\overline{J_{n,1/4}}}{|J_{n,1/4}|^2}
e(-y_{s_n}/4)=i^{C_{s_n}},\qquad
|J_{n,1/4}|>2\sin(\pi/512).
}
\]

The inverse gain is uniformly bounded. Delaying observations to s_n changes
bounded shell means by at most 2m(2B)/B. Thus this instrument measures the
same asymptotic gate with a declared source reference and carry correction.
One arm already observes the later source phase; this is an exact readout,
not a claim of computational acceleration or a distribution proof.
The reference division has bounded gain; deciding the correct carry branch
still requires its declared source observation and boundary certificate.

## The closed-loop statement and the signed target

The inherited authentic dyadic isometry gives, for n,k>=0,

\[
v_2(U_{n+2^k}-U_n)=k.
\]

Therefore a loop that closes at k dyadic bits flips the next-bit character
by exactly -1 and has squared character response 4. This is closure in a
finite source quotient, not a return of the full unwrapped rational state.
The exact transport is

\[
\chi_{2^{k+1}}(C_{n+2^k}-C_n)
=-\chi_{2^{k+1}}(-(y_{n+2^k}-y_n)).
\]

The actual four-pole clock obeys [U_n]_4=n mod4, and therefore

\[
\boxed{i^{C_n}=i^n\chi_4(-y_n).}
\]

The unresolved statistic is the temporal correlation of that clock with the
fractional cofactor. The clock alone also survives 2-integral rational seed
changes after time zero; the cofactor retains the real source selection.

The targeted signed quadrature has values (1,-1,-1,1) on carry residues
(0,1,2,3). Its non-locking indicator is

\[
A_n=1_{\{C_n\bmod4\in\{1,2\}\}},\qquad
w(C_n)=1-2A_n.
\]

The desired theorem is liminf_B B^-1 sum_(B<=n<2B) A_n>0. It would imply
R0 with the quantitative margin delta*(1-cos(pi/8)). It is a sufficient
condition for R0, not a general equivalence to R0 or to full normality.

## Quantized winding resolves the missing sign into three cells

Define M_n=floor(U_n+1/2), epsilon_n=U_n-M_n, and
K_n=M_(n+1)-16M_n. Every nonzero K_n at n>=1 forces

\[
|e(U_n)-1|^2+|e(U_{n+1})-1|^2\ge9/257.
\]

The published irrationality bound for pi yields at least one such winding
in every sufficiently late [M,8M), hence logarithmically many up to N.
This restates the inherited logarithmic mechanism in a literal integer
winding observable; it improves neither the known rate nor the stronger
inherited signed deficit.

The target indicator has the exact decomposition

\[
\boxed{
A_n=1_{\{K_{n-1}\equiv2\ (4)\}}
+1_{\{K_{n-1}\equiv1\ (4),\epsilon_n\ge0\}}
+1_{\{K_{n-1}\equiv3\ (4),\epsilon_n<0\}}.
}
\]

| K_(n-1) mod4 | epsilon_n >= 0 | epsilon_n < 0 |
|---:|:---:|:---:|
| 0 | No event | No event |
| 1 | Event | No event |
| 2 | Event | Event |
| 3 | No event | Event |

This is the precise joint winding/sign law a new source estimate must
restrict. Extensive packet counts alone need not populate these cells.

## Controls that identify the necessary source information

The controls are typed by the premise they change; none is a counterexample
to the original four-pole, zero-seeded gate.

- **Same forcing, changed seed:** a scaled Thue–Morse endpoint has positive
  winding packets at density 1/2, all in residue three with positive ending
  phase, and no selected events after time four. It still has R0. This
  separates response magnitude from the chosen signed orientation.
- **Same forcing, changed seed:** a Kempner endpoint of irrationality
  exponent two has no selected raw-carry events for n>=3. The future-tail
  borrow removes its sparse true one-digits.
- **Changed source, genuine zero pin:** a constructive analytic Mahler
  family preserves rational odd-denominator states, zero seed, global
  dyadic isometry, backward source zero, and the leading forcing decay,
  but has no selected events. For each fixed L, it can also match the
  authentic source and clock modulo 2^L at every index. Its freely chosen
  denominators break the exact finite four-pole law. The quantifiers are
  forall L, exists a changed source, not one changed source at all depths.

The next arithmetic estimate must therefore retain the literal pole law
and zero boundary together. NEXT.md exposes the exact growing odd-modulus
recurrence rather than replacing the source by a generic isometry.

## Finite source certificates

The probe certified raw carries for 1<=n<=32768 using an outward integer BBP
prefix enclosure and rigorous Green-tail comparisons. It used no numerical
pi oracle. There were no tail borrows in this finite range; each absence was
certified, not inferred from a tolerance.

| Shell [B,2B) | Selected events | Exact proportion | Mean quadrature |
|---:|---:|---:|---:|
| B=1024 | 509 | 509/1024 | 3/512 |
| B=2048 | 1058 | 529/1024 | -17/512 |
| B=4096 | 2083 | 2083/4096 | -35/2048 |
| B=8192 | 4047 | 4047/8192 | 49/4096 |
| B=16384 | 8178 | 4089/8192 | 7/4096 |

These are finite observations, not a fitted density model or an asymptotic
proof. The first 512 observations were checked against the exact unwrapped
rational recurrence, including all cofactor and packet/sign transports.
The two production algorithms share the inherited forcing implementation;
the standalone audit additionally expands all four signed fractions.

## Reading and reproduction

- [SOURCE_EXCITATION.md](SOURCE_EXCITATION.md): uniform pulse, reference,
  chronology, source-loop theorem, and clock/cofactor formula.
- [WINDING_PACKETS.md](WINDING_PACKETS.md): packet inequality, selected
  logarithmic count, inherited-result audit, and joint sign decomposition.
- [CONTROLS.md](CONTROLS.md): exact countermodels and source passports,
  including the fixed-precision globally zero-pinned construction.
- [CARRY_HAAR_BRIDGE.md](CARRY_HAAR_BRIDGE.md): complete carry-Haar normality
  equivalence and the dyadic Haar-wavelet energy.
- [NEXT.md](NEXT.md): remaining source-selected signed inequality and exact
  odd-modulus recurrence.
- [HOLE_CONTRACT.md](HOLE_CONTRACT.md), [CLAIM_LEDGER.json](CLAIM_LEDGER.json),
  [PROVENANCE.md](PROVENANCE.md), [AUDIT_NOTES.md](AUDIT_NOTES.md), and
  [VALIDATION.md](VALIDATION.md): scope, truth states, inputs and checks.

From the repository root:

```sh
python -m unittest tests.test_carry_quadrature -v
python scripts/carry_quadrature_probe.py --horizon 32768
python research/2026-11-15/carry_quadrature_assault/independent_audit.py
```

The mathematical advance in this round is a concrete uniform source
excitation, its stable oriented readout, and sharper source-premise
separation. No positive-density estimate for the original carry event was
obtained; that is the unchanged theorem to attack next.
