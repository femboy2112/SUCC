# Hostile audit of the Gaussian–Machin Padé theorem

Scope: `GAUSSIAN_PADE.md`, equations (1)–(13) and GP-03. Same-model paper
review, not external mathematical review or formal-kernel certification.
No theorem file was edited by this reviewer.

**Verdict:** the real convergence and the all-`k>=2` valuation theorem at
Padé degrees `n=2^k` survive this audit. The statement does **not** extend
its divisibility conclusion to all positive integer degrees. That distinction
is essential, not merely cosmetic.

## Checked mathematical steps

1. The partial-fraction residues in (4) match at `m=0,...,n` and the difference
   vanishes at infinity. Multiplying the identity by the log-series sign gives
   precisely the positive leading remainder coefficient in (5), with alternating
   signs thereafter. The `n=1` check is `Q=2+z`, `P=2z`, leading remainder
   `z^3/6`; the sign agrees.
2. Expanding `(1+zt)^(-n-1)` and integrating its beta moments yields
   `(-1)^j (n+j)!^2/[j!(2n+j+1)!]`. Both the complex evaluation at the stated
   `z_q` and its 2-adic evaluation lie in their respective convergence disks.
   No interchange between complex and 2-adic limits is used.
3. In the Legendre expansion at `-iq`, every summand has common phase
   `(-i)^n`. Consequently the real modulus cannot vanish, and retaining the
   leading monomial gives (7). Combining the three exponents from `z^(2n+1)`,
   the chord denominator, and `Q` gives exactly `(2/q)^(2n+1)`, as in (8).
4. The Gaussian identity `alpha_5^4/alpha_239=i` gives the Machin angle only
   after selecting a branch. The stated elementary arctangent bounds place
   `4 atan(1/5)-atan(1/239)` in `(0,pi/2)`, so the branch selection is valid.
5. For odd `q`, `q^2+1` has rational valuation one, so `v(q-i)=1/2` and
   `v(z_q)=1/2`. In `Q_2(i)`, the log converges and is additive on `1+m`;
   `i` lies there and its logarithm is zero since it is torsion. This is a
   legitimate zero local period, not an attempted 2-adic definition of pi.
6. At `n=2^k`, the constant term of `Q` has valuation one. Every intermediate
   term has valuation at least `k-v_2(j)+j/2>1`, and the final term has
   valuation `n/2>=2`. The unique least-valued term excludes denominator
   cancellation and proves exactly `v(Q)=1`.
7. The coefficient valuation estimate can be checked without quoting Kummer:
   factorial valuations give
   `v_2 binom(M,r)=sum_(a>=1)(floor(M/2^a)-floor(r/2^a)-floor((M-r)/2^a))`.
   Each summand is 0 or 1, and all vanish for `2^a>M`, so the total is at most
   `floor(log_2 M)`. This proves the denominator bound used in (12).
8. Monotonicity of the lower bound in (12) is valid already for `n>=4`:
   the derivative is `1/2-2/((2n+1+j)log 2)>0`. A rational elementary bound
   `log 2>2/3` makes this strict without a floating oracle.
9. The convergent remainder divided by `Q` loses exactly one valuation unit.
   Under `2n+1<2^(k+2)`, the real lower valuation bound is strictly greater
   than `n-2k-9/2`; integrality of the valuation of the **rational** `b_n`
   therefore yields `v_2(b_n)>=n-2k-4`.
10. Imaginary-part extraction is valid algebraically in both fields:
    `2 Im L=(L-conjugate(L))/i`. Conjugation preserves the unique local
    valuation. Subtracting the torsion log identity and its conjugate leaves
    only the controlled approximation errors. There is no illicit use of an
    ordering or an analytic imaginary-part map in the 2-adic field.
11. Any representation `b_n=B_n/A_n` has
    `v_2(A_n)-v_2(B_n)=-v_2(b_n)`, invariant under common rescaling. The real
    error bound is less than 1 for every `n>=1`, and `pi>3`, so `b_n>2` and
    its valuation is finite; no hidden `b_n=0` case is needed.
12. GP-03 is valid for the explicitly fixed arguments and coefficients and
    degrees `n=2^k`. A fixed finite coefficient/normalization valuation loss
    changes only the additive constant. A degree-dependent coefficient or
    denominator schedule is outside this proof.

## Retained corrections requested from the author

- Qualify the introductory claim of 2-adic convergence by **along the
  power-of-two degree subsequence**. Real convergence holds for all degrees,
  but the denominator lemma does not.
- Replace “real principal logarithm” with “complex principal logarithm.”
- Keep the non-power-of-two mutation explicit. At `n=3,q=5`, the denominator
  valuation is `15/2`, which falsifies an all-degree extension of (11).
- Match the recorded mutation count to the final script: the inspected script
  had acquired a third mutation/tilt check while the manuscript still said two.

These requests concern scope, terminology, and receipt consistency; no change
to GP-01, GP-02, or the stated GP-03 hypotheses is required.
A subsequent reread confirmed that the root incorporated the introductory
power-of-two qualification, complex-log terminology, and three-check receipt.
The manuscript also retains the new degree-three positive-tilt countercontrol
and its initially reversed error-sign assertion rather than suppressing that
failed test. The mathematical scope in this audit remains unchanged.

## Independent arithmetic implementation

A separate exact tuple-of-Fractions implementation evaluated `Q_n(z_q)` via
**the three-term Legendre recurrence**, not the manuscript script's binomial
coefficient polynomial evaluation:

`(j+1)P_(j+1)(w)=(2j+1)wP_j(w)-jP_(j-1)(w)`,
`w=-iq`, `z_q=(-2+2qi)/(q^2+1)`, `Q_n=z_q^n P_n(w)`.

All 30 fresh cases
`n in {4,8,16,32,64,128}`, `q in {11,13,29,43,101}` passed both
`v(Q)=1` and the **exact rational squared** version of the Archimedean lower
bound (7). The separate `n=3,q=5` control returned `15/2`.
These finite calculations test the implementation and normalization, not the
infinite quantifiers. The paper checks above supply the universal argument.

The official MIT 18.785 Fall 2021 Problem Set 10, Problem 2(c,d,h), was opened
and checked for the classical logarithm domain and homomorphism assertions:
<https://ocw.mit.edu/courses/18-785-number-theory-i-fall-2021/mit18_785f21_pset10.pdf>.
Its problem statements support precisely these standard facts; no broader
restricted-exponent or pi-normality conclusion is imported.

## Remaining mathematical boundary

A subsequence with no radix gain does not rule out every other subsequence,
a true simultaneous Hermite–Padé system, or all other multi-logarithm forms.
The result closes the advertised power-of-two componentwise Padé attempt.
A claimed global impossibility theorem for all Machin approximants would
exceed the proof. No new R0 bound or pi restricted exponent follows here.


## Replayable audit receipt

The independently written Legendre-recurrence checker is
[pade_audit_probe.py](pade_audit_probe.py); its exact output is
[PADE_AUDIT_RESULTS.json](PADE_AUDIT_RESULTS.json).
Reproduce with
`python research/2026-11-12/leah_gamma_twist/pade_audit_probe.py`.
The saved script was rerun successfully after packaging. It imports neither
`gaussian_probe.py` nor any shared Gaussian arithmetic implementation.
