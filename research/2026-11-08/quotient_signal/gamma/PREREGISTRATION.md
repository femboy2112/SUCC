# Gamma residual: exact source calibration

Pinned parent: `a974db527c19708006b9f6d7f0ca01d08d1e0524`.
Written after the symbolic derivation and before the finite oracle run.

The candidate is precise: for the authentic Green tail `T_n`, the
harmonically compensated weighted sum `C_N=sum(n*T_n-1/(64*n))` decreases
to a source constant `C`, with `0<C_N-C<7/(512*N)`. Replacing harmonic
subtraction by logarithmic subtraction leaves `gamma/64`.
The phase product in THEOREMS is a consequence of that identity. This is
not an asserted identity for prime/complement covariance.

Finite development N: 64,127. Fresh finite holdouts: 257,521,1031.
Future-tail cutoff J=24; exact Fraction arithmetic, rational geometric
tail bound, rational Machin/atanh enclosures for constants. Use a separate
backward recurrence with terminal tail zero to check telescoping; a
finite terminal tail is not silently substituted for the infinite tail.
Check all individual tail inequalities through n=1031, exact source
polynomial identities at rational x, and literal zero-seeded unwrapped
recurrence against an independent source sum.

Controls: changing the first coefficient 4 to 5 destroys the balanced
source and gives a 1/n tail instead; the old n^-2 calibration must reject
it. Same-forcing seeds have exactly the same source-corrected tail, while
their zero-anchored *unwrapped* defect differs by -16^n*s. Test rational
seeds 0,1/7,-2/11. The coherent real seed -pi/16 is a paper control:
U_n=-T_n and its fixed-h Weyl means tend to one. No claim is made that
1/5 is a nonnormal seed.

Success is reproduction of the stated finite inequalities and source
identities. It does not prove a covariance limit, normality, or academic
priority. Raw receipts retain exact outward dyadic endpoints and source
hashes; decimal displays are supplementary.
