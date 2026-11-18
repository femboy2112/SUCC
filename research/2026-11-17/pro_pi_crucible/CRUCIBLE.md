# Hostile division: retained failures and exact source boundaries

The original source is never replaced in an original-source claim. Every
changed seed, forcing, endpoint, or observer below is a control with its
own source label. A control can refute a proposed implication without
refuting R0 for pi.

## 1. Mandatory controls

| Control | Prediction required of a valid argument | Evidence in this operation |
|---|---|---|
| Same forcing, seed s=-pi/16 | Completed real-circle orbit locks at zero. The literal seed must be used by any purported proof. | Exact identity; inherited #662 wrong-seed test replayed. EPS has no claim about p-adic denominators of this irrational-seeded state. |
| Shell-dependent winding-erasure seed | Exponentially small seed error can remove the last-B terminal block. Uniform seed stability cannot imply coercivity. | Inherited endpoint/terminal-wall reports inspected; stronger zero-seeded forcing perturbation GSC derived here. |
| Terminal cofactor clone | Same terminal fractional phase, denominator and odd-primary residues can coexist with a cold backward norm. | #662 cofactor/phase-fiber tests replayed; global extension GG-01 below. The full radix residue tower is not preserved. |
| Gamma-matched all-prefix counterfeit | Any finite authentic prefix plus the leading source asymptotic can extend to a locked orbit. | #662 matched-source tests replayed; H-01--03 strengthens to every asymptotic coefficient and exact finite clock principal parts. |
| Two-BBP-form locked counterfeit | Nonzero pole-orbit obstruction, positivity, monotonicity and zero seed alone must not imply R0. | #657 source construction inspected; eight exact tests replayed. Its completed endpoint is 13/128. |
| Sparse irrational / Kempner control | Irrationality and infinite nonperiodic information must not be promoted to R0. | #657 sparse-source cold-shell exact test replayed. No irrationality-exponent bridge is assumed or proved. |
| Periodic rational shadows | A finite observation can have a nonnormal rational completion; finite agreement is not a uniform bound. | Exact fixed-phase Borwein controls and H-01--02. Growing-period approximation remains an inherited obstruction. |
| Source gauge | Correctly transformed forcing and tail preserve the completed orbit while changing raw carries. | GG-01, exact proof plus 80 chronological finite states. |
| Gamma false positives / observer masks | Positive moment forms, nonzero jets, hidden variance or Haar masks cannot supply signed source saving. | GSC preserves all-degree positive forms up to relative geometric error while its selected shell is cold; periodic measures reject a temporal reading of the Borwein inverse. |

Not every inherited historical numerical experiment was rerun. The exact
commands and scopes actually replayed are listed in VALIDATION.md.

## 2. GG-01: one global integer gauge erases every raw terminal block

Let U_n be the literal original zero-seeded rational history, and let
q_n=floor(n/2). Define for all n>=0

\[
g_n=-\bigl(\lfloor U_n\rfloor\bmod16^{q_n}\bigr).
\]

For n=0 this is zero. For all n, g_n is an integer and
|g_n|<16^{floor(n/2)}. Define a changed forcing and its own zero-seeded state:

\[
r^g(n)=r(n)+g_n-16g_{n-1},\qquad
U^g_0=0,\quad U^g_n=16U^g_{n-1}+r^g(n).
\]

Then induction gives U^g_n=U_n+g_n. Integer shifts preserve, at **every**
clock, the fractional state, the reduced denominator, the numerator modulo
that denominator, and every odd-primary rational principal part. They also
preserve the denominator of each forcing term. The new forcing is generally
not positive or a rational function of the clock; it is a different source.

The weighted forcing series converges absolutely because the gauge grows
at most as 16^(n/2). Its tail telescopes:

\[
T^g_n=\sum_{j\ge1}16^{-j}r^g(n+j)=T_n-g_n.
\]

Indeed the finite gauge sum is
16^{-J}g_(n+J)-g_n, whose first term tends to zero. Therefore

\[
U^g_n+T^g_n=U_n+T_n=16^n\pi/16.
\]

The completed original orbit and the zero seed are unchanged. Yet at n=2B,

\[
\lfloor U^g_{2B}\rfloor
=16^B\left\lfloor\frac{\lfloor U_{2B}\rfloor}{16^B}\right\rfloor.
\]

Its last B digits are all zero, so D_B^g=J_B^g=0. With
u_(2B)=U_(2B)-floor(U_(2B)) in [0,1),

\[
\mathcal R^g_B
=\frac{u_{2B}^2(1-256^{-B})}{255B}<\frac1{255B}.
\]

To verify the norm, divide by 16^k for 1<=k<=B. The integer part is divisible
by 16^k and u_(2B)/16^k lies in [0,1/16); its circle distance is itself.
Sum the geometric squares. This proves the all-B assertion, separately
from the 80-state implementation check.

**No contradiction with the inherited equivalence:** the tail T^g_n is
positive here but can be as large as 16^(n/2); it no longer has the original
small-tail bound. A raw terminal norm is source-gauge dependent. Applying
the fixed original-tail equivalence to this transformed source would be
the invalid step.

GG-01 also shows that even a complete chronological sequence of fractional
principal parts need not fix the integer carry presentation. The complete
rational state history does fix it; that stronger history was not preserved.

## 3. Two different source counterfeits, not one impossible conjunction

| Property | GSC f_B | H-01--03 fixed counterfeit |
|---|---|---|
| Literal zero seed | Yes | Yes |
| Positive and decreasing rational values | Yes | Yes |
| Complete positive moment cone | Yes | No for the concrete M=0 case; H-04 proves failure |
| Arbitrary exact authentic prefix | Not asserted | Yes |
| Every authentic asymptotic coefficient | No; leading coefficient only | Yes, with superexponential error |
| Exactly four finite clock poles | No; adds shifted poles | Yes, by an entire nonrational correction |
| Same weighted pole-orbit obstructions | Yes | Same finite principal parts; no rational coboundary claim |
| Fixed original rational function | No | No |
| Empty prescribed B-shell | Yes, with source depending on B | Yes at every sufficiently late shell of one source |
| Entire Gamma completion locally close | Yes, with explicit geometric bound | Not asserted |

The counterfeits defeat different relaxations of the passport. Their
preserved properties cannot be combined into a fictitious stronger control.

## 4. Failed candidate mechanisms retained

1. **Rational coefficient nonzero implies survival modulo p.** False without
   a numerator-height estimate. The p=19 and p=73 cancellations are retained.
   EPS-01 repairs exactly this step; it does not repair the winding gap.
2. **Rate-6 denominator growth is new.** Refuted as a novelty claim by the
   inspected CG-01 manuscript. Only the explicit shrinking cutoff is new
   relative to that source.
3. **Stable entire Gamma geometry gives a locally uniform wall lower bound.**
   Refuted by GSC, including simultaneous all-degree relative moment bounds.
   An exact-source theorem with a nonuniform onset is not refuted.
4. **All asymptotic jets and signed finite clock poles authenticate enough
   statistics.** Refuted in the broader meromorphic class by H-01--03.
   A global rational-function restriction rejects this counterfeit but
   still does not prove statistical saving.
5. **The flat locked counterfeit also preserves every positive moment
   constraint.** Refuted by H-04's exact negative alternating difference.
6. **The factor 1/8 in the Borwein Neumann inverse is a time contraction.**
   Refuted by the invariant measures delta_0 and delta_(1/15). It acts on
   reconstruction error in the origin variable of a fixed measure.
7. **Many terminal probes reconstruct chronological impulses.** Refuted by
   the inherited rank-one terminal map; its full history map is triangular
   and invertible. The corresponding exact tests were replayed.

The surviving boundary is an exact arithmetic inequality using the original
global rational source, literal zero seed and integer winding together.
No computation or proof here establishes that inequality.
