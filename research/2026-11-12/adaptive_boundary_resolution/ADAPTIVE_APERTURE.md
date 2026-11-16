# One channel when the damping can move

**Status: PROVED LOCAL / elementary coefficient isolation.** The near-sharp
channel bound in [INTEGER_INFORMATION.md](INTEGER_INFORMATION.md) fixes
the base `b` and observes the prefix `b^-1,...,b^-d`. It is not a lower
bound for arbitrary choices of measurement nodes. If the node may shrink
with the known mass, one response already isolates the integer zero count.
This is an essential restriction on the interpretation of that theorem.

## AA01: exact and noisy recovery

Let `c_h>=0` be finite-support masses, let `c_0` be an integer, and let
`sum_h c_h<=M` for a known positive integer `M`. At any `0<s<1`,

\[
F(s)=c_0+\sum_{h\ge1}c_hs^h,
\qquad 0\le F(s)-c_0\le s(M-c_0)\le Ms.
\tag{AA1}
\]

This follows term by term from `s^h<=s` for integer `h>=1`. Thus if
`Ms<1`,

\[
\boxed{c_0=\lfloor F(s)\rfloor.}
\tag{AA2}
\]

For example, `s=1/(M+1)` works with one exact response. Counts at the
other grades need not be integers; only the target count does. A zero
mass bound already determines the entire histogram and needs no response.

An authentic interval `F(s) in [l,u]` gives the rigorous integer bracket

\[
\boxed{
\max(0,\lceil l-Ms\rceil)\le c_0
\le\min(M,\lfloor u\rfloor).
}
\tag{AA3}
\]

Whenever `u-l+Ms<1`, the real interval `[l-Ms,u]` has length below one.
It contains the genuine integer target, so both rounded endpoints in
AA3 agree. An inconsistent packet must be rejected, not rounded anyway.
In particular, choose

\[
s=\frac1{4M},\qquad u-l\le\frac12.
\tag{AA4}
\]

The bracket then has width at most `3/4` and recovers the count. If the
response is normalized by the **known bound `M`**, the allowed interval
width is `1/(2M)`. Normalization by an actual mass `m<=M` also works if
`m` is separately supplied, so the response can be rescaled; the same
normalized width bound suffices. The normalizing mass cannot be omitted:
the sources `(1)` and `(2)` both have normalized response one at every
node but different zero counts, even with the common upper bound `M=2`.
The precision order agrees with the normalized-noise obstruction in
the integer-information note. Flooring an arbitrary noisy center is not
the rule; the interval is the certificate.

## AA02: a signed lower filter and the Goldbach equivalence

The known mass can also be used as a constant-node observation. If its
value is exactly `M`, the grade filter

\[
q_s(h)=\frac{s^h-s}{1-s}
\]

satisfies `q_s(0)=1`, `q_s(1)=0`, and `q_s(h)<=0` for every `h>=1`.
Its filtered response is

\[
B_s=\frac{F(s)-sM}{1-s}\le c_0.
\tag{AA5}
\]

If `Ms<1`, then `c_0>=1` implies `F(s)>=1>sM`, hence `B_s>0`.
Conversely `B_s>0` forces `c_0>0`. Therefore this positive certificate is
equivalent to a positive integer zero count in that regime. A mass upper
bound in place of exact mass gives the same safe lower bound and the
same implication under `Ms<1`.

For the authentic Goldbach response, set `M=n-1` and `s_n=1/[4(n-1)]`.
The pointwise claim becomes

\[
B_{s_n}(n)>0
\quad\Longleftrightarrow\quad
F_n\!\left(\frac1{4(n-1)}\right)>\frac14
\quad\Longleftrightarrow\quad G(n)>0.
\tag{AA6}
\]

This is an exact equivalent criterion, **not a new proof of Goldbach**.
Computing the genuine response by factoring every source pair already
examines the arithmetic source. A source-derived all-midpoint inequality
for this moving response remains unpaid.

## What moved and what did not

The fixed-base ladder spends more channels as `M` grows while keeping its
largest node fixed. This one-channel alternative instead permits the
node itself to approach zero at rate `1/M`. It requires that parameter
range, authentic response acquisition and normalized precision of order
`1/M`. No cost model for physical sensing or arithmetic evaluation is
assumed. Encoding a smaller rational node is not a proof that its response
is cheap to obtain.

At any **fixed** `s`, AA5 lies within the complex-bank theorem: nodes
`s,1`, with coefficient `-s/(1-s)` at `1`. Its arithmetic cumulative
response is eventually negative. Choosing `s=s_n` changes the bank with
the midpoint and leaves that theorem's scope; a fixed-parameter asymptotic
may not be substituted at a moving node.

The falsifiers are concrete. Without an integer target, AA2 need not equal
`c_0`. Without `Ms<1`, the source `(c_0,c_1)=(0,M)` can have `F(s)>=1`.
Without a valid uncertainty interval, flooring can change the answer.
Without source authentication, any reported response is merely a number.
The independent probe records each of these mathematical boundary cases
and the exact four-midpoint integration sample declared in
[PREREGISTRATION.md](PREREGISTRATION.md).
