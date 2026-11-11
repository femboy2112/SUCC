# Finite backend soundness and source binding

Status: PROVED PAPER, supported by exact arithmetic and separate CDF checks.
The canonical source is inherited unchanged from `duck_bbp.py`. Its classical
identification with pi uses the BBP identity. This document does not turn a
finite observation into an asymptotic proof.

## 1. Integer enclosure of the authentic source

For H>=1 set S=16^H and

```math
L_H=\sum_{j=1}^H\left\lfloor16^{H-j}r(j)\right\rfloor,
\qquad \alpha=\sum_{j\ge1}16^{-j}r(j).
```

Every floor loses less than one, and the scaled omitted tail is
`T_H <= r(H+1)/15 < 1`. Therefore

```math
L_H\le S\alpha<L_H+H+1.
```

The implementation computes each term through the canonical rational
polynomial and checks equality with the four original partial fractions.
The source is a fixed primitive in this grammar, not a caller-supplied
callback certified by a name. A source hash records the assumed identity;
its contents and the arithmetic checks perform different jobs.

Take q=16^k and a clock n with n+k<=H. If

```math
\left\lfloor\frac{L_H}{16^{H-n-k}}\right\rfloor
=\left\lfloor\frac{L_H+H+1}{16^{H-n-k}}\right\rfloor=J_n,
```

then `floor(q*16^n alpha)=J_n` exactly. Setting `a_n=J_n mod q` gives
`z_n={16^n alpha} in [a_n/q,(a_n+1)/q)`. The closed upper enclosure is
handled conservatively; ambiguous cells raise an exception instead of
rounding a digit. No circular crossing is disguised as a small interval error.

The public source verifier reconstructs the entire certificate, validates
every integer field by exact type, and compares the full output. It rejects
modified clocks, bounds, phase cells, and numeric type aliases. It assumes
the Python runtime and inspected code execute as specified; it is not a
cryptographic protection against arbitrary replacement of the running program.

## 2. Certified Wasserstein defect

Let `x_n=a_n/q` and let `mu_hat` be their empirical law. Match each x_n to
its true z_n. Their ordinary interval distances are below 1/q. They have
the same leading digit because q is divisible by 16 and the certified
small cell fits inside one leading-digit cell.

Within that same cell, T multiplies the displacement by 16. Applying C
couples each pair with the same new uniform digit and divides it by 16.
Consequently

```math
W_1(\mu,\widehat\mu)\le q^{-1},\qquad
W_1(Q\mu,Q\widehat\mu)\le q^{-1},\qquad
|D(\mu)-D(\widehat\mu)|\le 2q^{-1}.
```

This is a cell-certified local comparison. It does not assert that the
discontinuous interval operator Q is globally Lipschitz.

For an N-point grid sample, the signed CDF jumps of `(I-Q)mu_hat` have
integer weights in units `1/(16N)`. At a coordinate k/q the original point
contributes 16; its sixteen uniformly replaced leading digits contribute
-1 each at `(k mod (q/16))+a*q/16`. Summing gap lengths times the absolute
integer cumulative weight and dividing by `16Nq` is the exact interval W1.
Independent tests compare this integer algorithm against the inherited
general Fraction-valued CDF implementation, including all 216 triples
from a six-point grid.

The signed-overlap identity in CONSTRUCTION.md is computed by the same
CDF partition with separate early and late cumulative weights. If each
true defect differs by at most 2/q, then the exact identity implies that
the true overlap differs from the grid overlap by at most 4/q. No positive
asymptotic overlap is inferred.

## 3. Pascal and exact digit characters

Write `omega=exp(2 pi i/16)` and reduce its powers using `omega^8=-1`.
This represents each finite weighted sum as eight rational coefficients
in the basis `1,omega,...,omega^7`. The basis is linearly independent over
Q since `x^8+1` is the sixteenth cyclotomic polynomial. In particular the
h=8 character is exact digit parity, not the circle character `e(8z)`.

For degree m, the Bernstein derivative identity gives

```math
B'_{m,j}=m(B_{m-1,j-1}-B_{m-1,j}),\qquad
\|B'_{m,j}\|_\infty\le m.
```

Here out-of-range components are zero; two nonnegative components of a
partition of unity differ by at most one. The certified next-phase error
therefore changes any fixed signed moment by at most m/q in complex
modulus. The current digit is already exact. The sum of absolute values
of the eight rational coefficients, plus m/q, bounds that moment's modulus.

For positive square m, the public Pascal upper-bound API reconstructs all
fifteen characters and all m+1 components from the verified consecutive
source window. It derives N from that window. It uses the conservative
previously stated bound

```math
W_1(\mu_N,\lambda)
\le\frac{16}{15}\left[\sum_{h=1}^{15}\sum_{j=0}^m|G_{h;m,j}|
                  +\frac1{16\sqrt m}\right]+\frac1{15N}.
```

CONSTRUCTION.md proves a stronger factor 8/15 on the signed sum. The code
keeps the conservative version. Neither result bounds the asymptotic
source-selected moments. The positive-square restriction only avoids
floating square roots in this finite API.

## 4. Inputs, certificates, and what reductions can change

Public certified observation functions always authenticate their source
window. There is no `verify=False` escape hatch. Duplicate character
requests are rejected. Negative or inexact error fields and detached
caller-supplied character tables cannot enter the certified upper bound.

Low-level grid laws and algebraic residual intervals are mathematical
inputs, not proofs of their source. A finite residual verdict is conditional
on its supplied exact interval; the published probe obtains that interval
from the source-verified constructors. No primitive outputs a claim of
pi normality or statistical contraction.

A denotationally sound beta/delta rewrite preserves the represented source
state and therefore every correctly compiled finite observation. It cannot
strictly decrease that observation's *value* merely by changing its syntax.
A sample-length contraction must compare different temporal windows and
supply a new arithmetic estimate. The exact overlap decomposition shows
where such an estimate would enter.

## Primary and repository dependencies

- David H. Bailey and Richard E. Crandall, *Random Generators and Normal
  Numbers*, Experimental Mathematics 11 (2002), 527–546:
  https://www.davidhbailey.com/dhbpapers/bcnormal-em.pdf.
  This is background for the BBP dynamical approach, not an imported proof
  that pi is normal.
- John E. Hutchinson, *Fractals and Self Similarity*, Indiana University
  Mathematics Journal 30 (1981), 713–747, Section 4:
  https://maths-people.anu.edu.au/~john/Assets/Research%20Papers/fractals_self-similarity.pdf.
  The elementary inverse-branch coupling used here is written out above.
- Ralph Kritzinger and Friedrich Pillichshammer, *Exact order of extreme
  L_p discrepancy of infinite sequences in arbitrary dimension*, Archiv
  der Mathematik 118 (2022), 169–179, Theorem 1, including d=1,p=1:
  https://doi.org/10.1007/s00013-021-01688-9.
- Inherited exact source: `observational_succ/duck_bbp.py`; inherited
  conditional Haar theorem: `research/2026-11-09/recursive_haar_pinbed/THEOREMS.md`.
  All are pinned through the unchanged base and the execution hash receipts.
