# The complete carry-Haar target behind the fourth-root gate

**Status: exact reductions.** This records the carry bridge derived in the
preceding conversation, with its quantifiers and normalization. It does not
establish any of the limiting statements. The authentic source, C_n, y_n,
T_n and alpha=pi/16 are as in SOURCE_EXCITATION.md. All shell limits below
are through all positive integers B, with B<=n<2B.

## 1. Carry Haar is equivalent to the original normality target

For fixed integers m>=1 and h, put q=16^m and

\[
\varepsilon_{n,m}=\sum_{j=1}^{m}16^{-j}r(n+j),\qquad
0<\varepsilon_{n,m}<T_n.
\]

The exact finite recurrence gives

\[
\frac{C_{n+m}}q-C_n
=y_n+\varepsilon_{n,m}-\frac{y_{n+m}}q.
\tag{CH1}
\]

Thus for e(t)=exp(2 pi i t) and W_B^U(h)=B^{-1} sum e(h U_n),

\[
\left|W_B^U(h)-\frac1B\sum_{n=B}^{2B-1}e(h C_{n+m}/q)\right|
\le2\pi|h|\left(\frac1q+\frac1B\sum_{n=B}^{2B-1}T_n\right).
\tag{CH2}
\]

**Theorem.** The following are equivalent:

1. pi is normal in base 16.
2. The completed phases {16^n alpha}, or equivalently the raw phases y_n,
   are uniformly distributed on the circle.
3. For every fixed k>=1 and every a modulo 2^k,
   the shell proportion of C_n congruent to a modulo 2^k tends to 2^-k.

These are respectively the standard radix criterion, its vanishing-tail
transfer, and Haar equidistribution of the **integer carry archive** in Z_2.
The assertion in item 3 is not Haar equidistribution of the rational U_n,
which the source isometry already supplies at fixed dyadic depth.

**Proof of the new coordinate equivalence.** If item 3 holds, fix nonzero h
and choose m with q>|h|. The finite character average in (CH2) tends to zero;
shifting its time interval by fixed m changes it by at most 2m/B. Since
T_n tends to zero, limsup |W_B^U(h)|<=2 pi |h|/q. Let m tend to infinity.
The Weyl criterion proves item 2.

Conversely, U_n/q=U_(n-m)+epsilon_(n-m,m), for n>m. Therefore C_n modulo q
is the bin index of the circle phase {U_(n-m)+epsilon_(n-m,m)} in q equal
half-open bins. The perturbation tends to zero. Uniform distribution puts
vanishing limiting mass in shrinking neighborhoods of the finitely many
bin boundaries, so every bin has limiting frequency 1/q. Taking a power
q=16^m divisible by 2^k proves item 3. No boundary is silently ignored.
The usual prefix and all-integer-shell formulations of uniform distribution
are equivalent by subtraction and geometric decomposition of prefixes.

## 2. One positive exact energy for the entire dyadic archive

Let p_(B,k)(a) be the empirical distribution of C_n modulo 2^k on the shell.
Set Q_(B,k)=sum_a p_(B,k)(a)^2, with Q_(B,0)=1. Define

\[
\mathcal D_B=3\sum_{k\ge1}2^{-k}Q_{B,k}-1.
\tag{CH3}
\]

This quantity is nonnegative, despite the subtracted reference constant:

\[
\boxed{\mathcal D_B=
\sum_{j\ge0}2^{-j}\sum_{a=0}^{2^j-1}
\left[p_{B,j+1}(a)-p_{B,j+1}(a+2^j)\right]^2.}
\tag{CH4}
\]

**Proof.** The inner sum is exactly 2Q_(B,j+1)-Q_(B,j). Summing its
geometric weights telescopes to (CH3); every sum converges absolutely.
These are the squared dyadic child imbalances, an exact Haar-wavelet form.

Equivalently, with the standard 2-adic norm on integer differences,

\[
\boxed{\mathcal D_B=
2-\frac3{B^2}\sum_{n,m=B}^{2B-1}|C_n-C_m|_2.}
\tag{CH5}
\]

Indeed, sum_(k>=1) 2^-k 1_{C_n=C_m (mod 2^k)}=1-|C_n-C_m|_2,
including equal integers, where |0|_2=0. This proves (CH5).

**Complete target.** The theorem above and (CH4) imply

\[
\boxed{\pi\text{ normal in base }16
\quad\Longleftrightarrow\quad\mathcal D_B\longrightarrow0.}
\tag{CH6}
\]

For clarity, if D_B tends to zero, every fixed-depth child imbalance tends
to zero; inducting from total mass one gives all the uniform finite residue
laws. Conversely, those laws make every fixed-depth term vanish, and the
remaining geometric tail is uniformly bounded. This supplies both limit
directions without interchanging an uncontrolled depth and time limit.

A coherent archive C_n=C has D_B=2. Uniform mass on the consecutive
integers 0,...,2^K-1 gives D_B=2*4^-K. Both are exact calibrations.

The fourth-root gate in the present assault asks only for positive lower
mass in residues 1 and 2 modulo four. Full Haar would give mass 1/2. That
single lower bound suffices for R0, whereas (CH6) demands cancellation at
every fixed depth. No result in this dossier closes either limiting target.

## Provenance and next falsifier

The finite carry recurrence and Green completion are inherited from the
original BBP source. The coordinate equivalence and normalized energy were
derived in the immediately preceding SUCC conversation and are recorded
here as algebraic reductions. The standard radix/Weyl criterion is also
used in the maintained PI_NORMALITY_FRONTIER.md and the interference atlas.

A proposed proof using rational-source Haar in place of carry Haar is
falsified by the globally zero-pinned analytic controls in CONTROLS.md.
A proposed limit exchange must pay the fixed-depth/geometric-tail argument
above. Fixed positive D_B at arbitrarily large shells would refute the
normality target; a finite positive value does not.
